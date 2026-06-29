# WORKFLOW: Proposal And Handoff

## Purpose

Guide the agent from fit-gap output into estimation, proposal, SOW structure, Functional Design, Solution Design, or Technical Design handoff.

## When to use

Use this workflow when fit-gap decisions are stable enough to support commercials, scope definition, customer-facing design, or technical design handoff.

## Inputs

- `Fit-Gap Analysis.xlsx` or equivalent fit-gap workbook
- known assumptions or constraints
- desired output: estimate, proposal outline, SOW, Functional Design, Solution Design, or Technical Design handoff

## Required reads

- `skills/odoo-presales/SKILL.md`
- `skills/odoo-presales/references/functional-design-docx-guide.md`
- `skills/odoo-presales/references/solution-design-docx-guide.md`
- `skills/odoo-presales/references/effort-estimation-guide.md`
- `skills/odoo-presales/references/proposal-sow-templates.md`
- `skills/odoo-presales/references/design-artifact-handoff-guide.md`

## Optional reads

- `workflows/technical-design.md`
- `agents/odoo-technical-planner.md` when the work is already moving into technical design

## Steps

1. Confirm which output artifact is needed.
2. Load the estimation, proposal, and handoff references.
3. Produce only the smallest needed artifact:
   - estimate summary
   - proposal outline
   - SOW structure
   - `Functional Design.docx`
   - `Solution Design.docx`
   - Technical Design handoff notes
4. Keep strict separation between:
   - confirmed scope
   - assumptions
   - out of scope
   - clarification items that still belong in `Clarification Register.xlsx`
5. When Functional Design and Solution Design are ready enough, hand off to `workflows/technical-design.md` or `agents/odoo-technical-planner.md`.

## Outputs

- estimate summary
- proposal outline
- SOW structure
- Functional Design
- Solution Design
- or Technical Design handoff notes

## Validation gates

- output type matches the requested stage
- assumptions and excluded scope are not hidden inside implementation notes
- handoff artifacts are structured enough for Technical Design without rereading all presales prose
