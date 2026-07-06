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

String fields accept only letters, numbers, `.`, `_`, and `-`. Their maximum
lengths are 64 characters for `service` and 128 for `event` and `name`.
`duration_ms` is limited to `0`–`86400000`; `exit_code` is limited to
`0`–`255`. Unknown fields are rejected.

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

Forge stores validated events in SQLite with a server-generated UTC timestamp.
Stored fields are limited to service, event, name, duration, and exit code.
Unknown fields are rejected; IPs, tokens, request bodies, and command arguments
are not accepted.

Summaries are rebuilt from retained events and include request and error totals,
average and median latency, and counts by service and operation. Retention and
database-size limits delete the oldest rows.

## Delivery Guarantees

- Producer queues hold at most 1,000 events by default.
- Enqueueing does not block application requests.
- Events are dropped if a producer queue is full.
- Events may be lost while queued by a producer or during delivery.
- Forge persists accepted events, but there are no durable producer
  acknowledgements, retries, or cross-producer ordering guarantees.
- Telemetry delivery failures never fail Vaultsh commands or Atlas searches.

This best-effort model is intentional for the MVP.
