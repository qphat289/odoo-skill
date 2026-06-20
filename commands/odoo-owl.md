---
name: odoo-owl
description: Generate Odoo frontend components. Use when the user asks for a widget, client action, systray item, dialog, or other frontend component.
arguments:
  - name: type
    description: Component type (widget, action, systray, dialog, field)
    required: false
  - name: name
    description: Component name
    required: false
  - name: version
    description: Target Odoo version
    required: false
---

# /odoo-owl Command

Generate frontend components with version-aware Odoo patterns.

## Execution flow

1. Determine the target Odoo version.
2. Read `skills/odoo-owl/references/odoo-owl-components-{version}.md`.
3. Gather component type, name, services, and state needs.
4. Generate the component using the matching frontend structure.

## Version map

- 14.0: legacy JavaScript, no OWL skill usage
- 15.0: OWL 1.x
- 16.0-18.0: OWL 2-style patterns
- 19.0: verify current upstream frontend patterns before making major-version assumptions

## Output structure

### Odoo 15
```text
static/src/js/{component_name}.js
static/src/xml/{component_name}.xml
static/src/scss/{component_name}.scss
```

### Odoo 16+
```text
static/src/components/{component_name}/{component_name}.js
static/src/components/{component_name}/{component_name}.xml
static/src/components/{component_name}/{component_name}.scss
```

## Template note for 19.0

- keep `/** @odoo-module **/`
- keep `registry.category(...)`
- keep `useService(...)`
- verify props and hook style against current upstream `addons/web`
