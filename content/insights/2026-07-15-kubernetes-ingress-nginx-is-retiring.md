---
title: "Kubernetes ingress-nginx announces retirement"
date: 2026-07-15T12:10:55.908816+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Plan"
tags: ["kubernetes", "ingress", "deprecation"]
cves: []
source: "https://www.kubernetes.dev/blog/2025/11/12/ingress-nginx-retirement/"
source_name: "HN (kubernetes)"
status: "archived"
---
- **Platform/SRE — Plan:** ingress-nginx is one of the most widely deployed Kubernetes ingress controllers; its retirement means planning a migration to an alternative (e.g., Envoy Gateway, NGINX Gateway Fabric, or another Gateway API-conformant controller). No forced migration date is confirmed yet, so scope the migration project now before community support winds down.
- **CI/CD — Skip**
- **Leader — Plan:** If ingress-nginx is part of the org's Kubernetes golden path or standard stack, its retirement requires evaluating replacement ingress controllers and updating platform standards; begin that toolchain review this planning cycle before the project loses maintainer support.
- **Signals:** deprecation mentioned (no explicit date found)
