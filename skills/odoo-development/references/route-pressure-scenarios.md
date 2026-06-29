# Route Pressure Scenarios

Use this file when testing whether the Odoo skill pack routes flexibly enough under pressure without losing important guardrails.

For machine-checkable coverage, keep this file aligned with `../../../evals/routing-workflow-evals.json`.

## How to use

For each scenario:

1. predict the expected route
2. check whether the agent over-forces a larger workflow
3. check whether the agent skips a necessary guardrail
4. if it fails, patch the router, workflow, agent, or validator

## Scenarios

| ID | Scenario | Expected route | Must not do | Success signal |
|---|---|---|---|---|
| RP-001 | user gives a detailed customer requirement and explicitly wants end-to-end delivery | `workflows/full-delivery-loop.md` | skip presales or QA/QC stages | full chain selected with artifacts and loops |
| RP-002 | user asks to fix an existing Odoo module bug only | smallest technical workflow, usually `generate-module.md` or direct code/test path | force requirement analysis, FSD, solution design, or full loop | task stays narrow and version-aware |
| RP-003 | user asks to review one existing `Technical Design.md` and suggest gaps | `workflows/technical-design.md` in review/update mode | restart the whole artifact chain | design is reviewed with traceability preserved |
| RP-004 | user asks to generate only test code from an existing approved `Test Plan.md` | `workflows/generate-tests.md` plus quality references | regenerate presales or project tracking by default | test-code output maps back to TP IDs |
| RP-005 | user asks for project status update after a test run | `workflows/project-tracking.md` and possibly `workflows/test-plan.md` | create a new technical design | status and linked TP rows stay synchronized |
| RP-006 | user gives business pain points without a clear requirement document | `workflows/presales-discovery.md` | jump into code or technical design | clarification framing and scope shaping appear first |
| RP-007 | user gives a competitor analysis file plus customer requirements and wants Odoo fit-gap positioning | closest presales route, usually requirements analysis plus fit-gap | force full delivery chain | comparative output preserves source traceability without overbuilding artifacts |
| RP-008 | user asks only whether one feature is fit or gap in Odoo | `workflows/fit-gap.md` in lightweight mode | force XLSX or full presales pack when not needed | answer stays concise but traceable |
| RP-009 | user asks for a customer-facing FSD from approved fit-gap and requirements | `workflows/functional-design.md` | jump to technical design | business-readable FSD produced |
| RP-010 | user asks to maintain or improve the skill pack itself after wrong routing happened | `workflows/skill-maintenance.md` plus harness guide | patch files without updating pressure scenarios or validators | loophole is captured and harness layer updated |
| RP-011 | user asks to convert or deliver a design or QA artifact as customer-facing `.docx` | keep the nearest business or quality workflow and add DOCX capability only for the artifact step | treat DOCX as plain text or ignore visual QA | correct primary workflow stays intact and DOCX handling is explicit |
| RP-012 | user gives a requirement workbook and wants analysis without losing sheet or row traceability | requirements-analysis or closest presales route plus spreadsheet capability | flatten workbook context into vague notes | workbook structure is preserved where it matters |
| RP-013 | user wants the full plan -> code -> test -> fix -> retest -> report loop and status synchronization | `workflows/full-delivery-loop.md` with test and tracking loops | stop after first failed test or skip artifact status updates | defect loop closes and `Test Plan` / `Project Tracking` stay synchronized |

## Typical rationalizations to catch

- "the full loop is safer, so I'll do everything"
- "the workflow mentions this artifact, so I must create it"
- "the task is technical enough, I can skip presales"
- "the task is narrow, so I can skip traceability entirely"
- "the task is only planning, so status-sync rules do not matter"
- "this is just a DOCX/XLSX operation, so I do not need the real workflow"

## Expected maintenance reaction

If one of these rationalizations appears:

- update the closest router or workflow wording
- add or tighten a validator if possible
- record the loophole in `docs/CORRECTIONS_LOG.md`
