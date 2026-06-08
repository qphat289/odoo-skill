"""
Odoo test runner — discovers paths dynamically, no hardcoded values.

Usage:
    python run_tests.py                          # uses defaults / env vars
    python run_tests.py -d mydb -u my_module    # custom args

Environment variables (recommended — set once, avoid editing this file):
    ODOO_PYTHON  - Python executable bundled with Odoo
    ODOO_BIN     - Path to odoo-bin
    ODOO_CONF    - Path to odoo.conf
    ODOO_DB      - Database name
    ODOO_ADDONS  - Additional addons path (optional, for dev repos)
"""
import sys
import os


# === Edit these defaults to match your local Odoo install ===
# Or better: set env vars ODOO_PYTHON, ODOO_BIN, ODOO_CONF, ODOO_DB
DEFAULT_ODOO_PYTHON = r"C:\Program Files\Odoo 18.0\python\python.exe"
DEFAULT_ODOO_BIN = r"C:\Program Files\Odoo 18.0\server\odoo-bin"
DEFAULT_ODOO_CONF = r"C:\Program Files\Odoo 18.0\server\odoo.conf"
DEFAULT_ODOO_DB = "your_database_name"
DEFAULT_ODOO_ADDONS = None   # e.g. r"C:\Users\you\my-addons"


def get_path(var_name, default):
    return os.environ.get(var_name) or default


def validate_paths(paths):
    missing = [(k, v) for k, v in paths.items() if v and not os.path.exists(v)]
    if missing:
        print("ERROR: Paths not found. Set env vars or edit defaults in this script:")
        for k, v in missing:
            print(f"  {k}: {v}")
        print()
        print("PowerShell (run once per terminal):")
        print(f'  $env:ODOO_PYTHON = r"{DEFAULT_ODOO_PYTHON}"')
        print(f'  $env:ODOO_BIN    = r"{DEFAULT_ODOO_BIN}"')
        print(f'  $env:ODOO_CONF   = r"{DEFAULT_ODOO_CONF}"')
        print(f'  $env:ODOO_DB     = "your_database"')
        sys.exit(1)


def main():
    odoo_python = get_path("ODOO_PYTHON", DEFAULT_ODOO_PYTHON)
    odoo_bin = get_path("ODOO_BIN", DEFAULT_ODOO_BIN)
    odoo_conf = get_path("ODOO_CONF", DEFAULT_ODOO_CONF)
    odoo_db = get_path("ODOO_DB", DEFAULT_ODOO_DB)
    odoo_addons = get_path("ODOO_ADDONS", DEFAULT_ODOO_ADDONS)

    validate_paths({
        "ODOO_PYTHON": odoo_python,
        "ODOO_BIN": odoo_bin,
        "ODOO_CONF": odoo_conf,
        "ODOO_ADDONS": odoo_addons,
    })

    # Add Odoo server dir to Python path
    odoo_server_dir = os.path.dirname(os.path.abspath(odoo_bin))
    sys.path.insert(0, odoo_server_dir)

    import odoo
    import odoo.addons
    import odoo.cli

    # Inject additional addons path if provided
    if odoo_addons:
        class AddonsPath(list):
            _path_finder = None
        odoo.addons.__path__ = AddonsPath(
            [os.path.abspath(odoo_addons)] + list(odoo.addons.__path__)
        )

    print(f"Odoo server:  {odoo_bin}")
    print(f"Config:       {odoo_conf}")
    print(f"Database:     {odoo_db}")
    print(f"Addons path:  {odoo.addons.__path__}")

    # Build args — if none provided, default to test mode
    if len(sys.argv) == 1:
        sys.argv = [
            sys.argv[0],
            "-c", odoo_conf,
            "-d", odoo_db,
            "-u", "module_name",  # ← change this to your module
            "--test-enable",
            "--stop-after-init",
        ]
    else:
        if "-c" not in sys.argv and "--config" not in sys.argv:
            sys.argv.extend(["-c", odoo_conf])
        if "--test-enable" not in sys.argv:
            sys.argv.append("--test-enable")
        if "--stop-after-init" not in sys.argv:
            sys.argv.append("--stop-after-init")

    print(f"Running: {' '.join(sys.argv)}")
    odoo.cli.main()


if __name__ == "__main__":
    main()
