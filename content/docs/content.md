# Content

The `lab` repository owns `content/`. Docker Compose mounts it read-only into Vaultsh and Atlas at `/app/content`.

## Layout

```text
/
├── README.md
├── .motd
├── cv/
│   ├── about.md
│   ├── experience.md
│   ├── skills.md
│   └── contact.md
└── docs/
    ├── api.md
    ├── commands.md
    ├── content.md
    ├── deployment.md
    ├── events.md
    └── projects/
        ├── overview.md
        ├── atlas/
        │   ├── overview.md
        │   ├── roadmap.md
        │   └── architecture.md
        ├── forge/
        ├── oracle/
        ├── scribe/
        ├── sentinel/
        └── vaultsh/
```

Each project owns a folder under `docs/projects/` holding its `overview.md`,
`roadmap.md`, and `architecture.md`; `docs/projects/overview.md` is the
system-wide overview. Use UTF-8 Markdown, one H1 title per document, short
prose, and raw-text-friendly bullets. Relative links resolve inside the virtual
filesystem in Explorer.

Vaultsh and Atlas read the same raw files. `cat`, `grep`, `head`, `tail`, and `wc` operate on those files; Explorer renders previews, without storing a second content copy.
