# WORKFLOW: Project Tracking

## Purpose

Guide the agent through creating or updating `Project Tracking.md` as the delivery task tracker after Technical Design, and after Test Plan when detailed QA/QC scope already exists.

## When to use

Use this workflow when the user wants backlog, task breakdown, implementation tracking, phase tracking, defect-fix-retest visibility, or delivery status by module/phase/task.

## Inputs

- `Requirement Analysis.md` and `Fit-Gap Analysis.xlsx` when deep traceability is needed
- `Technical Design.md`
- `Test Plan.md` when available
- Functional Design and Solution Design references when available
- target Odoo version if implementation work is version-sensitive
- module or workstream list
- optional owner, phase, priority, or due-date information

## Required reads

- `skills/odoo-module-generation/references/project-tracking-template.md`
- `skills/odoo-module-generation/references/odoo-module-checklist.md`
- `skills/odoo-quality/references/common-bug-patterns.md`

## Optional reads

- `skills/odoo-module-generation/references/technical-design-template.md`
- `skills/odoo-module-generation/references/project-tracking-example-sale-approval.md` when a realistic sample would help shape the tracker
- `workflows/technical-design.md`
- `workflows/test-plan.md` when test planning is already defined
- `workflows/generate-tests.md` when test tasks need to be linked
- `workflows/review-module.md` when review tasks need to be linked
- matching domain references for specialized workstreams

## Steps

1. Confirm Technical Design is specific enough to break into tasks.
2. Identify phases, modules, workstreams, and implementation parts.
3. Split work into specific tasks with source references and acceptance criteria.
4. Add dependencies and blockers instead of hiding them in notes.
5. Add review and test queue rows for work that needs QA/QC or code review.
6. Reflect the execution loop when applicable:
   - implementation in progress
   - ready for test
   - testing
   - failed behavior in fix
   - ready for retest
   - done
7. Link Test Plan case IDs when the plan exists; use placeholders only when Test Plan work is intentionally deferred.
8. Preserve requirement-analysis IDs or fit-gap IDs in source references when they materially improve tracking traceability.
9. Produce or update `Project Tracking.md`.

## Outputs

- `Project Tracking.md`
- short blocker/status summary if useful

## Validation gates

- every task is specific enough to assign
- every task has a source reference or reason
- statuses follow the status model
- review/test work is visible
- defect/fix/retest transitions are visible when testing is in scope
- test-linked work cites `Test Plan.md` when available
- progress tracking is not mixed into `Technical Design.md`
