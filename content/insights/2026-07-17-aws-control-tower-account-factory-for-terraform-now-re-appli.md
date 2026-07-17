---
title: "AWS AFT auto re-applies customizations on account OU moves"
date: 2026-07-17T12:03:24.897479+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws-control-tower", "account-factory-terraform", "multi-account"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-control-tower-account/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Teams using AFT to manage multi-account AWS environments should evaluate enabling `aft_customization_triggers = ["account_move"]` this quarter to eliminate manual re-application steps and reduce compliance drift when accounts change OUs. No deadline, but the tighter logging bucket controls and enterprise-scale improvements are also worth reviewing alongside the opt-in.
- **CI/CD — Skip**
- **Leader — Skip**
