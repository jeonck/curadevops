---
title: "CloudWatch PromQL query window extends to 30 days for OTel metrics"
date: 2026-11-22T16:05:46.978423+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["cloudwatch", "observability", "promql"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-promql-query-30days/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Teams using CloudWatch + OpenTelemetry can now measure SLOs and error budgets over a full 30-day rolling window in a single PromQL query — previously impossible within the 7-day limit. Worth scheduling an update to SLO dashboards and budget-exhaustion alarms to leverage this GA capability this quarter.
- **CI/CD — Skip**
- **Leader — Learn:** CloudWatch's native PromQL window now matches the standard 30-day SLO period, narrowing the gap with dedicated observability platforms; worth factoring into future evaluations of CloudWatch versus third-party observability tooling for SLO use cases.
