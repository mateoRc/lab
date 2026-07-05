# Vaultsh

**Personal project** · Active

## Summary

A read-only virtual shell engine and backend-first terminal interface for
exploring structured professional and project content.

## Details

- **Technology:** Go, Docker, JavaScript, HTML, and CSS
- **API:** `POST /api/exec`, `POST /api/complete`, and `GET /api/status`

## Features

- Tokenizer, lexer, parser, AST, and pipeline execution
- Session-isolated virtual filesystem, paths, history, and autocomplete
- Atlas search and Forge telemetry integrations with graceful degradation
- Rate limits, size limits, security headers, and deployment visibility

## Decisions

- Keep the frontend small and ship it with the Go service.
- Never execute host commands or expose the host filesystem.
