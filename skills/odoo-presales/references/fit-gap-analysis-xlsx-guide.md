# Fit-Gap Analysis XLSX Guide

Use this guide when the fit-gap artifact must be created or updated as a spreadsheet.

Suggested filename: `Fit-Gap Analysis.xlsx`

## Purpose

Make fit-gap analysis auditable row by row. This workbook is the structured bridge between customer requirements and the later design, implementation, QA/QC, and delivery artifacts.

## Format rule

- Default fit-gap artifact format is `.xlsx`.
- If the user asks for another format, keep the same row logic and traceability.
- When building or editing the workbook, use spreadsheet runtime capabilities.

## Recommended workbook structure

### Sheet 1: `Overview`

Purpose:

- high-level scope summary
- version, customer, phase, and owner metadata
- quick counts by classification

Suggested fields:

| Field | Example |
|---|---|
| Customer / Project | `ABC Distribution - Odoo Rollout` |
| Target Odoo Version | `18.0` |
| Analysis Status | `Draft / In Review / Approved` |
| Prepared By | `FC / solution owner` |
| Scope Boundary | `Phase 1 sales + CRM + sync only` |
| Total Requirement Rows | `57` |

Optional summary table:

| Classification | Count |
|---|---|
| Fit |  |
| Configuration |  |
| Customization |  |
| Integration |  |
| Process change |  |
| Out of scope |  |

### Sheet 2: `Fit-Gap Matrix`

Purpose:

- one row per requirement
- canonical source for downstream references

Required columns:

| Column | Meaning |
|---|---|
| `ID` | stable fit-gap row ID such as `FG-001` |
| `Requirement ID` | customer or source requirement ID if available |
| `Requirement Summary` | short business-readable statement |
| `Business Area` | sales, CRM, stock, accounting, HR, etc. |
| `Module / Process` | target Odoo area or process name |
| `Classification` | Fit / Configuration / Customization / Integration / Process change / Out of scope |
| `Proposed Approach` | short explanation of how the requirement is addressed |
| `Scope Status` | In scope / Out of scope / Later phase |
| `Phase` | Phase 1 / Phase 2 / etc. |
| `Priority` | High / Medium / Low |
| `Source Ref` | source file, section, sheet, row, or note ID |
| `Clarification Ref` | related `CL-xxx` row when the classification depends on clarified input |
| `Notes` | short implementation or decision notes |

Recommended extra columns:

| Column | Use |
|---|---|
| `Functional Ref` | later map to Functional Design section |
| `Solution Ref` | later map to Solution Design section |
| `Technical Ref` | later map to Technical Design section |

### Optional Sheet 3: `Scope Summary`

Purpose:

- grouped view by module, phase, or classification for stakeholder review

Suggested columns:

| Column | Meaning |
|---|---|
| `Module / Area` | grouped business area |
| `Phase` | grouped delivery phase |
| `Fit` | count |
| `Config` | count |
| `Custom` | count |
| `Integration` | count |
| `Notes` | high-level scope note |

## Formatting guidance

- Freeze header row on each sheet.
- Use filters on the matrix sheet.
- Keep IDs stable once shared downstream.
- Use dropdown validation where practical for:
  - `Classification`
  - `Scope Status`
  - `Phase`
  - `Priority`
- Keep row text concise enough to scan.

## Traceability rules

1. One requirement per row.
2. Do not merge multiple requirements into one row just because they belong to the same module.
3. Keep source references precise enough that another person can trace back to the customer input.
4. Keep `FG-xxx` IDs stable and reuse them in later artifacts.
5. Do not defer unresolved blocking decisions into this workbook just to finish faster; keep them upstream in `Clarification Register.xlsx` until resolved or waived.
6. Separate out-of-scope and later-phase rows instead of burying them in notes.

## Downstream usage

This workbook should feed:

- `Functional Design.docx`
- `Solution Design.docx`
- `Technical Design.md`
- `Test Plan.md`
- `Project Tracking.md`
