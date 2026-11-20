---
title: "AWS CloudFormation StackSets adds custom execution roles and nested stack support"
date: 2026-11-20T18:55:43.487400+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["cloudformation", "aws", "iam"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/stacksets-custom-execution-roles/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability lets you scope StackSets permissions per target account via a least-privilege execution role, while also unlocking nested stacks and macros in service-managed deployments. Evaluate adopting custom execution role templates this quarter to harden multi-account IaC permissions rather than relying on the broad default role.
- **CI/CD — Skip**
- **Leader — Learn:** New StackSets execution role support enables least-privilege multi-account IaC deployments, which could inform a future security standard for org-wide CloudFormation use; no licensing, cost, or vendor-risk change is involved.
