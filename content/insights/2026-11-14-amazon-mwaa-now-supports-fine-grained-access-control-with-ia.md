---
title: "Amazon MWAA adds IAM Identity Center integration and multi-team environments"
date: 2026-11-14T16:48:22.800807+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Plan"
tags: ["mwaa", "iam-identity-center", "access-control"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/mwaa-fine-grained-access-control/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** The GA IAM Identity Center integration changes how multi-tenant MWAA environments are managed — worth evaluating if you operate MWAA for multiple teams. Note that multi-team DAG isolation is still in preview, so hold off on that portion until GA.
- **CI/CD — Skip**
- **Leader — Plan:** Shared MWAA environments reduce per-team infrastructure costs and the IAM Identity Center integration ties Airflow access to corporate identity, improving compliance posture — worth including in next planning cycle if data teams run MWAA at scale.
