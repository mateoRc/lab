# Content

The `lab` repository owns the files under `content/`. Docker Compose mounts
the directory read-only into Vault and Atlas at `/app/content`.

## Layout

```text
/
├── README.txt
├── cv/
│   ├── README.txt
│   ├── about.txt
│   ├── skills.txt
│   ├── interests.txt
│   ├── contact.txt
│   └── experience/
├── projects/
└── docs/
```

## Format

- Use UTF-8 plain text with LF line endings.
- Use uppercase document and section headings with `=` and `-` separators.
- Prefer short prose for summaries and bullets for responsibilities or features.
- Use one aligned category line for values that should be searchable together.
- Wrap long category values on an indented continuation line.
- Do not use Markdown.
- Do not include confidential or sensitive employer or project details.

Example:

```text
EXAMPLE
========

Backend Engineer | 2024-present

SUMMARY
-------
Backend work on a distributed production system.

DETAILS
-------
Focus       Backend services | Distributed systems
Technology  Go | Docker

RESPONSIBILITIES
----------------
- Delivered features from design through deployment.
```

Vault and Atlas read the same files directly; no copy or synchronization step
is required.
