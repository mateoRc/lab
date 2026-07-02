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
- [x] Support Vault events
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

## After MVP

- [x] Configurable dashboard width
- [x] Event filtering
- [x] Graceful handling of unknown event names
- [x] Versioned container images

## Explicitly Deferred

- Grafana
- Prometheus
- Database
- Persistent metrics
- Kafka
- External queues
- Authentication
- Distributed tracing
