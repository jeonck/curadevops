#!/usr/bin/env python3
"""CuraDevOps daily pipeline.

Collects new items from RSS/Reddit/HN/GitHub, drops release noise (patch
releases, pre-release tags), enriches the rest with urgency signals
(endoflife.date EOL anchor, deprecation deadlines, release semantics,
KEV/EPSS when CVEs appear), asks Claude for per-persona actionable verdicts
(Platform/SRE / CI-CD / Leader), and writes Hugo posts for anything that is
not Skip for every persona.

Usage:
    python pipeline/collect.py [--dry-run]

Env:
    JUDGE_BACKEND            "claude-code" | "api" (default: auto — claude-code
                             when the claude CLI is on PATH, api otherwise)
    CLAUDE_CODE_OAUTH_TOKEN  claude-code backend auth in CI (claude setup-token;
                             local runs use the claude CLI login session)
    ANTHROPIC_API_KEY        required for the api backend
    CLAUDE_MODEL             judge model (default claude-sonnet-4-6)
    MAX_ITEMS                max judgments per run (default 30)
    FEEDS_FILE               source definition file (default feeds.yaml)
    FRESH_HOURS              RSS freshness window in hours (default 48)
    GITHUB_TOKEN             optional — GitHub Search API rate-limit relief
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser
import requests
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from enrich import Enricher, extract_cves  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FEEDS_FILE = ROOT / os.environ.get("FEEDS_FILE", "feeds.yaml")
CONTEXT_FILE = ROOT / "context.md"
PERSONAS_DIR = ROOT / "personas"
PROCESSED_FILE = ROOT / "pipeline" / "processed.json"
CONTENT_DIR = ROOT / "content" / "insights"

USER_AGENT = "curadevops-pipeline/1.0"
FRESH_HOURS = int(os.environ.get("FRESH_HOURS", "48"))
PROCESSED_TTL_DAYS = 90   # retention for the processed-URL record
SUMMARY_MAX_CHARS = 1500  # body cap for the judge prompt

VERDICTS = ("Act", "Plan", "Learn", "Skip")
SEVERITY = {"Act": 0, "Plan": 1, "Learn": 2, "Skip": 3}
PERSONAS = ("platform", "cicd", "leader")
PERSONA_LABELS = {"platform": "Platform/SRE", "cicd": "CI/CD", "leader": "Leader"}

JUDGE_PROMPT = """Read the item below and reply ONLY with JSON in this exact shape. No other text.

{{"title": "concise factual headline, max 80 chars",
 "tags": ["kebab-case-tag", "max 3"],
 "personas": {{
  "platform": {{"verdict": "Act|Plan|Learn|Skip", "note": "1-2 sentences: why, plus the concrete action if Act/Plan (empty string if Skip)"}},
  "cicd": {{"verdict": "Act|Plan|Learn|Skip", "note": "same rules"}},
  "leader": {{"verdict": "Act|Plan|Learn|Skip", "note": "same rules"}}}}}}

Rules:
- Judge each persona INDEPENDENTLY against its own context section, using its
  verdict criteria and its "does NOT care about" list. Verdicts should often
  differ across personas — never copy one verdict to all three by default.
- Treat the enrichment signals (EOL dates / deprecation deadlines / release
  semantics / KEV / EPSS / corroboration) as the primary evidence when deciding
  Act vs Plan.
- NEVER invent urgency: Act requires a concrete anchor — a deadline or EOL date
  in the signals or the item, active exploitation, or a confirmed supply-chain
  compromise. With no deadline anywhere, the ceiling is Plan. A zero-Act run is
  normal and healthy.
- Pre-GA (alpha/beta/RC/preview/experimental) caps every persona at Learn.
- Act/Plan notes must name a concrete action AND the deadline when one exists
  ("upgrade EKS to 1.34 before 2026-10-27", "pin the action to a SHA",
  "evaluate migrating off X before the license change"), not generic advice.
- Vendor marketing, routine patch releases, duplicates, and items outside every
  persona's scope: Skip for all three.
- Write notes in your own words; never quote more than one sentence from the
  source (copyright rule).

Title: {title}
Source: {source_name}
Link: {url}
Enrichment signals: {signals}
Summary: {summary}"""


def log(msg: str) -> None:
    print(msg, flush=True)


def url_hash(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", title.lower()).strip("-")
    if not slug:
        slug = "item"
    return slug[:60].rstrip("-")


# ---------------------------------------------------------------- collection

def collect_rss(feeds: list) -> list:
    items = []
    cutoff = datetime.now(timezone.utc) - timedelta(hours=FRESH_HOURS)
    for feed in feeds:
        try:
            parsed = feedparser.parse(
                feed["url"], agent=USER_AGENT, request_headers={"Accept": "*/*"}
            )
            count = 0
            for e in parsed.entries:
                ts = e.get("published_parsed") or e.get("updated_parsed")
                if ts:
                    published = datetime.fromtimestamp(time.mktime(ts), tz=timezone.utc)
                    if published < cutoff:
                        continue
                link = e.get("link", "")
                if not link:
                    continue
                title = strip_html(e.get("title", "(no title)"))
                summary = strip_html(e.get("summary", ""))[:SUMMARY_MAX_CHARS]
                # per-feed keyword gate for firehose feeds (AWS/GCP/Azure):
                # keep only items mentioning whitelisted services/keywords
                require = feed.get("require_any")
                if require:
                    text = f"{title} {summary}".lower()
                    if not any(str(k).lower() in text for k in require):
                        continue
                items.append({
                    "title": title,
                    "url": link,
                    "summary": summary,
                    "source_name": feed["name"],
                })
                count += 1
            log(f"  [rss] {feed['name']}: {count} items")
        except Exception as exc:  # noqa: BLE001 — one source must not kill the run
            log(f"  [rss] {feed['name']}: failed ({exc})")
    return items


def collect_reddit(subs: list) -> list:
    items = []
    for sub in subs:
        url = (
            f"https://www.reddit.com/r/{sub['subreddit']}/{sub.get('listing', 'top')}.json"
            f"?t={sub.get('t', 'day')}&limit=25"
        )
        try:
            resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=15)
            resp.raise_for_status()
            count = 0
            for child in resp.json().get("data", {}).get("children", []):
                post = child.get("data", {})
                if post.get("score", 0) < sub.get("min_score", 0):
                    continue
                if post.get("stickied"):
                    continue
                permalink = "https://www.reddit.com" + post.get("permalink", "")
                summary = strip_html(post.get("selftext", ""))[:SUMMARY_MAX_CHARS]
                if not summary and post.get("url"):
                    summary = f"Link post: {post['url']}"
                items.append({
                    "title": post.get("title", "(no title)"),
                    "url": permalink,
                    "summary": summary,
                    "source_name": f"r/{sub['subreddit']}",
                })
                count += 1
            log(f"  [reddit] r/{sub['subreddit']}: {count} items")
        except Exception as exc:  # noqa: BLE001
            log(f"  [reddit] r/{sub['subreddit']}: failed ({exc})")
    return items


def collect_hackernews(queries: list) -> list:
    items = []
    for q in queries:
        url = f"https://hnrss.org/newest?q={requests.utils.quote(q['query'])}&points={q.get('min_points', 50)}"
        try:
            parsed = feedparser.parse(url, agent=USER_AGENT)
            count = 0
            for e in parsed.entries:
                link = e.get("link", "")
                if not link:
                    continue
                items.append({
                    "title": strip_html(e.get("title", "(no title)")),
                    "url": link,
                    "summary": strip_html(e.get("summary", ""))[:SUMMARY_MAX_CHARS],
                    "source_name": f"HN ({q['query']})",
                })
                count += 1
            log(f"  [hn] {q['query']}: {count} items")
        except Exception as exc:  # noqa: BLE001
            log(f"  [hn] {q['query']}: failed ({exc})")
    return items


def collect_github(searches: list) -> list:
    items = []
    headers = {"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    for search in searches:
        since = (datetime.now(timezone.utc) - timedelta(days=search.get("days_back", 7))).date()
        query = f"{search['query']} created:>{since.isoformat()}"
        try:
            resp = requests.get(
                "https://api.github.com/search/repositories",
                params={"q": query, "sort": "stars", "order": "desc", "per_page": 10},
                headers=headers, timeout=15,
            )
            resp.raise_for_status()
            count = 0
            for repo in resp.json().get("items", []):
                desc = repo.get("description") or ""
                items.append({
                    "title": f"{repo['full_name']} (★{repo.get('stargazers_count', 0)})",
                    "url": repo["html_url"],
                    "summary": desc[:SUMMARY_MAX_CHARS],
                    "source_name": "GitHub Trending",
                })
                count += 1
            log(f"  [github] {search['query']}: {count} items")
        except Exception as exc:  # noqa: BLE001
            log(f"  [github] {search['query']}: failed ({exc})")
    return items


# DevOps feeds are release-shaped and noisier than security feeds — drop the
# judgment-free noise before it eats MAX_ITEMS budget (PLAN.md §2.5).
PATCH_RELEASE_RE = re.compile(r"\bv?\d+\.\d+\.(?P<patch>[1-9]\d*)\b")
PRERELEASE_TAG_RE = re.compile(r"\bv?\d+\.\d+\.\d+-(alpha|beta|rc)", re.IGNORECASE)
SIGNIFICANT_RE = re.compile(
    r"cve|security|vulnerab|breaking|deprecat|end[\s-]of[\s-]life|\beol\b|"
    r"regression|urgent|critical|data loss",
    re.IGNORECASE,
)


def noise_filter(items: list) -> tuple[list, int]:
    """Drop patch-level releases (x.y.Z, no security/breaking content) and
    pre-release tags (vX.Y.Z-rc.N) before judgment."""
    kept, dropped = [], 0
    for item in items:
        title = item["title"]
        text = f"{title} {item['summary']}"
        if PRERELEASE_TAG_RE.search(title):
            dropped += 1
            continue
        if PATCH_RELEASE_RE.search(title) and not SIGNIFICANT_RE.search(text):
            dropped += 1
            continue
        kept.append(item)
    return kept, dropped


def interleave_by_source(items: list) -> list:
    """Round-robin across sources so the MAX_ITEMS cut favors no single source."""
    buckets: dict[str, list] = {}
    for item in items:
        buckets.setdefault(item["source_name"], []).append(item)
    result = []
    while any(buckets.values()):
        for name in list(buckets):
            if buckets[name]:
                result.append(buckets[name].pop(0))
    return result


# ------------------------------------------------------------------ judgment

class FatalAPIError(Exception):
    """Non-retryable error (credit exhaustion, auth failure) — abort the run."""


def is_fatal_api_error(exc: Exception) -> bool:
    msg = str(exc).lower()
    return any(marker in msg for marker in (
        "credit balance", "authenticat", "invalid x-api-key",
        "invalid api key", "invalid bearer token", "oauth token", "/login",
        "401",
    ))


def parse_judgment(text: str) -> dict | None:
    """Extract and validate the JSON judgment from the model response."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None
    if not isinstance(data.get("title"), str) or not data["title"].strip():
        return None
    personas = data.get("personas")
    if not isinstance(personas, dict):
        return None
    clean = {}
    for key in PERSONAS:
        entry = personas.get(key)
        if not isinstance(entry, dict) or entry.get("verdict") not in VERDICTS:
            return None
        clean[key] = {
            "verdict": entry["verdict"],
            "note": str(entry.get("note", "")).strip(),
        }
    data["personas"] = clean
    # overall verdict = most severe persona verdict; drives taxonomy + publish
    data["verdict"] = min(
        (clean[k]["verdict"] for k in PERSONAS), key=SEVERITY.__getitem__
    )
    tags = data.get("tags") or []
    if not isinstance(tags, list):
        tags = []
    data["tags"] = [slugify(str(t)) for t in tags[:3] if str(t).strip()]
    return data


def build_prompt(item: dict) -> str:
    return JUDGE_PROMPT.format(
        title=item["title"],
        source_name=item["source_name"],
        url=item["url"],
        signals=item.get("signals") or "none",
        summary=item["summary"] or "(no summary — judge from the title)",
    )


def judge_item_api(client, model: str, system_blocks: list, item: dict) -> dict | None:
    prompt = build_prompt(item)
    for attempt in (1, 2):  # one retry on JSON parse failure
        try:
            response = client.messages.create(
                model=model,
                max_tokens=1024,
                system=system_blocks,
                messages=[{"role": "user", "content": prompt}],
            )
        except Exception as exc:  # noqa: BLE001
            if is_fatal_api_error(exc):
                raise FatalAPIError(str(exc)) from exc
            log(f"    API error (attempt {attempt}): {exc}")
            if attempt == 2:
                return None
            time.sleep(3)
            continue
        text = next((b.text for b in response.content if b.type == "text"), "")
        judgment = parse_judgment(text)
        if judgment:
            return judgment
        log(f"    JSON parse failure (attempt {attempt}): {text[:120]!r}")
    return None


def judge_item_cli(model: str, system_text: str, item: dict) -> dict | None:
    """Judge via the Claude Code CLI (claude -p) — subscription auth, no API credits."""
    prompt = build_prompt(item)
    env = os.environ.copy()
    env.pop("ANTHROPIC_API_KEY", None)  # keep the CLI off API-key billing
    cmd = ["claude", "-p", "--model", model, "--tools", "",
           "--output-format", "text", "--append-system-prompt", system_text]
    for attempt in (1, 2):
        try:
            result = subprocess.run(cmd, input=prompt, env=env, timeout=180,
                                    capture_output=True, text=True)
        except subprocess.TimeoutExpired:
            log(f"    CLI timeout (attempt {attempt})")
            continue
        if result.returncode != 0:
            err = (result.stderr or result.stdout).strip()
            if is_fatal_api_error(RuntimeError(err)):
                raise FatalAPIError(err[:300])
            log(f"    CLI error (attempt {attempt}): {err[:200]}")
            if attempt == 2:
                return None
            time.sleep(3)
            continue
        judgment = parse_judgment(result.stdout)
        if judgment:
            return judgment
        log(f"    JSON parse failure (attempt {attempt}): {result.stdout[:120]!r}")
    return None


# -------------------------------------------------------------------- output

def yaml_quote(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write_post(item: dict, judgment: dict, date: datetime) -> Path:
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    base = f"{date.date().isoformat()}-{slugify(item['title'])}"
    path = CONTENT_DIR / f"{base}.md"
    n = 2
    while path.exists():
        path = CONTENT_DIR / f"{base}-{n}.md"
        n += 1
    tags = ", ".join(yaml_quote(t) for t in judgment["tags"])
    cves = ", ".join(yaml_quote(c) for c in item.get("cves", []))
    persona_fm = "\n".join(
        f"verdict_{key}: {yaml_quote(judgment['personas'][key]['verdict'])}"
        for key in PERSONAS
    )
    lines = []
    for key in PERSONAS:
        entry = judgment["personas"][key]
        label = PERSONA_LABELS[key]
        if entry["verdict"] == "Skip" or not entry["note"]:
            lines.append(f"- **{label} — {entry['verdict']}**")
        else:
            lines.append(f"- **{label} — {entry['verdict']}:** {entry['note']}")
    if item.get("signals"):
        lines.append(f"- **Signals:** {item['signals']}")
    body = f"""---
title: {yaml_quote(judgment["title"])}
date: {date.isoformat()}
verdict: {yaml_quote(judgment["verdict"])}
{persona_fm}
tags: [{tags}]
cves: [{cves}]
source: {yaml_quote(item["url"])}
source_name: {yaml_quote(item["source_name"])}
status: "active"
---
{chr(10).join(lines)}
"""
    path.write_text(body, encoding="utf-8")
    return path


# ---------------------------------------------------------------------- main

def load_processed() -> dict:
    if PROCESSED_FILE.exists():
        try:
            return json.loads(PROCESSED_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            log("processed.json parse failure — resetting")
    return {}


def prune_processed(processed: dict) -> dict:
    cutoff = (datetime.now(timezone.utc) - timedelta(days=PROCESSED_TTL_DAYS)).isoformat()
    return {k: v for k, v in processed.items() if v >= cutoff}


def load_system_text() -> str:
    parts = [
        "You are CuraDevOps's DevOps-curation judge. You assess each collected "
        "DevOps/platform item and issue independent, actionable verdicts for "
        "three practitioner personas, strictly following the channel context "
        "and the persona contexts below.",
        CONTEXT_FILE.read_text(encoding="utf-8"),
    ]
    for key in PERSONAS:
        persona_file = PERSONAS_DIR / f"{key}.md"
        parts.append(f"<!-- persona: {key} -->\n" + persona_file.read_text(encoding="utf-8"))
    return "\n\n".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description="CuraDevOps daily pipeline")
    parser.add_argument("--dry-run", action="store_true",
                        help="print judgments without writing posts or processed.json")
    parser.add_argument("--max-items", type=int,
                        default=int(os.environ.get("MAX_ITEMS", "30")),
                        help="max judgments per run")
    args = parser.parse_args()

    # judge backend: claude-code (subscription auth, default) or api (API-key billing)
    backend = os.environ.get("JUDGE_BACKEND", "").strip() or (
        "claude-code" if shutil.which("claude") else "api"
    )
    client = None
    if backend == "api":
        if not os.environ.get("ANTHROPIC_API_KEY"):
            log("error: the api backend requires ANTHROPIC_API_KEY")
            return 1
        import anthropic  # lazy import — unused on the claude-code backend

        client = anthropic.Anthropic()
    elif backend == "claude-code":
        if not shutil.which("claude"):
            log("error: the claude-code backend requires the claude CLI on PATH")
            return 1
    else:
        log(f"error: unknown JUDGE_BACKEND={backend!r} (claude-code | api)")
        return 1

    model = os.environ.get("CLAUDE_MODEL", "claude-sonnet-4-6")
    feeds = yaml.safe_load(FEEDS_FILE.read_text(encoding="utf-8"))
    system_text = load_system_text()
    # api backend: identical system text on every call → prompt cache savings
    system_blocks = [{
        "type": "text",
        "text": system_text,
        "cache_control": {"type": "ephemeral"},
    }]

    log(f"=== collection start (backend={backend}, model={model}, max_items={args.max_items}, dry_run={args.dry_run}) ===")
    collected = []
    collected += collect_rss(feeds.get("rss", []))
    collected += collect_reddit(feeds.get("reddit", []))
    collected += collect_hackernews(feeds.get("hackernews", []))
    collected += collect_github(feeds.get("github_search", []))

    # de-duplicate by URL (within this run)
    seen_urls = set()
    unique = []
    for item in collected:
        h = url_hash(item["url"])
        if h in seen_urls:
            continue
        seen_urls.add(h)
        item["hash"] = h
        unique.append(item)

    processed = prune_processed(load_processed())
    fresh = [i for i in unique if i["hash"] not in processed]
    fresh, noise_dropped = noise_filter(fresh)
    queue = interleave_by_source(fresh)[: args.max_items]

    # enrichment: EOL anchor / deadlines / release semantics / KEV / EPSS /
    # corroboration. Any source failing degrades to "unavailable" — never fatal.
    cve_sources: dict[str, set] = {}
    for item in unique:
        item["cves"] = extract_cves(f"{item['title']} {item['summary']}")
        for cve in item["cves"]:
            cve_sources.setdefault(cve, set()).add(item["source_name"])
    enricher = Enricher(github_token=os.environ.get("GITHUB_TOKEN"), log=log)
    enricher.prefetch_epss(sorted({c for i in queue for c in i["cves"]}))
    for item in queue:
        item["signals"] = enricher.signals_line(item, cve_sources)

    log(f"\ncollected {len(collected)} / after dedupe {len(unique)} / noise-dropped {noise_dropped} / new {len(fresh)} / to judge {len(queue)}\n")

    now = datetime.now(timezone.utc).astimezone()  # runner-local ISO timestamp
    verdict_counts = {v: 0 for v in VERDICTS}
    skipped = 0
    created_files = []

    fatal_error = None
    for i, item in enumerate(queue, 1):
        log(f"[{i}/{len(queue)}] {item['source_name']} | {item['title'][:80]}")
        try:
            if backend == "claude-code":
                judgment = judge_item_cli(model, system_text, item)
            else:
                judgment = judge_item_api(client, model, system_blocks, item)
        except FatalAPIError as exc:
            fatal_error = exc
            break
        if judgment is None:
            skipped += 1
            log("    → skipped (judgment failure)")
            continue
        verdict_counts[judgment["verdict"]] += 1
        detail = " / ".join(
            f"{PERSONA_LABELS[k]}: {judgment['personas'][k]['verdict']}" for k in PERSONAS
        )
        log(f"    → {judgment['verdict']} ({detail}) | {judgment['title']}")
        if item.get("signals"):
            log(f"      signals: {item['signals']}")

        if not args.dry_run:
            processed[item["hash"]] = now.isoformat()
            if judgment["verdict"] != "Skip":
                created_files.append(write_post(item, judgment, now))

    if not args.dry_run:
        PROCESSED_FILE.parent.mkdir(parents=True, exist_ok=True)
        PROCESSED_FILE.write_text(
            json.dumps(processed, indent=1, sort_keys=True), encoding="utf-8"
        )

    log("\n=== run summary ===")
    judged = sum(verdict_counts.values())
    log(f"collected: {len(collected)} / new: {len(fresh)} / judged: {judged} (failed-skip {skipped})")
    log("verdicts: " + " / ".join(f"{v} {c}" for v, c in verdict_counts.items()))
    if args.dry_run:
        log("(dry-run — no files written, no record updates)")
    elif created_files:
        log("created:")
        for f in created_files:
            log(f"  - {f.relative_to(ROOT)}")
    else:
        log("no files created")

    if fatal_error:
        log(f"\naborted: unrecoverable API error — {fatal_error}")
        log("→ check Anthropic credits / auth token. Unprocessed items retry on the next run.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
