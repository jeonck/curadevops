---
title: "npm trusted publishing gains opt-in dist-tag permissions via OIDC"
date: 2026-10-01T17:14:12.201245+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["npm", "trusted-publishing", "supply-chain"]
cves: []
source: "https://github.blog/changelog/2026-09-30-opt-in-dist-tag-permissions-for-npm-trusted-publishing"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Plan:** New GA capability lets npm trusted publishing configs manage dist-tags (latest, next, beta promotion) with short-lived OIDC credentials instead of long-lived tokens — schedule adoption to reduce static secret exposure in publish workflows.
- **Leader — Skip**
