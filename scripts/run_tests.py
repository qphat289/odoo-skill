"""
Odoo test runner for a local Windows Odoo installation.

Usage:
    python run_tests.py
    python run_tests.py -u my_module
    python run_tests.py --test-tags my_module

Environment variables:
    ODOO_PYTHON  - Python executable bundled with Odoo
    ODOO_BIN     - Path to odoo-bin
    ODOO_CONF    - Path to odoo.conf
    ODOO_DB      - Database name
    ODOO_MODULE  - Default module name for the no-argument mode
    ODOO_ADDONS  - Additional addons path (optional)
"""

import os
import sys


DEFAULT_ODOO_PYTHON = r"C:\Program Files\Odoo 18.0\python\python.exe"
DEFAULT_ODOO_BIN = r"C:\Program Files\Odoo 18.0\server\odoo-bin"
DEFAULT_ODOO_CONF = r"C:\Program Files\Odoo 18.0\server\odoo.conf"
DEFAULT_ODOO_DB = None
DEFAULT_ODOO_MODULE = None
DEFAULT_ODOO_ADDONS = None


def get_value(var_name, default):
    return os.environ.get(var_name) or default


def validate_paths(paths):
    missing = [(key, value) for key, value in paths.items() if value and not os.path.exists(value)]
    if not missing:
        return

    print("ERROR: One or more configured paths do not exist.")
    print("Set the environment variables or edit the defaults in this script.")
    for key, value in missing:
        print(f"  {key}: {value}")
    sys.exit(1)


def require_value(name, value, help_text):
    if value:
        return value

    print(f"ERROR: {name} is required.")
    print(help_text)
    sys.exit(1)


def main():
    odoo_python = get_value("ODOO_PYTHON", DEFAULT_ODOO_PYTHON)
    odoo_bin = get_value("ODOO_BIN", DEFAULT_ODOO_BIN)
    odoo_conf = get_value("ODOO_CONF", DEFAULT_ODOO_CONF)
    odoo_db = get_value("ODOO_DB", DEFAULT_ODOO_DB)
    odoo_module = get_value("ODOO_MODULE", DEFAULT_ODOO_MODULE)
    odoo_addons = get_value("ODOO_ADDONS", DEFAULT_ODOO_ADDONS)

    validate_paths(
        {
            "ODOO_PYTHON": odoo_python,
            "ODOO_BIN": odoo_bin,
            "ODOO_CONF": odoo_conf,
            "ODOO_ADDONS": odoo_addons,
        }
    )

    require_value(
        "ODOO_DB",
        odoo_db,
        'Example: $env:ODOO_DB = "my_database"',
    )

    if len(sys.argv) == 1:
        require_value(
            "ODOO_MODULE",
            odoo_module,
            'Example: $env:ODOO_MODULE = "my_module"',
        )

    odoo_server_dir = os.path.dirname(os.path.abspath(odoo_bin))
    sys.path.insert(0, odoo_server_dir)

    import odoo
    import odoo.addons
    import odoo.cli

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

    if len(sys.argv) == 1:
        sys.argv = [
            sys.argv[0],
            "-c",
            odoo_conf,
            "-d",
            odoo_db,
            "-u",
            odoo_module,
            "--test-enable",
            "--stop-after-init",
        ]
    else:
        if "-c" not in sys.argv and "--config" not in sys.argv:
            sys.argv.extend(["-c", odoo_conf])
        if "-d" not in sys.argv and "--database" not in sys.argv:
            sys.argv.extend(["-d", odoo_db])
        if "--test-enable" not in sys.argv:
            sys.argv.append("--test-enable")
        if "--stop-after-init" not in sys.argv:
            sys.argv.append("--stop-after-init")

    print(f"Running: {' '.join(sys.argv)}")
    odoo.cli.main()


if __name__ == "__main__":
    main()
