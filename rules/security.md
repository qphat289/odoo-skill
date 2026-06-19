# Odoo Security Rules

Use these rules across generation, review, and upgrade tasks. This file is not a replacement for version-specific security references; it is the cross-version security baseline.

## Access control

- Every persistent model must have explicit entries in `security/ir.model.access.csv`.
- Define record rules only when row-level filtering is required; avoid unnecessary global rules.
- Prefer least privilege. Add manager/admin overrides explicitly instead of broad user access.
- Review implied groups carefully; do not grant elevated groups transitively without intent.

## ORM and business logic

- Never trust UI-only restrictions for security. Enforce critical checks in Python.
- Validate privileged state transitions server-side.
- Use sudo narrowly and document why it is required.
- Avoid mixing unrestricted `sudo()` reads with user-visible results unless data exposure is intended.

## Multi-company

- Ensure company-scoped models and relational fields follow the target-version company rules.
- Review record rules for company leakage, especially when domains use user/company context.
- Test cross-company reads on list, form, many2one search, and computed fields.

## Controllers and external APIs

- Set auth level deliberately on every route.
- Validate input payloads and avoid exposing unrestricted search/read endpoints.
- Never leak internal exceptions, tokens, or stack traces in controller responses.

## Data files

- Load security files before views and menus in `__manifest__.py`.
- Keep `noupdate` intentional; do not freeze records that must remain upgradeable.

## Review checklist

- Missing ACLs
- Over-broad record rules
- Unsafe `sudo()`
- State changes without permission checks
- Controller auth/input issues
- Multi-company leakage
