# Oracle

## Purpose

A Python/FastAPI question-answering service for Vaultsh.

## Implemented

- Authenticated `POST /invoke` (lore) and `POST /ask` (plain) returning short answers with grounded source paths.
- Retrieval over the shared Markdown content with a scoped, read-only system prompt.
- Caching, concurrency, provider, and daily-budget limits.
- `mock`, OpenRouter, and Groq providers behind one interface.

## Design decisions

Keep the provider key and SDK out of Vaultsh and ground every answer in the same content Atlas and Vaultsh read. Give answers a short Delphic voice in the prompt while keeping them plainly factual. Answers are short plain text, so the terminal needs no second rendering UI.

## Status and limits

Active project. One-shot `invoke` (lore) and `ask` (plain) answers are implemented; interactive chat and multi-model selection are planned. Answers are best-effort, bounded by a daily budget, and return `invoke unavailable` or `ask unavailable` when the provider is down.

Source: [Oracle](https://github.com/mateoRc/oracle) · [Architecture](architecture.md) · [Roadmap](roadmap.md)
