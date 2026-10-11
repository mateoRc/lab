# Content

The `lab` repository owns `content/`. Docker Compose mounts it read-only into Vaultsh and Atlas at `/app/content`.

## Layout

```text
/
├── README.md
├── projects/
│   ├── overview.md
│   ├── vaultsh.md
│   ├── atlas.md
│   ├── forge.md
│   └── sentinel.md
├── docs/
└── cv/
    ├── about.md
    ├── experience.md
    ├── skills.md
    └── contact.md
```

Use UTF-8 Markdown, one H1 title per document, short prose, and raw-text-friendly bullets. Do not include confidential employer or project details. Relative links resolve inside the virtual filesystem in Explorer.

Vaultsh and Atlas read the same raw files. `cat`, `grep`, `head`, `tail`, and `wc` operate on those files; Explorer renders previews, including existing Mermaid diagrams, without storing a second content copy.
