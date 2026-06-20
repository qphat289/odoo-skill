# Agent Quick Start Guide

Use this file as a fast operational checklist for Odoo work.

## One rule first

Identify the target Odoo version before generating, reviewing, or upgrading code.

## 3-step process

### Step 1: Get the version

- Ask the user if the version is not explicit
- Or infer it from `__manifest__.py`, existing ORM/view patterns, and dependency layout

### Step 2: Load the right references

Always load:
- `odoo-module-generator-{version}.md`
- `odoo-model-patterns-{version}.md`
- `odoo-security-guide-{version}.md`

Load additionally when relevant:
- `odoo-owl-components-{version}.md`
- version-hop migration guides such as `odoo-version-knowledge-18-19.md`

### Step 3: Generate or review code

- Use only patterns that match the target version
- Do not mix version-specific guidance
- Verify uncertain syntax against official Odoo docs or source

## Quick matrix

| Version | Main cues |
|---------|-----------|
| 14 | `@api.multi`, `track_visibility`, `attrs` |
| 15 | no `@api.multi`, `tracking=True`, OWL 1.x |
| 16 | `Command`, assets in manifest, OWL 2.x style |
| 17 | no `attrs`, `@api.model_create_multi`, direct XML expressions |
| 18 | `_check_company_auto`, `check_company=True`, `SQL()` preferred |
| 19 | `models.Constraint(...)` preferred, type hints/SQL/frontend claims must be verified conservatively |

## Manifest order reminder

```python
"data": [
    "security/module_security.xml",
    "security/ir.model.access.csv",
    "data/data.xml",
    "views/model_views.xml",
    "views/menuitems.xml",
]
```

## Operating stance for 19.0

- prefer type hints on new or touched code
- prefer `SQL()` in new or risky raw SQL
- prefer `models.Constraint(...)` over `_sql_constraints`
- verify frontend and runtime assumptions against the current upstream branch
