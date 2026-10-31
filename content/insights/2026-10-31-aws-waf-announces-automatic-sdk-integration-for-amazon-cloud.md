---
title: "AWS WAF adds automatic JavaScript SDK injection for CloudFront distributions"
date: 2026-10-31T15:55:53.676814+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws-waf", "cloudfront", "security"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-waf-automatic-sdk-integration-amazon-cloudfront/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability worth evaluating this quarter: enabling automatic SDK integration on existing CloudFront web ACLs that use Bot Control (targeted), ATP, or ACFP rule groups eliminates per-application script-tag maintenance and reduces misconfiguration risk. Review your WAF web ACLs and enable the setting via Console, CLI, CDK, or CloudFormation.
- **CI/CD — Skip**
- **Leader — Learn:** This reduces recurring per-application engineering overhead for teams protecting many CloudFront-fronted properties with advanced WAF rule groups — useful context when assessing operational cost of the WAF managed-rule investment, but no strategic decision is required.
