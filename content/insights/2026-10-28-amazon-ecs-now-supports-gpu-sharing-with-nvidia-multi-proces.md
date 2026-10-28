---
title: "Amazon ECS adds GPU sharing via NVIDIA MPS for multi-task GPU workloads"
date: 2026-10-28T16:55:14.213180+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["amazon-ecs", "gpu-sharing", "infrastructure-cost"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ecs-gpu-sharing-nvidia-mps/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** GA feature that meaningfully changes GPU capacity planning on ECS — teams running small-model inference or multi-model serving should evaluate adopting MPS sharing to improve GPU utilization and reduce per-workload instance costs this quarter.
- **CI/CD — Skip**
- **Leader — Learn:** GPU workload cost density improvement is worth noting for teams with ML inference spend on ECS, but adoption is optional and operational — no strategic vendor, licensing, or pricing-model decision required.
