# Backend Lab

Orchestration, deployment configuration, and shared content for Vaultsh,
Atlas, Forge, and Sentinel.

This repository owns Docker Compose, Caddy, environment configuration, release
policy, and `content/`. Each service repository owns its code, tests,
dependencies, Dockerfile, and development instructions.

## Run locally

Prerequisites: Docker Engine or Docker Desktop with Compose v2, plus sibling
clones of `vaultsh`, `atlas`, and `forge`.

```sh
cp .env.example .env
openssl rand -hex 32 # ATLAS_AUTH_TOKEN
openssl rand -hex 32 # FORGE_AUTH_TOKEN
docker compose up --build
```

Open http://localhost:8080. Atlas and Forge are available only on the private
Compose network.

```sh
docker compose logs --tail=100
docker compose logs -f vault atlas forge
docker compose down
```

Do not commit `.env`. Set `ATLAS_AUTH_TOKEN` and `FORGE_AUTH_TOKEN` to
independent values; Compose rejects missing tokens.

## Production

Pushes to `main` deploy immutable, Git-SHA-tagged service images to
[mateolabs.dev](https://mateolabs.dev). Caddy is the only container that
publishes host ports. See the [deployment guide](content/docs/deployment.md)
for host setup, security controls, updates, and rollback.

## Repository scope

- `compose.yaml` and `compose.prod.yaml`: local and production topology
- `Caddyfile`: HTTPS ingress
- `content/`: canonical Markdown mounted read-only by Vaultsh and Atlas
- `sentinel.yml` and `sentinel-impact.json`: release-analysis policy
- `.github/workflows/`: integration, assessment, and deployment automation

Application logs go to container stdout and remain separate from Forge
telemetry.

## Documentation

- [Architecture overview](content/docs/architecture/overview.md)
- [HTTP API](content/docs/api.md)
- [Command reference](content/docs/commands.md)
- [Event catalog](content/docs/events.md)
- [Content format](content/docs/content.md)
- [Roadmaps](content/docs/roadmaps/)

Service-specific architecture is under
[`content/docs/architecture/`](content/docs/architecture/). Development
commands belong in each service repository README.
