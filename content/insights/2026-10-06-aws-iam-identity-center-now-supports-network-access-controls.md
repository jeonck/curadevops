---
title: "AWS IAM Identity Center adds network access controls for Identity Store API"
date: 2026-10-06T17:01:10.589165+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws", "iam", "network-security"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-identity-store-network-controls/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability to restrict Identity Store and SCIM API access by VPC endpoint or IP allowlist; evaluate enforcing VPC-endpoint-only access for the Identity Store API as part of your AWS SSO hardening roadmap this quarter.
- **CI/CD — Skip**
- **Leader — Learn:** AWS now allows network-level perimeter controls around the APIs that manage SSO users and groups; worth noting as an available hardening option when setting identity-security standards across accounts.
