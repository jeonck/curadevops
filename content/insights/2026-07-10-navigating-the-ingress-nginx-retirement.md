---
title: "ingress-NGINX retirement: migrate off the retired SIG Network controller"
date: 2026-07-10T11:00:57.610632-05:00
verdict: "Act"
verdict_platform: "Act"
verdict_cicd: "Skip"
verdict_leader: "Act"
tags: ["ingress-nginx", "kubernetes", "eol"]
cves: []
source: "https://www.cncf.io/blog/2026/07/09/navigating-the-ingress-nginx-retirement/"
source_name: "CNCF Blog"
status: "active"
---
- **Platform/SRE — Act:** ingress-nginx reached end-of-life in March 2026 (now four months past); remaining on it means exposure to unpatched CVEs in a critical ingress path with no upstream fixes coming. Audit clusters for ingress-nginx usage and complete migration to a maintained alternative (Envoy Gateway, Ingress-NGINX from F5, Traefik) immediately.
- **CI/CD — Skip**
- **Leader — Act:** The SIG Network ingress-nginx controller is retired, making any org standardized on it subject to growing unpatched CVE exposure with no remediation path; this warrants a brief to leadership and a decision on a replacement ingress standard before the vulnerability surface widens further.
- **Signals:** deprecation mentioned (no explicit date found)
