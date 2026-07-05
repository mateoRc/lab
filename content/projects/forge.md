# Forge

**Personal project** · Active

## Summary

A lightweight telemetry service for Vaultsh and Atlas with in-memory
aggregation and terminal-friendly activity dashboards.

## Details

- **Technology:** Python, FastAPI, and Docker
- **API:** `POST /events`, `GET /healthz`, `GET /summary`, and `GET /dashboard`
- **Event fields:** Service, event, name, duration, and exit code

## Features

- Request, error, latency, service, and command aggregation
- Filtered summaries and configurable ASCII dashboards
- Bearer service authentication
- Version-labeled container images

## Decisions

- Keep live telemetry in memory and accept reset-on-redeploy behavior.
- Avoid Grafana, Prometheus, Kafka, and a database until persistence is needed.
