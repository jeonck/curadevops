---
title: "GitHub Actions auto-holds suspicious workflows for approval"
date: 2026-07-29T12:56:53.259576+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Plan"
verdict_leader: "Learn"
tags: ["github-actions", "supply-chain", "security"]
cves: []
source: "https://github.blog/changelog/2026-07-28-github-actions-holds-potentially-malicious-workflows-for-approval"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Plan:** GitHub now holds potentially malicious workflow runs for review in public repositories; audit your org's Actions approval settings and ensure maintainers understand how to review held runs before merging external contributions.
- **Leader — Learn:** GitHub's new default protection against credential-stealing workflow attacks reduces supply-chain risk for orgs using public repos; worth noting as a positive vendor-risk signal when assessing GitHub Actions dependency.
