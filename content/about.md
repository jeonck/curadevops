---
title: "About CuraDevOps"
---
## What this is

CuraDevOps is a daily, AI-curated DevOps intelligence channel. Most DevOps
news tells you *what was released*; CuraDevOps tells you **who should do what,
now** — every item gets three independent verdicts, one per practitioner
persona:

| Persona | Judged on |
|---|---|
| **Platform/SRE** (Infrastructure/Cloud) | upgrades, migrations, EOL exposure, operational impact |
| **CI/CD** (Build/Release/DevEx) | pipeline changes, supply-chain integrity, build/deploy mechanics |
| **Leader** (Platform/Eng Management) | toolchain strategy, licensing, vendor risk, cost |

## The verdicts

| Verdict | Meaning |
|---|---|
| **Act** | do or check something now (imminent EOL, dated deprecation, supply-chain compromise, exploited CVE) |
| **Plan** | review within the quarter (announced breaking changes, new GA capabilities, migrations) |
| **Learn** | worth knowing, no action required |
| **Skip** | not published — marketing, routine patch releases, duplicates |

Items judged Skip for *all three* personas are never published. A zero-Act day
is normal — genuine urgency is rare in DevOps, and this channel does not
manufacture it.

## How verdicts are made

1. **Collection** — RSS (Kubernetes, CNCF, GitHub Changelog, GitLab, HashiCorp,
   Docker, Grafana, AWS/GCP/Azure release feeds), Hacker News, Reddit, and
   GitHub, daily at 11:00 UTC. A weekly Release Radar scans minor/major
   releases of ~20 core open-source repos. Routine patch releases and
   pre-release tags are filtered out before judgment.
2. **Enrichment** — every product+version mention is cross-referenced against
   the [endoflife.date](https://endoflife.date) EOL calendar; deprecation
   deadlines are extracted from the text; release maturity (pre-GA/GA),
   breaking-change flags, and major-version signals are detected; CVEs, when
   present, are checked against CISA KEV and EPSS.
3. **Judgment** — Claude (Anthropic) judges each item against
   [context.md](https://github.com/jeonck/curadevops/blob/main/context.md) and
   the [persona definitions](https://github.com/jeonck/curadevops/tree/main/personas),
   producing a verdict and a 1–2 sentence evidence-based note per persona.

## Trust principles

- **AI disclosure** — every post and page states that curation and verdicts are
  automated. There is no human editor writing these judgments.
- **Evidence required** — every non-Skip verdict carries its reasoning and the
  enrichment signals it was based on. Act verdicts require a concrete anchor
  (a date, an exploited CVE, a confirmed compromise) — never invented urgency.
- **Corrections log** — confirmed misjudgments are recorded on the
  [corrections page](../corrections/), not silently edited.
- **Human review period** — during the channel's first 30 days, a human reviews
  published verdicts daily and corrects errors.

Verdicts are starting points, not authoritative guidance — always verify
against the original source before acting.

## Feedback

Bad verdict? Broken source? Open an issue on
[GitHub](https://github.com/jeonck/curadevops/issues).
