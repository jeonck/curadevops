---
title: "Amazon SNS now supports message payloads up to 1 MiB"
date: 2026-09-19T14:03:42.839126+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws", "messaging", "sns"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-sns-1mib-support"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability worth evaluating this quarter: workloads that currently split or offload large SNS payloads can be simplified by setting the new MaximumMessageSize topic attribute on Standard or FIFO topics, though note the constraint of up to 100 subscriptions per topic at the larger size.
- **CI/CD — Skip**
- **Leader — Skip**
