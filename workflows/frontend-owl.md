# WORKFLOW: Frontend OWL

## Purpose

Guide the agent through Odoo frontend and OWL component work using version-correct structure and asset validation.

## When to use

Use this workflow for widgets, field components, dialogs, systray items, client actions, and other web-client assets.

## Inputs

- target Odoo version
- component type
- component name
- required services, state, and placement

## Required reads

- `skills/odoo-owl/SKILL.md`

## Optional reads

- `skills/odoo-owl/references/odoo-owl-components-{version}.md`

## Steps

1. Confirm the version and component type.
2. Load the shared OWL skill and the version-specific frontend reference when available.
3. Capture the required services, state, events, and placement in the web client.
4. Generate the smallest correct component structure for that version.
5. Validate asset paths, template naming, registry usage, and service injection style.
6. For 19.0 or uncertain frontend APIs, verify against official upstream source before claiming a major pattern difference.

## Outputs

- component file structure
- version-sensitive frontend notes
- validation summary

## Validation gates

- file layout matches the target version
- registry and service usage match current patterns
- uncertain frontend claims are verified before being treated as standards

