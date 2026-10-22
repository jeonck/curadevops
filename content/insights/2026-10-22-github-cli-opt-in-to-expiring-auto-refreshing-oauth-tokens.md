---
title: "GitHub CLI: opt-in expiring OAuth tokens now in public preview"
date: 2026-10-22T15:46:09.169989+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["github-cli", "oauth", "security"]
cves: []
source: "https://github.blog/changelog/2026-10-21-github-cli-opt-in-to-expiring-auto-refreshing-oauth-tokens"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Learn:** Pre-GA preview of short-lived, auto-refreshing OAuth tokens in gh CLI; worth tracking if your teams use GitHub CLI for scripted infra workflows, but no action warranted until GA.
- **CI/CD — Learn:** Expiring tokens would improve credential hygiene for pipelines that invoke gh CLI, but this is public preview — evaluate once it reaches GA before updating pipeline auth patterns.
- **Leader — Skip**
