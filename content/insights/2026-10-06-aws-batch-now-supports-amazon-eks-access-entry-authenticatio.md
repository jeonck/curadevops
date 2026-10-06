---
title: "AWS Batch gains EKS access entry authentication support"
date: 2026-10-06T17:01:10.589165+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws-batch", "eks", "authentication"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-batch-access-entries/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** If you run AWS Batch compute environments on EKS, you can now migrate from the aws-auth ConfigMap to the newer access entry API for IAM-principal authentication; schedule an UpdateComputeEnvironment pass to set accessEntry.desiredState=ENABLED, simplifying auth lifecycle management on those clusters.
- **CI/CD — Skip**
- **Leader — Skip**
