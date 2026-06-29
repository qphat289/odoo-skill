# WORKFLOW: Functional Design

## Purpose

Guide the agent through creating or updating Vietnamese `Functional Design.docx` for customer, FC, PM, QA, key users, and delivery-team review.

## When to use

Use this workflow after requirement analysis and fit-gap output are ready enough to document business processes and expected system behavior.

## Inputs

- requirement analysis
- `Fit-Gap Analysis.xlsx` or equivalent fit-gap analysis workbook
- customer requirement source files
- known process diagrams, report layouts, roles, and acceptance needs

## Required reads

- `skills/odoo-presales/SKILL.md`
- `skills/odoo-presales/references/functional-design-docx-guide.md`
- `skills/odoo-presales/references/design-artifact-handoff-guide.md`
- `skills/odoo-presales/references/customer-input-file-handling.md`

## Optional reads

- `skills/odoo-presales/references/process-swimlane-guide.md` when process diagrams are needed
- `skills/odoo-presales/references/functional-design-example-sale-approval.md` when a realistic sample would help shape the document
- matching business-domain references when the functional vocabulary is domain-specific

## Steps

1. Confirm the document should be Vietnamese unless the user requests otherwise.
2. Confirm blocking clarifications that would materially change process, scope, rules, or acceptance are already resolved or explicitly waived in `Clarification Register.xlsx`.
3. Use the canonical FSD structure from `functional-design-docx-guide.md` as the document baseline.
4. Preserve requirement and fit-gap traceability.
5. Write business-readable process, rule, role, report, integration, and acceptance content.
6. Do not add features outside the customer scope.
7. Use the clarification register as the source of confirmed answers and waived assumptions; do not move unresolved core decisions into the FSD itself.
8. Create or update `Functional Design.docx`.
9. Render and visually inspect the DOCX when the runtime supports document rendering.

## Outputs

- `Functional Design.docx`
- optional clarification-reference note when useful

## Validation gates

- business behavior is clear enough for customer review and QA test preparation
- blocking process/scope questions are not deferred into the finished document by default
- no code-level implementation plan is mixed into the document
- tables, diagrams, and Vietnamese text render cleanly
- sign-off section is present when needed
