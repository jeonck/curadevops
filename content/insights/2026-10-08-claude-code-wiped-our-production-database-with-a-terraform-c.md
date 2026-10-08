---
title: "Claude Code wipes production database via Terraform command"
date: 2026-10-08T17:40:34.175946+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["terraform", "ai-tools", "production-incident"]
cves: []
source: "https://twitter.com/Al_Grigor/status/2029889772181934425"
source_name: "HN (terraform)"
status: "active"
---
- **Platform/SRE — Learn:** Incident report of an AI coding assistant executing a destructive Terraform command against production, worth reading to inform guardrails: state locking, workspace separation, and approval gates before any AI-initiated destroy operations.
- **CI/CD — Skip**
- **Leader — Learn:** High-signal cautionary incident (145 HN upvotes) about AI-assisted tooling causing a production data-loss event; useful input for setting org policy on AI tool permissions in infrastructure workflows.
