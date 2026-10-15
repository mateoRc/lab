# Oracle Roadmap

This file tracks delivery status. Current behavior belongs in
[Oracle architecture](architecture.md) and the
[command reference](../../commands.md).

**Status:** One-shot `invoke` answers are implemented. The service is read-only
and stateless apart from an in-memory answer cache.

## Completed

- [x] Authenticated `POST /ask` returning answers with grounded source paths
- [x] Retrieval over the shared content with a scoped system prompt
- [x] Caching, concurrency, provider, and daily-budget limits
- [x] `mock`, OpenRouter, and Groq providers behind one interface
- [x] Two query modes: `invoke` (lore) and `ask` (plain)
- [x] Rotate across OpenRouter's free models when one is rate limited
- [x] Vaultsh `invoke` command with graceful degradation
- [x] Immutable images, health checks, and Compose wiring

## Models

- [ ] Allow choosing a model per request or per session from an allowlist, for
  example a Vaultsh `model` command or a `/model` slash command.
- [ ] Report the active model in the reply and in `GET /status`.
- [ ] Track questions and cost per model within the shared daily budget.
- [ ] Fall back across providers (for example Groq, then OpenRouter) when a
  provider is exhausted or a free model is retired.

## Conversation

- [ ] Add an interactive `chat` mode with bounded session history.
- [ ] Stream answers so the terminal renders tokens as they arrive.
- [ ] Keep multi-turn context small and re-ground every turn in the content.

## Operations

- [ ] Emit request and latency telemetry to Forge.
- [ ] Record which source documents grounded each answer.
- [ ] Evaluate a local model path for fully offline answers.
