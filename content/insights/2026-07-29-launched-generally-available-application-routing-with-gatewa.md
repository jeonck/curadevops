---
title: "AKS Application Routing with Gateway API reaches GA"
date: 2026-07-29T12:56:53.259576+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["kubernetes-gateway-api", "aks", "ingress"]
cves: []
source: "https://azure.microsoft.com/updates?id=567944"
source_name: "Azure Updates"
status: "archived"
---
- **Platform/SRE — Plan:** The Kubernetes Gateway API is the intended successor to the Ingress API, and it's now GA on AKS — plan a migration evaluation from existing Ingress controllers to the managed Gateway API offering this quarter. No forced deadline exists, but adopting early reduces future migration debt as the Ingress API ages out.
- **CI/CD — Skip**
- **Leader — Learn:** Gateway API going GA on AKS signals accelerating industry standardization on the new Kubernetes networking model, worth tracking as context for ingress-tooling decisions if an AKS golden-path review is upcoming.
- **Signals:** GA announcement
