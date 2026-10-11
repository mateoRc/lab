# Forge

## Purpose

A Python/FastAPI telemetry service for Vaultsh and Atlas.

## Implemented

- Authenticated event ingestion, bounded SQLite storage, and filtered summaries.
- Request, error, latency, service, and command analytics with terminal-friendly dashboards.
- Retention and database-size limits, migrations, and backup and restore procedures.

## Design decisions

Store only sanitized, bounded event fields. SQLite fits the single-instance deployment; plain-text dashboards work in Vaultsh without another analytics UI.

## Status and limits

Active project. Producer queues are best-effort, so events can be lost before Forge accepts them. Accepted events survive service restarts.

Source: [Forge](https://github.com/mateoRc/forge) · [Architecture](../docs/architecture/forge.md) · [Roadmap](../docs/roadmaps/forge.md)
