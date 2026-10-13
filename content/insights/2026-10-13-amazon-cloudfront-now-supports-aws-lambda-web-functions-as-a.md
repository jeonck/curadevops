---
title: "CloudFront adds Lambda Web Functions as a native origin with OAC support"
date: 2026-10-13T17:52:48.720055+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["cloudfront", "lambda", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/cloudfront-lambda-web-functions-origin/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** This GA capability changes how serverless web apps can be architected on AWS — Lambda Web Functions can now sit behind CloudFront for edge TLS, caching, DDoS protection, and WAF, with OAC locking down direct access. Worth evaluating for teams running Lambda-based web workloads this quarter.
- **CI/CD — Skip**
- **Leader — Learn:** New AWS capability that shifts the serverless-plus-CDN architecture picture — Lambda Web Functions are now a first-class CloudFront origin — but no pricing change, licensing impact, or forced migration means no decision is pending.
