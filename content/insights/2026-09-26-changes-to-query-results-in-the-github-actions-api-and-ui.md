---
title: "GitHub Actions API/UI workflow run query counts now less precise"
date: 2026-09-26T14:49:11.187076+00:00
verdict: "Learn"
verdict_platform: "Skip"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["github-actions", "api-change", "ci-cd"]
cves: []
source: "https://github.blog/changelog/2026-09-25-changes-to-query-results-in-the-github-actions-api-and-ui"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Learn:** Workflow run count queries in the GitHub Actions API and UI now return approximate rather than exact counts; worth reviewing if your pipelines or dashboards rely on precise record counts from these endpoints.
- **Leader — Skip**
