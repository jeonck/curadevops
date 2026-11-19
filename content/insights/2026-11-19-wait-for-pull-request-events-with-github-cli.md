---
title: "GitHub CLI v2.105.0 adds event-stream wait for pull requests"
date: 2026-11-19T19:16:29.978589+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["github-cli", "pull-requests", "automation"]
cves: []
source: "https://github.blog/changelog/2026-11-18-wait-for-pull-request-events-with-github-cli"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Plan:** GitHub CLI v2.105.0 introduces event-stream support so pipeline automation and release scripts can block on PR state changes without polling; worth adopting to simplify any workflow that currently loops on `gh pr view` to detect merges or reviews.
- **Leader — Skip**
