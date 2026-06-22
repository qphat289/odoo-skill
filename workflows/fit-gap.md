# WORKFLOW: Fit-Gap

## Purpose

Guide the agent through turning discovery output into a structured decision table that can feed `01-business-to-implementation-spec.md`.

## When to use

Use this workflow after discovery and before estimation, proposal, or implementation planning.

## Inputs

- discovery notes
- requirement statements
- known priorities or phase constraints

## Required reads

- `skills/odoo-presales/SKILL.md`
- `skills/odoo-presales/references/fit-gap-analysis-guide.md`
- `skills/odoo-presales/references/business-to-implementation-spec-template.md`

## Optional reads

- `skills/odoo-presales/references/discovery-questionnaire.md`

## Steps

1. Split the discovery output into one row per distinct requirement.
2. Load the fit-gap guide and classification model.
3. Classify each row as:
   - Fit
   - Configuration
   - Customization
   - Integration
   - Process change
   - Out of scope
4. Preserve traceability to the source discovery note.
5. Record unresolved ambiguity as open questions instead of assuming a solution.
6. Hand the finished table to proposal or business-to-implementation-spec work when ready.

## Outputs

- fit-gap table
- open-question list
- next-step recommendation
- updated requirement traceability input for `01-business-to-implementation-spec.md`

## Validation gates

- each requirement has exactly one primary classification
- open questions are explicit
- out-of-scope items are visible and not mixed into confirmed scope
