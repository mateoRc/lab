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

## Persistent analytics

Keep persistence inside Forge unless storage requires independent operational
ownership.

- [ ] Store events in SQLite on a persistent volume.
- [ ] Enable WAL mode and schema migrations.
- [ ] Record timestamps without IPs, tokens, request bodies, or arguments.
- [ ] Build summaries from persisted events.
- [ ] Define retention and database-size limits.
- [ ] Add off-server backup and restore procedures.

## Explicitly deferred

- Grafana and Prometheus
- Kafka or external queues
- End-user authentication
- Distributed tracing
