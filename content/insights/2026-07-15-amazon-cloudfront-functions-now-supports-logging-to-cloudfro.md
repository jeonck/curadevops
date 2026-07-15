---
title: "CloudFront Functions can now write custom data into access logs"
date: 2026-07-15T12:10:55.908816+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["cloudfront", "observability", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/07/cloudfront-functions-access-logs/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability that consolidates CloudFront Function decisions (A/B variants, auth outcomes, routing) directly into access log records, eliminating cross-system correlation with CloudWatch Logs. Worth adopting in existing CloudFront Functions this quarter by replacing or augmenting console.log() with cf.logCustomData().
- **CI/CD — Skip**
- **Leader — Skip**
