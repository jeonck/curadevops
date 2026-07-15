---
title: "AWS DRS adds EBS volume initialization rate for faster recovery"
date: 2026-07-15T12:10:55.908816+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws", "disaster-recovery", "ebs"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-drs-fast-hydration/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Teams running I/O-intensive workloads (databases, etc.) on AWS DRS should evaluate setting an EBS initialization rate on DRS launch templates to reduce time-to-full-performance during recovery drills — no deadline, but worth scheduling as a DR configuration review this quarter.
- **CI/CD — Skip**
- **Leader — Skip**
