# Sentinel

**Personal project** · Active, pre-1.0

## Summary

An agentic CI/CD release guardian that analyzes changes, tests, security
checks, and deployments to explain failures and assess release risk.

## Details

- **Technology:** Python and GitHub Actions
- **Interface:** CLI, CI reports, and pull request checks

## Current capabilities

- Deterministic regression and security checks
- Strict policy validation and normalized evidence
- Advisory release-risk assessments
- Markdown, JSON, and sanitized runtime reports
- Extensible check adapters with bounded output

## Planned capabilities

- Change-aware release risk assessment
- Production LLM analysis with evidence references
- Pull-request reporting
- Human approval for high-risk releases

## Decisions

- Deterministic policies own pass/fail decisions.
- Agent analysis is advisory and evidence-based.
- Repository access is read-only and production changes require approval.
