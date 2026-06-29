# WORKFLOW: Full Delivery Loop

## Purpose

Guide the agent through the full customer-requirement-to-delivery loop: analyze, design, implement, generate tests, execute tests, debug/fix, retest, and report status until the scoped work is complete.

## When to use

Use this workflow only when the input is a detailed customer requirement or requirement set and the user wants the end-to-end delivery loop, not just one isolated step such as planning only, review only, test only, or fix only.

This is a large-loop playbook, not a mandatory starting point for every task.

## Inputs

- customer requirement document, SOW, or structured requirement set
- target Odoo version if known
- target modules, business areas, or functions
- optional environment or delivery constraints

## Required reads

- `SKILL.md`
- `skills/odoo-development/SKILL.md`
- `workflows/requirements-analysis.md`
- `workflows/fit-gap.md`
- `workflows/functional-design.md`
- `workflows/solution-design.md`
- `workflows/technical-design.md`
- `workflows/test-plan.md`
- `workflows/project-tracking.md`
- `workflows/generate-module.md`
- `workflows/generate-tests.md`
- `workflows/test-module.md`
- `rules/security.md`
- `rules/coding-style.md`

## Optional reads

- `workflows/review-module.md`
- `workflows/security-module.md`
- `agents/odoo-presales-consultant.md`
- `agents/odoo-technical-planner.md`
- `agents/odoo-qa-qc.md`
- `agents/odoo-tester.md`
- matching domain skills and version skills as each stage requires

## Steps

1. Analyze the customer input with `Requirement Analysis.md`, resolve the needed rows in `Clarification Register.xlsx`, and only then finalize `Fit-Gap Analysis.xlsx`.
   - if equivalent upstream artifacts already exist and are trustworthy, reuse them instead of recreating them
2. Produce or confirm `Functional Design.docx` and `Solution Design.docx` when the requirement needs business-facing design artifacts.
3. Produce `Technical Design.md`.
4. Produce `Test Plan.md` with QA/QC coverage, automation mapping, and defect/retest tracking.
5. Produce `Project Tracking.md` with implementation, review, test, and status breakdown.
6. Implement the scoped functionality.
7. Generate automated test code where the Test Plan marks cases as automated or mixed.
8. Execute tests and collect evidence.
9. If bugs, gaps, or missing behavior are found:
   - update `Test Plan.md`
   - update `Project Tracking.md`
   - debug or fix the code
   - rerun the affected tests
   - repeat until the in-scope cases are complete or a real blocker remains
10. Keep the loop evidence-based:
   - do not mark done before relevant tests pass or are explicitly waived
   - do not keep failure information only in chat
11. Finish with:
   - updated `Test Plan.md`
   - updated `Project Tracking.md`
   - delivery summary

## Outputs

- end-to-end delivery artifact chain
- implementation and test evidence
- final QA/QC and delivery status reflected in `Test Plan.md` and `Project Tracking.md`

## Validation gates

- this workflow is used only for true end-to-end requests
- requirement traceability survives from customer input through code and test
- implementation and test status stay synchronized
- defect/fix/retest loops are reflected in the artifacts
- final reporting lives in `Test Plan.md` and `Project Tracking.md`, not chat alone
