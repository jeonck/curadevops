---
title: "AWS Lambda Durable Functions raises op limit 10x, checkpoint to 1 MB"
date: 2026-10-15T15:27:57.001735+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws-lambda", "serverless", "agentic-workflows"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-gen-limit-increase/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If your platform runs multi-step or agentic Lambda workflows, the 30,000 operation limit and 1 MB checkpoint open up architectures previously blocked by quota; evaluate whether existing workflows hitting the old 3,000-op ceiling should be redesigned to take advantage.
- **CI/CD — Skip**
- **Leader — Learn:** The expanded limits make Lambda durable functions more viable for long-running agentic AI orchestration, worth tracking if your org is evaluating serverless vs. container-based workflow engines for AI workloads.
