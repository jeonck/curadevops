---
title: "Amazon ECS adds LiveTaskCount metric; RunningTaskCount now free in Container Insights"
date: 2026-10-14T15:39:00.930991+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws-ecs", "observability", "autoscaling"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/ecs-service-metrics/"
source_name: "AWS What's New"
status: "archived"
---
- **Platform/SRE — Learn:** LiveTaskCount covers tasks in ACTIVATING, RUNNING, and DEACTIVATING states, making it a more complete signal for autoscaling policies than RunningTaskCount; worth evaluating when next tuning ECS autoscaling or capacity planning, but no existing configuration requires updating.
- **CI/CD — Skip**
- **Leader — Skip**
