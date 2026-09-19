---
title: "AWS PrivateLink adds Tunnel Endpoints for CIDR-range cross-account access"
date: 2026-09-19T14:03:42.839126+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws-privatelink", "vpc-networking", "multi-account"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/9/privatelink-tunnel-endpoint/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** GA capability that replaces per-resource PrivateLink configurations with shareable CIDR ranges via RAM and GENEVE encapsulation — evaluate whether this simplifies existing multi-account or vendor-access network architectures this quarter.
- **CI/CD — Skip**
- **Leader — Learn:** New cross-account connectivity model for vendor access patterns; introduces hourly and per-GB pricing worth factoring into future multi-account networking cost models, but no forced decision today.
