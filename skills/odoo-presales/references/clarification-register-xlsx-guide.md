# Clarification Register XLSX Guide

Use this guide when the project needs one structured workbook to collect all necessary clarification questions and answers before fit-gap and downstream design work proceed.

Suggested filename: `Clarification Register.xlsx`

## Purpose

Keep clarification disciplined:

- ask only what materially matters
- resolve it early
- store the answer in one structured place
- avoid scattering questions across fit-gap, Functional Design, and Solution Design

## Format rule

- Default clarification-register format is `.xlsx`.
- If the user prefers another format, preserve the same row logic and traceability.
- When the user answers by chat, the agent should update the workbook on the user's behalf.

## Recommended workbook structure

### Sheet 1: `Clarifications`

| Column | Meaning |
|---|---|
| `Q ID` | stable clarification ID such as `CL-001` |
| `Requirement ID` | related `RQ-xxx` or customer requirement ID |
| `Area / Process` | sales, CRM, approval, integration, finance, etc. |
| `Question` | the exact clarification needed |
| `Why It Matters` | fit-gap / scope / solution / estimate / risk / acceptance |
| `Blocking Level` | Blocking / Minor |
| `Owner` | customer / FC / solution owner / PM / tech lead |
| `Answer` | confirmed answer text |
| `Answer Source` | meeting, chat, email, workshop, document section, etc. |
| `Status` | Open / Answered / Waived |
| `Impact Summary` | what changed or was confirmed after the answer |

### Sheet 2: `Summary`

| Field | Example |
|---|---|
| Customer / Project | `ABC Distribution - Sales Approval Rollout` |
| Target Odoo Version | `18.0` |
| Register Status | `In Review / Ready / Partial` |
| Blocking Count | `3` |
| Minor Count | `2` |
| Ready For Fit-Gap | `Yes / No` |

## Working rules

1. One clarification per row.
2. Ask only high-value, directly relevant questions.
3. Do not create "nice to know" rows.
4. Blocking rows must be resolved or explicitly waived before fit-gap or customer-facing design is treated as stable.
5. Minor rows may remain only if they do not change classification, scope, or solution direction.
6. When an answer is given in chat, update the workbook instead of leaving the answer only in conversation.

## Downstream usage

This workbook should feed:

- `Requirement Analysis.md`
- `Fit-Gap Analysis.xlsx`
- `Functional Design.docx`
- `Solution Design.docx`
- `Technical Design.md`
