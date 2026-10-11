# Backend Lab: system overview

Backend Lab is an integrated backend engineering showcase. A browser terminal and Explorer expose a read-only Markdown filesystem; separate services add search and telemetry, while the Lab repository owns the shared content and deployment.

## Components

- **Vaultsh** serves the terminal, Explorer, virtual shell, sessions, completion, and read-only document browsing.
- **Atlas** scans the shared Markdown files for case-insensitive search and returns source paths and line numbers.
- **Forge** accepts bounded telemetry events, stores them in SQLite, and returns summaries and text dashboards.
- **Sentinel** runs in CI to collect evidence and apply deterministic release policy. It is not a runtime service. Its current analysis provider is a mock; production LLM analysis is planned.
- **Lab** owns Docker Compose, Caddy ingress, shared content, deployment workflows, and project-specific Sentinel policy.

## Design decisions

Vaultsh and Atlas read one content mount; neither writes to it. Caddy is the public entry point, with Atlas and Forge on the private backend network. Atlas search and Forge telemetry degrade independently. Lab deploys immutable service images by commit SHA and supports targeted updates and tested rollback.

## Status and limits

The shell, browse API, line scanning, SQLite telemetry, and CI assessment are implemented. Search has no index or ranking; Forge producers use best-effort queues; Vaultsh sessions are local and expire. Sentinel's Lab policy is advisory, and its analysis provider is a mock.

## Explore next

- [Vaultsh](vaultsh.md) · terminal, parser, and virtual filesystem
- [Atlas](atlas.md) · search design
- [Forge](forge.md) · telemetry and dashboard
- [Sentinel](sentinel.md) · CI release assessment
- [Architecture](../docs/architecture/overview.md) · runtime topology and boundaries
- [Deployment](../docs/deployment.md) · orchestration and rollback

Source: [Lab](https://github.com/mateoRc/lab), [Vaultsh](https://github.com/mateoRc/vaultsh), [Atlas](https://github.com/mateoRc/atlas), [Forge](https://github.com/mateoRc/forge), and [Sentinel](https://github.com/mateoRc/sentinel).
