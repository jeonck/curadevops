---
title: "AWS KMS adds ML-KEM post-quantum key encapsulation (FIPS 203)"
date: 2026-10-27T16:07:53.688542+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["post-quantum-cryptography", "aws-kms", "key-management"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/kms-ml-kem-post-quantum/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** AWS KMS now GA with all three ML-KEM key specs, backed by FIPS 140-3 HSMs — evaluate adopting ML-KEM for workloads handling long-lived sensitive data as part of a PQC migration plan this quarter; no forced deadline, but the NIST IR 8547 roadmap signals classical key-exchange schemes will be phased out.
- **CI/CD — Skip**
- **Leader — Learn:** AWS KMS adding ML-KEM signals cloud providers are operationalizing NIST's PQC standards; useful context for shaping a post-quantum cryptography roadmap, but no licensing change, cost impact, or deadline requires a decision now.
