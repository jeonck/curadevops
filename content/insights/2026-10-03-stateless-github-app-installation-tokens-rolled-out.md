---
title: "GitHub App installation tokens now fully stateless format"
date: 2026-10-03T15:01:20.079187+00:00
verdict: "Plan"
verdict_platform: "Learn"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["github", "authentication", "ci-cd"]
cves: []
source: "https://github.blog/changelog/2026-10-02-stateless-github-app-installation-tokens-rolled-out"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Learn:** Infrastructure automation using GitHub App tokens (e.g., Flux, Argo CD, Terraform GitHub provider) should still work without changes, but teams relying on token introspection or format-specific parsing should verify compatibility with the new stateless format.
- **CI/CD — Plan:** The rollout is complete, so all newly minted GitHub App installation tokens already use the stateless format; audit any pipeline code or tooling that parses or makes structural assumptions about token format to confirm nothing breaks.
- **Leader — Skip**
