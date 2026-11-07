---
title: "AWS Glue Data Catalog adds vended credentials for Iceberg REST catalog federation"
date: 2026-11-07T16:41:59.640651+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws-glue", "apache-iceberg", "data-platform"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/glue-catalog-vended-credentials-iceberg/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability enabling externally-vended, S3-prefix-scoped credentials for Iceberg REST catalog federation via Athena, EMR, Redshift, and Glue. Plan to evaluate whether this changes your Lake Formation access-control architecture or cross-account data-sharing model this quarter.
- **CI/CD — Skip**
- **Leader — Learn:** This enhancement to Glue and Lake Formation's Iceberg federation model enables finer-grained, catalog-delegated access control across AWS analytics engines; worth tracking as it shapes data governance and cross-account sharing strategy options.
