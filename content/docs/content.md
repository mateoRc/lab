# Content

The `lab` repository owns the files under `content/`. Docker Compose mounts
the directory read-only into Vault and Atlas at `/app/content`.

## Layout

```text
/
├── README.md
├── cv/
│   ├── README.md
│   ├── about.md
│   ├── skills.md
│   ├── interests.md
│   ├── contact.md
│   └── experience/
├── projects/
└── docs/
```

## Format

- Use UTF-8 Markdown with LF line endings.
- Use ATX headings (`#`) with a single H1 document title.
- Prefer short prose for summaries and bullets for responsibilities or features.
- Use bold labels in bullets for compact metadata.
- Wrap prose at approximately 80 characters.
- Keep content readable as raw Markdown in terminal commands.
- Do not add hidden rendered text or maintain a separate rendered representation.
- Do not include confidential or sensitive employer or project details.

Example:

```markdown
# Example

**Backend Engineer** · 2024–present

## Summary

Backend work on a distributed production system.

## Details

- **Focus:** Backend services and distributed systems
- **Technology:** Go and Docker

## Responsibilities

- Delivered features from design through deployment.
```

Vaultsh and Atlas read the same raw Markdown files directly; no rendering,
copy, or synchronization step is required. `cat`, `grep`, `head`, `tail`, and
`wc` operate on the original Markdown text.
