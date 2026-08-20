---
title: "CloudWatch Log Centralization adds tag propagation to destination log groups"
date: 2026-08-20T11:19:17.091246+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["cloudwatch", "observability", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudwatch-centralization-tag-propogation/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Teams using CloudWatch Centralization can now preserve cost, ownership, and compliance tags across accounts — worth enabling tag propagation on existing centralization rules to unlock IAM scoping and per-team cost attribution in Cost Explorer.
- **CI/CD — Skip**
- **Leader — Learn:** Tag propagation on centralized logs enables per-team observability cost attribution out of the box, which may inform how your org structures log ownership and FinOps reporting for multi-account environments.
