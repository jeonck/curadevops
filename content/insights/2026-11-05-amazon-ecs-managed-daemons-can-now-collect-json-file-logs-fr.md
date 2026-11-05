---
title: "Amazon ECS Managed Daemons add json-file log driver support for log collection"
date: 2026-11-05T18:24:13.891932+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["ecs", "observability", "logging"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ecs-managed-instances-json-file-log-driver/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If you run ECS Managed Instances, this new GA capability lets a single managed daemon collect logs from all application containers via volume mount — without root or host bind paths. Worth evaluating this quarter as a cleaner alternative to current sidecar or host-mount log collection patterns.
- **CI/CD — Skip**
- **Leader — Skip**
