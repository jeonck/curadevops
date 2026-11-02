---
title: "GitHub Actions blocks pull_request_target by default Dec 2"
date: 2026-11-02T20:36:17.574365+00:00
verdict: "Act"
verdict_platform: "Skip"
verdict_cicd: "Act"
verdict_leader: "Skip"
tags: ["github-actions", "pipeline-security", "deprecation"]
cves: []
source: "https://github.blog/changelog/2026-11-02-pull_request_target-blocked-by-default-december-2"
source_name: "GitHub Changelog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Act:** Audit all public-repo workflows for `pull_request_target` triggers and ensure an explicit Actions event policy allows them before December 2, 2026, or those pipelines will be blocked silently.
- **Leader — Skip**
