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
- [ ] Strict configuration validation
- [ ] Extensible check-adapter registry
- [ ] Source metadata for every evidence item

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
