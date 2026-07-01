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
- Write one lowercase `key: value` pair per line.
- Repeat keys when a field has multiple values.
- Use blank lines to separate sections.
- Do not use Markdown.
- Do not include confidential or sensitive employer or project details.

Example:

```text
company: Example
role: Backend Engineer

focus: backend services
focus: distributed systems

technology: Go
technology: Docker
```

Vault and Atlas read the same files directly; no copy or synchronization step
is required.
