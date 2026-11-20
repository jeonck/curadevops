---
title: "Route 53 Private Endpoint Health Checks now GA in all regions"
date: 2026-11-20T18:55:43.487400+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["route53", "dns", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-private-endpoint-health-checks/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** This GA feature replaces the common CloudWatch + Lambda + Route 53 API workaround for private DNS failover, bringing sub-second detection and no public exposure. Plan to evaluate adopting Private Endpoint Health Checks for internal APIs, databases, and hybrid endpoints this quarter and retire custom control loops where applicable.
- **CI/CD — Skip**
- **Leader — Learn:** Route 53 now handles DNS failover for private workloads natively, eliminating a category of bespoke Lambda-based glue that platform teams commonly build; worth noting as a managed-service option that reduces operational overhead when reviewing internal reliability architecture.
