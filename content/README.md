# Vaultsh

A read-only virtual shell for exploring backend work and project documentation.
Commands operate on mounted portfolio content, never on the host operating system.

## Vaults

- `cv/` — Professional profile, skills, and experience
- `projects/` — Project summaries and engineering decisions
- `docs/` — Architecture, APIs, commands, deployment, and roadmaps

## Start here

```sh
tree /cv
cat /cv/about.md
cat /cv/skills.md
cat /projects/vaultsh.md
dashboard
```

This is not a Linux shell. It is a Go backend with a virtual filesystem,
session state, command parsing, pipelines, search, and telemetry integrations.
