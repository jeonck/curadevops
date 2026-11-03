---
title: "Amazon CloudFront now supports self-service quota increases via AWS Service Quotas"
date: 2026-11-03T18:12:21.270782+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["cloudfront", "aws", "service-quotas"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/cloudfront-self-service-quotas/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Teams running large CloudFront deployments approaching limits (500+ distributions, 100+ alternate domain names) should switch to Service Quotas for proactive monitoring and automatic approvals; set CloudWatch alarms on quota usage metrics to get ahead of limits before they bite.
- **CI/CD — Skip**
- **Leader — Skip**
