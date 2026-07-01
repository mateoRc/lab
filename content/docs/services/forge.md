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

### Summary

```http
GET /summary
```

Returns structured JSON containing request totals, error totals, average
duration, and counts grouped by service and operation.

### Dashboard

```http
GET /dashboard
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

Forge owns its source code, tests, dependencies, and Dockerfile. The `lab`
repository owns only its Compose configuration, environment configuration,
shared content, and local orchestration.

## Constraints

- No Grafana
- No Prometheus
- No database
- No persistent metrics
- No Kafka, queues, or asynchronous transport
- No authentication for the MVP

All counters reset when the Forge process restarts.

