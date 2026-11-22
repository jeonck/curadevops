---
title: "Amazon EventBridge Custom Event Bus adds native Webhook Events support"
date: 2026-11-22T16:05:46.978423+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws-eventbridge", "event-driven", "serverless"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eventbridge-webhook-events"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability that replaces custom webhook-receiver infrastructure (API Gateway + compute) with a managed EventBridge HTTPS endpoint and built-in HMAC/token auth. Worth evaluating this quarter to simplify the event ingestion layer for SaaS integrations on the platform.
- **CI/CD — Skip**
- **Leader — Learn:** EventBridge natively absorbing webhook ingestion reduces the custom infrastructure teams must own for SaaS event pipelines, a build-vs-buy point worth noting when reviewing the event-driven integration strategy.
