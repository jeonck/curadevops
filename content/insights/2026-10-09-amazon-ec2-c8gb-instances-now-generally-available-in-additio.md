---
title: "Amazon EC2 C8gb (Graviton4) instances GA in additional regions"
date: 2026-10-09T17:15:30.772048+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws-ec2", "graviton", "compute"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ec2-c8gb/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA instance type offering 30% better compute than Graviton3 and higher EBS bandwidth (up to 300 Gbps / 1.6M IOPS) is worth evaluating this quarter for EBS-bound workloads like high-performance file systems; no forced migration, just an adoption decision.
- **CI/CD — Skip**
- **Leader — Learn:** Graviton4-based C8gb instances improve the performance-per-dollar profile for compute and storage-intensive workloads, useful background for future FinOps or Graviton migration conversations, but no strategic decision is forced now.
- **Signals:** GA announcement
