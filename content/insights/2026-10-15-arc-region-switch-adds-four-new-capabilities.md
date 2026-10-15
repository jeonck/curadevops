---
title: "AWS ARC Region Switch gains SSM, quota checks, and target health blocks"
date: 2026-10-15T15:27:57.001735+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["disaster-recovery", "aws-arc", "multi-region"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/region-switch-target-health-ssm-lambda/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** The new service quota parity checks and wait-for-target-group-health blocks directly address common multi-region failover failure modes; platform teams using ARC Region switch should evaluate updating their recovery plans to incorporate these execution blocks this quarter.
- **CI/CD — Skip**
- **Leader — Skip**
