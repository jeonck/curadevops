---
title: "AWS Lambda adds self-managed S3 code storage, raises default limit to 300GB"
date: 2026-07-15T12:10:55.908816+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws-lambda", "serverless", "s3"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/07/lambda-self-managed-code-storage/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** This GA capability removes the per-Region Lambda-managed storage quota for teams running large function/layer footprints; evaluate adopting `S3ObjectStorageMode=REFERENCE` this quarter for deployments approaching the old 75GB ceiling, and note the default limit has already been raised to 300GB for all accounts.
- **CI/CD — Skip**
- **Leader — Learn:** Cost impact is neutral-to-positive (standard S3 rates replace implicit Lambda storage overhead) with no forced migration, but worth flagging to platform teams running high function counts so they can evaluate whether S3-backed storage fits their existing artifact management posture.
