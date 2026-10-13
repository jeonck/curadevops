---
title: "Kubernetes ingress-nginx announces retirement"
date: 2026-10-13T17:52:48.720055+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Plan"
tags: ["kubernetes", "ingress", "deprecation"]
cves: []
source: "https://www.kubernetes.dev/blog/2025/11/12/ingress-nginx-retirement/"
source_name: "HN (kubernetes)"
status: "active"
---
- **Platform/SRE — Plan:** ingress-nginx is one of the most widely deployed Kubernetes ingress controllers; its retirement means planning a migration to an alternative (Gateway API, Traefik, Emissary, etc.) before it goes unmaintained. No hard deadline surfaced in signals, so schedule migration evaluation this quarter.
- **CI/CD — Skip**
- **Leader — Plan:** Organizations standardized on ingress-nginx will need to choose and adopt a replacement ingress strategy; evaluate Gateway API or alternative controllers and factor the migration into the next infrastructure planning cycle.
- **Signals:** deprecation mentioned (no explicit date found)
