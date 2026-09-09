---
title: "Dependabot gains automatic access to private GitHub Packages registries"
date: 2026-09-09T14:56:08.335953+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["dependabot", "github-packages", "supply-chain"]
cves: []
source: "https://github.blog/changelog/2026-09-08-automatic-dependabot-access-to-github-hosted-registries"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Plan:** Dependabot can now pull from private GitHub Packages registries without a PAT, using the existing 'Manage Actions access' permission — evaluate removing hardcoded tokens from Dependabot config to simplify credential management and reduce secret sprawl.
- **Leader — Skip**
