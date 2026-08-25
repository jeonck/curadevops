---
title: "EC2 Dedicated Hosts support Host Resource Groups without License Manager SMLs"
date: 2026-07-25T11:58:38.501915+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["ec2", "aws", "license-management"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/07/ec2-dedicated-hosts-hrg/"
source_name: "AWS What's New"
status: "archived"
---
- **Platform/SRE — Plan:** If you run EC2 Dedicated Hosts or Mac Instances for isolation rather than BYOL, you can now create Host Resource Groups without the AWS License Manager self-managed license prerequisite, simplifying the provisioning workflow. Review and update any Terraform/IaC automation that currently creates SMLs solely to satisfy the HRG requirement.
- **CI/CD — Skip**
- **Leader — Skip**
