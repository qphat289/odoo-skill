---
name: odoo-test-execution
description: Use when running, executing, or debugging automated unit tests and integration tests for Odoo modules.
---

# Odoo Test Execution

## Overview

Execute Odoo tests against a targeted database with a known Odoo installation and explicit environment settings.

## Environment Detection

Before running test commands, detect the local Odoo environment in this order:

1. Check `ODOO_PYTHON`, `ODOO_BIN`, `ODOO_CONF`, `ODOO_DB`, and `ODOO_MODULE`
2. On Windows, check the default Odoo install path under `C:\Program Files\Odoo *`
3. On Linux, check `which odoo-bin`
4. Read the Odoo config file for the database name if available
5. Ask the user if the paths or database name are still unclear

PowerShell example:

```powershell
$odoo_python = "C:\Program Files\Odoo 18.0\python\python.exe"
$odoo_bin    = "C:\Program Files\Odoo 18.0\server\odoo-bin"
$odoo_conf   = "C:\Program Files\Odoo 18.0\server\odoo.conf"
$db_name     = "my_database"
$module_name = "my_module"
```

Environment variable example:

```powershell
$env:ODOO_PYTHON = "C:\Program Files\Odoo 18.0\python\python.exe"
$env:ODOO_BIN    = "C:\Program Files\Odoo 18.0\server\odoo-bin"
$env:ODOO_CONF   = "C:\Program Files\Odoo 18.0\server\odoo.conf"
$env:ODOO_DB     = "my_database"
$env:ODOO_MODULE = "my_module"
```

## Core Command Patterns

### Run the module test suite

```powershell
$py = if ($env:ODOO_PYTHON) { $env:ODOO_PYTHON } else { $odoo_python }
$bin = if ($env:ODOO_BIN) { $env:ODOO_BIN } else { $odoo_bin }
$conf = if ($env:ODOO_CONF) { $env:ODOO_CONF } else { $odoo_conf }
$db = if ($env:ODOO_DB) { $env:ODOO_DB } else { $db_name }
$module = if ($env:ODOO_MODULE) { $env:ODOO_MODULE } else { $module_name }
& "$py" "$bin" -c "$conf" -d $db -i $module --test-enable --stop-after-init
```

### Run a specific test class or tag

```powershell
& "$py" "$bin" -c "$conf" -d $db --test-tags "$module.TestClass" --stop-after-init
```

### Run security-focused tests

```powershell
& "$py" "$bin" -c "$conf" -d $db --test-tags security --stop-after-init
```

## Error Reading

| Log Exception | Meaning | Common Action |
|---------------|---------|---------------|
| `AssertionError` | Business logic or expected values do not match. | Re-check method behavior and test setup. |
| `AccessError` | Security rules block the operation. | Review access rights and record rules. |
| `ValidationError` | Constraints reject the data. | Fix the test data or the constraint logic. |
| `KeyError` | A model, field, or XML ID is missing. | Verify inheritance and manifest data loading. |
| `ProgrammingError` | Database structure or SQL is out of sync. | Restart Odoo and update the module with `-u my_module`. |

## Common Mistakes

- Running tests against a production database
- Forgetting to install or update the module before executing tests
- Using the wrong module name for `--test-tags`
- Debugging test failures without checking the Odoo version first
