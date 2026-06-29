---
name: odoo-presales
description: Domain skill for Odoo customer requirement analysis, fit-gap analysis in XLSX, Functional Design DOCX, Solution Design DOCX, estimation, proposal/SOW support, and handoff to Technical Design.
---

# Odoo Presales

Use this skill when the task happens before coding starts, when customer requirements must be analyzed without inventing scope, or when project delivery needs Functional Design, Solution Design, or a clean handoff to Technical Design.

## Quick reference

| Topic | File | When to use |
|---|---|---|
| Customer input files | `references/customer-input-file-handling.md` | Read DOCX/XLSX/CSV/PDF requirements safely and preserve traceability |
| Detailed requirement analysis | `references/requirement-analysis-guide.md` | Normalize customer-provided Scope of Work, module lists, or function lists |
| Requirement-analysis artifact | `references/requirement-analysis-artifact-guide.md` | Build or update `Requirement Analysis.md` as the normalized presales analysis baseline |
| Requirement-analysis example | `references/requirement-analysis-example-sale-approval.md` | See a realistic requirement-analysis artifact before drafting a new one |
| Clarification register workbook | `references/clarification-register-xlsx-guide.md` | Gather only the necessary clarification questions and answers before fit-gap or design |
| Clarification register example | `references/clarification-register-example-sale-approval.md` | See a realistic clarification workbook example before drafting a new one |
| Discovery workshops | `references/discovery-questionnaire.md` | Collect requirements when the customer input is not detailed enough |
| Fit-gap classification | `references/fit-gap-analysis-guide.md` | Map requirements to fit, config, custom, integration in `Fit-Gap Analysis.xlsx` |
| Fit-gap workbook structure | `references/fit-gap-analysis-xlsx-guide.md` | Build or update the XLSX artifact structure for fit-gap work |
| Fit-gap example | `references/fit-gap-analysis-example-sale-approval.md` | See a realistic fit-gap workbook example before drafting a new one |
| Rough estimation | `references/effort-estimation-guide.md` | Size work before planning or proposal |
| Proposal and SOW structure | `references/proposal-sow-templates.md` | Build commercial and scope documents |
| Functional Design | `references/functional-design-docx-guide.md` | Create Vietnamese `Functional Design.docx` for customer/team review |
| Functional Design example | `references/functional-design-example-sale-approval.md` | See a realistic FSD example aligned to the canonical section order |
| Solution Design | `references/solution-design-docx-guide.md` | Create Vietnamese `Solution Design.docx` to explain selected solution decisions |
| Solution Design example | `references/solution-design-example-sale-approval.md` | See a realistic solution-decision document before drafting a new one |
| Design handoff | `references/design-artifact-handoff-guide.md` | Preserve traceability across Functional, Solution, and Technical Design |
| Process swimlanes | `references/process-swimlane-guide.md` | Build business-process swimlanes for FSD sections |

## Rules

1. Use this skill before `odoo-technical-planner` when the scope is still business-facing, customer-facing, or ambiguous.
2. Do not suggest extra modules, features, or scope unless the user explicitly asks for recommendations.
3. Verify only information that is materially needed for fit-gap, Functional Design, Solution Design, Technical Design, estimation, risk, or acceptance.
4. Keep business requirements traceable from customer input to fit-gap to Functional Design, Solution Design, and Technical Design.
5. Default requirement-analysis output to `Requirement Analysis.md` unless the user explicitly asks for another format.
6. Default fit-gap output to `Fit-Gap Analysis.xlsx` unless the user explicitly asks for another format.
7. Produce `Functional Design.docx` and `Solution Design.docx` in Vietnamese unless the user requests otherwise.
8. Do not treat customer-facing DOCX artifacts as coding instructions alone; they are also communication and sign-off documents.
9. Do not mix signed scope, exploratory ideas, and phase-2 backlog in one table.
10. When a requirement is not confirmed and it materially affects scope, fit-gap, solution direction, estimate, risk, or acceptance, capture it in `Clarification Register.xlsx` instead of turning it into implementation detail.
11. Treat `.docx`, `.xlsx`, `.xls`, `.csv`, and `.tsv` handling as presales-related file capability when they are part of the task, not as a separate planning workflow by default.
12. Ask only clarifications that materially affect fit-gap, scope, solution direction, estimate, risk, or acceptance; do not ask low-value or side-track questions.
13. Resolve blocking clarifications before finalizing fit-gap or customer-facing design artifacts.
14. Do not scatter unresolved core questions across fit-gap, Functional Design, or Solution Design; resolve or explicitly waive them in the clarification register first.
