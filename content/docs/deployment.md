# Production Deployment

The production Compose stack exposes only Caddy. Caddy terminates HTTPS and
proxies requests to Vaultsh over a private frontend network. Atlas and Forge
are attached only to an internal backend network.

```text
Internet -> Caddy :443 -> Vaultsh -> Atlas / Forge
```

## Prerequisites

- A Linux server with Docker Engine and Docker Compose v2
- A public domain with `A` and/or `AAAA` records pointing to the server
- Inbound TCP ports 80 and 443 and UDP port 443 allowed by the firewall

## Configuration

Create `lab/.env` from `.env.example`:

```sh
cp .env.example .env
openssl rand -hex 32
openssl rand -hex 32
```

Set the generated values and deployment domain:

```dotenv
DOMAIN=portfolio.example.com
ATLAS_AUTH_TOKEN=<first-generated-token>
FORGE_AUTH_TOKEN=<second-generated-token>
SESSION_LIMIT=5000
```

Never commit `.env`. Store production values in the deployment platform's
secret manager when one is available.

## Start

```sh
docker compose -f docker-compose.prod.yml config
docker compose -f docker-compose.prod.yml up --build -d --wait
```

Caddy automatically obtains and renews the domain's HTTPS certificate. Check
the deployment:

```sh
curl -I https://portfolio.example.com/healthz
docker compose -f docker-compose.prod.yml ps
docker compose -f docker-compose.prod.yml logs --tail=100
```

Stop the deployment:

```sh
docker compose -f docker-compose.prod.yml down
```

Do not add host `ports` entries to Vaultsh, Atlas, or Forge.

## Protection Limits

Vaultsh enforces:

- 16 KB maximum JSON request body
- 4,096-byte command and completion input limit
- 30 execution requests per minute per client, burst 10
- 120 completion requests per minute per client, burst 20
- 120 service-status requests per minute per client, burst 20
- 5,000 active sessions by default
- HTTP header, read, write, and idle timeouts
- Content Security Policy and defensive response headers

Caddy independently limits request bodies to 16 KB, adds HTTPS security
headers, and applies upstream timeouts. Compose limits CPU, memory, process
counts, Linux capabilities, filesystem writes, and network reachability.

Rate limits are per application instance and reset when Vaultsh restarts. A
multi-instance deployment should use the hosting provider or CDN for a shared
edge rate limit.

## Cloudflare

Start with DNS-only records while validating the deployment. When enabling the
Cloudflare proxy:

- Set SSL/TLS mode to `Full (strict)`.
- Keep the Caddy origin certificate active.
- Add Cloudflare rate-limiting rules for `/api/exec` and `/api/complete`.
- Restrict origin ports 80 and 443 to Cloudflare IP ranges if the origin must
  not be reachable directly.
- Configure trusted proxy ranges before relying on forwarded client addresses
  for application rate limiting.

Do not use Cloudflare's `Flexible` TLS mode.

## Suggested Cloudflare Rules

- `/api/exec`: 30 requests per minute per IP
- `/api/complete`: 120 requests per minute per IP
- Block request bodies larger than 16 KB

Cloudflare availability and rule quotas depend on the selected account plan.

## Updating

```sh
git pull
docker compose -f docker-compose.prod.yml up --build -d --wait
```

Review logs and health status after every update. Do not automatically prune
images until the updated stack has passed its health checks.

## Targeted Service Updates

The services are independently rebuildable within the same Compose project.
For a manual service-only update:

```sh
git -C ../atlas pull --ff-only
docker compose -f docker-compose.prod.yml config --quiet
docker compose -f docker-compose.prod.yml up --build -d --wait --no-deps atlas
```

Replace `atlas` and its source path with `vault`/`../vaultsh` or
`forge`/`../forge` as needed. Use a full-stack update when Compose
configuration, shared content, service tokens, or cross-service contracts
change.

The automated deployment remains centralized in Lab. Separate per-service
deployment workflows should wait until production uses pinned image versions
and defines API compatibility rules; otherwise independent pipelines would
increase coordination risk without isolating the shared deployment state.
