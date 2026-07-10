# CuraDevOps

**DevOps intelligence with actionable verdicts.** Every day at 11:00 UTC this
pipeline collects new items from RSS / Hacker News / Reddit / GitHub, drops
release noise (patch releases, pre-release tags), enriches each item with
urgency signals (endoflife.date EOL calendar, deprecation deadlines, release
semantics, CISA KEV/EPSS when CVEs appear), and has Claude judge it
**independently for three practitioner personas** — then publishes everything
that matters to [jeonck.github.io/curadevops](https://jeonck.github.io/curadevops/)
with an RSS feed.

Sister channel: [CuraSec](https://jeonck.github.io/curasec/) (security) — same
architecture, security-domain signals.

## Verdict system

Each item gets one verdict *per persona*, e.g. `Platform: Act / CI/CD: Skip / Leader: Skip`:

| Verdict | Meaning | Published |
|---|---|---|
| 🔥 **Act** | do or check something now (imminent EOL, dated deprecation, supply-chain compromise, exploited CVE) | yes |
| 📌 **Plan** | review within the quarter (announced breaking changes, new GA capabilities, migrations) | yes |
| 📚 **Learn** | worth knowing, no action needed | yes |
| **Skip** | marketing / routine patch release / duplicate / irrelevant | **only if Skip for all 3 personas → not published** |

A zero-Act day is normal — genuine urgency is rare in DevOps and the judge is
instructed never to invent it (Act requires a concrete anchor: a date, active
exploitation, or a confirmed compromise).

The personas (the heart of judgment quality — edit these to change verdicts):

- [`personas/platform.md`](personas/platform.md) — Platform/SRE Engineer: upgrades, migrations, EOL exposure
- [`personas/cicd.md`](personas/cicd.md) — CI/CD & Release Engineer: pipelines, supply chain, build/deploy
- [`personas/leader.md`](personas/leader.md) — Engineering/Platform Leader: toolchain strategy, licensing, vendor risk

## Structure

```
.
├── context.md                  # channel-wide judgment rules + calibration examples
├── personas/                   # per-persona verdict criteria (fed into every judgment)
├── feeds.yaml                  # daily sources (all URLs HTTP-200 verified)
├── feeds-weekly.yaml           # weekly Release Radar (~20 core repos' releases.atom)
├── pipeline/
│   ├── collect.py              # collect → noise filter → enrich → judge → write posts
│   ├── enrich.py               # endoflife.date EOL / deadlines / release semantics / KEV / EPSS
│   ├── expire.py               # auto-archive: Learn >14d, others >30d
│   ├── processed.json          # judged-URL record (dedupe, 90-day retention)
│   └── done.sh                 # manual archive helper
├── content/insights/           # generated posts
├── content/about.md            # methodology + trust principles (AI disclosure)
├── content/corrections.md      # public corrections log
├── layouts/                    # self-contained Hugo layouts (no theme)
└── .github/workflows/
    ├── daily.yml               # 11:00 UTC cron: collect + judge + deploy
    ├── weekly.yml              # Monday 12:00 UTC: Release Radar
    └── control.yml             # pause / resume collection
```

## Setup

1. **Judge auth** — one of the two (repo Settings → Secrets and variables → Actions):
   - **Recommended: Claude subscription (Pro/Max)** — run `claude setup-token`
     locally, complete browser auth, then register the **final printed token**
     (`sk-ant-oat01-...`, *not* the browser auth code) as the
     `CLAUDE_CODE_OAUTH_TOKEN` secret. No API credits needed.
   - **Alternative: API key** — register `ANTHROPIC_API_KEY` (used only when
     the OAuth token secret is absent).
2. **Pages** — Settings → Pages → Source: **GitHub Actions**
3. **First run** — Actions tab → `Daily Curation` → Run workflow
   (manual runs deploy even with zero new items)

Then it runs daily at 11:00 UTC (06:00–07:00 US East) with no human in the loop.

## Failure handling (designed for zero-touch operation)

- **A failed judge step opens a GitHub issue automatically** (plus the normal
  Actions failure email) — the pipeline never dies silently.
- Fatal auth/credit errors abort fast; judgments completed before the abort are
  still committed and deployed. Unprocessed items retry the next day.
- Every collection source is error-isolated — one broken feed cannot kill a run.
- Every enrichment lookup (endoflife.date, KEV, EPSS) degrades to
  "unavailable" on failure — never fatal.
- Zero-new-item days skip both commit and deploy (no empty publishes).
- Pause/resume: Actions tab → **Pipeline Control** (or `pipeline/pause.sh` /
  `resume.sh`) — state is a `.collect-paused` marker file in the repo.

## Local run

```bash
pip install -r pipeline/requirements.txt

# uses your local claude CLI login (subscription auth, no API key needed)
MAX_ITEMS=5 python pipeline/collect.py --dry-run

# real run + preview
python pipeline/collect.py
hugo server        # → http://localhost:1313/curadevops/
```

Env knobs: `JUDGE_BACKEND` (`claude-code`|`api`), `CLAUDE_MODEL`
(default `claude-sonnet-4-6`), `MAX_ITEMS` (30), `FEEDS_FILE`, `FRESH_HOURS`,
`GITHUB_TOKEN` (search rate-limit relief).

## Operating routine

**First 30 days (trust-building period)** — skim the day's verdicts once daily
(~5 min, published 20:00 KST). Fix a bad verdict by editing the post's front
matter + note, and log confirmed errors in
[content/corrections.md](content/corrections.md). If verdicts consistently miss,
edit the persona files — not the pipeline.

**After day 30** — fully automatic. Weekly skim optional.

**Day 90 — continue/stop decision** — evaluate RSS subscribers and return
visits per PLAN.md.

## Known constraints

- **Reddit**: cloud IPs (GitHub Actions) often get 403 from the `.json` API.
  Error isolation keeps other sources healthy.
- **hnrss.org**: occasional 502 — that run collects 0 from HN, self-heals next run.
- **GitHub Search**: `created:>N days` + star filters return 0 on many days (normal).
- **endoflife.date coverage**: ~460 products, but not everything (no helm/vault
  slugs) — uncovered products fall back to text-extracted deadlines.
- **Firehose feeds**: AWS/GCP/Azure feeds pass a service-keyword whitelist
  (`require_any` in feeds.yaml) — tune it there, not in code.
- **OAuth token expiry**: re-run `claude setup-token`, update the secret, close
  the auto-opened issue.

## Trust principles

Public channel, automated judgments — so: AI disclosure on every page, evidence
required on every verdict, a public corrections log, and a 30-day human review
period at launch. See [About](https://jeonck.github.io/curadevops/about/).
