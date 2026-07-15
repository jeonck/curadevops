---
title: "Dependabot adds 3-day cooldown before opening version update PRs"
date: 2026-07-15T12:10:55.908816+00:00
verdict: "Learn"
verdict_platform: "Skip"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["dependabot", "supply-chain", "github-actions"]
cves: []
source: "https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Learn:** Dependabot's new default 3-day cooldown before raising version-update PRs reduces noise from yanked or quickly-patched releases; no pipeline changes required, but worth understanding if teams rely on same-day dependency PRs.
- **Leader — Skip**
