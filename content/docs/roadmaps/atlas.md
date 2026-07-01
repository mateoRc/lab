# Atlas Roadmap

## MVP

### Bootstrap

- [x] Spring Boot HTTP service
- [x] Docker image
- [x] Shared Docker Compose in `lab`
- [x] `GET /healthz`

### Content

- [x] Load plain text files from `/app/content`
- [x] Recursively discover files
- [x] Treat content as read-only

### Search

- [x] `GET /search?q=<query>`
- [x] Case-insensitive line scan
- [x] Return file path, line number, and line text
- [x] Return query, result count, and results as JSON
- [x] Validate missing and blank queries

### Tests

- [x] Health endpoint unit test
- [x] Content scanning tests
- [x] Search API tests
- [x] Empty-result test
- [x] Query validation tests

### Developer Experience

- [x] Docker-only local setup
- [x] Container health check
- [x] Mount shared content at `/app/content` as read-only
- [x] Document API usage
- [x] GitHub Actions CI
- [x] Shared local deployment for Vault and Atlas

## After MVP

- [ ] Vault HTTP integration
- [ ] Versioned container images

## Explicitly Deferred

- Inverted index
- Ranking
- Database
- Cache
- Authentication
- Embeddings
- External search libraries
- Queues and asynchronous events
- Anvil integration
- Forge telemetry

