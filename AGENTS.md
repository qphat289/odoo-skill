# Odoo Skill-Pack Workspace

Use this repository as an Odoo skill-pack workspace for presales analysis, implementation planning, QA/QC planning, development, review, testing, upgrade, and skill maintenance.

## Canonical role

`AGENTS.md` is the canonical repository instruction file.

Host-specific files such as `CLAUDE.md`, `GEMINI.md`, `HERMES_SETUP.md`, `.cursorrules`, `.clinerules`, `.windsurfrules`, and `.github/copilot-instructions.md` should stay thin and point back to this file instead of duplicating the full workflow.

## Repository layout

- `SKILL.md` is the project-mode router.
- `skills/` contains native skill folders only.
- `skills/odoo-development/` is the packaged top-level router.
- `skills/odoo-14.0/` through `skills/odoo-19.0/` contain version routing notes.
- Domain skill folders under `skills/` contain the reusable Odoo knowledge base.
- `skills/odoo-documents/` and `skills/odoo-spreadsheets/` contain project-owned office capability support for DOCX and workbook tasks.
- `workflows/` contains execution playbooks.
- `rules/` contains cross-version coding and security rules.
- `agents/` contains optional helper prompts.
- `docs/CORRECTIONS_LOG.md` contains repository maintenance logs for recurring mistakes and corrections.
- `scripts/` contains installer and validation helpers.

## Default routing workflow

1. Read `SKILL.md`.
2. Classify the user input before choosing a workflow:
   - detailed customer requirement that should go from analysis to planning, code, test, fix, retest, and reporting -> full delivery loop
   - business discovery, fit-gap, estimation, proposal, or unclear scope -> presales route
   - Functional Design and Solution Design that need implementation detail -> technical design route
   - Technical Design that needs detailed QA/QC coverage, test scope, or test status planning -> test plan route
   - Technical Design or Test Plan that need backlog, phase/module breakdown, or delivery status -> project tracking route
   - code generation, review, test generation, test execution, upgrade, security, OWL, operations, or integrations -> technical route
   - skill-pack correction or repository maintenance -> skill maintenance route
3. Use the full delivery loop only when the user wants an end-to-end customer-requirement-to-delivery workflow; otherwise route to the smallest workflow that matches the request.
4. Treat workflows as default playbooks, not rigid rails:
   - if one workflow fits exactly, use it
   - if the task is narrower, use only the closest slice
   - if no workflow fits exactly, combine the smallest matching skill set and preserve traceability where practical
5. Treat canonical artifacts as the default output for formal delivery work, not as mandatory output for every narrow request.
6. For detailed requirement-analysis work, resolve the needed rows in `Clarification Register.xlsx` before treating fit-gap, Functional Design, or Solution Design as stable.
7. Narrow requests may stay in chat or Markdown when that better matches the task, as long as source traceability and key decisions do not disappear.
8. Keep hard constraints firm even when the route is flexible:
   - do not skip presales routing for business-facing ambiguity
   - do not scatter unresolved business clarifications across downstream artifacts; keep them in the clarification register until resolved or explicitly waived
   - do not guess the Odoo version for version-sensitive work
   - do not skip security, manifest-order, and test validation for technical work
9. Detect or confirm the target Odoo version before code generation, code review, tests, upgrades, or version-sensitive planning.
10. Read `skills/odoo-development/SKILL.md`, then load the matching workflow and the smallest relevant domain skill.
11. Read only the references needed for the selected route.
12. Use helper prompts from `agents/` only when they materially improve routing, planning, review, testing, or context gathering.
13. Read `rules/security.md` and `rules/coding-style.md` when generating, reviewing, upgrading, or planning implementation work.
14. Verify uncertain syntax or version-sensitive behavior against official Odoo sources.
15. Validate security, manifest order, version fit, and tests before finishing technical work.
16. When office-file handling materially matters, load `skills/odoo-documents/` or `skills/odoo-spreadsheets/` as support skills without replacing the primary workflow.

## Harness stance

- Use `skills/odoo-development/references/skill-pack-harness-guide.md` when improving the pack itself.
- Use `skills/odoo-development/references/eval-campaign-guide.md` when routing, artifact behavior, helper-agent behavior, or loop synchronization must be pressure-tested.
- Pressure-test routing and artifact behavior with `skills/odoo-development/references/route-pressure-scenarios.md`.
- Treat `evals/routing-workflow-evals.json` as the machine-checkable eval coverage set for the pressure scenarios.
- Record meaningful RED/GREEN/REFACTOR runs in `docs/HARNESS_EVAL_LOG.md`.
- Use validators in `scripts/` to keep layout and skill-pack contracts machine-checkable.
- When the active task touches `.docx`, `.xlsx`, `.xls`, `.csv`, or `.tsv`, treat document/spreadsheet handling as a task capability tied to the selected route instead of as a separate business workflow by default.
