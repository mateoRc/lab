# Forge Roadmap

This file lists unfinished work only. Current behavior belongs in
[Forge architecture](../architecture/forge.md).

## Persistent analytics

Keep persistence inside Forge unless storage requires independent operational
ownership.

- Store events in SQLite on a persistent volume.
- Enable WAL mode and schema migrations.
- Record timestamps without IPs, tokens, request bodies, or arguments.
- Build summaries from persisted events.
- Define retention and database-size limits.
- Add off-server backup and restore procedures.

## Explicitly deferred

- Grafana and Prometheus
- Kafka or external queues
- End-user authentication
- Distributed tracing
