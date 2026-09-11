---
title: "AWS Storage Gateway adds FIPS-compliant PrivateLink for S3 File Gateway"
date: 2026-09-11T14:43:59.795234+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws", "fips", "storage-gateway"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/storage-gateway-fips-privatelink-s3/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If you run S3 File Gateway for regulated workloads, you can now route FIPS-compliant traffic over PrivateLink instead of the public internet — plan to create FIPS VPC endpoints and upgrade gateway software to 2.1.10 or later to enable this.
- **CI/CD — Skip**
- **Leader — Learn:** This expands compliance options for regulated workloads using AWS Storage Gateway, potentially simplifying FIPS requirements in GovCloud or heavily regulated environments — no immediate decision required.
