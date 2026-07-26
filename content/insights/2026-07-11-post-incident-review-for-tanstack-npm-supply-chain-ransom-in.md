---
title: "Grafana Labs post-incident review: TanStack npm supply chain ransom"
date: 2026-07-11T15:50:13.633791+00:00
verdict: "Learn"
verdict_platform: "Learn"
verdict_cicd: "Learn"
verdict_leader: "Learn"
tags: ["supply-chain", "security", "grafana"]
cves: []
source: "https://grafana.com/blog/post-incident-review-for-tanstack-npm-supply-chain-ransom-incident/"
source_name: "Grafana Blog"
status: "archived"
---
- **Platform/SRE — Learn:** Grafana's PIR confirms no customer production impact and no Grafana Cloud compromise from the TanStack npm attack; useful background on how supply chain attacks can reach observability vendors, but no operational change is required.
- **CI/CD — Learn:** The report details how a compromised npm package triggered a ransom incident and exposed a missed credential rotation — valuable for evaluating the depth of your own supply chain audit and rotation runbooks, even though Grafana's customer pipelines were unaffected.
- **Leader — Learn:** Grafana's independently audited transparency report (Mandiant confirmed no code tampering or repository poisoning) is useful context for assessing vendor security maturity; no strategic action is required since customer exposure was ruled out.
