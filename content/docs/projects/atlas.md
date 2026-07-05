# Atlas

**Personal project** · Active

## Summary

An authenticated HTTP search service that performs case-insensitive search
across the shared portfolio content used by Vaultsh.

## Details

- **Technology:** Java, Spring Boot, Maven, and Docker
- **API:** `GET /search` and `GET /healthz`

## Features

- Recursive UTF-8 content discovery and line-by-line scanning
- File path and line number results
- Query validation and integration tests
- Bearer service authentication
- Best-effort telemetry delivery to Forge

## Decisions

- Keep search infrastructure minimal for the current content size.
- Avoid a database or external search engine until indexing is justified.
