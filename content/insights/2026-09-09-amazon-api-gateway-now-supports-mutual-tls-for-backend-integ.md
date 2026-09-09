---
title: "Amazon API Gateway adds mTLS support for backend integrations"
date: 2026-09-09T14:56:08.335953+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["api-gateway", "mtls", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-api-gateway-mutual-tls-backend/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** GA feature enabling ACM-backed mTLS from API Gateway to backend services — worth adopting for any zero-trust or regulated workload this quarter; audit existing REST API integrations and plan certificate provisioning via ACM or AWS Private CA.
- **CI/CD — Skip**
- **Leader — Learn:** Closes a common compliance gap in regulated industries (finance, healthcare) by extending mTLS to the API-to-backend path; relevant context if the org is pursuing zero-trust architecture or FedRAMP/HIPAA posture.
