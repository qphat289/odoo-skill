# Odoo Version Routing

Use this file as the compact, central version quick-reference for agents and workflows.

## Skill routing

| Target version | Preferred skill |
|----------------|-----------------|
| 14.0 | `skills/odoo-14.0/SKILL.md` |
| 15.0 | `skills/odoo-15.0/SKILL.md` |
| 16.0 | `skills/odoo-16.0/SKILL.md` |
| 17.0 | `skills/odoo-17.0/SKILL.md` |
| 18.0 | `skills/odoo-18.0/SKILL.md` |
| 19.0 | `skills/odoo-19.0/SKILL.md` |

## Quick syntax matrix

| Feature | 14.0 | 15.0 | 16.0 | 17.0 | 18.0 | 19.0 |
|---------|------|------|------|------|------|------|
| `@api.multi` | Deprecated | Removed | Removed | Removed | Removed | Removed |
| `track_visibility` | Legacy | Replace with `tracking` | Removed from new code | Removed from new code | Removed from new code | Removed from new code |
| x2many `Command` | Optional | Optional | Preferred | Preferred | Preferred | Preferred |
| `attrs` in views | Allowed | Allowed | Deprecated | Removed | Removed | Removed |
| Direct `invisible="expr"` | No | No | Transitional | Required | Required | Required |
| `_check_company_auto` | No | No | No | No | Preferred for company-aware models | Preferred |
| SQL builder | No | No | No | No | Preferred | Strongly preferred / required by policy |
| Type hints on business methods | Optional | Optional | Optional | Optional | Recommended | Strongly expected |

## Use rules

- Use this file only as a router and quick matrix.
- Pull the final implementation detail from:
  - `odoo-version-knowledge-{version}.md`
  - the matching version skill
  - `rules/security.md`
  - `rules/coding-style.md`
