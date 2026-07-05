# Backend Lab

**Personal project** · Active

## Summary

The integration and deployment repository for Vaultsh, Atlas, and Forge.
It is the single source of truth for shared searchable portfolio content.

## Details

- **Technology:** Docker, Docker Compose, Caddy, and GitHub Actions
- **Services:** Vaultsh, Atlas, and Forge

## Features

- Reproducible multi-service local and production startup
- Shared read-only content mounts and isolated service networking
- HTTPS ingress, health checks, resource limits, and deployment metadata
- Immutable service images and targeted deployment through GitHub Actions
- Tested release manifests and full-stack rollback

## Decisions

- Keep service repositories independent.
- Centralize orchestration without duplicating content.
