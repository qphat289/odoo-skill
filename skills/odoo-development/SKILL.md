---
name: odoo-development
description: Odoo router for Odoo 14-19 presales, business analysis, implementation planning, QA/QC planning, module generation, models, security, views, OWL, integrations, operations, upgrades, testing, performance, and reviews. Use when the task needs Odoo-specific triage before loading version and domain references.
---

# Odoo Router

Use this skill as the top-level router for the Odoo pack. Classify the input stage first, then load only the matching workflow, version skill, domain skill, and helper prompt.

## Adaptive procedure

1. Classify the task stage:
   - full delivery loop from customer requirement to tested delivery
   - presales/business analysis
   - technical design
   - test planning
   - project tracking
   - code generation or feature work
   - review, test generation, test execution, upgrade, security, frontend, integration, operations, or skill maintenance
2. Use the full delivery loop only when the user wants end-to-end execution from requirement analysis through implementation, QA/QC, fixes, retest, and reporting.
3. Route presales/business input before technical planning when requirements are still raw, exploratory, commercial, or ambiguous.
4. Detect or confirm the target Odoo version before code-facing or version-sensitive work. If needed, run `python ../../scripts/detect_odoo_version.py`.
5. Switch to the matching version-specific skill when version matters:
   - `../odoo-14.0/SKILL.md`
   - `../odoo-15.0/SKILL.md`
   - `../odoo-16.0/SKILL.md`
   - `../odoo-17.0/SKILL.md`
   - `../odoo-18.0/SKILL.md`
   - `../odoo-19.0/SKILL.md`
6. Load the matching domain skill:
   - `../odoo-presales/SKILL.md`
   - `../odoo-module-generation/SKILL.md`
   - `../odoo-models/SKILL.md`
   - `../odoo-security/SKILL.md`
   - `../odoo-views/SKILL.md`
   - `../odoo-owl/SKILL.md`
   - `../odoo-upgrade/SKILL.md`
   - `../odoo-quality/SKILL.md`
   - `../odoo-integrations/SKILL.md`
   - `../odoo-automation/SKILL.md`
   - `../odoo-business-domains/SKILL.md`
   - `../odoo-operations/SKILL.md`
   - `../odoo-documents/SKILL.md` when DOCX handling materially matters
   - `../odoo-spreadsheets/SKILL.md` when workbook handling materially matters
7. Read the matching workflow in `../../workflows/`.
8. Read only the references needed for the stage, version, and domain.
9. Read `../../rules/security.md` and `../../rules/coding-style.md` for implementation planning, generation, review, and upgrade work.
10. Use helper prompts from `../../agents/` only when they materially improve the task.
11. Verify uncertain syntax against official Odoo docs or source.
12. Validate security, manifest order, version fit, and tests before finishing technical work.

## Flexibility rules

- Treat workflows as default playbooks, not rigid rails.
- If no workflow fits exactly, use the smallest matching skill set and preserve traceability where practical.
- Use canonical artifacts by default for formal delivery work.
- For narrow tasks, adapt the output to the request instead of forcing the full artifact chain.
- Keep `.docx` and spreadsheet handling attached to the active route when those file types are part of the input or output.
- When changing the pack itself, pair router/workflow edits with eval scenarios, eval log updates, and validators where practical.
- Keep hard constraints non-negotiable for version detection, security, manifest order, and technical validation.

## Stage routing

| Stage | Use when | Workflow | Helper |
|---|---|---|---|
| Full delivery loop | input is a detailed customer requirement and the user wants the full analyze -> design -> build -> QA/QC -> fix -> retest -> report cycle | `../../workflows/full-delivery-loop.md` | helper agents by stage |
| Presales discovery | input is raw business context, pain points, or unclear needs | `../../workflows/presales-discovery.md` | `../../agents/odoo-presales-consultant.md` |
| Fit-gap | requirements need classification before scope or estimate | `../../workflows/fit-gap.md` | `../../agents/odoo-presales-consultant.md` |
| Requirement analysis | detailed customer SOW, module list, function list, or requirement file needs normalization | `../../workflows/requirements-analysis.md` | `../../agents/odoo-presales-consultant.md` |
| Proposal and handoff | output is estimate, proposal, SOW, or design handoff | `../../workflows/proposal-handoff.md` | `../../agents/odoo-presales-consultant.md` |
| Functional Design | customer/team-facing Vietnamese FSD is needed | `../../workflows/functional-design.md` | `../../agents/odoo-presales-consultant.md` |
| Solution Design | customer/team-facing solution decision document is needed | `../../workflows/solution-design.md` | `../../agents/odoo-presales-consultant.md` |
| Technical Design | Functional Design and Solution Design are ready enough to feed `Technical Design.md` | `../../workflows/technical-design.md` | `../../agents/odoo-technical-planner.md` |
| Test Plan | Technical Design is ready enough to feed a detailed `Test Plan.md` with QA/QC coverage and status | `../../workflows/test-plan.md` | `../../agents/odoo-qa-qc.md` |
| Project Tracking | Technical Design or Test Plan is ready enough for phase/module/task tracking | `../../workflows/project-tracking.md` | none by default |
| Technical execution | code, review, tests, upgrade, OWL, security, integrations, or operations | matching technical workflow | matching helper prompt when useful |
| Skill maintenance | this pack needs correction or stronger guidance | `../../workflows/skill-maintenance.md` | none by default |

## Quick reference

| Domain | Skill | When to use |
|---|---|---|
| Version routing | `odoo-14.0` to `odoo-19.0` | Choose exact version before coding |
| Module scaffolding | `odoo-module-generation` | Manifest, file tree, scaffold, install order |
| ORM and model logic | `odoo-models` | Fields, domains, computes, inheritance, CRUD |
| Security | `odoo-security` | ACL, record rules, groups, multi-company |
| XML and reports | `odoo-views` | Views, QWeb, actions, menus, reports, wizards |
| OWL and frontend | `odoo-owl` | OWL components, assets, web client changes |
| Upgrade and migration | `odoo-upgrade` | Version deltas, migration references, troubleshooting |
| Testing and quality | `odoo-quality` | QA/QC planning, test generation, execution guidance, performance, and validation |
| Integrations | `odoo-integrations` | Controllers, import/export, APIs, website, attachments |
| Automation | `odoo-automation` | Cron jobs, sequences, mail, background flows |
| Business flows | `odoo-business-domains` | Sales, stock, accounting, HR, project, pricing patterns |
| Operations | `odoo-operations` | Settings, validation, debugging, error handling, i18n |
| Presales and handoff | `odoo-presales` | Discovery, fit-gap, estimation, proposal, implementation handoff |
| Document support | `odoo-documents` | DOCX requirement docs, Functional Design, Solution Design, export/review support |
| Spreadsheet support | `odoo-spreadsheets` | Requirement workbooks, fit-gap sheets, structured tabular handling |

## Router-only references

Keep `references/` under this skill for repository routing and skill-authoring material only.
Do not treat it as the main implementation knowledge base when a domain skill already exists.

For pack-maintenance work, the key router-level references are:

- `references/skill-pack-harness-guide.md`
- `references/eval-campaign-guide.md`
- `references/route-pressure-scenarios.md`

## Hard rules

- Do not skip presales routing when the input is business-facing, exploratory, commercial, or ambiguous.
- Never guess the Odoo version for code-facing or version-sensitive work when the manifest is missing or unclear.
- For Odoo 17+, use direct XML attributes such as `invisible="expr"` instead of `attrs`.
- For Odoo 16+, prefer `Command` for x2many operations.
- For Odoo 17+, use `@api.model_create_multi` for `create()`.
- For Odoo 18+, use `_check_company_auto = True`, `check_company=True`, keep record rules on `company_ids`, and use `allowed_company_ids` only for Python/context propagation when needed.
- Every model needs access rights in `security/ir.model.access.csv`.
