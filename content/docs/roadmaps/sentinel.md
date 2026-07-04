# Sentinel Roadmap

## Pre-1.0

### Bootstrap

- [x] Python package and CLI entry point
- [x] Unit-test and GitHub Actions foundation
- [x] Initial Backend Lab configuration
- [x] Normalized check and assessment models
- [x] Mock analysis provider
- [x] Markdown and JSON reports
- [x] Advisory Backend Lab workflow
- [x] Strict configuration validation
- [x] Extensible check-adapter registry
- [x] Source metadata for every evidence item

### Deterministic Checks

- [x] Run allowlisted commands with timeouts and output limits
- [x] Apply policy to test, security, and deployment results
- [x] Fail closed on invalid configuration or missing required evidence
- [ ] Redact secrets from logs and reports

### Regression Analysis

- [ ] Identify changed repositories, services, and files
- [ ] Map changes to relevant unit, integration, and deployment tests
- [x] Aggregate Vaultsh, Atlas, Forge, and Compose checks
- [ ] Verify parser, API, session, service-contract, and degradation paths
- [ ] Report missing coverage without inventing results

### Security Analysis

- [ ] Verify missing and invalid service tokens are rejected
- [ ] Test path traversal, malformed input, and command-injection strings
- [ ] Verify request limits, rate limits, headers, and internal-port isolation
- [x] Verify configured security headers and internal-network isolation
- [x] Ingest dependency, container, and secret-scanning results

## Version 1.0

### Agent Analysis

- [ ] Add a provider-independent analysis interface
- [ ] Integrate a production LLM provider
- [ ] Restrict context to diffs, configuration, and check evidence
- [ ] Require file, line, check, or log references for findings
- [ ] Defend against prompt injection in repository content and logs
- [ ] Explain failures, release risk, and missing verification
- [ ] Replace the mock provider in the release workflow

### Release Integration

- [x] Run an advisory mock assessment on pull requests and `main`
- [x] Publish step summaries and report artifacts
- [ ] Publish or update pull-request comments
- [ ] Use protected environments for high-risk release approval
- [x] Dogfood Sentinel on Vaultsh, Atlas, Forge, and Lab
- [x] Expose sanitized status in the existing deployment dashboard

## Explicitly Deferred

- Autonomous fixes or deployments
- Multi-agent workflows
- Persistent databases or vector stores
- Kubernetes deployment
- A continuously running Sentinel service
