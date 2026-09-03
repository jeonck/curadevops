---
title: "Kubernetes Gateway API v1.6: TCPRoute and UDPRoute reach GA"
date: 2026-08-04T12:54:10.769117+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["kubernetes", "gateway-api", "networking"]
cves: []
source: "https://kubernetes.io/blog/2026/08/03/gateway-api-v1-6-release/"
source_name: "Kubernetes Blog"
status: "archived"
---
- **Platform/SRE — Plan:** TCPRoute and UDPRoute are now stable in the v1 API, making portable L4 routing viable for production workloads like databases, DNS, and VoIP. If you're already using experimental Gateway API resources, audit for the new gateway.networking.x-k8s.io API group separation to avoid breakage on upgrade.
- **CI/CD — Skip**
- **Leader — Learn:** Gateway API continues maturing as the unified Kubernetes networking standard; L4 GA coverage strengthens the case for standardizing on it as the org's golden-path ingress model over implementation-specific CRDs.
