# Forge Roadmap

This file tracks delivery status. Current design belongs in
[Forge architecture](../architecture/forge.md).

**Status:** SQLite-backed telemetry service implemented. File-backed storage
is used in the integrated stack; direct development can use in-memory SQLite.

## Completed

- [x] FastAPI service, container image, and health endpoint
- [x] Validated event ingestion for Vaultsh and Atlas
- [x] Serialized SQLite access and SQL-backed time-window summaries
- [x] Filtered JSON summaries and ASCII dashboards
- [x] Average, p50, and p95 latency from retained events
- [x] Unit, API, and container tests
- [x] Bearer service authentication and versioned images
- [x] SQLite event persistence on a dedicated volume
- [x] WAL mode and ordered schema migrations
- [x] Server-generated timestamps and bounded sanitized fields
- [x] Summaries rebuilt from persisted events
- [x] Retention and database-size limits
- [x] Verified backup and restore tooling
- [x] 24-hour, 7-day, and 30-day activity windows with p95 latency
- [x] Dashboard retention and database-usage visibility
- [x] Separate runtime errors from user command failures in summaries
- [x] Count Vaultsh commands separately from Atlas search operations
- [x] Report the exact timestamp of the oldest retained event
- [ ] incrase default retention limit to 256

## Explicitly deferred

- Grafana and Prometheus
- Kafka or external queues
- End-user authentication
- Distributed tracing
