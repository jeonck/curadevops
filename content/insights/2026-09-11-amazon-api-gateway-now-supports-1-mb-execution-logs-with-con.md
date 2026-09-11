---
title: "Amazon API Gateway adds 1 MB execution logs with multi-destination routing"
date: 2026-09-11T14:43:59.795234+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["api-gateway", "observability", "logging"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-api-gateway-1-mb-execution-logs/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** This GA feature meaningfully improves API Gateway observability: 1 KB log truncation was a real debugging blind spot, and the new ability to route up to 1 MB events to S3 (Parquet/Athena), CloudWatch, or Firehose simultaneously is worth adding to the observability platform this quarter. Plan to reconfigure API Gateway REST API logging destinations and validate cost impact under vended logs pricing.
- **CI/CD — Skip**
- **Leader — Learn:** The shift to vended logs pricing and multi-destination routing is relevant for observability cost architecture — routing long-term logs to S3/Athena instead of CloudWatch can reduce ingestion costs — but no strategic decision or vendor risk is triggered here.
