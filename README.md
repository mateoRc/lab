# Backend Lab

Local orchestration and shared content for Vault and Atlas.

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
