# WORKFLOW: Proposal And Handoff

## Purpose

Guide the agent from fit-gap output into estimation, proposal, SOW structure, and a confirmed `01-business-to-implementation-spec.md`.

## When to use

Use this workflow when fit-gap decisions are stable enough to support commercials, scope definition, or delivery planning.

## Inputs

- fit-gap table
- known assumptions or constraints
- desired output: estimate, proposal outline, SOW, or `01-business-to-implementation-spec.md`

## Required reads

- `skills/odoo-presales/SKILL.md`
- `skills/odoo-presales/references/business-to-implementation-spec-template.md`
- `skills/odoo-presales/references/effort-estimation-guide.md`
- `skills/odoo-presales/references/proposal-sow-templates.md`
- `skills/odoo-presales/references/implementation-handoff-guide.md`

## Optional reads

- `workflows/implementation-planning.md`
- `agents/odoo-planner.md` when the work is already moving into implementation planning

## Steps

1. Confirm which output artifact is needed.
2. Load the estimation, proposal, and handoff references.
3. Produce only the smallest needed artifact:
   - estimate summary
   - proposal outline
   - SOW structure
   - `01-business-to-implementation-spec.md`
4. Keep strict separation between:
   - confirmed scope
   - assumptions
   - out of scope
   - open questions
5. When the result is implementation-ready, hand off to `workflows/implementation-planning.md` or `agents/odoo-planner.md`.

## Outputs

- estimate summary
- proposal outline
- SOW structure
- or `01-business-to-implementation-spec.md`

## Validation gates

- output type matches the requested stage
- assumptions and excluded scope are not hidden inside implementation notes
- handoff artifact is structured enough for planning without rereading all presales prose
