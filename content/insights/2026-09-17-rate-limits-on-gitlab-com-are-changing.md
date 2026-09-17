---
title: "GitLab.com rate limits go subscription-tiered starting Oct 19, 2026"
date: 2026-09-17T15:22:47.330544+00:00
verdict: "Act"
verdict_platform: "Skip"
verdict_cicd: "Act"
verdict_leader: "Plan"
tags: ["gitlab", "rate-limits", "ci-cd"]
cves: []
source: "https://about.gitlab.com/blog/rate-limit-change-2026/"
source_name: "GitLab Blog"
status: "active"
---
- **Platform/SRE — Skip**
- **CI/CD — Act:** Unauthenticated GitLab.com API requests will be hard-capped at 60/hour per IP starting October 19, 2026 — automation running against paid accounts without credentials is also affected. Audit all pipelines and scripts for unauthenticated GitLab.com calls and ensure they use authenticated tokens before October 19; a preview enforcement window runs October 7 and 14.
- **Leader — Plan:** Rate limits will align with subscription tier (Free on October 19, Premium/Ultimate in January 2027), which may expose gaps in how teams authenticate automation or whether the org's tier is adequate. Schedule a review of GitLab.com subscription tier and org-wide authentication standards before October 19.
