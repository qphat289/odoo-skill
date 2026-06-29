# WORKFLOW: Test Plan

## Purpose

Guide the agent through creating or updating `Test Plan.md` as the detailed QA/QC planning and execution-tracking artifact after `Technical Design.md`.

## When to use

Use this workflow when the user needs a real test plan with module-by-module, workflow, function/method logic, integration, security, regression, automation, defect/retest, and status coverage rather than only test execution or scattered test notes.

## Inputs

- `Requirement Analysis.md` and `Fit-Gap Analysis.xlsx` when deep traceability is needed
- `Technical Design.md`
- `Functional Design.docx` and `Solution Design.docx` when traceability is needed
- target Odoo version
- target modules, integrations, and business flows
- optional `Project Tracking.md`

## Required reads

- `skills/odoo-quality/SKILL.md`
- `skills/odoo-quality/references/test-plan-template.md`
- `skills/odoo-quality/references/odoo-test-patterns.md`
- `skills/odoo-quality/references/test-tooling-patterns.md`
- `rules/security.md`

## Optional reads

- `agents/odoo-qa-qc.md`
- matching version skill
- `skills/odoo-quality/references/common-bug-patterns.md`
- `skills/odoo-quality/references/test-plan-example-sale-approval.md` when a realistic sample would help shape the artifact
- `workflows/technical-design.md`
- `workflows/project-tracking.md`
- `workflows/generate-tests.md`
- `workflows/test-module.md`
- matching domain skills when the business flow is specialized

## Steps

1. Confirm `Technical Design.md` is detailed enough to derive concrete test coverage.
2. Load the test-plan template and relevant Odoo test references.
3. Break coverage down by module, business flow, technical layer, and risk area.
4. Define case IDs, objectives, preconditions, expected results, automation target, and status for each meaningful scenario.
5. Make security, integration, multi-company, role-based access, and regression coverage explicit when they matter.
6. Make logic coverage explicit down to the needed technical level such as compute methods, constraints, onchange behavior, CRUD overrides, state transitions, cron jobs, and controller/service functions.
7. Define the execution loop for each relevant case or group of cases:
   - implement or generate test code
   - execute
   - capture failures, bugs, or missing behavior
   - fix/debug
   - retest
   - update status and evidence
8. Link each test scenario back to Functional Design, Solution Design, Technical Design, and `Project Tracking.md` when available.
9. Preserve requirement-analysis IDs or fit-gap IDs too when they materially improve traceability.
10. Produce or update `Test Plan.md`.
11. If the user later asks for a DOCX version of the test plan, treat that as a DOCX-related task and use document runtime capabilities for the conversion or editing pass.

## Outputs

- `Test Plan.md`
- short QA/QC risk summary when useful

## Validation gates

- coverage is broken down by real modules and workflows, not vague test buckets
- business logic, integration, security, and regression paths are visible
- each test case has a clear expected result and status
- defect/retest flow is explicit where meaningful
- test status is not mixed into `Technical Design.md`
- traceability back to source artifacts is preserved
