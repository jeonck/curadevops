---
title: "Amazon ECS Action Logs adds deployment and daemon operation visibility"
date: 2026-07-22T12:23:02.611708+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["ecs", "observability", "deployment"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ecs-action-logs/"
source_name: "AWS What's New"
status: "archived"
---
- **Platform/SRE — Plan:** This GA feature surfaces previously opaque ECS service-side deployment events — state transitions, circuit-breaker rollbacks, Managed Daemon updates — directly into CloudWatch, S3, or Firehose. Platform teams running ECS should evaluate opting in at the cluster level to reduce MTTR on deployment incidents without waiting on AWS Support.
- **CI/CD — Learn:** ECS Action Logs expose service-side operations that can help diagnose failures in pipeline-triggered deployments, but no pipeline changes are required — this is an opt-in ECS console/CloudWatch feature, not a build or artifact system change.
- **Leader — Skip**
