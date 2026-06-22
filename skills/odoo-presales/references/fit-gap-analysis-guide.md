# Odoo Fit-Gap Analysis Guide

Use this reference to convert discovery findings into a decision table that is usable by delivery teams.

## Classification model

| Label | Meaning |
|---|---|
| Fit | Standard Odoo behavior covers the need |
| Configuration | Covered through settings, access setup, sequences, views, automation, or Studio-style configuration |
| Customization | Requires custom module or code changes |
| Integration | Requires external API, connector, import bridge, or sync flow |
| Process change | Customer can adopt Odoo standard behavior instead of custom development |
| Out of scope | Intentionally excluded from the current phase |

## Table structure

| ID | Requirement | Business area | Classification | Proposed approach | Effort note | Open questions |
|---|---|---|---|---|---|---|

## Working rules

1. One distinct requirement per row.
2. Keep language business-readable first, then add technical notes.
3. Preserve traceability to the discovery note or workshop statement.
4. If the requirement is still ambiguous, keep it as an open question instead of forcing a solution.
5. Prefer process change over customization when it solves the same business goal cleanly.

## Output usage

- `Fit` rows become implementation assumptions or standard usage notes.
- `Configuration` rows become `Configuration Notes` during handoff.
- `Customization` rows become functional, workflow, reporting, or security entries in `01-business-to-implementation-spec.md`.
- `Integration` rows become integration contracts and data-flow notes.
- `Out of scope` rows stay visible so the delivery team does not absorb them accidentally.
