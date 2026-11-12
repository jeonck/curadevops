---
title: "Claude Code 'don't ask again' file leaks secrets into GitLab repos"
date: 2026-11-12T18:39:17.321944+00:00
verdict: "Plan"
verdict_platform: "Plan"
verdict_cicd: "Plan"
verdict_leader: "Plan"
tags: ["secrets-management", "claude-code", "supply-chain"]
cves: []
source: "https://about.gitlab.com/blog/prevent-leaks-from-claude-code-dont-ask-again-file/"
source_name: "GitLab Blog"
status: "active"
---
- **Platform/SRE — Plan:** If developers use Claude Code on infra repos, infrastructure credentials may be in committed .claude/settings.local.json files. Audit GitLab repos for that file, rotate any exposed tokens, and add a project-level .gitignore entry to prevent recurrence.
- **CI/CD — Plan:** CI/CD tokens passed to Claude Code shell commands (e.g., registry auth, PRIVATE-TOKENs) could be sitting in committed settings files across pipeline repos. Audit all pipeline repositories for .claude/settings.local.json, rotate any exposed tokens, and enforce a project-level .gitignore entry as a standard pipeline-repo requirement.
- **Leader — Plan:** Apiiro confirmed 1,122 public repos already holding live secrets from this Claude Code behavior — a developer-tool policy gap affecting the whole org. Establish and enforce a policy requiring project-level .gitignore coverage for Claude Code files, and assess internal repo exposure before this quarter ends.
