# Vaultsh Roadmap

This file lists unfinished work only. Current behavior belongs in
[Vaultsh architecture](../architecture/vaultsh.md) and the
[command reference](../commands.md).

## Shell and state

- Add file timestamps and `ls -t`.
- Introduce session-store and filesystem abstractions.
- Add an external session store if Vaultsh runs multiple replicas.
- Evaluate aliases, environment variables, plugins, and multiple mounted
  vaults.
- Add fuzzy history search with `Ctrl+R`.

## Search and performance

- Add indexing, ranking, and a query language through Atlas.
- Add benchmarks and profiling before introducing an LRU cache.

## Content and documents

- Add education, certifications, achievements, public contact links, and
  additional technical write-ups.
- Export selected canonical Markdown documents to deterministic PDFs outside
  the searchable content tree.
- Evaluate an `open <path.md>` command for generated documents.
- Mount cached provider content from the proposed [Scribe service](scribe.md).

## Operations

- Keep a short sanitized deployment history.
- Evaluate JWT authentication only if a user-specific access model is added.
- Evaluate WebSocket, TUI, and CLI clients if the HTTP terminal is
  insufficient.

## Optional product details

- Add session-scoped command-sequence easter eggs.
