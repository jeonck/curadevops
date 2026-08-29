---
title: "Kubernetes v1.37: Pod Certificates and Cluster Trust Bundles go GA"
date: 2026-08-29T15:23:50.121809+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["kubernetes", "workload-identity", "mtls"]
cves: []
source: "https://kubernetes.io/blog/2026/08/28/kubernetes-v1-37-pod-certificates-and-cluster-trust-bundles/"
source_name: "Kubernetes Blog"
status: "active"
---
- **Platform/SRE — Plan:** Pod Certificates and Cluster Trust Bundles reaching GA in Kubernetes 1.37 introduces native X.509/mTLS workload identity as an alternative to service account JWTs; evaluate adopting cluster trust bundles and pod certificate issuance this quarter for services requiring mTLS.
- **CI/CD — Skip**
- **Leader — Learn:** Native X.509 workload identity baked into Kubernetes core shifts how orgs can approach service-to-service auth without a service mesh; worth tracking as input to future golden-path and identity-standards decisions.
- **Signals:** Kubernetes 1.37 EOL 2027-10-28
