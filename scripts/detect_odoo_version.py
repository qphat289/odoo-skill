from __future__ import annotations

import ast
import json
import re
from collections import Counter
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    tomllib = None


ROOT = Path.cwd()
MANIFEST_NAMES = {"__manifest__.py", "__openerp__.py"}
VERSION_RE = re.compile(r"(\d+)\.0")


def read_json(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def parse_manifest(path: Path) -> str | None:
    try:
        data = ast.literal_eval(path.read_text(encoding="utf-8"))
    except Exception:
        return None
    if not isinstance(data, dict):
        return None
    version = data.get("version")
    if not isinstance(version, str):
        return None
    match = VERSION_RE.search(version)
    return f"{match.group(1)}.0" if match else None


def detect_from_manifests(root: Path) -> str | None:
    versions: list[str] = []
    for path in root.rglob("__manifest__.py"):
        if any(part.startswith(".") for part in path.parts):
            continue
        version = parse_manifest(path)
        if version:
            versions.append(version)
    if not versions:
        return None
    return Counter(versions).most_common(1)[0][0]


def main() -> None:
    odoo_version_file = ROOT / ".odoo-version"
    if odoo_version_file.exists():
        print(odoo_version_file.read_text(encoding="utf-8").strip())
        return

    claude_odoo = ROOT / ".claude" / "odoo.json"
    if claude_odoo.exists():
        data = read_json(claude_odoo)
        version = data.get("odoo_version") if isinstance(data, dict) else None
        if isinstance(version, str) and version:
            print(version)
            return

    package_json = ROOT / "package.json"
    if package_json.exists():
        data = read_json(package_json)
        odoo = data.get("odoo") if isinstance(data, dict) else None
        version = odoo.get("version") if isinstance(odoo, dict) else None
        if isinstance(version, str) and version:
            print(version)
            return

    pyproject = ROOT / "pyproject.toml"
    if pyproject.exists() and tomllib is not None:
        try:
            data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
        except Exception:
            data = {}
        tool = data.get("tool", {})
        odoo = tool.get("odoo", {}) if isinstance(tool, dict) else {}
        version = odoo.get("version") if isinstance(odoo, dict) else None
        if isinstance(version, str) and version:
            print(version)
            return

    detected = detect_from_manifests(ROOT)
    if detected:
        print(detected)
        return

    print("UNKNOWN")


if __name__ == "__main__":
    main()
