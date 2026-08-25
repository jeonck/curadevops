---
title: "Amazon ECS adds automatic detection and repair of impaired agent connectivity"
date: 2026-08-25T11:19:32.404793+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["ecs", "availability", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ecs-agent-connectivity-health"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** A new GA ECS capability worth adopting this quarter: Fargate and Managed Instances now auto-drain and replace impaired instances, while EC2-based ECS surfaces the new AGENT_CONNECTIVITY health event that teams must wire into their own instance-replacement automation. No deadline, but teams running ECS on EC2 should build the event-driven replacement workflow to gain equivalent resilience.
- **CI/CD — Skip**
- **Leader — Skip**
