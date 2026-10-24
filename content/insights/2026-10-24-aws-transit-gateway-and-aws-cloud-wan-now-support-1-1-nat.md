---
title: "AWS Transit Gateway and Cloud WAN add managed 1:1 NAT for overlapping CIDRs"
date: 2026-10-24T14:11:23.013433+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Learn"
tags: ["aws", "networking", "transit-gateway"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-transit-gateway-cloud-wan-1-1-nat/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** This GA capability eliminates the need for a NAT appliance or IP renumbering when connecting networks with overlapping CIDRs — directly relevant if the org has pending M&A integration, partner VPN, or multicloud connectivity work blocked by address conflicts. Evaluate adding to the network-connectivity pattern for such scenarios this quarter.
- **CI/CD — Skip**
- **Leader — Learn:** Managed 1:1 NAT on Transit Gateway removes the appliance cost and renumbering complexity historically incurred during M&A network integration; worth noting as an option when assessing future acquisition or partner-connectivity scope.
