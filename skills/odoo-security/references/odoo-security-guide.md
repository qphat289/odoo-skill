# Odoo Security Guide - Version Dispatcher

Use this file as the routing entrypoint for version-specific Odoo security guidance.

## Mandatory version matching

Use the security guide that matches the target Odoo version. Mixing security patterns across versions can introduce broken behavior, weak access control, or deprecated code.

Before implementing security:
1. Identify the target Odoo version.
2. Decide whether the task is new development, upgrade work, or concept review.
3. Load the matching version-specific file.

## Version-specific files

| Target Version | File to Use | Status |
|----------------|-------------|--------|
| Odoo 14.0 | `odoo-security-guide-14.md` | Legacy |
| Odoo 15.0 | `odoo-security-guide-15.md` | Legacy |
| Odoo 16.0 | `odoo-security-guide-16.md` | Supported |
| Odoo 17.0 | `odoo-security-guide-17.md` | Supported |
| Odoo 18.0 | `odoo-security-guide-18.md` | Current |
| Odoo 19.0 | `odoo-security-guide-19.md` | Current |
| All versions | `odoo-security-guide-all.md` | Shared concepts |

## Migration guides

| Migration Path | File |
|----------------|------|
| 14.0 -> 15.0 | `odoo-security-guide-14-15.md` |
| 15.0 -> 16.0 | `odoo-security-guide-15-16.md` |
| 16.0 -> 17.0 | `odoo-security-guide-16-17.md` |
| 17.0 -> 18.0 | `odoo-security-guide-17-18.md` |
| 18.0 -> 19.0 | `odoo-security-guide-18-19.md` |

## How to use

### New development

Load the single-version guide, for example:

```text
Read: skills/odoo-security/references/odoo-security-guide-18.md
```

### Upgrade work

Load the migration guide, for example:

```text
Read: skills/odoo-security/references/odoo-security-guide-17-18.md
```

### Concept review

Load:

```text
Read: skills/odoo-security/references/odoo-security-guide-all.md
```

## Version detection hints

If the version is unclear, look for these clues:

| Indicator | Version |
|-----------|---------|
| `@api.multi` decorator | 14.0 |
| `track_visibility` parameter | 14.0-15.0 |
| `tracking` parameter | 15.0+ |
| `Command` class usage | 16.0+ |
| `attrs` in views | 14.0-16.0 |
| Direct `invisible` / `readonly` | 17.0+ |
| `_check_company_auto` | 18.0+ |
| Type hints on fields | 18.0+ |
| `SQL()` builder | 18.0+ |

## Security deltas by version

| Version band | Security-sensitive delta |
|---|---|
| `14-15` | Legacy patterns still appear in the wild; company checks are usually manual, and view visibility can still use `attrs`. |
| `16` | Transitional release: keep security logic modernized, but many codebases still carry older view/company patterns. |
| `17+` | View-layer assumptions change because `attrs` disappears; do not confuse UI visibility with real security. |
| `18+` | Prefer `_check_company_auto = True` and `check_company=True` for company-aware models; keep record-rule variables and context keys distinct. |
| `19` | Recheck newer typing/SQL/security conventions against current upstream references before broad rollout. |

## Related sources

- `rules/security.md`
- `rules/coding-style.md`
- `odoo-version-routing.md`
- `odoo-manifest-data-order.md`

Do not implement security directly from this dispatcher. Always load the matching version-specific guide first.

