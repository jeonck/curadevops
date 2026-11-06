---
title: "Amazon EC2 adds ImdsV1Enabled CloudWatch metric for IMDSv2 migration tracking"
date: 2026-11-06T17:46:36.988901+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["ec2", "imdsv2", "cloudwatch"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/ec2-imdsv1enabled-cloudwatch-metric/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Set up CloudWatch dashboards and alarms using the new ImdsV1Enabled metric to identify and prioritize EC2 instances still running IMDSv1 across accounts and regions; no forced-migration deadline is announced, but this removes the last tooling excuse for incomplete IMDSv2 adoption.
- **CI/CD — Skip**
- **Leader — Skip**
