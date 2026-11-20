---
title: "Argo CD self-heal can silently skip sync hooks during deny windows"
date: 2026-11-20T18:55:43.487400+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["argo-cd", "gitops", "deployment-hooks"]
cves: []
source: "https://www.cncf.io/blog/2026/11/20/when-a-sync-window-closes-how-argo-cd-self-heal-skipped-the-migration-hook/"
source_name: "CNCF Blog"
status: "active"
---
- **Platform/SRE — Learn:** Documents a non-obvious Argo CD behavior: self-heal triggering within a sync deny window can mark a sync successful while skipping pre/post hooks like database migration jobs. Worth reviewing if you rely on Argo CD hooks for stateful operations.
- **CI/CD — Learn:** If your release process uses Argo CD sync hooks to run migrations or ordered steps, this case study reveals a gap where self-heal plus a deny window can silently bypass those hooks — worth auditing your hook design against this pattern.
- **Leader — Skip**
