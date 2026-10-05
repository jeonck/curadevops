---
title: "AWS Private CA adds detailed certificate issuance CloudTrail events"
date: 2026-10-05T19:28:00.991762+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws-private-ca", "cloudtrail", "certificate-management"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-private-ca-certificate-issuance-logs/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If you operate AWS Private CA, the new IssueCertificateDetails CloudTrail management event (auto-delivered, no opt-in) enables compliance auditing and failed-issuance alerting that wasn't possible before; schedule a review of your CloudTrail-based monitoring to add rules for this event, including pre-signing failures and algorithm tracking.
- **CI/CD — Skip**
- **Leader — Skip**
