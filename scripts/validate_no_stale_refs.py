from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SELF_PATH = Path(__file__).resolve()

TEXT_SUFFIXES = {
    ".md",
    ".json",
    ".yaml",
    ".yml",
    ".py",
    ".ps1",
    ".html",
}

BANNED_PATTERNS = [
    "docs/correct-log/CORRECTIONS_LOG.md",
    "docs\\correct-log\\CORRECTIONS_LOG.md",
    "workflows/implementation-planning.md",
    "workflows\\implementation-planning.md",
    "business-to-implementation",
    "business-to-imple",
    "agents/odoo-planner.md",
    "agents\\odoo-planner.md",
]

EXCLUDED_PARTS = {
    ".git",
    "__pycache__",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.resolve() == SELF_PATH:
            continue
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        files.append(path)
    return files


def main() -> None:
    hits: list[str] = []
    for path in iter_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in BANNED_PATTERNS:
            if pattern in text:
                hits.append(f"{path.relative_to(REPO_ROOT)} -> {pattern}")

    if hits:
        fail("Stale references found:\n" + "\n".join(hits))

    print("No stale references OK")


if __name__ == "__main__":
    main()
