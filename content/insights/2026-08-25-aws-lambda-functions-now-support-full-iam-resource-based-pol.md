---
title: "AWS Lambda gains full IAM resource-based policy support"
date: 2026-08-25T11:19:32.404793+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws-lambda", "iam", "cloud-security"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-lambda-full-iam-resource-based-policies/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Platform teams managing Lambda in multi-account architectures can now consolidate per-principal permission statements into single policy documents with full IAM condition key support (source IP, principal tags, etc.). Plan a policy consolidation pass for existing Lambda functions to reduce policy sprawl and simplify ongoing management.
- **CI/CD — Skip**
- **Leader — Learn:** This GA capability reduces IAM policy complexity for Lambda-heavy multi-account orgs, but it's an incremental improvement rather than a strategic or cost-model shift — no leadership decision required.
