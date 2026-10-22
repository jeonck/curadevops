---
title: "AWS Network Firewall adds Route 53 IP validation for non-HTTP protocols"
date: 2026-10-22T15:46:09.169989+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["aws", "network-security", "firewall"]
cves: []
source: "https://aws.amazon.com/about-aws/whats-new/2026/10/network-firewall-route-53-ip-validation/"
source_name: "AWS What's New"
status: "active"
---
- **Platform/SRE — Plan:** This GA capability closes a real security gap by validating destination IPs against Route 53-resolved addresses, extending domain-based filtering to SFTP, SSH, and other protocols beyond HTTP/HTTPS. Evaluate adding Route 53 Resolved IP Validation to existing Network Firewall policies to harden egress controls and prevent SNI spoofing.
- **CI/CD — Skip**
- **Leader — Skip**
