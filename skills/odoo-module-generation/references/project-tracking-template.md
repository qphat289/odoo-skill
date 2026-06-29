# Odoo Project Tracking Template

Use this template after `Technical Design.md` is coherent enough to break work into delivery tasks.

Suggested filename: `Project Tracking.md`

## Purpose

Track implementation work by phase, module, workstream, task, owner, dependency, and status. This is the execution tracker; do not put progress/status tracking inside `Technical Design.md`.

## Status model

| Status | Meaning |
|---|---|
| Backlog | captured but not ready |
| Ready | clear enough to start |
| In Progress | actively being worked |
| In Fix | failed behavior is being corrected |
| Blocked | waiting on decision, dependency, access, or input |
| In Review | implementation done and under review |
| Ready For Test | review passed or ready for QA |
| Testing | test execution or UAT in progress |
| Ready For Retest | fix is ready and waiting for retest |
| Done | accepted for the current scope |
| Deferred | intentionally moved out of current scope |

## Template

```markdown
# Project Tracking

## 1. Source Artifacts

| Artifact | Path / Version | Status | Notes |
|---|---|---|---|
| Requirement Analysis |  | Draft / Approved |  |
| Clarification Register |  | Draft / Approved |  |
| Fit/Gap Analysis |  | Draft / Approved |  |
| Functional Design |  | Draft / Approved |  |
| Solution Design |  | Draft / Approved |  |
| Technical Design |  | Draft / Approved |  |
| Test Plan |  | Not Started / Draft / Approved |  |

## 2. Phase Summary

| Phase | Goal | Scope | Entry Criteria | Exit Criteria | Status |
|---|---|---|---|---|---|

## 3. Module / Workstream Summary

| Module / Area | Owner | Scope Summary | Key Dependencies | Status |
|---|---|---|---|---|

## 4. Task Breakdown

| Task ID | Phase | Module / Area | Part | Task | Description | Source Ref | Dependencies | Owner | Priority | Status | Acceptance / Done Criteria | Test Plan Ref | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T-001 | Phase 1 |  | Models |  |  | FD-x / SD-x / TD-x |  |  | High / Medium / Low | Backlog |  | TP-x |  |

## 5. Blockers And Decisions

| ID | Related Task | Blocker / Decision | Impact | Owner | Due / Review Date | Status |
|---|---|---|---|---|---|---|

## 6. Review And Test Queue

| Task ID | Review Needed | Test Needed | Reviewer / Tester | Status | Notes |
|---|---|---|---|---|---|

## 7. Change Notes

| Date | Change | Reason | Impacted Tasks |
|---|---|---|---|
```

## Breakdown rules

1. Break tasks down by phase, module/area, and part such as models, security, views, reports, integration, data, tests, or deployment.
2. Keep each task small enough to be assigned and verified.
3. Link each task to Requirement Analysis, Fit-Gap, Functional Design, Solution Design, Technical Design, or Test Plan references as appropriate.
4. Do not use vague tasks such as "build module"; split into specific implementation, review, and testable units.
5. Keep deferred scope visible but separate.
6. Update status only from evidence: code done, review done, tests run, or customer acceptance.
7. When a task is verified through formal test cases, cite the `Test Plan.md` case IDs in `Test Plan Ref`.
8. When test status changes materially, keep linked tasks in sync with `Test Plan.md`.

## Suggested part labels

- Models
- Security
- Views
- Reports
- Wizard
- Automation
- Integration
- Data Migration
- Configuration
- Tests
- Review
- Deployment
- Documentation
