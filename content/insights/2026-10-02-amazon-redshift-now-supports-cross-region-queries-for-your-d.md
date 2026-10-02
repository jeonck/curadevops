---
title: "Amazon Redshift adds cross-Region S3 data lake queries with VPC routing"
date: 2026-10-02T16:25:37.540030+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["redshift", "data-lake", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/redshift-cross-Region-queries-for-data-lake"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability lets Redshift query S3 tables in remote regions without replication, with enhanced VPC routing keeping traffic off public networks; evaluate for multi-region data lake architectures or compliance-sensitive workloads this quarter.
- **CI/CD — Skip**
- **Leader — Learn:** Relevant to orgs with data-residency or compliance constraints (financial, healthcare, government) — cross-region querying without replication simplifies global analytics architecture, but no strategic decision is forced by this announcement.
