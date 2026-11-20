---
title: "AWS EC2 T9g (Graviton5) instances now GA with 45% better price-perf vs T4g"
date: 2026-11-20T18:55:43.487400+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Plan"
tags: ["ec2", "graviton", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/ec2-t9g-instances-ga/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA burstable instance type with the same CPU credit model as T4g makes in-place upgrades low-risk; evaluate migrating T4g workloads (dev/staging, login gateways, small services) this quarter to capture the price-performance improvement.
- **CI/CD — Skip**
- **Leader — Plan:** A 45% price-performance gain over T4g with no credit-model change is a credible FinOps opportunity; add an EC2 instance-family review to the next cost-optimization planning cycle to quantify TCO impact across T4g workloads.
- **Signals:** GA announcement
