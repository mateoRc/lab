# Forge Roadmap

## MVP

### Bootstrap

- [ ] FastAPI HTTP service
- [ ] Docker image
- [ ] Shared Docker Compose integration in `lab`
- [ ] `GET /healthz`

### Events

- [ ] `POST /events`
- [ ] Validate service, event, and name
- [ ] Accept duration and exit code
- [ ] Support Vault events
- [ ] Support Atlas events

### Aggregation

- [ ] Store counters in memory
- [ ] Count total requests
- [ ] Count errors
- [ ] Calculate average duration
- [ ] Aggregate by service
- [ ] Aggregate by command or operation

### Output

- [ ] `GET /summary`
- [ ] `GET /dashboard`
- [ ] Render a plain-text dashboard
- [ ] Render proportional ASCII bars

### Tests

- [ ] Event validation tests
- [ ] Counter aggregation tests
- [ ] Average-duration tests
- [ ] Summary API tests
- [ ] Dashboard rendering tests

### Developer Experience

- [ ] Docker-only local setup
- [ ] Container health check
- [ ] Document API usage
- [ ] GitHub Actions CI

## After MVP

- [ ] Configurable dashboard width
- [ ] Event filtering
- [ ] Graceful handling of unknown event names
- [ ] Versioned container images

## Explicitly Deferred

- Grafana
- Prometheus
- Database
- Persistent metrics
- Kafka
- Queues
- Authentication
- Distributed tracing

