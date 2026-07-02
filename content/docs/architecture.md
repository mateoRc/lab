# Backend Lab

The Backend Lab is a collection of small, focused backend services built
mostly by one developer. The goal is not to create microservices for their own
sake, but to make each project solve one problem well and remain independently
useful.

## Projects

### Vault

Vault is a read-only virtual shell engine.

Responsibilities:

- Virtual filesystem
- Shell engine
- Session management
- Command execution
- Parser
- Pipelines
- Terminal API

Vault owns the user experience. It does not own search or telemetry logic.

### Atlas

Atlas is the portfolio's lightweight search engine.

Responsibilities:

- Read UTF-8 text documents from shared storage
- Search documents
- Return matching files and lines

Atlas reads the shared content mounted by the Backend Lab.

Initial implementation:

- Plain-text and Markdown documents
- Case-insensitive line search
- HTTP API
- In-memory only
- No persistence

Future ideas:

- Inverted index
- Ranking
- Prefix search
- Fuzzy search
- Stemming
- Synonyms
- Caching

### Forge

Forge is the portfolio's telemetry analytics and event-processing service.

Responsibilities:

- Receive events from backend services
- Aggregate metrics
- Produce simple operational insights
- Render terminal-friendly ASCII dashboards

Initial implementation:

- HTTP event ingestion
- In-memory counters
- Average latency
- Error count
- Command distribution
- ASCII dashboard

Future ideas:

- Rolling windows
- Histograms
- Percentiles
- Event streaming
- Prometheus exporter

## Communication

```text
Vault
  ├── HTTP ──> Atlas
  └── HTTP ──> Forge
```

HTTP is intentionally sufficient for the MVP. Vault and Atlas enqueue
telemetry in bounded in-process queues, then background workers deliver it to
Forge over HTTP. There is no external queue, Kafka, or message broker. A
durable broker may replace this best-effort delivery only if a concrete future
need justifies it.

## External Services

Vault can integrate with external backend services.

Defined integration targets:

- Atlas — indexing and search
- Forge — telemetry and metrics

Integrations are optional. If an external service is unavailable, Vault
continues functioning with degraded capabilities rather than failing unrelated
command execution.

## Shared Content

The Lab repository owns the single shared content directory:

```text
lab/
└── content/
    ├── cv/
    ├── projects/
    └── docs/
```

Vault mounts this directory as its virtual filesystem. Atlas searches the same
directory. Content must never be duplicated between service repositories.

## User Experience

Vault exposes friendly shell commands:

```text
search kafka
metrics
dashboard
```

Internally, these commands call Atlas and Forge over HTTP. Direct API access
remains available for debugging:

```sh
docker compose exec vault wget -qO- \
  --header="Authorization: Bearer $ATLAS_AUTH_TOKEN" \
  "http://atlas:8080/search?q=kafka"
docker compose exec vault wget -qO- http://atlas:8080/healthz
docker compose exec vault wget -qO- \
  --header="Authorization: Bearer $FORGE_AUTH_TOKEN" \
  http://forge:8080/summary
```

Commands are the product interface. HTTP requests are the debugging interface.

Only Vault publishes a host port. Atlas and Forge are private Compose services.
Their non-health endpoints require independent bearer service tokens. TLS must
terminate at the deployment ingress so browser traffic to Vault is encrypted.

## Design Principles

- Small, focused services
- One responsibility per project
- Docker-first
- HTTP-first
- Standard library where practical
- Independent repositories
- Shared content
- Incremental complexity
- Avoid unnecessary abstractions

## Repository Layout

```text
backend-lab/
├── vaultsh/
├── atlas/
├── forge/
└── lab/
```

Each service repository owns its source code, tests, dependencies, and
Dockerfile. Lab owns Docker Compose, environment configuration, shared content,
and local orchestration.

## Local Logs

Services write operational logs to container stdout. Lab configures Docker's
`json-file` driver with a 10 MB maximum file size and three retained files per
service. Logs remain separate from Forge telemetry and can be inspected with
`docker compose logs`.

## Production Boundary

The production stack places Caddy on the public frontend network. Vaultsh is
reachable from Caddy but has no published host port. Atlas and Forge exist only
on an internal backend network, which Vaultsh joins for service calls.

Caddy owns HTTPS certificate management. Vaultsh owns API rate limits, request
and command size limits, active-session capacity, and HTTP timeouts. Compose
applies container resource and privilege restrictions.
