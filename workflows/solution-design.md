# WORKFLOW: Solution Design

## Purpose

Guide the agent through creating or updating Vietnamese `Solution Design.docx` to explain selected Odoo solution decisions for customer and delivery-team alignment.

## When to use

Use this workflow after fit-gap analysis and enough Functional Design content exist to decide the solution approach.

## Inputs

- requirement analysis
- `Fit-Gap Analysis.xlsx` or equivalent fit-gap analysis workbook
- Functional Design draft or confirmed sections
- known technical constraints or delivery assumptions

## Required reads

- `skills/odoo-presales/SKILL.md`
- `skills/odoo-presales/references/solution-design-docx-guide.md`
- `skills/odoo-presales/references/design-artifact-handoff-guide.md`

## Optional reads

- `skills/odoo-presales/references/functional-design-docx-guide.md`
- `skills/odoo-presales/references/solution-design-example-sale-approval.md` when a realistic sample would help shape the document
- `skills/odoo-presales/references/effort-estimation-guide.md`
- matching business-domain, integration, automation, operations, or security references when solution decisions depend on them

## Steps

1. Confirm the document should be Vietnamese unless the user requests otherwise.
2. Confirm blocking clarifications that would materially change treatment choice, scope, or delivery assumptions are already resolved or explicitly waived in `Clarification Register.xlsx`.
3. Use the canonical Solution Design structure from `solution-design-docx-guide.md` as the document baseline.
4. Map major requirement groups to standard, configuration, customization, integration, or process-change treatment.
5. Explain the selected solution and why it is appropriate.
6. Record rejected alternatives only when they clarify the decision.
7. Keep assumptions, dependencies, risks, and customer responsibilities explicit.
8. Do not add optional features outside scope unless the user asks for recommendations.
9. Use the clarification register as the source of confirmed answers and waived assumptions; do not defer unresolved core decisions into the document itself.
10. Create or update `Solution Design.docx`.
11. Render and visually inspect the DOCX when the runtime supports document rendering.

## Outputs

- `Solution Design.docx`
- decision/clarification summary when useful

## Validation gates

- each major decision maps back to requirements or fit-gap groups
- standard/config/custom/integration boundaries are clear
- unresolved business decisions are not left hidden in the finished document
- document is readable by customer and delivery stakeholders
