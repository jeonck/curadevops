---
title: "Amazon Managed Grafana adds Grafana 13.2 support with Git Sync and PromQL"
date: 2026-10-01T17:14:12.201245+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["grafana", "observability", "aws"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-managed-grafana-now-supports-creating-grafana-13-2-workspaces"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Grafana 13.2 on AMG brings Git Sync (dashboards as code tied to a repo), dynamic dashboards, and PromQL support in the CloudWatch data source — plan an evaluation and workspace upgrade this quarter if you run AMG; 13.2 is supported until 2027-05-18.
- **CI/CD — Skip**
- **Leader — Learn:** Git Sync enabling dashboard-as-code and PromQL queries against CloudWatch OTLP metrics represent a meaningful shift in managed observability capabilities, worth factoring into platform tooling direction — but no strategic decision is required now.
- **Signals:** Grafana 13.2 EOL 2027-05-18 · GA announcement
