---
title: "AWS VPC IPAM adds BGP route protection monitoring and delegated RPKI for BYOIP"
date: 2026-08-09T11:24:01.234031+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws", "networking", "ipam"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-vpc-ipam-bgp-rpki-byoip/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** Relevant to any team using BYOIP prefixes on AWS: the new delegated RPKI automation eliminates manual ROA creation/renewal at the RIR, and the centralized dashboard surfaces hijacking risk via route overlap detection. Evaluate enabling this during the next IPAM configuration review cycle.
- **CI/CD — Skip**
- **Leader — Skip**
