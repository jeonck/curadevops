---
title: "CloudWatch EKS add-on gains native OTLP ingestion and Prometheus scraping (v8.0.0)"
date: 2026-11-22T16:05:46.978423+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["observability", "opentelemetry", "eks"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-eks-addon-custom-telemetry/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Version 8.0.0 of the EKS add-on is now GA and can replace a standalone OTel collector and Prometheus operator; evaluate whether consolidating onto the CloudWatch agent simplifies your observability stack this quarter, noting the $0.08/GB ingestion cost.
- **CI/CD — Skip**
- **Leader — Learn:** This shapes the build-vs-buy calculus on running a self-managed OTel/Prometheus stack versus consolidating into CloudWatch, with a concrete per-GB pricing signal ($0.08/GB) to factor into observability cost modeling.
