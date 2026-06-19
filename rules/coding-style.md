# Odoo Coding Style Rules

Use these rules across generation, review, and upgrade tasks. This file complements version-specific references and keeps style decisions consistent.

## Module structure

- Keep manifest data ordered by dependency; use `skills/odoo-development/references/odoo-manifest-data-order.md` as the central ordering reference.
- Keep models, wizards, controllers, and reports in their standard folders.
- Use one clear responsibility per file where practical.

## Model code

- Prefer explicit field names and business-oriented method names.
- Keep compute, inverse, onchange, and constraint methods small and focused.
- Use `mapped`, `filtered`, and batched recordset operations instead of row-by-row anti-patterns when suitable.
- Avoid hidden side effects in compute methods.

## XML and views

- Group fields by business meaning, not by declaration order.
- Keep xpath changes minimal and targeted.
- Use version-correct list/tree and visibility syntax.

## Tests

- Add at least one behavioral test for non-trivial business logic.
- Test permissions and record rules when security is part of the feature.
- Prefer targeted tests over broad smoke tests when time is limited.

## Review checklist

- Manifest ordering
- Naming clarity
- Method size/cohesion
- Version-correct XML syntax
- Missing tests for business/security logic
