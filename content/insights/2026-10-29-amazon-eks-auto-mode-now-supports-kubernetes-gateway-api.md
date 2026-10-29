---
title: "Amazon EKS Auto Mode adds native Kubernetes Gateway API support"
date: 2026-10-29T17:12:51.882644+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["eks", "kubernetes-networking", "gateway-api"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-eks-auto-mode-kubernetes-gateway-api/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** EKS Auto Mode now natively manages Gateway API resources (Gateway, HTTPRoute) including weighted routing, header-based routing, and ACM TLS — eliminating the need for a separate ingress controller. Evaluate adopting Gateway/HTTPRoute as the standard traffic-management pattern for EKS Auto Mode clusters this quarter.
- **CI/CD — Skip**
- **Leader — Learn:** EKS Auto Mode's native Gateway API support signals Kubernetes standardizing on a single next-gen ingress model; worth tracking as a data point when reviewing golden-path networking standards for EKS-based platforms.
