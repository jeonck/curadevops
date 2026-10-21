---
title: "DynamoDB global tables now support replica disassociation without data loss"
date: 2026-10-21T15:46:15.304693+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["dynamodb", "multi-region", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/dynamodb-global-tables-disassociate/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** This new GA capability lets platform teams detach a DynamoDB replica into a standalone single-region table without recreating it — useful for regional isolation, offboarding a region, or audit scenarios. Worth evaluating if your platform runs global tables and needs cleaner multi-region lifecycle management.
- **CI/CD — Skip**
- **Leader — Learn:** Adds flexibility to multi-region DynamoDB architectures (including multi-account global tables), which may inform future data residency or regional isolation decisions, but no strategic action is required now.
