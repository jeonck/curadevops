---
title: "AWS Lambda raises max timeout to 90 min for async/ESM on Managed Instances"
date: 2026-09-10T14:43:05.673701+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["lambda", "serverless", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-lambda-90-minute-function/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** This GA capability removes a key architectural constraint that pushed long-running workloads off Lambda toward ECS/Batch/Step Functions; evaluate whether existing workarounds in the platform's serverless stack can be simplified this quarter.
- **CI/CD — Skip**
- **Leader — Learn:** The 6x timeout increase changes the serverless vs. dedicated-compute trade-off for batch and AI inference workloads, worth factoring into the next platform strategy review, but no urgent decision is required.
