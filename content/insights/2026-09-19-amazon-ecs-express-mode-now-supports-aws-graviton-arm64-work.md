---
title: "Amazon ECS Express Mode adds ARM64/Graviton support"
date: 2026-09-19T14:03:42.839126+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Plan"
tags: ["ecs", "graviton", "arm64"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ecs-express-mode-arm-architecture/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** ECS Express Mode now supports ARM64 as a GA option, enabling Graviton-powered workloads with up to 40% better price-performance. Worth evaluating as an architecture choice for new or cost-sensitive services this quarter, with no deadline pressure.
- **CI/CD — Skip**
- **Leader — Plan:** Graviton ARM64 support in ECS Express Mode represents a concrete FinOps opportunity — evaluate adopting Graviton as part of the standard compute profile to capture the claimed 40% price-performance improvement in this quarter's platform roadmap.
