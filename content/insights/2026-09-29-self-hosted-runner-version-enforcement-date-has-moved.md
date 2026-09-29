---
title: "GitHub Actions self-hosted runner version enforcement date shifts"
date: 2026-09-29T16:42:54.308653+00:00
verdict: "Act"
verdict_platform: "Skip"
verdict_cicd: "Act"
verdict_leader: "Skip"
tags: ["github-actions", "self-hosted-runners", "version-enforcement"]
cves: []
source: "https://github.blog/changelog/2026-09-28-self-hosted-runner-version-enforcement-date-has-moved"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Act:** Minimum version enforcement for self-hosted runners on GitHub Enterprise Cloud took effect September 28, 2026; audit all self-hosted runner instances immediately and upgrade any falling below the new minimum version to prevent pipeline failures across every team using them.
- **Leader — Skip**
