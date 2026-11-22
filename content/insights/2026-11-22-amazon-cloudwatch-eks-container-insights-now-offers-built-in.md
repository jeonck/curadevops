---
title: "CloudWatch EKS Container Insights adds built-in monitoring for Karpenter, KEDA, vLLM, Ray"
date: 2026-11-22T16:05:46.978423+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["observability", "eks", "karpenter"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-eks-kubernetes-tools/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** New GA capability lets EKS operators get Karpenter, KEDA, and AI inference metrics without running self-managed Prometheus or Grafana — worth evaluating the upgrade to add-on v8.0.0+ this quarter and comparing CloudWatch ingestion costs against your existing observability stack.
- **CI/CD — Skip**
- **Leader — Learn:** CloudWatch now covers a meaningful slice of the self-managed observability stack on EKS, updating the build-vs-buy calculus for Prometheus/Grafana; no immediate strategic decision required, but useful context when revisiting the observability platform roadmap.
