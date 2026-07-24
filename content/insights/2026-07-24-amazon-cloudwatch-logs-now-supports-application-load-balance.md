---
title: "Amazon CloudWatch Logs adds native ALB log ingestion as vended logs"
date: 2026-07-24T12:15:09.739667+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["observability", "aws", "networking"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-logs/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** ALB logs are now a first-class CloudWatch vended log type, enabling Logs Insights queries, metric filters, and Live Tail for load balancer traffic without custom shipping pipelines; evaluate adopting telemetry enablement rules to standardize coverage across accounts, noting the per-GB vended log cost vs. free S3 delivery.
- **CI/CD — Skip**
- **Leader — Skip**
