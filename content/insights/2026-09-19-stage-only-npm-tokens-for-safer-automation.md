---
title: "GitHub adds stage-only scope for npm granular access tokens"
date: 2026-09-19T14:03:42.839126+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["npm", "supply-chain", "token-security"]
cves: []
source: "https://github.blog/changelog/2026-09-18-stage-only-npm-tokens-for-safer-automation"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Plan:** Adopt the new 'stage only' permission when minting npm automation tokens to enforce least-privilege publishing; schedule a rotation of existing CI npm tokens to apply the tighter scope and reduce blast radius from a leaked credential.
- **Leader — Skip**
