# Event Catalog

Vaultsh and Atlas send best-effort telemetry events to Forge over HTTP. Events
are queued temporarily in each producer's memory and delivered by a background
worker using `POST /events`.

Forge requires `Authorization: Bearer <FORGE_AUTH_TOKEN>` for event ingestion
and metrics reads. Its health endpoint is intentionally unauthenticated.

## Event Schema

```json
{
  "service": "vault",
  "event": "command.executed",
  "name": "grep",
  "duration_ms": 8,
  "exit_code": 0
}
```

Fields:

- `service` — event producer.
- `event` — event type.
- `name` — command or operation.
- `duration_ms` — execution duration in milliseconds.
- `exit_code` — `0` for success; non-zero values count as errors.

## Vaultsh Events

### `command.executed`

Emitted after every Vaultsh command execution.

```json
{
  "service": "vault",
  "event": "command.executed",
  "name": "search",
  "duration_ms": 12,
  "exit_code": 0
}
```

`name` contains the first command in the submitted command line, including
built-ins such as `cat`, `grep`, `ls`, `search`, `metrics`, and `dashboard`.

## Atlas Events

### `search.executed`

Emitted after every valid Atlas search request.

```json
{
  "service": "atlas",
  "event": "search.executed",
  "name": "search",
  "duration_ms": 4,
  "exit_code": 0
}
```

Blank or missing queries rejected before search execution do not emit an
event. Search failures use a non-zero exit code.

## Forge Storage

Forge does not save raw events and has no database. It immediately aggregates
events into in-memory values:

- Total requests
- Total errors
- Total duration, average latency, and bounded-sample median latency
- Counts by service
- Counts by command or operation

All counters reset when Forge restarts.

## Delivery Guarantees

- Producer queues hold at most 1,000 events by default.
- Enqueueing does not block application requests.
- Events are dropped if a producer queue is full.
- Events may be lost when a producer or Forge restarts.
- There are no durable acknowledgements, retries, persistence, or ordering
  guarantees.
- Telemetry delivery failures never fail Vaultsh commands or Atlas searches.

This best-effort model is intentional for the MVP.
