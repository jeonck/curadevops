---
title: "Node 20 removed from GitHub Actions runners, Node 24 now default"
date: 2026-09-24T15:37:11.888748+00:00
verdict: "Act"
verdict_platform: "Skip"
verdict_cicd: "Act"
verdict_leader: "Skip"
tags: ["github-actions", "node-runtime", "breaking-change"]
cves: []
source: "https://github.blog/changelog/2026-09-23-node-20-is-no-longer-available-in-github-actions"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Act:** Node 20 is already gone from GitHub Actions runners and the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION escape hatch is also removed, meaning any JavaScript actions still targeting Node 20 are broken now. Audit all JavaScript actions in your pipelines and update them to Node 24 compatibility immediately.
- **Leader — Skip**
