---
title: "Amazon ECS adds IAM condition keys for CPU/memory on RunTask and StartTask"
date: 2026-09-11T14:43:59.795234+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws-ecs", "iam", "security"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ecs-expands-condition-key-support/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If your org runs ECS and uses IAM SCPs or permission boundaries to govern resource allocation, update your IAM policies to enforce ecs:task-cpu and ecs:task-memory on RunTask and StartTask — this closes a gap where those controls were previously bypassable at launch time.
- **CI/CD — Skip**
- **Leader — Skip**
