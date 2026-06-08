---
name: odoo-test-execution
description: Use when running, executing, or debugging automated unit tests and integration tests for Odoo modules.
---

# Odoo Test Execution

## Overview
Executing and validating Odoo tests requires running the python server in a test-enabled mode against a targeted database. This skill covers launching tests, configuring logs, and debugging traceback exceptions.

## When to Use
Use this skill when:
- Running a test suite for a custom or inherited Odoo module.
- Verifying security groups, record rules, or constraints before committing changes.
- Diagnosing Odoo Server Error log messages containing `AssertionError`, `AccessError`, or `ValidationError`.
- Running TDD (Test-Driven Development) cycles on Odoo logic.

---

## Environment Detection

**Before running any command, discover local Odoo install paths.**

Detection methods (try in order):
1. Check `$env:ODOO_PYTHON` / `$env:ODOO_BIN` / `$env:ODOO_CONF` / `$env:ODOO_DB` environment variables
2. On Windows: `where odoo-bin` or check `C:\Program Files\Odoo *\server\odoo-bin`
3. On Linux: `which odoo-bin` or `find / -name "odoo-bin" 2>/dev/null`
4. Check Windows Registry: `HKLM:\Software\Odoo\InstallDir`
5. Read Odoo config file for `db_name` (usually `odoo.conf` or `~/.odoorc`)
6. Ask user for paths if not found

Set variables after detection:
```powershell
$odoo_python = "C:\Program Files\Odoo 18.0\python\python.exe"   # ← EDIT THIS
$odoo_bin    = "C:\Program Files\Odoo 18.0\server\odoo-bin"     # ← EDIT THIS
$odoo_conf   = "C:\Program Files\Odoo 18.0\server\odoo.conf"    # ← EDIT THIS
$db_name     = "your_database_name"                              # ← EDIT THIS
```

Or use env vars (so commands below work untampered):
```powershell
$env:ODOO_PYTHON = "C:\Program Files\Odoo 18.0\python\python.exe"
$env:ODOO_BIN    = "C:\Program Files\Odoo 18.0\server\odoo-bin"
$env:ODOO_CONF   = "C:\Program Files\Odoo 18.0\server\odoo.conf"
$env:ODOO_DB     = "your_database_name"
```

## Core Command Patterns

### 1. Run All Module Tests (Full Install and Run)
Use this command to install the module on a test database and run its entire test suite.
```powershell
$py = if ($env:ODOO_PYTHON) { $env:ODOO_PYTHON } else { $odoo_python }
$bin = if ($env:ODOO_BIN) { $env:ODOO_BIN } else { $odoo_bin }
$conf = if ($env:ODOO_CONF) { $env:ODOO_CONF } else { $odoo_conf }
$db = if ($env:ODOO_DB) { $env:ODOO_DB } else { $db_name }
& "$py" "$bin" -c "$conf" -d $db -i <module_name> --test-enable --stop-after-init
```

### 2. Run Specific Test Class or Tag
Use `--test-tags` to run a subset of tests, bypassing other tests for speed.
```powershell
& "$py" "$bin" -c "$conf" -d $db --test-tags <module_name>.<TestClass> --stop-after-init
```

### 3. Run Security-Only Tests
```powershell
& "$py" "$bin" -c "$conf" -d $db --test-tags security --stop-after-init
```

---

## Parsing Log Exceptions

| Log Exception | Meaning / Root Cause | Common Solution |
|---------------|----------------------|-----------------|
| `AssertionError` | Test assertion failed. Logic return value doesn't match expectation. | Check model method logic or test data setup values. |
| `AccessError` | Access rights or Record Rules prevent user from executing CRUD. | Review `security/ir.model.access.csv` or record rules. |
| `ValidationError` | Model constraint violated (e.g. `@api.constrains`). | Ensure test values comply with constraints, or adjust constraints logic. |
| `KeyError` | Missing field, model, or XML ID in environment context. | Verify model `_inherit` syntax or ensure XML data is loaded in manifest. |
| `ProgrammingError` | DB structure out-of-sync or SQL syntax error. | Restart Odoo server and update the module with `-u <module_name>`. |

---

## Common Mistakes

- **Mismatching Database**: Running tests on a production database instead of a test database. This can cause data corruption.
- **Forgetting Module Install (`-i`)**: Tests will not run if the module isn't explicitly flagged for install/update when the database doesn't have it.
- **Missing `@tagged` Decorators**: If tests are not tagged with `'post_install'`, Odoo may run them at install phase before demo data or views are properly compiled.
- **Relying on Outdated Rules**: In Odoo 19, company checks (`_check_company_auto`) are strictly enforced. Standard tests must create records that belong to the correct company context.
