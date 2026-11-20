---
title: "AWS WAF Security Analytics Dashboard GA: cross-WebACL visibility, 21-day logs"
date: 2026-11-20T18:55:43.487400+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws-waf", "security", "observability"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/02/aws-waf-security-analytics-dashboard/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** GA feature that consolidates traffic analysis across all WebACLs into one view and includes 21 days of full-fidelity request data at no extra cost, potentially eliminating the need for a separate WAF logging pipeline to CloudWatch/S3/Firehose; evaluate adopting this quarter to simplify security-incident investigation workflows.
- **CI/CD — Skip**
- **Leader — Learn:** The bundled 21-day free log retention may reduce spend on external WAF logging destinations, but no strategic vendor-risk or pricing-model change is involved; worth noting as an operational efficiency signal for FinOps reviews.
