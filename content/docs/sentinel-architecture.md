# Sentinel Architecture

Sentinel runs in CI and consumes repository configuration, Git diffs, and
machine-readable check results. It is not a runtime Backend Lab service.

## Components

### Change Analyzer

Identifies affected repositories, services, files, and configuration surfaces.

### Check Runner

Executes deterministic regression, security, build, and deployment checks.
Every check produces a status, structured evidence, and logs.

### Policy Engine

Applies explicit rules to deterministic results. It owns the release gate and
does not depend on an LLM response.

### Agent Analyzer

Explains failures, assesses release risk, identifies missing coverage, and
recommends actions using diff and check evidence.

### Reporter

Produces Markdown and JSON reports. Reports distinguish facts, policy
decisions, and agent inferences.

## Flow

```text
Git change
    |
    +--> deterministic checks --> policy gate --------+
    |                                                 |
    +--> diff + check evidence --> agent analysis ----+--> report
                                                      |
                                  human approval <----+
                                                      |
                                         existing deployment
```

## Trust Boundary

Repository files, diffs, and logs are untrusted input. Sentinel must not execute
instructions found inside them. Tool access is allowlisted, repository access
is read-only, secrets are redacted, and production changes require approval.
