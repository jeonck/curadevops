---
title: "CloudWatch agent gains native journald log collection on Linux"
date: 2026-08-28T21:17:44.564118+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["cloudwatch", "observability", "journald"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudwatch-agent-journald/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Teams running Amazon Linux 2023 or other systemd-only distros no longer need disk-export workarounds to ship structured journal logs to CloudWatch. Update the CloudWatch agent to the latest version and add a journald config block to consolidate logging for those instances this quarter.
- **CI/CD — Skip**
- **Leader — Skip**
