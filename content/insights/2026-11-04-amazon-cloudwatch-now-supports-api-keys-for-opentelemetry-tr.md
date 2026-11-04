---
title: "Amazon CloudWatch adds bearer token auth for OTel OTLP traces"
date: 2026-11-04T18:20:30.510987+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["opentelemetry", "cloudwatch", "observability"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-api-keys-opentelemetry/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA CloudWatch capability unblocks OTel trace ingestion from on-prem or non-AWS workloads that can't use SigV4; evaluate enabling bearer token auth if you operate hybrid or multi-cloud observability pipelines.
- **CI/CD — Learn:** Bearer token auth could simplify trace export from CI runners without AWS credential access (e.g., third-party SaaS CI), but no existing pipelines break and no deadline applies.
- **Leader — Skip**
