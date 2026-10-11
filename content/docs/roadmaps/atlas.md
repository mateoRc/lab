# Atlas Roadmap

This file tracks delivery status. Current design belongs in
[Atlas architecture](../architecture/atlas.md).

**Status:** Search service implemented; search remains a linear scan of the
shared Markdown content.

## Completed

- [x] Spring Boot service, container image, health endpoint, and uptime status
- [x] Read-only recursive Markdown discovery
- [x] Validated, case-insensitive search API
- [x] Deterministic path, line-number, and source-line results
- [x] Unit, integration, and container tests
- [x] Vaultsh integration and bearer service authentication
- [x] Bounded, asynchronous best-effort Forge search telemetry
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
