---
title: "Actions Runner Controller 0.15.0: reliability and scalability improvements"
date: 2026-10-01T17:14:12.201245+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["github-actions", "kubernetes", "runner-controller"]
cves: []
source: "https://github.blog/changelog/2026-10-01-actions-runner-controller-release-0-15-0"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Plan:** ARC runs on Kubernetes clusters you operate; the 0.15.0 improvements to runner scale-set reliability during cluster upgrades are worth evaluating and scheduling for adoption this quarter. No deadline or security fix in the signals.
- **CI/CD — Plan:** If you operate self-hosted GitHub Actions runners via ARC, 0.15.0 brings reliability and observability gains for large runner fleets — worth scheduling an upgrade to reduce disruption during runner or cluster maintenance windows.
- **Leader — Skip**
