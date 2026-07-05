import argparse
import json
import os
import re
from pathlib import Path

SERVICES = ("vault", "atlas", "forge")
_SHA = re.compile(r"^[0-9a-f]{40}$")


def prepare(
    runtime: Path,
    latest: dict[str, str],
    target: str,
    requested_version: str = "",
) -> dict[str, str]:
    _validate_versions(latest)
    if target not in {*SERVICES, "all"}:
        raise ValueError(f"unsupported deployment target: {target}")
    if target == "all" and requested_version:
        raise ValueError("a requested version requires a targeted service")
    current = load_release(runtime / "release.json", required=False)
    release = dict(current or latest)
    if target == "all":
        release = dict(latest)
    else:
        release[target] = requested_version or latest[target]
    _validate_versions(release)
    if current:
        _atomic_json(runtime / "previous-release.json", current)
    _publish(runtime, release)
    return release


def rollback(runtime: Path) -> dict[str, str]:
    current = load_release(runtime / "release.json")
    previous = load_release(runtime / "previous-release.json")
    _atomic_json(runtime / "previous-release.json", current)
    _publish(runtime, previous)
    return previous


def load_release(path: Path, required: bool = True) -> dict[str, str]:
    if not path.is_file():
        if required:
            raise ValueError(f"release manifest does not exist: {path}")
        return {}
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("release manifest must be an object")
    release = {str(name): str(version) for name, version in value.items()}
    _validate_versions(release)
    return release


def _publish(runtime: Path, release: dict[str, str]) -> None:
    runtime.mkdir(parents=True, exist_ok=True)
    _atomic_json(runtime / "release.json", release)
    lines = [
        f"{service.upper()}_IMAGE=ghcr.io/mateorc/"
        f"{'vaultsh' if service == 'vault' else service}:{release[service]}"
        for service in SERVICES
    ]
    _atomic_text(runtime / "versions.env", "\n".join(lines) + "\n")


def _validate_versions(release: dict[str, str]) -> None:
    if set(release) != set(SERVICES):
        raise ValueError("release manifest must contain vault, atlas, and forge")
    for service, version in release.items():
        if not _SHA.fullmatch(version):
            raise ValueError(f"{service} version must be a full Git SHA")


def _atomic_json(path: Path, value: dict[str, str]) -> None:
    _atomic_text(path, json.dumps(value, sort_keys=True) + "\n")


def _atomic_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(value, encoding="utf-8")
    os.replace(temporary, path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("prepare", "rollback"))
    parser.add_argument("--runtime", type=Path, required=True)
    parser.add_argument("--target", choices=(*SERVICES, "all"), default="all")
    parser.add_argument("--vault")
    parser.add_argument("--atlas")
    parser.add_argument("--forge")
    parser.add_argument("--version", default="")
    arguments = parser.parse_args()
    if arguments.action == "rollback":
        release = rollback(arguments.runtime)
    else:
        latest = {
            "vault": arguments.vault or "",
            "atlas": arguments.atlas or "",
            "forge": arguments.forge or "",
        }
        release = prepare(
            arguments.runtime,
            latest,
            arguments.target,
            arguments.version,
        )
    print(json.dumps(release, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
