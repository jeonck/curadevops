---
title: "AWS Secrets Manager adds managed rotation for Databricks and Twilio credentials"
date: 2026-10-13T17:52:48.720055+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["secrets-management", "aws", "databricks"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/secrets-manager-managed-external-secrets-databricks-twilio/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability worth evaluating this quarter for any workloads using Databricks or Twilio: eliminates custom rotation Lambda functions and ensures applications pick up rotated credentials automatically without code changes.
- **CI/CD — Learn:** Relevant if pipelines consume Databricks personal access tokens or Twilio API keys, but there is no deadline or pipeline breakage — file as a pattern to consider when next reviewing how build credentials are rotated.
- **Leader — Skip**
