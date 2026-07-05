# Forge Roadmap

## MVP

### Bootstrap

- [x] FastAPI HTTP service
- [x] Docker image
- [x] Shared Docker Compose integration in `lab`
- [x] `GET /healthz`

### Events

- [x] `POST /events`
- [x] Validate service, event, and name
- [x] Accept duration and exit code
- [x] Support Vaultsh events
- [x] Support Atlas events

### Aggregation

- [x] Store counters in memory
- [x] Count total requests
- [x] Count errors
- [x] Calculate average duration
- [x] Aggregate by service
- [x] Aggregate by command or operation

### Output

- [x] `GET /summary`
- [x] `GET /dashboard`
- [x] Render a plain-text dashboard
- [x] Render proportional ASCII bars

### Tests

- [x] Event validation tests
- [x] Counter aggregation tests
- [x] Average-duration tests
- [x] Summary API tests
- [x] Dashboard rendering tests

### Developer Experience

- [x] Docker-only local setup
- [x] Container health check
- [x] Document API usage
- [x] GitHub Actions CI
- [x] Bearer service authentication

## After MVP

- [x] Configurable dashboard width
- [x] Event filtering
- [x] Graceful handling of unknown event names
- [x] Versioned container images

## Planned

### Persistent Analytics

Decision: persistence remains an internal Forge capability, not a separate
product or service. Forge owns telemetry ingestion, storage, aggregation, and
reporting; SQLite is an implementation detail behind that boundary. Revisit
this boundary only if storage needs independent scaling or operational
ownership.

- [ ] Store events in SQLite on a persistent Docker volume
- [ ] Enable WAL mode and add schema migrations
- [ ] Record timestamps without storing IPs, tokens, request bodies, or arguments
- [ ] Build summaries from persisted events
- [ ] Define retention and database-size limits
- [ ] Add automated off-server backups and a restore procedure

## Explicitly Deferred

- Grafana
- Prometheus
- Kafka
- External queues
- End-user authentication
- Distributed tracing
