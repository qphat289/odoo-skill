---
name: odoo-development
description: Project-mode router for this Odoo skill repository. Use when working inside this repository to classify Odoo inputs, route presales/business analysis, technical planning, implementation, review, testing, upgrade, or skill-maintenance work to the right packaged skill, workflow, references, and helper agent.
---

# Odoo Skill-Pack Router

This root file is the project-mode entrypoint for the repository. Route the task before loading detailed references.

## Input triage

1. Identify the input stage:
   - Full delivery loop: detailed customer requirement should go from analysis through implementation, QA/QC, fix, retest, and reporting.
   - Business or unclear scope: discovery notes, raw requirements, fit-gap, estimation, proposal, SOW, or handoff.
   - Technical design: Functional Design and Solution Design are ready enough to feed `Technical Design.md`.
   - Test planning: `Technical Design.md` is ready enough to feed `Test Plan.md`.
   - Technical execution: code generation, module changes, review, test generation, test execution, security, OWL, integrations, operations, or upgrade.
   - Project tracking: task breakdown, backlog, implementation status, test status, or phase/module tracking.
   - Skill maintenance: correcting this skill pack, routing rules, references, workflows, or backlog.
2. If the stage is full delivery loop, route to `workflows/full-delivery-loop.md`.
3. If the stage is business-facing or ambiguous, route to `skills/odoo-presales/` and a presales workflow before technical planning or coding.
4. If the stage is technical-design-ready, route to `workflows/technical-design.md` and `agents/odoo-technical-planner.md`.
5. If the stage is test-plan-ready, route to `workflows/test-plan.md` and `agents/odoo-qa-qc.md`.
6. If the stage is code-facing or test-execution-facing, confirm the target Odoo version before writing, reviewing, testing, or upgrading code. If it is not explicit, run `python scripts/detect_odoo_version.py`.
7. Read `skills/odoo-development/SKILL.md`, then the selected workflow and the smallest matching domain skill under `skills/`.
8. Read only the references needed for the selected route.
9. Read the relevant helper prompt from `agents/` when it materially improves the task.
10. Read `rules/security.md` and `rules/coding-style.md` for implementation planning, generation, review, and upgrade work.
11. Verify uncertain syntax against official Odoo sources.
12. Validate security, manifest order, version fit, and tests before finishing technical work.
13. If the task materially touches `.docx`, `.xlsx`, `.xls`, `.csv`, or `.tsv`, load `skills/odoo-documents/` or `skills/odoo-spreadsheets/` as support skills while keeping the same primary route.

## Flexible routing rules

- Workflows are default playbooks, not rigid rails.
- If no workflow fits exactly, combine the smallest matching skill set and adapt the output to the real task.
- Use canonical artifacts for formal delivery work; for narrow requests, lighter outputs are acceptable when traceability and key decisions stay visible.
- Do not force the full artifact chain for simple review, comparison, fix, or status-update tasks.
- If the task touches `.docx` or spreadsheet files, keep the same primary workflow and add document/spreadsheet capability only where the artifact actually matters.
- When maintaining the pack itself, use the harness guides, pressure scenarios, eval manifest, and validators together instead of patching instructions in isolation.

## Route map

| Input | Workflow | Primary skill | Helper agent |
|---|---|---|---|
| Detailed customer requirement to end-to-end delivery | `workflows/full-delivery-loop.md` | routed across presales, technical, quality, and tracking skills | helper agents by stage |
| Raw business requirement or discovery need | `workflows/presales-discovery.md` | `skills/odoo-presales/` | `agents/odoo-presales-consultant.md` |
| Detailed customer SOW, module list, or requirement file | `workflows/requirements-analysis.md` | `skills/odoo-presales/` | `agents/odoo-presales-consultant.md` |
| Discovery notes to classify | `workflows/fit-gap.md` | `skills/odoo-presales/` | `agents/odoo-presales-consultant.md` |
| Estimate, proposal, SOW, or handoff | `workflows/proposal-handoff.md` | `skills/odoo-presales/` | `agents/odoo-presales-consultant.md` |
| Functional Design document | `workflows/functional-design.md` | `skills/odoo-presales/` | `agents/odoo-presales-consultant.md` |
| Solution Design document | `workflows/solution-design.md` | `skills/odoo-presales/` | `agents/odoo-presales-consultant.md` |
| Functional/Solution Design to Technical Design | `workflows/technical-design.md` | `skills/odoo-module-generation/` plus needed domains | `agents/odoo-technical-planner.md` |
| Technical Design to Test Plan | `workflows/test-plan.md` | `skills/odoo-quality/` | `agents/odoo-qa-qc.md` |
| Technical Design or Test Plan to task tracking | `workflows/project-tracking.md` | `skills/odoo-module-generation/` | none by default |
| New module or feature implementation | `workflows/generate-module.md` | matching technical domain skills | `agents/odoo-context-gatherer.md` when existing code matters |
| Review, audit, tests, upgrade, frontend, security, or maintenance | matching workflow in `workflows/` | smallest matching domain skill | matching helper prompt when useful |

## Support skills

| Support need | Skill | When to add |
|---|---|---|
| DOCX input/output or customer-facing document handling | `skills/odoo-documents/` | Requirement docs, FSD, Solution Design, DOCX export or review |
| XLSX/CSV/TSV workbook handling | `skills/odoo-spreadsheets/` | Requirement workbooks, fit-gap sheets, structured tracking imports/exports |

## Hard rules

- Do not turn ambiguous business input into technical implementation detail; use presales routing first.
- Never guess the Odoo version for code-facing or version-sensitive work when the manifest is missing or unclear.
- For Odoo 17+, use direct XML attributes such as `invisible="expr"` instead of `attrs`.
- For Odoo 16+, prefer `Command` for x2many operations.
- For Odoo 17+, use `@api.model_create_multi` for `create()`.
- For Odoo 18+, use `_check_company_auto = True`, `check_company=True`, and `allowed_company_ids` where applicable.
- Every model needs access rights in `security/ir.model.access.csv`.
