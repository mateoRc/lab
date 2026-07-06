# Atlas Roadmap

This file tracks delivery status. Current design belongs in
[Atlas architecture](../architecture/atlas.md).

## Completed

- [x] Spring Boot service, container image, and health endpoint
- [x] Read-only recursive Markdown discovery
- [x] Validated, case-insensitive search API
- [x] Deterministic path, line-number, and source-line results
- [x] Unit, integration, and container tests
- [x] Vaultsh integration and bearer service authentication
- [x] Best-effort Forge telemetry
- [x] Immutable commit-tagged images

## Candidates

- [ ] Add an inverted index when measured content size or query load makes linear
  scans inadequate.
- [ ] Add ranking, token-aware matching, and a query language if substring results
  become too imprecise.
- [ ] Evaluate caching only after profiling.

## Explicitly deferred

- Database
- Embeddings or external search libraries
- Durable or external telemetry queues
- End-user authentication
- Anvil integration
