# Forge

Forge is a lightweight telemetry service for Vault and Atlas. It receives
events over HTTP, aggregates counters in memory, and exposes summaries and a
plain-text ASCII dashboard.

## Flow

```text
Vault / Atlas
      |
      | POST /events
      v
    Forge
      |
      | in-memory aggregation
      v
GET /summary and GET /dashboard
```

## API

### Health

```http
GET /healthz
```

Returns `200 OK` when Forge is ready to receive events.

### Record an Event

```http
POST /events
Content-Type: application/json
```

```json
{
  "service": "vault",
  "event": "command.executed",
  "name": "grep",
  "duration_ms": 8,
  "exit_code": 0
}
```

Forge validates the event and updates its in-memory counters.
The request must include `Authorization: Bearer <FORGE_AUTH_TOKEN>`.

### Summary

```http
GET /summary
```

Returns structured JSON containing request totals, error totals, average
duration, and counts grouped by service and operation.

Filter results by exact field values using any combination of `service`,
`event`, and `name`:

```sh
curl -H "Authorization: Bearer $FORGE_AUTH_TOKEN" \
  "http://localhost:8082/summary?service=vault"
curl -H "Authorization: Bearer $FORGE_AUTH_TOKEN" \
  "http://localhost:8082/summary?event=search.executed&name=search"
```

### Dashboard

```http
GET /dashboard
```

Set proportional bar width from 1 through 100 and apply the same filters:

```sh
curl -H "Authorization: Bearer $FORGE_AUTH_TOKEN" \
  "http://localhost:8082/dashboard?width=30&service=vault"
```

Returns a plain-text dashboard:

```text
Forge dashboard

requests: 184
errors:   3
avg ms:   6

services:
vault   ███████████████ 162
atlas   ██ 22

commands:
cat     ████████ 61
grep    █████ 39
ls      ███ 25
tree    ██ 14
```

## Implementation

- Python and FastAPI
- In-memory counters
- Simple proportional ASCII bar renderer
- Dockerized service
- Docker-only local development

Vault and Atlas submit telemetry asynchronously through their own bounded
in-process queues. Their background workers use `POST /events`; Forge does not
own or run a message broker.

Forge owns its source code, tests, dependencies, and Dockerfile. The `lab`
repository owns only its Compose configuration, environment configuration,
shared content, and local orchestration.

## Constraints

- No Grafana
- No Prometheus
- No database
- No persistent metrics
- No Kafka, external queues, or message broker
- No end-user authentication; internal APIs use bearer service tokens

All counters reset when the Forge process restarts.

Unknown event types are accepted and aggregated. This permits producers to
introduce telemetry before Forge is redeployed.

Images accept a version at build time and expose it through the standard OCI
image label:

```sh
docker build --build-arg VERSION=1.0.0 --tag forge:1.0.0 .
```
