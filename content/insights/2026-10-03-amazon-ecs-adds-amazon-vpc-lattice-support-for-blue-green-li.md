---
title: "Amazon ECS adds VPC Lattice blue/green, linear, and canary deployments"
date: 2026-10-03T15:01:20.079187+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["ecs", "deployment-strategies", "vpc-lattice"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ecs-vpc-lattice-blue-green-deployments"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** GA capability that changes how ECS services using VPC Lattice handle progressive delivery — evaluate adopting native traffic-shifting to replace or simplify any existing CodeDeploy or manual canary setups this quarter.
- **CI/CD — Plan:** Native canary/linear deployment strategies with CloudWatch alarm rollback and lifecycle hooks are worth integrating into ECS deployment pipelines; evaluate replacing custom traffic-shifting logic with this managed approach.
- **Leader — Skip**
