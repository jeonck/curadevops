---
title: "AWS adds amortized cost visibility for EC2 Capacity Blocks in CUR 2.0 and Cost Explorer"
date: 2026-11-07T16:41:59.640651+00:00
verdict: "Plan"
verdict_platform: "Learn"
verdict_cicd: "Skip"
verdict_leader: "Plan"
tags: ["ec2-capacity-blocks", "finops", "ml-infrastructure"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-ec2-capacity-blocks-ml/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Learn:** If you operate GPU clusters via Capacity Blocks, the new amortized cost columns in CUR 2.0 (reservation_amortized_upfront_fee_for_billing_period, reservation_effective_cost) could improve showback dashboards, but no operational change is required.
- **CI/CD — Skip**
- **Leader — Plan:** If the org uses EC2 Capacity Blocks for ML, enable the amortized cost view in Cost Explorer this quarter to allocate GPU reservation costs to owning teams and identify unused capacity — a concrete FinOps chargeback opportunity with no additional charge.
