---
title: "GitHub deprecates CodeQL all-platform bundle starting CLI 2.27.0"
date: 2026-09-22T15:18:39.517003+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["codeql", "security-scanning", "deprecation"]
cves: []
source: "https://github.blog/changelog/2026-09-22-deprecation-notice-all-platform-codeql-bundle"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Plan:** Pipelines that download codeql-bundle.tar.gz or .tar.zst need to migrate to platform-specific CodeQL bundles; no hard removal date announced yet, so audit your CodeQL download steps and update references to the appropriate per-platform bundle this quarter.
- **Leader — Skip**
- **Signals:** deprecation mentioned (no explicit date found)
