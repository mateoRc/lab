# Sentinel Roadmap

This file tracks delivery status. Current design belongs in
[Sentinel architecture](architecture.md).

**Status:** Advisory CI assessment is integrated. The mock provider remains
active; Sentinel does not gate deployment.

## Completed

- [x] Python CLI, normalized evidence model, and strict configuration
- [x] Allowlisted, bounded deterministic check adapters
- [x] Change-aware check selection across Backend Lab repositories
- [x] Regression, security, contract, and degradation checks
- [x] Central evidence redaction and deterministic remediation
- [x] Mock analysis provider and advisory release policy
- [x] Markdown, JSON, pull-request, and sanitized runtime reports
- [x] Lab workflow dispatch and change-selected integration checks

## Before 1.0

- [ ] Add change-selected parser, API, and session checks.
- [ ] Report missing coverage without inventing results.
- [ ] Integrate a production LLM provider.
- [ ] Restrict model context to diffs, configuration, and check evidence.
- [ ] Require file, line, check, or log references for findings.
- [ ] Defend against prompt injection in repository content and logs.
- [ ] Explain failures, release risk, and missing verification.
- [ ] Replace the mock provider in the release workflow after the production
  provider and evidence controls are ready.
- [ ] Promote the workflow from advisory reporting to an enforced release gate
  only after check coverage is proven.
- [ ] Use protected environments for high-risk approval.

## Explicitly deferred

- Autonomous fixes or deployments
- Multi-agent workflows
- Persistent databases or vector stores
- Kubernetes
- A continuously running Sentinel service
