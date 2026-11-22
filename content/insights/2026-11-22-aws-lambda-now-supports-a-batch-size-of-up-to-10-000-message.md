---
title: "AWS Lambda SQS FIFO batch size raised to 10,000 in provisioned mode"
date: 2026-11-22T16:05:46.978423+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws-lambda", "sqs", "event-driven"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-10K-batch-size-SQSFIFO/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Learn:** New GA capability that could reduce operational overhead for high-throughput ordered workloads on Lambda/SQS FIFO; worth noting for teams running provisioned-mode ESMs, but no current infrastructure change required.
- **CI/CD — Skip**
- **Leader — Learn:** Teams using SQS FIFO with Lambda in provisioned mode may now reduce invocation count and simplify custom buffering logic, with potential cost and complexity improvements worth flagging to relevant engineering teams.
