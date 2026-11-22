---
title: "CloudWatch Observability EKS add-on v8.0.0 adds telemetry filtering"
date: 2026-11-22T16:05:46.978423+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Plan"
tags: ["observability", "eks", "finops"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-eks-otel-addon-filtering/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** GA telemetry filtering in EKS add-on v8.0.0+ lets you exclude non-production namespaces and drop high-cardinality metrics, directly reducing per-GB CloudWatch ingestion costs. Plan an upgrade to v8.0.0 and define cluster-wide filter configs this quarter.
- **CI/CD — Skip**
- **Leader — Plan:** Per-GB CloudWatch ingestion charges make this a concrete FinOps lever — filtering unused telemetry at the add-on level can materially reduce observability spend at scale. Evaluate enabling this across EKS clusters as part of the next cost-optimization cycle.
