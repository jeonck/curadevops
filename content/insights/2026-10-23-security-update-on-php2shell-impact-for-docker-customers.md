---
title: "PHP2Shell Critical CVEs Impact Docker Customers Using PHP Images"
date: 2026-10-23T15:33:11.401461+00:00
verdict: "Plan"
verdict_platform: "Skip"
verdict_cicd: "Plan"
verdict_leader: "Skip"
tags: ["php2shell", "docker-security", "base-images"]
cves: ["CVE-2026-109618", "CVE-2026-109619"]
source: "https://www.docker.com/blog/security-update-on-php2shell-impact-for-docker-customers/"
source_name: "Docker Blog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Plan:** Two critical PHP CVEs affect Docker images built on PHP; audit pipelines for PHP-based container images and update base images to patched PHP versions. Neither CVE is KEV-listed and EPSS scores are low (0.12/0.06), so no emergency, but schedule the base-image refresh this sprint.
- **Leader — Skip**
- **Signals:** CVE-2026-109618 — CISA KEV: not listed, EPSS 0.12, reported by 2 collected sources · CVE-2026-109619 — CISA KEV: not listed, EPSS 0.06, reported by 2 collected sources
