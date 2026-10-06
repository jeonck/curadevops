---
title: "ACM adds PrivateLink support for ACME public certificate issuance"
date: 2026-10-06T17:01:10.589165+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws-acm", "tls-certificates", "privatelink"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/AWS-Certificate-Manager-ACME-Privatelink"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability keeps ACME cert issuance traffic inside the AWS network via a VPC interface endpoint; worth scheduling adoption this quarter for compliance-sensitive or egress-restricted environments that already use ACM with ACME clients.
- **CI/CD — Skip**
- **Leader — Learn:** ACM now offers a private network path for certificate issuance, which strengthens the compliance and network-isolation story for regulated workloads; no strategic decision or cost change is forced by this GA addition.
