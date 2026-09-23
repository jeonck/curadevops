---
title: "Amazon EMR introduces LTS releases starting with Spark 4.1 (emr-spark-8.1.0)"
date: 2026-09-23T15:14:55.611695+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Plan"
tags: ["amazon-emr", "apache-spark", "data-platform"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-emr-long-term-support-spark-4-1/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Teams running EMR on EKS should evaluate migrating production Spark workloads to emr-spark-8.1.0 to take advantage of the new 36-month LTS support window, reducing forced upgrade pressure; no hard deadline exists yet.
- **CI/CD — Skip**
- **Leader — Plan:** EMR LTS changes the upgrade economics for data platform teams — evaluate standardizing on LTS releases to extend support cycles and reduce upgrade toil as part of the next data platform planning cycle.
