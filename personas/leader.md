# Persona: Engineering / Platform Leader

## Who this is
The person accountable for the DevOps/platform **function** rather than any single
system. Typical titles: Platform Engineering Manager, Head of Infrastructure,
Director of DevOps/SRE, VP Engineering (infra-leaning), Staff/Principal Platform
Architect. They set the toolchain strategy, own the infrastructure budget,
negotiate vendor contracts, define standards teams must follow, and answer to
their own leadership for reliability, cost, and delivery speed. They do not merge
the pipeline fix — they decide whether the org should be on that tool at all.

## Environment assumptions
- Owns a **portfolio of tools and vendors**, not one system: cloud providers,
  CI/CD platforms, observability and IaC vendors, container platforms, and the
  build-vs-buy line between them.
- Owns a **budget** and watches unit economics: cloud spend, per-seat SaaS
  licensing, data-egress and observability-ingestion costs, FinOps.
- Owns **standards and org direction**: golden paths, the internal developer
  platform strategy, reliability targets (SLOs), and hiring/skills planning.
- Cares about **vendor risk and lock-in**: licensing changes (e.g. an
  open-source project relicensing, a fork gaining/losing momentum), acquisitions,
  pricing-model shifts, and the long-term viability of a tool the org depends on.
- Their decision horizon is quarters to years, not the next patch window.

## What they must decide from each item
"Does this change our **toolchain strategy, cost, vendor risk, standards, or
skills plan** — do I need to reconsider what we standardize on, renegotiate, or
brief my own leadership?"

## Verdict criteria
- **Act** — a strategic or contractual fact that forces a leadership decision now:
  - a **license change / relicensing / acquisition / EOL-of-product** for a tool
    the org is standardized on (e.g. a core OSS tool going source-available, a
    vendor being acquired and sunsetting a product) — forcing a migration or
    renegotiation decision;
  - a **material, non-optional cost or pricing-model change** on a vendor in the
    stack;
  - a widely-reported **security or reliability failure of a vendor** the org
    depends on that warrants a risk review or a note to their own leadership.
  The note must name the leadership action: "evaluate migrating off <tool> before
  the license takes effect", "reassess the <vendor> contract given the new
  pricing", "brief leadership on <vendor> outage exposure".
- **Plan** — strategically relevant, decide within a quarter/planning cycle: a
  maturing tool or standard worth **evaluating for the golden path**; a market
  shift (a fork gaining momentum, a new managed offering) that may change a
  build-vs-buy call later; an emerging cost-optimization or FinOps opportunity;
  an industry standard (supply-chain, reliability) to adopt as policy.
- **Learn** — shapes their **mental model / strategy thinking** but no decision
  pending: adoption-trend reports, notable platform-engineering case studies,
  a State-of-DevOps/benchmark finding, an interesting org-design or reliability
  essay.
- **Skip** — implementation-level detail with no strategy, cost, or vendor-risk
  angle (a specific patch or pipeline fix is the engineers' concern, not theirs);
  vendor marketing; re-announcements with no new strategic fact.

## What they do NOT care about (do not inflate verdicts for these)
- Individual patches, version bumps, API removals, or pipeline fixes with no
  budget/vendor/standards implication — those are Platform or CI/CD, and should
  be **Skip** for the Leader even when they're Act for an engineer. This is the
  most common inflation error: a routine CVE patch is not a leadership item.
- Deep technical tutorials or how-to content with no strategic takeaway.
- Hype about pre-GA tech with no near-term adoption decision (Learn at most).
