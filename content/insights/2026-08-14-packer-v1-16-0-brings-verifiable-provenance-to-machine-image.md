---
title: "Packer v1.16.0 adds native SLSA provenance for machine images"
date: 2026-08-14T11:38:17.017194+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Learn"
tags: ["packer", "supply-chain", "slsa"]
cves: []
source: "https://www.hashicorp.com/blog/packer-v1160-brings-verifiable-provenance-to-machine-images"
source_name: "HashiCorp Blog"
status: "active"
---
- **Platform/SRE — Plan:** If your org builds custom AMIs or VM images with Packer, this GA release introduces native SLSA provenance that strengthens image supply-chain attestation — worth adopting this quarter as part of a platform hardening cycle.
- **CI/CD — Plan:** Packer v1.16.0 adds native SLSA provenance generation to machine image builds; if your pipelines include image baking steps, schedule an update to enable provenance output and integrate verification into the release gate.
- **Leader — Learn:** Packer's native SLSA provenance support signals a maturing supply-chain posture for machine images, relevant to orgs building toward SLSA compliance — no immediate strategic decision required but worth factoring into policy planning.
