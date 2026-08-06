---
title: "GitHub code scanning default setup now supports custom CodeQL config at scale"
date: 2026-08-06T12:51:55.355481+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Plan"
verdict_leader: "Plan"
tags: ["github-actions", "code-scanning", "supply-chain"]
cves: []
source: "https://github.blog/changelog/2026-08-04-customize-code-scanning-default-setup-at-scale"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Plan:** If your org uses GitHub code scanning default setup, evaluate adopting the new github-codeql-config-file repository property to standardize CodeQL scan behavior across repos without per-repo overrides.
- **Leader — Plan:** This enables centralized enforcement of code scanning standards across the org's repositories — worth incorporating into the golden path or security policy for teams already on GitHub Advanced Security.
