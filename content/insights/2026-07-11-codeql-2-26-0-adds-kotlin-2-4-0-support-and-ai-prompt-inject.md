---
title: "CodeQL 2.26.0 adds Kotlin 2.4.0 support and AI prompt injection detection"
date: 2026-07-11T15:50:13.633791+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["static-analysis", "security", "github-actions"]
cves: []
source: "https://github.blog/changelog/2026-07-10-codeql-2-26-0-adds-kotlin-2-4-0-support-and-ai-prompt-injection-detection"
source_name: "GitHub Changelog"
status: "archived"
---
- **Platform/SRE — Skip**
- **CI/CD — Plan:** If pipelines run CodeQL scanning on Kotlin 2.4.0 codebases, upgrade to CodeQL 2.26.0 this quarter to maintain scan coverage; the new AI prompt injection queries are worth enabling if building LLM-integrated apps.
- **Leader — Skip**
