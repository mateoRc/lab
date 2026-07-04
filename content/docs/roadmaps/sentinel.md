# Sentinel Roadmap

## MVP

### Bootstrap

- [x] Python package and CLI entry point
- [x] Unit-test and GitHub Actions foundation
- [x] Initial Backend Lab configuration
- [ ] Strict configuration validation
- [ ] Normalized check, evidence, finding, and risk models
- [ ] Markdown and JSON reports

### Deterministic Checks

- [ ] Run allowlisted commands with timeouts and output limits
- [ ] Apply policy to test, security, and deployment results
- [ ] Fail closed on invalid configuration or missing required evidence
- [ ] Redact secrets from logs and reports

### Regression Analysis

- [ ] Identify changed repositories, services, and files
- [ ] Map changes to relevant unit, integration, and deployment tests
- [ ] Verify parser, API, session, service-contract, and degradation paths
- [ ] Report missing coverage without inventing results

### Security Analysis

- [ ] Verify missing and invalid service tokens are rejected
- [ ] Test path traversal, malformed input, and command-injection strings
- [ ] Verify request limits, rate limits, headers, and internal-port isolation
- [ ] Ingest dependency, container, and secret-scanning results

## After MVP

### Agent Analysis

- [ ] Add a provider-independent analysis interface
- [ ] Restrict context to diffs, configuration, and check evidence
- [ ] Require file, line, check, or log references for findings
- [ ] Defend against prompt injection in repository content and logs
- [ ] Explain failures, release risk, and missing verification

### GitHub Integration

- [ ] Run on pull requests and releases
- [ ] Publish step summaries, report artifacts, and updated PR comments
- [ ] Use protected environments for high-risk release approval
- [ ] Dogfood Sentinel on Vaultsh, Atlas, Forge, and Lab
- [ ] Expose sanitized status in the existing deployment dashboard

## Explicitly Deferred

- Autonomous fixes or deployments
- Multi-agent workflows
- Persistent databases or vector stores
- Kubernetes deployment
- A continuously running Sentinel service
