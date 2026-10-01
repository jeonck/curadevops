---
title: "GitHub scheduled code scanning now skips inactive repositories"
date: 2026-10-01T17:14:12.201245+00:00
verdict: "Learn"
verdict_platform: "Skip"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["github-actions", "code-scanning", "security"]
cves: []
source: "https://github.blog/changelog/2026-10-01-scheduled-code-scanning-skips-inactive-repositories"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Learn:** GitHub's scheduled code scanning now requires a prior push or PR to activate weekly scans, which may silently drop coverage on dormant repos; review which repos rely on scheduled-only scanning to avoid gaps.
- **Leader — Skip**
