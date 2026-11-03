---
title: "AWS Lambda Kafka ESM gains queue support via Kafka 4.2 share groups"
date: 2026-11-03T18:12:21.270782+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["kafka", "aws-lambda", "event-driven"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-queue-kafka-esm/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If you run self-managed Kafka clusters with Lambda ESM and need higher parallelism, evaluate upgrading to Kafka 4.2 (share groups) and enabling queue mode — it decouples consumer concurrency from partition count with no producer-side changes. No deadline; schedule as a platform improvement this quarter.
- **CI/CD — Skip**
- **Leader — Learn:** This GA capability lets Lambda consumers scale beyond partition count on self-managed Kafka, potentially reducing over-provisioning costs and the need for auxiliary queuing infrastructure — worth factoring into event-driven architecture standards.
- **Signals:** Kafka 4.2 supported · GA announcement
