---
title: "CloudFront OAC now supports S3 Multi-Region Access Points natively"
date: 2026-08-21T11:18:28.032860+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["cloudfront", "s3", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudfront-oac-s3-mrap"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If you use S3 MRAP with CloudFront, you can now drop the Lambda@Edge workaround for SigV4a signing and let CloudFront handle OAC natively — plan to migrate existing custom auth header functions to simplify the architecture.
- **CI/CD — Skip**
- **Leader — Skip**
