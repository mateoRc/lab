# HTTP API

Vaultsh exposes JSON endpoints for command execution and autocomplete.

These browser-facing Vaultsh endpoints remain public. Atlas and Forge are
private backend services protected by bearer service tokens.

## Health

```http
GET /healthz
```

Successful response:

```text
ok
```

## Service Status

```http
GET /api/status
```

Response:

```json
{
  "atlas": true,
  "forge": true
}
```

The values report whether Vaultsh can currently reach each optional service.

## Execute a Command

```http
POST /api/exec
Content-Type: application/json
```

Request:

```json
{
  "line": "pwd",
  "session_id": ""
}
```

Response:

```json
{
  "output": "/",
  "exit_code": 0,
  "session_id": "<session-id>",
  "current_directory": "/"
}
```

The first request can omit `session_id`. The server generates one and returns
it. Send that value with later requests to preserve the working directory and
command history.

```sh
curl -X POST http://localhost:8080/api/exec \
  -H "Content-Type: application/json" \
  -d '{"line":"cd /cv/experience"}'
```

Continue the session:

```sh
curl -X POST http://localhost:8080/api/exec \
  -H "Content-Type: application/json" \
  -d '{"line":"pwd","session_id":"<session-id>"}'
```

Sessions expire after 30 minutes of inactivity.

Some commands return a frontend action:

```json
{
  "output": "",
  "exit_code": 0,
  "action": "clear",
  "session_id": "<session-id>",
  "current_directory": "/cv/experience"
}
```

Add `--verbose` as the final argument to return execution metadata without
changing command output:

```json
{
  "line": "cat /cv/skills.md | grep Languages --verbose"
}
```

```json
{
  "output": "- **Languages:** Python, Java, JavaScript, TypeScript, Go, and C#",
  "exit_code": 0,
  "verbose": "pipeline=cat,grep; stages=2; completed=2",
  "session_id": "<session-id>",
  "current_directory": "/"
}
```

The `verbose` field is omitted from normal responses. Commands do not receive
the global flag.

## Complete Input

```http
POST /api/complete
Content-Type: application/json
```

Request:

```json
{
  "line": "cat /cv/exp",
  "cursor": 11,
  "session_id": "<session-id>"
}
```

Response:

```json
{
  "start": 4,
  "end": 11,
  "replacement": "/cv/experience/",
  "candidates": [
    "/cv/experience/"
  ],
  "session_id": "<session-id>",
  "current_directory": "/"
}
```

`start` and `end` identify the input range the client should replace.
`replacement` is the longest common candidate prefix. Both endpoints return
`current_directory` so clients can render session state without duplicating
path resolution.

## Errors

- Invalid JSON returns HTTP `400`.
- Session creation failure returns HTTP `500`.
- Shell command failures are returned as HTTP `200` with a non-zero
  `exit_code`.
