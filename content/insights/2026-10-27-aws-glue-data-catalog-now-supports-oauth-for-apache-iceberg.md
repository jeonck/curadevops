---
title: "AWS Glue Data Catalog adds OAuth 2.0 support for Iceberg REST APIs"
date: 2026-10-27T16:07:53.688542+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws-glue", "apache-iceberg", "oauth"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/glue-catalog-oauth-iceberg-rest/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability that changes how external query engines and partners authenticate to Glue-hosted Iceberg tables — teams running Iceberg on Glue should evaluate replacing SigV4 paths with OAuth token exchange to eliminate credential distribution to third-party analytics platforms.
- **CI/CD — Skip**
- **Leader — Learn:** OAuth-based federated access to Iceberg tables without distributing AWS credentials is a meaningful shift in data-partnership architecture, relevant for orgs negotiating third-party analytics integrations, but no immediate strategic decision is triggered.
