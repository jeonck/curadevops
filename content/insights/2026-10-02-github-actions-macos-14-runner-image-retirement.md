---
title: "GitHub Actions macOS 14 runner image retires November 2, 2026"
date: 2026-10-02T16:25:37.540030+00:00
verdict: "Act"
verdict_platform: "Skip"
verdict_cicd: "Act"
verdict_leader: "Skip"
tags: ["github-actions", "runner-images", "cicd"]
cves: []
source: "https://github.blog/changelog/2026-10-01-github-actions-macos-14-runner-image-retirement"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Act:** Any pipeline referencing the macOS 14 runner label will fail when GitHub begins pre-retirement disruption runs, then permanently break on November 2, 2026. Audit all workflow files and replace 'macos-14' with 'macos-15' (or another supported image) before that date.
- **Leader — Skip**
- **Signals:** deprecation/EOL deadline mentioned: November 2, 2026
