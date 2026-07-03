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
- Atlas: private Compose network only
- Forge: private Compose network only

Stop the stack:

```sh
docker compose down
```

To get a temporary public URL for the local app:

```sh
docker run --rm cloudflare/cloudflared:latest tunnel --url http://host.docker.internal:8080
```

Open the `trycloudflare.com` URL printed by the command.

## Server access

```powershell
ssh -i C:\dev\backend_lab\keys\ssh-key-2026-07-02.key root@<server-ip>
```

## Logs

All services write logs to container stdout. Docker rotates each service's
local JSON logs at 10 MB and retains three files.

```sh
docker compose logs --tail=100
docker compose logs -f forge
docker compose logs -f vault atlas
```

Logs are local operational output, not Forge telemetry. Forge keeps aggregated
telemetry counters in memory and does not store application logs.

## Configuration

Copy `.env.example` to `.env`, then generate independent service tokens:

```sh
openssl rand -hex 32
openssl rand -hex 32
```

Set the results as `ATLAS_AUTH_TOKEN` and `FORGE_AUTH_TOKEN`. Compose refuses
to start when either token is missing. Do not commit `.env`.

Only Vault publishes a host port. Atlas and Forge are reachable exclusively
through the private Compose network and require bearer authentication on all
non-health endpoints.

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
