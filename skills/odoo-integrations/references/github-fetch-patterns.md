# GitHub Fetch Patterns for Agents

Use this file to verify Odoo behavior against official upstream code before making strong repo claims.

## Raw URL format

```text
https://raw.githubusercontent.com/odoo/odoo/{branch}/{path}
```

## Branch mapping

| Version | Branch |
|---------|--------|
| 14.0 | `14.0` |
| 15.0 | `15.0` |
| 16.0 | `16.0` |
| 17.0 | `17.0` |
| 18.0 | `18.0` |
| 19.0 | `19.0` |

## High-value verification targets

| Topic | Path | Why fetch it |
|------|------|---------------|
| ORM model behavior | `odoo/models.py` | CRUD and registry behavior |
| Fields and `Command` | `odoo/fields.py` | x2many patterns |
| API decorators | `odoo/api.py` | create, depends, constrains |
| SQL builder | `odoo/tools/sql.py` | `SQL()` usage |
| 19.0 constraints | `odoo/orm/model_classes.py` | `_sql_constraints` status |
| frontend package | `addons/web/tooling/_package.json` | current frontend dependency version |
| frontend examples | `addons/web/static/src/` | hooks, services, registries |

## Example fetch prompts

```text
URL: https://raw.githubusercontent.com/odoo/odoo/19.0/odoo/orm/model_classes.py
Prompt: "Show how Odoo 19 handles _sql_constraints and models.Constraint."

URL: https://raw.githubusercontent.com/odoo/odoo/19.0/addons/web/tooling/_package.json
Prompt: "Show the current frontend package versions used by Odoo 19."

URL: https://raw.githubusercontent.com/odoo/odoo/19.0/odoo/tools/sql.py
Prompt: "Show the SQL helper API and typical usage patterns."
```

## Verification workflow

1. Identify the exact version branch.
2. Fetch the smallest upstream file that can prove or disprove the claim.
3. Prefer source files over secondary commentary.
4. Mark the result as one of:
   - verified
   - preferred pattern
   - verify target build

## 19.0 audit stance

Use GitHub fetches to avoid overclaiming on:
- mandatory type hints
- mandatory `SQL()` usage everywhere
- frontend major-version labels
- universal `res.users` provisioning rules
