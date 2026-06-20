# Odoo OWL Components - Core Concepts

This file covers frontend concepts shared across versions.
Use the version-specific frontend files for implementation details.

## Version map

- Odoo 15: OWL 1.x
- Odoo 16-18: OWL 2-style patterns
- Odoo 19: verify current upstream `@odoo/owl` and `@web` patterns instead of assuming a major-version label

## Shared component concepts

1. Components combine template, logic, and state.
2. Templates stay in QWeb XML.
3. State changes drive re-rendering.
4. Props pass data into child components.
5. Hooks and services connect UI to framework behavior.

## Shared Odoo frontend anchors

- `registry.category(...)`
- `useService(...)`
- `useState(...)`
- action, field, systray, and main-component registration patterns

## Shared QWeb directives

| Directive | Purpose |
|-----------|---------|
| `t-if` / `t-elif` / `t-else` | Conditional rendering |
| `t-foreach` / `t-as` / `t-key` | Iteration |
| `t-esc` | Escaped text output |
| `t-out` | Raw HTML output |
| `t-att-*` | Dynamic attributes |
| `t-on-*` | Event handlers |
| `t-ref` | Element reference |

## Guidance

- keep concept docs generic
- keep version claims in the version-specific files
- verify uncertain 19.0 frontend behavior against upstream source
