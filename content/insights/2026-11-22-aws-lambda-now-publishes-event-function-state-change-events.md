---
title: "AWS Lambda publishes function state change events to EventBridge"
date: 2026-11-22T16:05:46.978423+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Learn"
tags: ["lambda", "eventbridge", "event-driven"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-function-state-events/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** This GA feature eliminates polling the GetFunction API for Lambda state tracking — platform teams managing thousands of functions should evaluate replacing custom polling logic with EventBridge rules this quarter.
- **CI/CD — Plan:** Lambda deployment pipelines can now react to function state changes via EventBridge instead of polling, removing custom retry logic and API quota pressure; worth adopting in Lambda-based release workflows this quarter.
- **Leader — Learn:** Informs platform-engineering strategy around event-driven automation at scale — no licensing, cost, or vendor-risk decision required at this time.
