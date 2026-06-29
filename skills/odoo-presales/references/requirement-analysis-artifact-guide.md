# Requirement Analysis Artifact Guide

Use this guide when the requirement-analysis artifact must be created or updated as a normalized working document.

Suggested filename: `Requirement Analysis.md`

## Purpose

Capture the customer input in a cleaner, normalized structure before fit-gap classification starts. This artifact is the bridge between raw customer material and `Fit-Gap Analysis.xlsx`.

## Format rule

- Default requirement-analysis artifact format is `.md`.
- If the user asks for another format, preserve the same structure and traceability.
- Keep it normalized and working-oriented, not customer-polished like Functional Design or Solution Design.

## Recommended structure

```markdown
# Requirement Analysis

## 1. Source Files

| File | Type | Scope / Notes |
|---|---|---|

## 2. Analysis Summary

- Customer / project:
- Target Odoo version:
- Analysis status:
- Main business areas:
- Known phase boundary:
- Main assumptions:

## 3. Requirement Inventory

| Req ID | Module / Area | Process / Function | Customer Requirement | Source Ref | Priority | Scope Status | Notes |
|---|---|---|---|---|---|---|---|

## 4. Requirement Grouping

| Group ID | Group Name | Included Req IDs | Why Grouped |
|---|---|---|---|

## 5. Clarification Register Status

- Clarification artifact: `Clarification Register.xlsx`
- Blocking clarification status:
- Minor clarification status:
- Ready for fit-gap:

## 6. Scope Boundaries

### In Scope

### Out Of Scope

### Later Phase / Backlog Candidates

## 7. Next-Step Recommendation

- Recommended next workflow:
- Ready for fit-gap:
- Key blockers before fit-gap:
```

## Working rules

1. Preserve customer requirement IDs, section labels, sheet names, and business wording whenever possible.
2. Normalize only enough to make the input analyzable.
3. Keep one logical requirement per row unless the customer source already split them better.
4. Separate actual requirements from assumptions, ideas, or future-phase items.
5. Record clarification needs in `Clarification Register.xlsx` only when they materially affect fit-gap, design, estimate, risk, or acceptance or when they are useful low-impact confirmations worth keeping centrally.
6. Keep the requirement-analysis file focused on readiness and traceability instead of duplicating the clarification rows inline.
7. Keep `Req ID` stable so it can be cited later in fit-gap, Functional Design, Solution Design, Technical Design, Test Plan, and Project Tracking.

## Downstream usage

This artifact should feed:

- `Clarification Register.xlsx`
- `Fit-Gap Analysis.xlsx`
- `Functional Design.docx`
- `Solution Design.docx`
- `Technical Design.md`

It may also be cited indirectly by:

- `Test Plan.md`
- `Project Tracking.md`
