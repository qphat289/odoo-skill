# Odoo Fit-Gap Analysis Guide

Use this reference to convert discovery findings into a decision table that is usable by delivery teams.

Suggested artifact: `Fit-Gap Analysis.xlsx`

Default format rule:

- Use `.xlsx` as the primary artifact for fit-gap unless the user explicitly requests another format.
- Use spreadsheet runtime capabilities when creating or editing the workbook.

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

Minimum workbook sheet: `Fit-Gap Matrix`

| ID | Requirement ID | Requirement Summary | Business Area | Module / Process | Classification | Proposed Approach | Scope Status | Phase | Priority | Source Ref | Clarification Ref | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Working rules

1. One distinct requirement per row.
2. Keep language business-readable first, then add technical notes.
3. Preserve traceability to the discovery note or workshop statement.
4. If the ambiguity would change classification, scope, solution direction, estimate, or acceptance, resolve it before treating the row as final.
5. Use `Clarification Ref` to cite the relevant row from `Clarification Register.xlsx` when a fit-gap decision depends on confirmed clarification.
6. Prefer process change over customization when it solves the same business goal cleanly.
7. Keep out-of-scope and later-phase items explicit instead of burying them in notes.
8. Keep workbook rows stable so Functional Design, Solution Design, Technical Design, Test Plan, and Project Tracking can cite the same IDs later.

## Output usage

- `Fit` rows become implementation assumptions or standard usage notes.
- `Configuration` rows become `Configuration Notes` during handoff.
- `Customization` rows become Functional Design entries and Technical Design sections.
- `Integration` rows become integration contracts and data-flow notes.
- `Out of scope` rows stay visible so the delivery team does not absorb them accidentally.
- The workbook should feed:
  - `Functional Design.docx`
  - `Solution Design.docx`
  - `Technical Design.md`
  - `Test Plan.md`
  - `Project Tracking.md`
