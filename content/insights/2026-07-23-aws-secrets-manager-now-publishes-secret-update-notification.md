---
title: "AWS Secrets Manager natively publishes rotation events to EventBridge"
date: 2026-07-23T12:19:57.837621+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["secrets-management", "eventbridge", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/07/secrets-manager-update-notifications"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability removes the CloudTrail-parsing workaround for secret rotation events; evaluate adding EventBridge rules this quarter to auto-refresh credential caches or trigger service restarts on rotation, reducing the lag window between rotation and downstream adoption.
- **CI/CD — Learn:** Could inform future pipeline designs that need to react to secret rotation (e.g., invalidating cached build credentials), but no current pipeline change is required and no deprecation is introduced.
- **Leader — Skip**
