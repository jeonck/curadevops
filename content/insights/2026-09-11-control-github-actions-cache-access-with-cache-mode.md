---
title: "GitHub Actions cache-mode enables least-privilege cache access"
date: 2026-09-11T14:43:59.795234+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["github-actions", "supply-chain", "least-privilege"]
cves: []
source: "https://github.blog/changelog/2026-09-10-control-github-actions-cache-access-with-cache-mode"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Plan:** New GA GitHub Actions feature lets you scope cache read/write permissions per workflow or job, reducing blast radius of a compromised workflow. Evaluate and adopt cache-mode across pipelines this quarter as a supply-chain hardening step.
- **Leader — Skip**
