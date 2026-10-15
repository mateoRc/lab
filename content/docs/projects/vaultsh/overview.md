# Vaultsh

## Purpose

A Go virtual shell and browser Explorer for reading project documentation and exercising backend services.

## Implemented

- Tokenizer, parser, pipelines, composable commands, session-isolated paths, history, and completion.
- Read-only virtual filesystem, document browsing, Markdown previews, and Mermaid diagrams.
- Optional Atlas search and Forge telemetry and dashboard integrations.

## Design decisions

Commands run inside the Go process against mounted content. No host shell or host filesystem is exposed. Explorer reads the same filesystem through a read-only API; sessions are bounded, local, and expiring.

## Status and limits

Active project. Search and live analytics depend on Atlas and Forge availability. Session state is lost on restart; Markdown preview supports a deliberate subset of Markdown.

Source: [Vaultsh](https://github.com/mateoRc/vaultsh) · [Architecture](architecture.md) · [Roadmap](roadmap.md)
