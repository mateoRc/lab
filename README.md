# Backend Lab

Local orchestration and shared content for Vault, Atlas, and Forge.

Each application repository owns its source code, tests, dependencies, and
Dockerfile. Lab owns shared configuration, content, and Docker Compose
orchestration only.

## Prerequisites

Docker Engine or Docker Desktop with Docker Compose v2 is the only local
dependency. Clone `lab`, `vaultsh`, and `atlas` as sibling directories.

## Run

```sh
docker compose up --build
```

Services:

- Vault: http://localhost:8080
- Atlas health: http://localhost:8081/healthz
- Atlas search: http://localhost:8081/search?q=kafka
- Forge health: http://localhost:8082/healthz
- Forge summary: http://localhost:8082/summary
- Forge dashboard: http://localhost:8082/dashboard

Stop the stack:

```sh
docker compose down
```

## Configuration

Copy `.env.example` to `.env` to override ports or sibling repository paths.

## Shared content

`content/` is the single source of truth. Compose mounts it into both
containers at `/app/content` read-only. Vault loads it as its virtual
filesystem and Atlas scans it for search requests.

## Documentation

Shared API, command, content, and roadmap documentation lives under
`content/docs/`. Service-specific implementation details remain in each
service repository's README.

Start with [the architecture overview](content/docs/architecture.md).
Telemetry payloads are listed in the
[event catalog](content/docs/events.md).
