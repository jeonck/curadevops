---
title: "Amazon ECS Managed Daemons add non-critical daemon support"
date: 2026-09-04T14:38:54.847255+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["ecs", "aws", "observability"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/ecs-managed-daemons-non-critical/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Teams running ECS with Managed Daemons for logging or metrics collection should evaluate configuring auxiliary daemons as non-critical to prevent churn on mission-critical tasks; no deadline, but worth adopting this quarter when reviewing ECS daemon configurations.
- **CI/CD — Skip**
- **Leader — Skip**
