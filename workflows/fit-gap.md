# WORKFLOW: Fit-Gap

## Purpose

Guide the agent through turning customer requirements or discovery output into `Fit-Gap Analysis.xlsx`, a structured decision workbook that can feed Functional Design, Solution Design, and Technical Design.

## When to use

Use this workflow after requirement analysis or discovery and before Functional Design, Solution Design, estimation, proposal, or Technical Design.

## Inputs

- discovery notes
- requirement statements
- Scope of Work, module list, function list, or customer requirement file
- known priorities or phase constraints

## Required reads

- `skills/odoo-presales/SKILL.md`
- `skills/odoo-presales/references/requirement-analysis-guide.md`
- `skills/odoo-presales/references/clarification-register-xlsx-guide.md`
- `skills/odoo-presales/references/fit-gap-analysis-guide.md`
- `skills/odoo-presales/references/fit-gap-analysis-xlsx-guide.md`
- `skills/odoo-presales/references/design-artifact-handoff-guide.md`

## Optional reads

- `skills/odoo-presales/references/discovery-questionnaire.md`
- `skills/odoo-presales/references/fit-gap-analysis-example-sale-approval.md` when a realistic sample would help shape the workbook

## Steps

1. Split the input into one row per distinct requirement without adding new scope.
2. Check `Clarification Register.xlsx` or equivalent clarification capture first.
3. If any unanswered blocking clarification would materially change classification, scope, solution direction, estimate, or acceptance, resolve or explicitly waive it before finalizing the workbook.
4. Load the fit-gap guide, clarification-register guide, XLSX structure guide, and classification model.
5. Classify each row as:
   - Fit
   - Configuration
   - Customization
   - Integration
   - Process change
   - Out of scope
6. Preserve traceability to the source discovery note, file section, sheet, or requirement ID.
7. Build or update `Fit-Gap Analysis.xlsx` as the primary artifact unless the user requested another format.
8. Cite clarification IDs or confirmation notes where a row depends on prior clarification.
9. Hand the finished workbook to Functional Design, Solution Design, proposal, or Technical Design work when ready.

## Outputs

- `Fit-Gap Analysis.xlsx`
- next-step recommendation
- updated requirement traceability input for Functional Design, Solution Design, and Technical Design

## Validation gates

- each requirement has exactly one primary classification
- blocking clarifications are resolved before final classification is treated as stable
- clarification-dependent rows cite the relevant clarification source when needed
- workbook rows stay traceable and stable
- out-of-scope items are visible and not mixed into confirmed scope
