# Odoo OWL Components - Version Dispatcher

Use this file to route frontend work to the right version-specific reference.

## Version matching

Frontend patterns vary sharply across Odoo versions. Always identify the target version first, then load the matching frontend file.

## Version-specific files

| Target Version | Frontend baseline | File to Use |
|----------------|-------------------|-------------|
| Odoo 14.0 | Legacy JS | `odoo-owl-components-14.md` |
| Odoo 15.0 | OWL 1.x | `odoo-owl-components-15.md` |
| Odoo 16.0 | OWL 2.x style | `odoo-owl-components-16.md` |
| Odoo 17.0 | OWL 2.x style | `odoo-owl-components-17.md` |
| Odoo 18.0 | OWL 2.x style | `odoo-owl-components-18.md` |
| Odoo 19.0 | Verify current `@odoo/owl` patterns in upstream source | `odoo-owl-components-19.md` |
| All versions | Shared concepts | `odoo-owl-components-all.md` |

## Migration guides

| Migration Path | File |
|----------------|------|
| 14.0 -> 15.0 | `odoo-owl-components-14-15.md` |
| 15.0 -> 16.0 | `odoo-owl-components-15-16.md` |
| 16.0 -> 17.0 | `odoo-owl-components-16-17.md` |
| 17.0 -> 18.0 | `odoo-owl-components-17-18.md` |
| 18.0 -> 19.0 | `odoo-owl-components-18-19.md` |

## Quick reference

### Odoo 14
- Legacy `odoo.define(...)`
- Widget-based frontend

### Odoo 15
- OWL 1.x patterns
- `odoo.define(...)` still present

### Odoo 16-18
- `/** @odoo-module **/`
- ES modules
- `@web` services and registries

### Odoo 19
- Keep `/** @odoo-module **/`
- Verify current `@web` imports, hooks, and props style against the `19.0` branch
- Do not hardcode a repo-wide OWL major-version claim without upstream proof

## Detection hints

| Indicator | Version hint |
|-----------|--------------|
| `odoo.define()` | 14 or 15 |
| `require('web.Widget')` | 14 |
| `const { Component } = owl` | 15 |
| `/** @odoo-module **/` | 16+ |
| `import { Component } from "@odoo/owl"` | 16+ |

## Shared frontend anchors

- `registry.category(...)`
- `useService(...)`
- `useState(...)`
- action, field, and main component registries

Always verify uncertain 19.0 frontend assumptions against the current upstream web source.
