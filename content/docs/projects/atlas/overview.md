# Atlas

## Purpose

An authenticated Java/Spring Boot service that searches the Markdown content shared with Vaultsh.

## Implemented

- Deterministic, case-insensitive line scanning with source paths, line numbers, and original text.
- Service authentication, status reporting, and best-effort Forge telemetry.

## Design decisions

Scan the read-only content mount on each request. This keeps results current and avoids maintaining a separate index.

## Status and limits

Active project. Search is linear and has no ranking or index. Telemetry failure does not fail search.

Source: [Atlas](https://github.com/mateoRc/atlas) · [Architecture](architecture.md) · [Roadmap](roadmap.md)
