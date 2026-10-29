---
title: "AWS Lambda adds SOCI lazy loading for container-image functions"
date: 2026-10-29T17:12:51.882644+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["lambda", "container-images", "cold-start"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-seekable-oci-soci/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** GA capability that can cut cold-start latency up to 70% for large Lambda container workloads; evaluate adding SOCI index creation to ECR push workflows for any function images over a few hundred MB this quarter.
- **CI/CD — Learn:** Adopting SOCI requires a new pipeline step (generate SOCI index, push a second tagged manifest to ECR), but it is fully opt-in with no deadline — worth noting as a future build-pipeline enhancement if cold starts are a pain point.
- **Leader — Skip**
