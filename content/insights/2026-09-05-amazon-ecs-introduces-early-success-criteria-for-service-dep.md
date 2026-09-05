---
title: "Amazon ECS adds Early Success Criteria for rolling deployments"
date: 2026-09-05T13:37:34.984053+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["ecs", "deployments", "progressive-delivery"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ecs-deployments-early-success/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA ECS capability worth evaluating this quarter, especially for GPU or other constrained-capacity workloads where task launch latency inflates deployment windows; review healthy-percent thresholds and source-revision cleanup mode (BLOCKING vs DEFERRED) for your services.
- **CI/CD — Plan:** ECS deployments can now signal success before full scale-out, directly unblocking downstream pipeline stages; plan to configure Early Success Criteria on services where slow task launches currently stall pipeline gates.
- **Leader — Skip**
