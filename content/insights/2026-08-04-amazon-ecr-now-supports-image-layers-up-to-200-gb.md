---
title: "Amazon ECR raises Docker push image layer limit to 200 GB"
date: 2026-08-04T12:54:10.769117+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Learn"
verdict_leader: "Skip"
tags: ["ecr", "container-registry", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ecr-image-layers/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Learn:** Useful capability increase for teams packaging large artifacts (LLMs, genomics datasets) into container images, but no operational change required — existing workloads are unaffected and there is no migration deadline.
- **CI/CD — Learn:** Pipelines that previously split large layers or used external storage workarounds can now simplify, but this is an optional improvement with no deadline or deprecation pressure.
- **Leader — Skip**
