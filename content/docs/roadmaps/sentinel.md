# Sentinel Roadmap

This file tracks delivery status. Current design belongs in
[Sentinel architecture](../architecture/sentinel.md).

## Completed

- [x] Python CLI, normalized evidence model, and strict configuration
- [x] Allowlisted, bounded deterministic check adapters
- [x] Change-aware check selection across Backend Lab repositories
- [x] Regression, security, contract, and degradation checks
- [x] Central evidence redaction and deterministic remediation
- [x] Mock analysis provider and advisory release policy
- [x] Markdown, JSON, pull-request, and sanitized runtime reports

## Before 1.0

- [ ] Add change-selected parser, API, and session checks.
- [ ] Report missing coverage without inventing results.
- [ ] Integrate a production LLM provider.
- [ ] Restrict model context to diffs, configuration, and check evidence.
- [ ] Require file, line, check, or log references for findings.
- [ ] Defend against prompt injection in repository content and logs.
- [ ] Explain failures, release risk, and missing verification.
- [ ] Replace the mock provider in the release workflow.
- [ ] Use protected environments for high-risk approval.

## Explicitly deferred

- Autonomous fixes or deployments
- Multi-agent workflows
- Persistent databases or vector stores
- Kubernetes
- A continuously running Sentinel service
