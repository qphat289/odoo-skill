# WORKFLOW: Orchestrator

## Purpose

Act as the top-level router for workflow selection inside this repository.

## When to use

Use this file first when the task type is still broad and the agent must decide which specialized workflow to load.

## Inputs

- request type
- input stage or artifact maturity
- target Odoo version if known
- module path or business context if available

## Required reads

- `SKILL.md`
- `skills/odoo-development/SKILL.md`

## Optional reads

- `skills/odoo-upgrade/references/odoo-version-routing.md`
- `skills/odoo-module-generation/references/odoo-manifest-data-order.md`
- `rules/security.md`
- `rules/coding-style.md`

## Steps

1. Identify the request type and input maturity:
   - detailed customer requirement that should run end-to-end through analysis, design, implementation, QA/QC, fixes, retest, and reporting
   - raw business context
   - discovery notes
   - fit-gap or proposal material
   - Functional Design / Solution Design ready for Technical Design
   - Technical Design ready for Test Plan
   - Technical Design or Test Plan ready for project tracking
   - existing code/module
   - skill-pack maintenance request
2. If the user wants end-to-end delivery from customer requirement to tested output, route first to `workflows/full-delivery-loop.md`.
3. Route business-facing or ambiguous input through presales before technical planning.
4. Detect or confirm the Odoo version before any code generation, review, upgrade, test execution, or version-sensitive implementation planning.
5. Load the matching version skill from `skills/odoo-14.0/` through `skills/odoo-19.0/` when version matters.
6. Route to the matching specialized workflow:
   - detailed customer requirement to full delivery -> `workflows/full-delivery-loop.md`
   - raw business requirement or discovery -> `workflows/presales-discovery.md`
   - detailed customer SOW, module list, or requirement file -> `workflows/requirements-analysis.md`
   - requirement classification -> `workflows/fit-gap.md`
   - estimate, proposal, SOW, or handoff -> `workflows/proposal-handoff.md`
   - Functional Design DOCX -> `workflows/functional-design.md`
   - Solution Design DOCX -> `workflows/solution-design.md`
   - Functional/Solution Design to Technical Design -> `workflows/technical-design.md`
   - Technical Design to Test Plan -> `workflows/test-plan.md`
   - technical task breakdown, backlog, implementation status, or test status tracking -> `workflows/project-tracking.md`
   - create or extend module -> `workflows/generate-module.md`
   - review or audit module -> `workflows/review-module.md`
   - upgrade or migrate module -> `workflows/upgrade-module.md`
   - generate or audit security -> `workflows/security-module.md`
   - run or debug tests -> `workflows/test-module.md`
   - generate tests -> `workflows/generate-tests.md`
   - OWL or frontend work -> `workflows/frontend-owl.md`
   - skill-pack self-maintenance -> `workflows/skill-maintenance.md`
7. Select the helper prompt only if useful:
   - presales -> `agents/odoo-presales-consultant.md`
   - technical design -> `agents/odoo-technical-planner.md`
   - QA/QC planning -> `agents/odoo-qa-qc.md`
   - existing-code context -> `agents/odoo-context-gatherer.md`
   - review -> `agents/odoo-code-reviewer.md`
   - tests -> `agents/odoo-tester.md`
   - upgrade -> `agents/odoo-upgrade-analyzer.md`
8. Load only the smallest relevant domain skill and references for that workflow.
9. Apply `rules/security.md` and `rules/coding-style.md` for implementation planning, generation, review, and upgrade tasks.
10. If no workflow fits exactly:
   - keep the closest workflow as the primary playbook
   - borrow only the smallest additional skill or reference set needed
   - adapt the output to the task instead of forcing the full artifact chain
11. If the task involves `.docx`, `.xlsx`, `.xls`, `.csv`, or `.tsv`:
   - keep the selected business, design, quality, or tracking workflow as the primary route
   - add document or spreadsheet capability only for the file-handling part
   - do not turn office-file handling into a reason to restart the artifact chain

## Outputs

- selected workflow
- selected version skill
- minimal reference set to load next
- note when a partial or hybrid route was intentionally used
- note when document or spreadsheet capability is needed for the chosen route

## Validation gates

- request type is mapped to exactly one primary workflow
- the full delivery loop is used only for true end-to-end requests, not simple narrow tasks
- business-facing input is not prematurely routed into code generation
- version is not guessed when it materially affects syntax or rules
- shared rules are loaded for code-facing work
- only needed references are loaded after routing
- partial or hybrid routing still preserves the key traceability needed for the task
- office-file handling is recognized when relevant without distorting the primary workflow choice
