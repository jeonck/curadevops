---
title: "AWS EC2 Auto Scaling adds account-level Launch Before Terminate default"
date: 2026-10-27T16:07:53.688542+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws", "auto-scaling", "availability"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/ec2-auto-scaling-launch-before-terminate/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability lets you enable Launch Before Terminate once at the account level via PutAccountSetting, ensuring full capacity is maintained during instance refreshes, rebalancing, and health-check replacements across all ASGs. Worth scheduling a review and enabling this quarter to reduce availability risk during replacement events.
- **CI/CD — Skip**
- **Leader — Skip**
