---
title: "Amazon CloudWatch Logs adds intelligent storage tiering (3 tiers)"
date: 2026-07-16T12:15:50.892178+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Plan"
tags: ["cloudwatch", "observability", "cost-optimization"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-intelligent-tiering/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability that can eliminate the need to export verbose logs to S3 or filter them for cost reasons — evaluate enabling account-level intelligent tiering this quarter to simplify your observability stack and reduce log storage spend.
- **CI/CD — Skip**
- **Leader — Plan:** This changes the unit economics of CloudWatch log retention, making it viable to keep high-volume logs natively rather than running export pipelines to cheaper storage; include in the next FinOps/observability cost review cycle.
