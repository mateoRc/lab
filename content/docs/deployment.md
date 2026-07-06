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
FORGE_RETENTION_DAYS=30
FORGE_MAX_DATABASE_BYTES=134217728
SESSION_LIMIT=5000
```

Never commit `.env`. Store production values in the deployment platform's
secret manager when one is available.

For private GHCR packages, the production GitHub environment also requires:

- `GHCR_TOKEN` — package token with read access
- `GHCR_USERNAME` — optional account override; defaults to `mateoRc`
- Existing SSH, service-token, and server-host secrets

Public packages can be pulled anonymously; the workflow skips registry login
when `GHCR_TOKEN` is absent.

Each service repository can define `LAB_DISPATCH_TOKEN`, scoped to dispatch the
Lab workflow, so successful `main` CI runs trigger an advisory Sentinel
assessment for that exact service commit.

## Immutable Images

Vaultsh, Atlas, and Forge CI publish GHCR images tagged with the full Git commit
SHA. Production Compose contains no service build contexts; it reads pinned
image references from `runtime/versions.env`.

During the initial migration, merge and run all three service CI workflows
before deploying the image-only Lab Compose configuration. The first Lab
deployment fails safely if any resolved SHA has not been published.

Lab's deployment workflow:

1. Resolves the selected service commits.
2. Updates a tested release manifest.
3. Pulls the immutable images.
4. Starts either the full release or one selected service.
5. Waits for health checks and verifies public HTTPS.
6. Publishes the release and all three service versions to Vaultsh.

Caddy automatically obtains and renews the domain's HTTPS certificate. Check
the deployment:

```sh
curl -I https://portfolio.example.com/healthz
docker compose \
  --env-file .env \
  --env-file runtime/versions.env \
  -f docker-compose.prod.yml ps
docker compose \
  --env-file .env \
  --env-file runtime/versions.env \
  -f docker-compose.prod.yml logs --tail=100
```

Stop the deployment:

```sh
docker compose \
  --env-file .env \
  --env-file runtime/versions.env \
  -f docker-compose.prod.yml down
```

Do not add host `ports` entries to Vaultsh, Atlas, or Forge.

## Forge data

Forge stores accepted events in `/app/data/forge.db` on the `forge_data` named
volume. The default policy retains 30 days and limits the SQLite database plus
WAL to 128 MiB. Normal `docker compose down` preserves this volume; do not use
`down --volumes` unless deleting analytics is intentional.

Create a consistent backup file while Forge remains online:

```sh
mkdir -p backups
docker compose \
  --env-file .env \
  --env-file runtime/versions.env \
  -f docker-compose.prod.yml \
  exec forge python -m scripts.database backup \
  --database /app/data/forge.db \
  --output /app/data/forge-backup.db
docker compose \
  --env-file .env \
  --env-file runtime/versions.env \
  -f docker-compose.prod.yml \
  cp forge:/app/data/forge-backup.db backups/forge.db
docker compose \
  --env-file .env \
  --env-file runtime/versions.env \
  -f docker-compose.prod.yml \
  exec forge rm /app/data/forge-backup.db
```

Transfer `backups/forge.db` off the host. To restore, stop Forge, replace the
database through a one-off container, and start Forge again:

```sh
docker compose \
  --env-file .env \
  --env-file runtime/versions.env \
  -f docker-compose.prod.yml stop forge
docker compose \
  --env-file .env \
  --env-file runtime/versions.env \
  -f docker-compose.prod.yml \
  run --rm \
  -v "$(pwd)/backups:/backup:ro" \
  forge python -m scripts.database restore \
  --database /app/data/forge.db \
  --input /backup/forge.db
docker compose \
  --env-file .env \
  --env-file runtime/versions.env \
  -f docker-compose.prod.yml up -d --wait forge
```

Restore validates SQLite integrity and atomically replaces the database.

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

Use the Lab `Deploy` workflow.

- A push to Lab `main` deploys the latest successful service SHAs together.
- A manual `deploy` run can target `vault`, `atlas`, `forge`, or `all`.
- A targeted run can optionally select an existing full Git SHA.

Review logs and health status after every update. Do not automatically prune
images until the updated stack has passed its health checks.

## Rollback

Run the Lab `Deploy` workflow manually with `action=rollback`. Rollback swaps
the current and previous tested release manifests, pulls those exact images,
updates the full Compose stack, waits for health, and verifies public HTTPS.

The manifest behavior is covered by `tests/test_release_versions.py`.

For emergency server-side recovery:

```sh
cd /home/deploy/backend_lab/lab
python3 scripts/release_versions.py rollback --runtime runtime
docker compose \
  --env-file .env \
  --env-file runtime/versions.env \
  -f docker-compose.prod.yml pull
docker compose \
  --env-file .env \
  --env-file runtime/versions.env \
  -f docker-compose.prod.yml up -d --wait
```

Deployment remains centralized in Lab so secrets, Compose state, release
history, and rollback stay under one concurrency lock.
