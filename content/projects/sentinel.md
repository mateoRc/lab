# Sentinel

**Personal project** · Planned

## Summary

An agentic CI/CD release guardian that analyzes changes, tests, security
checks, and deployments to explain failures and assess release risk.

## Details

- **Technology:** Python and GitHub Actions
- **Interface:** CLI, CI reports, and pull request checks

## Planned capabilities

- Change-aware release risk assessment
- Deterministic regression and security checks
- CI failure analysis with file and line references
- Deployment and rollback recommendations
- Human approval for high-risk releases

## Decisions

- Deterministic policies own pass/fail decisions.
- Agent analysis is advisory and evidence-based.
- Repository access is read-only and production changes require approval.
