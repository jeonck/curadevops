---
title: "PHP2Shell: critical pre-auth RCE in PHP engine (CVE-2026-109618/19)"
date: 2026-10-23T15:33:11.401461+00:00
verdict: "Act"
verdict_platform: "Act"
verdict_cicd: "Skip"
verdict_leader: "Skip"
tags: ["php", "security", "remote-code-execution"]
cves: ["CVE-2026-109618", "CVE-2026-109619"]
source: "https://about.gitlab.com/blog/gitlab-helps-remediate-critical-php-flaws/"
source_name: "GitLab Blog"
status: "active"
---
- **Platform/SRE — Act:** CVSS 9.2 pre-auth RCE in the PHP engine itself with a vendor-confirmed attack path on Apache/mod_php and no application-level workaround; upgrade every web-serving host or container to PHP 8.5.12, 8.4.27, 8.3.36, or 8.2.35 now (patch released 2026-10-21).
- **CI/CD — Skip**
- **Leader — Skip**
- **Signals:** CVE-2026-109618 — CISA KEV: not listed, EPSS 0.12, reported by 2 collected sources · CVE-2026-109619 — CISA KEV: not listed, EPSS 0.06, reported by 2 collected sources
