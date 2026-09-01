---
title: "Amazon Redshift adds IAM Identity Center auth with enhanced VPC routing"
date: 2026-09-01T15:20:27.675053+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws", "redshift", "iam"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-redshift-supports-idc-evr"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If Redshift is in your stack and you have data residency or network-isolation requirements, this is worth adopting: SSO via IAM Identity Center with all auth traffic staying inside your VPC via PrivateLink. Evaluate enabling EVR and wiring up Identity Center for your provisioned clusters or serverless workgroups this quarter.
- **CI/CD — Skip**
- **Leader — Learn:** Redshift now supports SSO via IAM Identity Center with network traffic fully contained in your VPC — relevant context if your org has regulatory or data-residency mandates for analytics infrastructure, but no decision is forced by this launch.
