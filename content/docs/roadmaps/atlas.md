# Atlas Roadmap

This file lists unfinished work only. Current behavior belongs in
[Atlas architecture](../architecture/atlas.md).

## Candidates

- Add an inverted index when measured content size or query load makes linear
  scans inadequate.
- Add ranking, token-aware matching, and a query language if substring results
  become too imprecise.
- Evaluate caching only after profiling.

## Explicitly deferred

- Database
- Embeddings or external search libraries
- Durable or external telemetry queues
- End-user authentication
- Anvil integration
