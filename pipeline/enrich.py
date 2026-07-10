#!/usr/bin/env python3
"""Enrichment for CuraDevOps judgments.

Cross-references each item with machine-checkable urgency signals:
  - EOL anchor: endoflife.date API — product+version mentions are matched to
    release cycles and their EOL/support dates (the KEV-equivalent for DevOps)
  - deadline extraction: deprecation/sunset/removal dates found in the text
  - release semantics: pre-GA markers, GA announcements, breaking-change flags,
    major-version releases
  - CVE path (kept light from CuraSec): CISA KEV + EPSS when CVEs are present,
    plus cross-source corroboration

Every network call degrades to "unavailable" on failure — enrichment must
never abort the pipeline.
"""

import re
import time
from datetime import date, datetime

import requests

KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
EPSS_URL = "https://api.first.org/data/v1/epss"
EOL_URL = "https://endoflife.date/api/{slug}.json"
USER_AGENT = "curadevops-pipeline/1.0"

CVE_RE = re.compile(r"CVE-\d{4}-\d{4,7}", re.IGNORECASE)
MAX_CVES_PER_ITEM = 3
EOL_SOON_DAYS = 90        # "EOL in Nd" flagged when within this window
MAX_EOL_HITS_PER_ITEM = 3

# Product + adjacent version ("Kubernetes 1.33", "Terraform v1.13") — version
# adjacency is required, which keeps false positives near zero. Slugs verified
# against endoflife.date /api/all.json on 2026-07-10 (helm/vault not covered).
PRODUCTS = [
    ("Kubernetes", "kubernetes", r"(?:kubernetes|k8s)"),
    ("Amazon EKS", "amazon-eks", r"(?:amazon\s+)?eks"),
    ("AKS", "azure-kubernetes-service", r"aks"),
    ("GKE", "google-kubernetes-engine", r"gke"),
    ("Terraform", "terraform", r"terraform"),
    ("OpenTofu", "opentofu", r"opentofu"),
    ("Jenkins", "jenkins", r"jenkins"),
    ("GitLab", "gitlab", r"gitlab"),
    ("Istio", "istio", r"istio"),
    ("Argo CD", "argo-cd", r"argo[\s-]?cd"),
    ("Flux", "flux", r"flux(?:cd)?"),
    ("Docker Engine", "docker-engine", r"docker(?:\s+engine)?"),
    ("containerd", "containerd", r"containerd"),
    ("Envoy", "envoy", r"envoy"),
    ("etcd", "etcd", r"etcd"),
    ("Prometheus", "prometheus", r"prometheus"),
    ("Grafana", "grafana", r"grafana"),
    ("Ansible", "ansible", r"ansible"),
    ("nginx", "nginx", r"nginx"),
    ("PostgreSQL", "postgresql", r"postgres(?:ql)?"),
    ("Ubuntu", "ubuntu", r"ubuntu"),
    ("Node.js", "nodejs", r"node(?:\.js)?"),
    ("Python", "python", r"python"),
    ("Redis", "redis", r"redis"),
    ("RabbitMQ", "rabbitmq", r"rabbitmq"),
    ("Kafka", "apache-kafka", r"(?:apache\s+)?kafka"),
    ("Consul", "consul", r"consul"),
    ("Nomad", "nomad", r"nomad"),
]
PRODUCT_RES = [
    (name, slug, re.compile(rf"\b{pat}[\s/]*v?(\d+\.\d+)\b", re.IGNORECASE))
    for name, slug, pat in PRODUCTS
]

DEADLINE_KEYWORD_RE = re.compile(
    r"deprecat|sunset|end[\s-]of[\s-]life|\beol\b|retir|will be removed|"
    r"removed in|shut\s?down|discontinu|no longer support",
    re.IGNORECASE,
)
DATE_RE = re.compile(
    r"\b(?:January|February|March|April|May|June|July|August|September|"
    r"October|November|December)\s+\d{1,2},?\s+\d{4}\b"
    r"|\b\d{4}-\d{2}-\d{2}\b",
)

PRE_GA_RE = re.compile(
    r"\b(alpha|beta|rc\d*|release candidate|preview|experimental|early access)\b",
    re.IGNORECASE,
)
GA_RE = re.compile(
    r"\b(generally available|general availability|now ga|reaches ga|is now stable)\b",
    re.IGNORECASE,
)
BREAKING_RE = re.compile(r"breaking[\s-]change", re.IGNORECASE)
MAJOR_RELEASE_RE = re.compile(r"(?<![.\d])v?(\d+)\.0(?:\.0)?\b")


def extract_cves(text: str) -> list:
    """Unique, normalized CVE ids found in text (capped per item)."""
    return sorted({m.upper() for m in CVE_RE.findall(text or "")})[:MAX_CVES_PER_ITEM]


def _parse_eol_date(value) -> date | None:
    """endoflife.date 'eol'/'support' fields are ISO dates, or booleans."""
    if isinstance(value, str):
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            return None
    return None


class Enricher:
    def __init__(self, github_token: str | None = None, log=print):
        self.log = log
        self._kev: set | None = None
        self._kev_failed = False
        self._epss: dict[str, float] = {}
        self._epss_failed = False
        self._eol: dict[str, list | None] = {}   # slug → cycles (None = failed)

    # ------------------------------------------------------------------ KEV

    def kev_set(self) -> set:
        if self._kev is None and not self._kev_failed:
            try:
                resp = requests.get(
                    KEV_URL, headers={"User-Agent": USER_AGENT}, timeout=30
                )
                resp.raise_for_status()
                self._kev = {
                    v.get("cveID", "").upper()
                    for v in resp.json().get("vulnerabilities", [])
                }
                self.log(f"  [enrich] KEV catalog loaded: {len(self._kev)} CVEs")
            except Exception as exc:  # noqa: BLE001
                self._kev_failed = True
                self.log(f"  [enrich] KEV fetch failed ({exc}) — degrading")
        return self._kev or set()

    # ----------------------------------------------------------------- EPSS

    def prefetch_epss(self, cves: list) -> None:
        """One batch call for all CVEs in this run's queue."""
        missing = [c for c in cves if c not in self._epss]
        if not missing or self._epss_failed:
            return
        try:
            resp = requests.get(
                EPSS_URL,
                params={"cve": ",".join(missing[:100])},
                headers={"User-Agent": USER_AGENT},
                timeout=30,
            )
            resp.raise_for_status()
            for row in resp.json().get("data", []):
                self._epss[row["cve"].upper()] = float(row["epss"])
            self.log(f"  [enrich] EPSS scores fetched for {len(missing)} CVEs")
        except Exception as exc:  # noqa: BLE001
            self._epss_failed = True
            self.log(f"  [enrich] EPSS fetch failed ({exc}) — degrading")

    # ------------------------------------------------------------ EOL anchor

    def _cycles(self, slug: str) -> list:
        if slug not in self._eol:
            try:
                resp = requests.get(
                    EOL_URL.format(slug=slug),
                    headers={"User-Agent": USER_AGENT},
                    timeout=20,
                )
                resp.raise_for_status()
                self._eol[slug] = resp.json()
                time.sleep(0.3)
            except Exception as exc:  # noqa: BLE001
                self._eol[slug] = None
                self.log(f"  [enrich] EOL fetch failed for {slug} ({exc}) — degrading")
        return self._eol[slug] or []

    def eol_signals(self, text: str) -> list:
        """EOL/support status for every product+version mention in the text."""
        today = date.today()
        signals = []
        seen = set()
        for name, slug, pattern in PRODUCT_RES:
            for m in pattern.finditer(text or ""):
                version = m.group(1)
                key = (slug, version)
                if key in seen:
                    continue
                seen.add(key)
                cycle = next(
                    (c for c in self._cycles(slug) if str(c.get("cycle")) == version),
                    None,
                )
                if cycle is None:
                    continue
                eol = _parse_eol_date(cycle.get("eol"))
                support = _parse_eol_date(cycle.get("support"))
                if eol:
                    days = (eol - today).days
                    if days < 0:
                        signals.append(f"{name} {version} is past EOL ({eol}, {-days}d ago)")
                    elif days <= EOL_SOON_DAYS:
                        signals.append(f"{name} {version} reaches EOL in {days}d ({eol})")
                    else:
                        signals.append(f"{name} {version} EOL {eol}")
                elif cycle.get("eol") is False:
                    line = f"{name} {version} supported"
                    if support:
                        line += f" (active support until {support})"
                    signals.append(line)
                if len(signals) >= MAX_EOL_HITS_PER_ITEM:
                    return signals
        return signals

    # -------------------------------------------------- text-derived signals

    @staticmethod
    def deadline_signals(text: str) -> list:
        """Deprecation/sunset deadlines: keyword + explicit date in one sentence."""
        dates = []
        for sentence in re.split(r"(?<=[.!?])\s+", text or ""):
            if not DEADLINE_KEYWORD_RE.search(sentence):
                continue
            for d in DATE_RE.findall(sentence):
                if d not in dates:
                    dates.append(d)
        if dates:
            return ["deprecation/EOL deadline mentioned: " + "; ".join(dates[:3])]
        if DEADLINE_KEYWORD_RE.search(text or ""):
            return ["deprecation mentioned (no explicit date found)"]
        return []

    @staticmethod
    def release_signals(title: str, text: str) -> list:
        signals = []
        if PRE_GA_RE.search(title or ""):
            signals.append("pre-GA (alpha/beta/RC/preview)")
        elif GA_RE.search(text or ""):
            signals.append("GA announcement")
        if BREAKING_RE.search(text or ""):
            signals.append("breaking-change flagged")
        m = MAJOR_RELEASE_RE.search(title or "")
        if m and not PRE_GA_RE.search(title or ""):
            signals.append(f"major release ({m.group(0).lstrip('v')})")
        return signals

    # -------------------------------------------------------------- assembly

    def signals_line(self, item: dict, cve_sources: dict) -> str:
        """Human-readable enrichment summary fed to the judge and the post."""
        title = item.get("title", "")
        text = f"{title} {item.get('summary', '')}"
        parts = []
        parts += self.eol_signals(text)
        parts += self.deadline_signals(text)
        parts += self.release_signals(title, text)

        cves = item.get("cves") or []
        if cves:
            kev = self.kev_set()
            for cve in cves:
                bits = []
                bits.append("CISA KEV: listed" if cve in kev else "CISA KEV: not listed")
                score = self._epss.get(cve)
                bits.append(f"EPSS {score:.2f}" if score is not None else "EPSS n/a")
                sources = cve_sources.get(cve, set())
                if len(sources) > 1:
                    bits.append(f"reported by {len(sources)} collected sources")
                parts.append(f"{cve} — " + ", ".join(bits))
        return " · ".join(parts)
