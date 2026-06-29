# WORKFLOW: Requirements Analysis

## Purpose

Guide the agent through analyzing detailed customer-provided Scope of Work, module lists, function lists, spreadsheets, or requirement documents before fit-gap and design work.

## When to use

Use this workflow when the customer input is already detailed enough that broad discovery questions would be wasteful.

## Inputs

- customer requirement document, SOW, DOCX, XLSX, CSV, PDF, or notes
- target Odoo version if known
- known customer modules, business areas, or phase boundaries

## Required reads

- `skills/odoo-presales/SKILL.md`
- `skills/odoo-presales/references/customer-input-file-handling.md`
- `skills/odoo-presales/references/requirement-analysis-guide.md`
- `skills/odoo-presales/references/requirement-analysis-artifact-guide.md`
- `skills/odoo-presales/references/clarification-register-xlsx-guide.md`

## Optional reads

- `skills/odoo-presales/references/discovery-questionnaire.md` only when the input is incomplete
- `skills/odoo-presales/references/requirement-analysis-example-sale-approval.md` when a realistic sample would help shape the artifact
- `skills/odoo-business-domains/SKILL.md` and one matching business-domain reference when domain vocabulary needs clarification

## Steps

1. Identify the source files and preserve their names, sections, sheets, or requirement IDs.
2. Extract a requirement inventory without adding new modules or features.
3. Normalize module/function names while keeping customer terminology traceable.
4. Classify clarification needs before writing downstream design or fit-gap conclusions:
   - blocking clarifications: unanswered points that would change fit-gap, scope, solution direction, estimate, major risk, or acceptance
   - minor clarifications: useful details that should still be recorded centrally even when they do not block immediate classification
5. Build or update `Clarification Register.xlsx` with only the smallest high-value clarification set needed; do not ask side-track or low-impact questions.
6. Build or update `Requirement Analysis.md` as the primary artifact unless the user requested another format.
7. Separate in-scope, out-of-scope, and later-phase/backlog candidates.
8. Hand off to `workflows/fit-gap.md` only when the clarification register is ready enough for fit-gap or the remaining items were explicitly waived by the user.

## Outputs

- `Requirement Analysis.md`
- `Clarification Register.xlsx`
- scope-boundary notes
- recommended next workflow

## Validation gates

- no extra scope was invented
- clarification rows are minimal and explain why they are necessary
- low-value or side-track questions are filtered out
- customer-provided module/function structure remains traceable
- output can feed fit-gap analysis
