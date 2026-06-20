---
name: odoo-security
description: Domain skill for Odoo ACL, record rules, groups, multi-company security, and security review across Odoo 14-19.
---

# Odoo Security

Use this skill when the task is about `ir.model.access.csv`, record rules, groups, field visibility, multi-company, or security review.

## Quick reference

| Topic | File | When to use |
|---|---|---|
| Shared overview | `references/odoo-security-guide.md` | Pick the right version file |
| Multi-company | `references/multi-company-patterns.md` | Company scoping and access behavior |
| Portal and external access | `references/portal-access-patterns.md` | Portal or limited external users |
| Version files | `references/odoo-security-guide-<version>.md` | Version-specific ACL and rule patterns |
| Upgrade deltas | `references/odoo-security-guide-<from>-<to>.md` | Security migration changes |

## Rules

1. Every model needs explicit access rights unless the model is intentionally internal-only.
2. Use version-specific security references before copying ACL or rule examples.
3. Pair this skill with `odoo-quality` for review and validation before handoff.
