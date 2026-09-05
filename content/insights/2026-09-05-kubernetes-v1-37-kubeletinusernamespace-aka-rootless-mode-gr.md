---
title: "Kubernetes v1.37: KubeletInUserNamespace (Rootless Mode) Reaches Beta"
date: 2026-09-05T13:37:34.984053+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["kubernetes", "security", "rootless"]
cves: ["CVE-2019-19921", "CVE-2022-0811", "CVE-2023-27561"]
source: "https://kubernetes.io/blog/2026/09/04/kubernetes-v1-37-rootless-beta/"
source_name: "Kubernetes Blog"
status: "active"
---
- **Platform/SRE — Learn:** Beta (pre-GA) cap applies, but this is worth evaluating: running kubelet and container runtimes in a Linux user namespace reduces blast radius of node-component CVEs like cr8escape and the 2023 runc procfs bypass; test in non-production clusters before v1.38 targets GA.
- **CI/CD — Skip**
- **Leader — Learn:** Rootless-node mode reaching beta signals a maturing Kubernetes security posture option; relevant context for teams in regulated industries evaluating host-isolation requirements, but no adoption decision warranted before GA.
- **Signals:** Kubernetes 1.37 EOL 2027-10-28 · Kubernetes 1.22 is past EOL (2022-10-28, 1408d ago) · pre-GA (alpha/beta/RC/preview) · CVE-2019-19921 — CISA KEV: not listed, EPSS 0.00 · CVE-2022-0811 — CISA KEV: not listed, EPSS 0.19 · CVE-2023-27561 — CISA KEV: not listed, EPSS 0.00
