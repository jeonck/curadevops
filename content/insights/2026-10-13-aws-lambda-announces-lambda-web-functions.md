---
title: "AWS Lambda Web Functions adds HTTP-native serverless compute"
date: 2026-10-13T17:52:48.720055+00:00
verdict: "Plan"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Plan"
tags: ["aws-lambda", "serverless", "cloud-compute"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-web-functions/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Learn:** New GA AWS Lambda primitive supporting direct HTTP handling (Express/Hono, no adapters) with a different billing model; worth tracking for future platform architecture patterns, but no existing infrastructure needs changing and existing Lambda Event Functions require no migration.
- **CI/CD — Skip**
- **Leader — Plan:** The active-CPU billing model (vs. idle CPU) could meaningfully reduce Lambda costs for I/O-bound workloads; evaluate this as a golden-path serverless option and assess cost-optimization potential against current Lambda spend this planning cycle.
