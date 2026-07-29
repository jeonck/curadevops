---
title: "Docker: AI coding agents risk exposing secrets in supply chain attacks"
date: 2026-07-29T12:56:53.259576+00:00
verdict: "Learn"
verdict_platform: "Skip"
verdict_cicd: "Learn"
verdict_leader: "Learn"
tags: ["supply-chain-security", "ai-agents", "secrets-management"]
cves: []
source: "https://www.docker.com/blog/coding-agent-horror-stories-the-29-million-secret-problem/"
source_name: "Docker Blog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Learn:** Vendor-authored post highlighting how AI coding agents can leak credentials into build/deploy contexts; worth evaluating your secret isolation controls if agents touch pipelines, but no concrete deadline or confirmed compromise here.
- **Leader — Learn:** Surfaces a real risk category—AI agent access to secrets in the software supply chain—worth factoring into your AI tooling policy and golden-path standards, though this is Docker marketing with no specific incident or actionable deadline.
