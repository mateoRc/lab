# Forge Roadmap

This file tracks delivery status. Current design belongs in
[Forge architecture](../architecture/forge.md).

## Completed

- [x] FastAPI service, container image, and health endpoint
- [x] Validated event ingestion for Vaultsh and Atlas
- [x] Thread-safe in-memory aggregation
- [x] Filtered JSON summaries and ASCII dashboards
- [x] Bounded median-latency samples
- [x] Unit, API, and container tests
- [x] Bearer service authentication and versioned images
- [x] SQLite event persistence on a dedicated volume
- [x] WAL mode and ordered schema migrations
- [x] Server-generated timestamps and bounded sanitized fields
- [x] Summaries rebuilt from persisted events
- [x] Retention and database-size limits
- [x] Verified backup and restore tooling

## Explicitly deferred

- Grafana and Prometheus
- Kafka or external queues
- End-user authentication
- Distributed tracing
