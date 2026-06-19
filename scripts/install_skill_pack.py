from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SKILL_NAMES = [
    "odoo-development",
    "odoo-14.0",
    "odoo-15.0",
    "odoo-16.0",
    "odoo-17.0",
    "odoo-18.0",
    "odoo-19.0",
]
SUPPORT_FOLDERS = [
    "agents",
    "workflows",
    "rules",
    "scripts",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Install the Odoo skill pack to any skill root.")
    parser.add_argument("destination_root", help="Destination directory that will contain skill folders.")
    parser.add_argument("--source-root", default=str(Path(__file__).resolve().parent.parent / "skills"))
    parser.add_argument(
        "--support-root",
        default=str(Path(__file__).resolve().parent.parent),
        help="Repository root that contains support folders such as agents/workflows/rules/scripts.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing destination folders.")
    args = parser.parse_args()

    source_root = Path(args.source_root).resolve()
    destination_root = Path(args.destination_root).resolve()
    support_root = Path(args.support_root).resolve()
    destination_root.mkdir(parents=True, exist_ok=True)

    for skill_name in SKILL_NAMES:
        source = source_root / skill_name
        if not source.exists():
            raise SystemExit(f"Missing source skill: {source}")
        destination = destination_root / skill_name
        if destination.exists():
            if not args.force:
                raise SystemExit(f"Destination exists: {destination}. Re-run with --force.")
            shutil.rmtree(destination)
        shutil.copytree(source, destination)
        print(f"Installed: {destination}")

    shared_root = destination_root.parent
    for folder_name in SUPPORT_FOLDERS:
        source = support_root / folder_name
        if not source.exists():
            raise SystemExit(f"Missing support folder: {source}")
        destination = shared_root / folder_name
        if destination.exists():
            if not args.force:
                raise SystemExit(f"Destination exists: {destination}. Re-run with --force.")
            shutil.rmtree(destination)
        shutil.copytree(source, destination)
        print(f"Installed support folder: {destination}")


if __name__ == "__main__":
    main()
