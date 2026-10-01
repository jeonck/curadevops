---
title: "X25519-only TLS connections to GHE.com drop on October 7"
date: 2026-10-01T17:14:12.201245+00:00
verdict: "Act"
verdict_platform: "Act"
verdict_cicd: "Act"
verdict_leader: "Skip"
tags: ["github-enterprise", "tls", "deprecation"]
cves: []
source: "https://github.blog/changelog/2026-09-30-x25519-only-tls-ends-for-ghe-com-on-september-15"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Act:** If your org uses GitHub Enterprise Cloud with data residency, audit any internal tooling, Terraform GitHub provider clients, or API automation that may negotiate TLS using only X25519 before October 7 — connections from those clients will break.
- **CI/CD — Act:** Verify that CI runners and pipeline scripts connecting to GHE.com with data residency use a TLS stack that offers multiple key-agreement algorithms, not X25519 exclusively; the hard cutoff is October 7, 2026.
- **Leader — Skip**
