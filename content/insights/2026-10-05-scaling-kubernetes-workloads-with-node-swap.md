---
title: "Kubernetes Node Swap Hits GA in v1.34, Up to 3× Pod Density Gain"
date: 2026-10-05T19:28:00.991762+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Learn"
verdict_leader: "Plan"
tags: ["kubernetes", "node-swap", "memory-optimization"]
cves: []
source: "https://kubernetes.io/blog/2026/10/05/scaling-kubernetes-workloads-with-node-swap/"
source_name: "Kubernetes Blog"
status: "active"
---
- **Platform/SRE — Plan:** Kubernetes v1.34 GA swap support with NVMe backing is worth evaluating for memory-dense node pools this quarter; assess enabling swap on nodes running agentic AI or sandboxed workloads to reduce OOM kills and improve pod density without fleet-wide urgency.
- **CI/CD — Learn:** The benchmark covers CI/CD kernel build workloads as a validated use case, but enabling swap on nodes is a platform configuration decision — useful context for understanding build pod resource headroom if your CI runs on shared Kubernetes clusters.
- **Leader — Plan:** Up to 3× pod density on existing hardware is a material FinOps opportunity worth adding to the next infrastructure planning cycle; evaluate whether adopting Kubernetes v1.34 swap + NVMe changes the cost model for memory-intensive AI and build workloads in your standard platform stack.
- **Signals:** GA announcement
