---
title: "AWS Storage Gateway FIPS endpoints now available over PrivateLink"
date: 2026-08-20T11:19:17.091246+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws", "storage-gateway", "fips"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/storage-gateway-fips-privatelink/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If you run Tape or Volume Gateway for regulated workloads, you can now route FIPS-compliant traffic privately via PrivateLink instead of over the public internet; plan to create a FIPS interface VPC endpoint and re-activate gateways on software version 3.2.7 or later.
- **CI/CD — Skip**
- **Leader — Learn:** For organizations with compliance mandates (FedRAMP, HIPAA) using Storage Gateway, this removes a previous architectural constraint — FIPS traffic can now stay private — which may simplify audit scope for regulated workloads.
