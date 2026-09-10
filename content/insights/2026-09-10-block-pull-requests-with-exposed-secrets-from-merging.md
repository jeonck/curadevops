---
title: "GitHub repo rulesets can now block PRs that introduce exposed secrets"
date: 2026-09-10T14:43:05.673701+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Plan"
verdict_leader: "Plan"
tags: ["secret-scanning", "github", "supply-chain-security"]
cves: []
source: "https://github.blog/changelog/2026-09-09-block-pull-requests-with-exposed-secrets-from-merging"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Plan:** New GA GitHub capability lets teams enforce secret-blocking via repository rulesets; schedule a rollout to enable this across all repos as a supply-chain hardening step this quarter.
- **Leader — Plan:** This is a concrete org-wide policy lever — evaluate mandating the new secret-blocking ruleset as a standard across all GitHub repositories to reduce credential-leak risk at the merge gate.
