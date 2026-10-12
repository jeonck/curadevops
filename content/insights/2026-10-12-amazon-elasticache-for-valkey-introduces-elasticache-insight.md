---
title: "Amazon ElastiCache for Valkey adds CloudWatch Insights dashboard"
date: 2026-10-12T20:04:11.786944+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["elasticache", "observability", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-elasticache-valkey-elasticache-insights/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** A new GA CloudWatch dashboard surfacing OTel metrics (memory, network, latency, keyspace, errors) for Valkey node clusters — worth scheduling adoption to consolidate cache observability; note that detailed 15-second metrics incur standard CloudWatch OTel pricing.
- **CI/CD — Skip**
- **Leader — Learn:** AWS now bundles a pre-built observability layer for ElastiCache Valkey at no additional platform cost (standard CloudWatch OTel pricing applies for enhanced polling), relevant context if the org is evaluating its caching observability spend.
