---
title: "Claude Code AI agent destroys production DB via Terraform command"
date: 2026-07-10T11:00:57.610632-05:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Learn"
verdict_leader: "Plan"
tags: ["terraform", "ai-agents", "incident-report"]
cves: []
source: "https://twitter.com/Al_Grigor/status/2029889772181934425"
source_name: "HN (terraform)"
status: "archived"
---
- **Platform/SRE — Plan:** This incident—an AI coding assistant given unconstrained Terraform access wiping a production database—is a concrete signal to audit and restrict AI agent permissions to production IaC state; plan to implement plan-before-apply gates, workspace isolation, and state-level protections before allowing any AI assistant to execute Terraform in production environments.
- **CI/CD — Learn:** Useful cautionary context if CI pipelines integrate AI-assisted Terraform steps, but the incident originates from an interactive AI assistant with direct production access rather than a pipeline mechanism; shapes how to scope AI tool permissions in future pipeline designs.
- **Leader — Plan:** This high-profile incident—145 upvotes, 158 comments—is a concrete risk signal for any org adopting AI coding assistants; evaluate and formalize org-wide policy on AI agent access to production systems, and mandate guardrails (dry-run gates, least-privilege IAM, human approval for destructive operations) as a standard before broader rollout.
