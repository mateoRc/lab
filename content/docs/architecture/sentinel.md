# Sentinel Architecture

Sentinel runs in CI and consumes repository configuration, Git diffs, and
machine-readable check results. It is not a runtime Backend Lab service.

## Components

### Change Analyzer

Identifies affected repositories, services, files, and configuration surfaces.

### Check Runner

Executes deterministic regression, security, build, and deployment checks.
Every check produces a status, structured evidence, and logs.

Checks use adapters that convert tool-specific output into one normalized
result contract. Adding a scanner or test suite should require a new adapter,
not changes to policy, agent, or reporting code.

### Policy Engine

Applies explicit rules to deterministic results. It owns the release gate and
does not depend on an LLM response.

### Agent Analyzer

Explains failures, assesses release risk, identifies missing coverage, and
recommends actions using diff and check evidence.

### Reporter

Produces Markdown and JSON reports. Reports distinguish facts, policy
decisions, and agent inferences.

On `main`, CI also publishes a reduced assessment containing risk, check
statuses, provider, commit, timestamp, and summary. Vaultsh reads this file
through Lab's existing read-only runtime mount and shows the last assessment
without treating Sentinel as an online service.

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

## Decisions

- Deterministic evidence and policy are the authoritative product core.
- Check adapters are extensible; policy depends only on normalized results.
- LLM providers explain evidence and context but never decide check outcomes.
- Sentinel runs as an ephemeral CI CLI and stores no database initially.
- Repository writes and deployments require separate human-controlled tooling.

Backend Lab owns the versioned policy in `lab/sentinel.yml`. Unknown or missing
required fields will fail validation, agent capabilities are advisory, and
secrets must come from CI rather than YAML.
