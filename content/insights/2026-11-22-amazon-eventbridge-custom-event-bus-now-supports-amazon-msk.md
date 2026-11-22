---
title: "EventBridge Custom event bus adds Amazon MSK as a native target"
date: 2026-11-22T16:05:46.978423+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["eventbridge", "aws", "kafka"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eventbridge-msk-target/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability lets EventBridge route events directly to MSK topics without a custom producer, which could simplify event-driven architectures on AWS; evaluate whether this replaces any bespoke Kafka producer Lambda or Fargate service in your current platform.
- **CI/CD — Skip**
- **Leader — Learn:** This new managed integration between EventBridge and MSK may shift the build-vs-buy calculus for teams operating Kafka-based event pipelines on AWS, worth noting as a potential simplification in future platform roadmap discussions.
