---
title: "AWS IAM Identity Center makes account management optional for new instances"
date: 2026-08-07T00:23:45.191261+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["iam", "aws", "identity"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-identity-center-accounts-optional/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Learn:** New configuration option for net-new IAM Identity Center instances reduces the service-linked role footprint when only AWS application SSO is needed. Worth noting for future greenfield deployments; no action required on existing instances.
- **CI/CD — Skip**
- **Leader — Learn:** Reduces the access surface when standardizing on IAM Identity Center for application SSO without requiring full AWS account management delegation — useful context when evaluating identity architecture for new AWS org setups.
