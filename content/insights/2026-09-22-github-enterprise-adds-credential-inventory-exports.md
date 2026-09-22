---
title: "GitHub Enterprise adds credential inventory exports"
date: 2026-09-22T15:18:39.517003+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Learn"
verdict_leader: "Plan"
tags: ["github-enterprise", "credential-management", "supply-chain-security"]
cves: []
source: "https://github.blog/changelog/2026-09-21-github-enterprise-adds-credential-inventory-exports"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Learn:** A full exportable inventory of SSH keys, PATs, and OAuth tokens touching the enterprise is useful context for supply-chain hygiene thinking, but it introduces no pipeline mechanic to change today.
- **Leader — Plan:** Schedule a review of GitHub Enterprise credential inventory exports as part of your next access-review or compliance cycle; the capability directly supports audit readiness for SOC 2 / ISO 27001 controls around privileged access.
