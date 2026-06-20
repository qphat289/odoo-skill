---
name: odoo-upgrade
description: Analyze and guide Odoo module upgrades across versions.
arguments:
  - name: path
    description: Module path
    required: true
  - name: source
    description: Source Odoo version
    required: false
  - name: target
    description: Target Odoo version
    required: false
---

# /odoo-upgrade Command

Analyze upgrade work with version-hop references.

## Flow

1. Detect or confirm source and target versions.
2. Read the matching hop references:
   - `odoo-version-knowledge-{source}-{target}.md`
   - `odoo-module-generator-{source}-{target}.md`
   - `odoo-model-patterns-{source}-{target}.md`
   - `odoo-security-guide-{source}-{target}.md`
3. Review the module for version-sensitive patterns.
4. Report required fixes, preferred cleanups, and items that still need upstream verification.

## High-risk hops

### 17 -> 18
- add `_check_company_auto`
- add `check_company=True`
- review record-rule and context company handling
- prefer `SQL()` and useful type hints

### 18 -> 19
- migrate `_sql_constraints` toward `models.Constraint(...)`
- add type hints where they improve maintained code
- prefer migrating raw SQL helpers to `SQL()`
- verify frontend and runtime assumptions against the current upstream branch

## Example usage

```text
/odoo-upgrade ./my_module
/odoo-upgrade ./my_module 17.0 18.0
/odoo-upgrade ./my_module 18.0 19.0
```
