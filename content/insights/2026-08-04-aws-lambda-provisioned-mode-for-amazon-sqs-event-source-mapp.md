---
title: "AWS Lambda SQS ESM Provisioned Mode scales to 10,000 pollers (5x increase)"
date: 2026-08-04T12:54:10.769117+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws-lambda", "sqs", "event-driven"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-Lambda-provisioned-sqs-esm-max-pollers/"
source_name: "AWS What's New"
status: "archived"
---
- **Platform/SRE — Plan:** If you run high-throughput SQS-to-Lambda pipelines that previously required splitting workloads across multiple ESMs, this GA increase to 10,000 pollers and 100,000 concurrent invocations is worth consolidating architecture this quarter.
- **CI/CD — Skip**
- **Leader — Skip**
- **Signals:** GA announcement
