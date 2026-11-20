---
title: "Amazon Cognito integrates with AWS Secrets Manager for app client secrets"
date: 2026-11-20T18:55:43.487400+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["secrets-management", "aws-cognito", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/cognito-secrets-manager-integration/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability allows Cognito app client secrets to be centralized in Secrets Manager with automatic rotation, IAM-scoped access, and KMS encryption; evaluate adopting this quarter for any workloads using Cognito to improve rotation posture and reduce console exposure.
- **CI/CD — Skip**
- **Leader — Learn:** Cognito now supports centralized secret rotation via Secrets Manager, which may simplify compliance around credential hygiene; no strategic decision required but worth noting if the org has open compliance gaps around periodic rotation.
