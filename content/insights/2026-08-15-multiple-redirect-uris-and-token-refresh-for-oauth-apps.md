---
title: "GitHub OAuth Apps gain multiple redirect URIs and token refresh"
date: 2026-08-15T11:12:44.845201+00:00
verdict: "Learn"
verdict_platform: "Skip"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["oauth", "github", "security"]
cves: []
source: "https://github.blog/changelog/2026-08-14-multiple-redirect-uris-and-token-refresh-for-oauth-apps"
source_name: "GitHub Changelog"
status: "archived"
---
- **Platform/SRE — Skip**
- **CI/CD — Learn:** If pipelines use GitHub OAuth Apps for automation or registry auth, expiring tokens and refresh support may require updates to credential flows — worth evaluating when authoring new integrations.
- **Leader — Skip**
