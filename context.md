# CuraDevOps Channel Context

> This file plus the three persona files (personas/*.md) form the judgment
> criteria. This section defines channel-wide rules; each persona file defines
> that persona's verdict criteria.

## Channel mission

CuraDevOps is a public curation channel for DevOps and platform practitioners
(US/global audience). Its value is the **actionable verdict**: for every item,
each of three personas — Platform/SRE Engineer, CI/CD & Release Engineer,
Engineering/Platform Leader — gets an independent verdict
(Act / Plan / Learn / Skip) with evidence-based reasoning. Readers already
subscribe to changelogs, DevOps Weekly, and vendor blogs; CuraDevOps's job is
the cross-referenced judgment **with deadlines**, not re-delivery of release
notes.

## Channel-wide Skip rules (apply to all personas)

Skip for every persona when the item is:
- vendor marketing, product launches without substance, webinars, awards,
  conference booth coverage, or sponsored content
- a **patch-level release** (x.y.Z) with no security fix, no breaking change,
  and no notable regression
- a re-announcement of an already-covered release/deprecation with no new
  version, date, or fact
- a funding/valuation announcement with no product or licensing consequence yet
- regional/local news with no relevance to a US/global engineering audience
- job postings, event announcements, personal-productivity or career-advice
  content

## Evidence discipline

- Prefer verdicts anchored in the enrichment signals: an **EOL/support date**
  (endoflife.date), an extracted **deprecation deadline**, a **semver major
  bump** or breaking-change flag, KEV/EPSS when CVEs are present, and
  multi-source corroboration.
- **Never invent urgency.** Act requires a concrete anchor in the item or the
  signals — a date, an active exploitation report, or a confirmed supply-chain
  compromise. If no deadline exists anywhere, the ceiling is Plan.
- **A zero-Act day is normal and healthy.** Genuine Act items are rare in
  DevOps (target distribution: Act 5–10%, Plan ~30%, Learn ~40%, Skip 20–30%).
  Do not promote Plan items to Act to make the channel look urgent.
- **Pre-GA is capped at Learn.** Alpha/beta/RC/experimental features are never
  Act or Plan for any persona.
- Never invent facts not present in the item or the signals. When the summary
  is too thin to judge, lean toward Learn or Skip rather than guessing.
- Notes must be original phrasing; quote at most one short sentence from the
  source (copyright rule).

## Verdict calibration examples

These canonical items define the persona boundaries. Verdicts should often
diverge across personas — never copy one verdict to all three by default.

| Item | Platform | CI/CD | Leader |
|---|---|---|---|
| Managed Kubernetes version EOL with forced-upgrade date | **Act** | Skip | Skip |
| KEV-listed CVE in ingress-nginx / a service mesh | **Act** | Skip | Skip |
| Routine CVE patch in infra software, no exploitation, no KEV | Plan | Skip | Skip |
| Backdoored popular GitHub Action / malicious npm package wave | Skip | **Act** | Skip |
| CI runner image retirement with a dated migration deadline | Skip | **Act** | Skip |
| Core IaC tool relicensed (open source → source-available) | Plan | Skip | **Act** |
| Major vendor pricing-model change on a standard-stack product | Skip | Skip | **Act** |
| New GA build-cache / provenance feature in a major CI platform | Skip | Plan | Skip |
| New GA managed-service capability changing platform architecture | Plan | Skip | Learn |
| eBPF observability benchmark / scaling post-mortem | Learn | Skip | Skip |
| State of DevOps–style industry report | Skip | Skip | Learn |
| Alpha/experimental feature announcement in any tool | Learn | Learn | Skip |
