---
title: "Amazon Inspector adds vulnerability scanning for EC2 AMIs"
date: 2026-11-03T18:12:21.270782+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Learn"
tags: ["amazon-inspector", "ami-security", "vulnerability-scanning"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/ec2-amis-scanned-through-inspector/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability lets platform teams scan their AMI catalogs continuously via Inspector without launching instances; worth enabling this quarter to catch vulnerabilities before fleet deploys and to enforce security criteria org-wide via Declarative Policies.
- **CI/CD — Plan:** EC2 Image Builder pipelines can now integrate Inspector AMI scanning directly and block distribution of non-compliant AMIs; schedule adoption as a supply-chain hardening step to gate AMI publishing on scan results.
- **Leader — Learn:** Awareness item: AWS now offers org-wide AMI vulnerability enforcement via Inspector and Declarative Policies, which could inform updated security standards around base image management but requires no immediate strategic decision.
