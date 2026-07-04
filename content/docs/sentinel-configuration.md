# Sentinel Configuration

Backend Lab owns Sentinel policy in [`../../sentinel.yml`](../../sentinel.yml).
The initial schema is `sentinel.dev/v1alpha1` and remains inactive until CI
integration is implemented.

## Rules

- Unknown or missing required fields fail validation.
- Agent capabilities default to disabled.
- Repository writes and deployment are disabled.
- Secrets are referenced through CI environment variables, never YAML.
- Deterministic failures cannot be overridden by agent analysis.

## Sections

| Section | Purpose |
| --- | --- |
| `project` | Project identity and default branch |
| `repositories` | Repositories included in release analysis |
| `checks` | Deterministic check groups to execute |
| `policy` | Conditions that block or require approval |
| `agent` | Advisory analysis capabilities |
| `report` | Human- and machine-readable output |

The schema will expand only when the corresponding deterministic behavior is
implemented and tested.
