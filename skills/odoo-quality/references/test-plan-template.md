# Odoo Test Plan Template

Use this template when `Technical Design.md` is stable enough to produce a real `Test Plan.md`.

Suggested filename: `Test Plan.md`

## Purpose

Describe how the solution will be validated across module behavior, function/method logic, role/security rules, integration, regression scope, automation coverage, defect handling, and execution status. This is the QA/QC planning artifact; do not collapse it into `Technical Design.md` or `Project Tracking.md`.

## Document status model

| Status | Meaning |
|---|---|
| Draft | initial planning in progress |
| In Review | QA lead, dev lead, or PM is reviewing the plan |
| Approved | ready to drive test generation or execution |
| In Execution | cases are actively being executed |
| Completed | planned scope executed for the current phase |
| Blocked | execution cannot continue because of environment, dependency, or unresolved design issues |

## Test case status model

| Status | Meaning |
|---|---|
| Backlog | known case, not yet designed in detail |
| Designed | objective and expected result are defined |
| Ready | data and dependencies are clear enough to execute or automate |
| In Progress | being automated or executed |
| In Fix | failed or missing behavior is being corrected |
| Blocked | waiting on env, fix, access, or decision |
| Passed | executed successfully |
| Failed | executed and did not meet expectation |
| Ready For Retest | fix is available and awaiting rerun |
| Retest | fix exists and the case must be rerun |
| Waived | intentionally skipped with approval |
| Deferred | moved out of the current phase or release |

## Template

```markdown
# Test Plan

## 1. Source Artifacts

| Artifact | Path / Version | Status | Notes |
|---|---|---|---|
| Requirement Analysis |  | Draft / Approved |  |
| Clarification Register |  | Draft / Approved |  |
| Fit/Gap Analysis |  | Draft / Approved |  |
| Functional Design |  | Draft / Approved |  |
| Solution Design |  | Draft / Approved |  |
| Technical Design |  | Draft / Approved |  |
| Project Tracking |  | Draft / In Use |  |

## 2. QA/QC Strategy Summary

- Target Odoo version:
- Target module(s):
- Test Plan status:
- In-scope business flows:
- In-scope integrations:
- In-scope security / roles:
- Out of scope for this phase:
- Test environments:
- Test data strategy:
- Automation target summary:
- Key risks:
- Artifact sync rule:
  - whenever a test status changes materially, update linked rows in `Project Tracking.md`
- Reporting rule:
  - update `Test Plan.md` and `Project Tracking.md` after each meaningful execution cycle

## 3. Coverage Matrix

| Module / Area | Business Flow | Logic | Security | Integration | UI / Report | Regression | Owner | Status |
|---|---|---|---|---|---|---|---|---|

## 4. Detailed Test Cases

| TP ID | Module / Area | Layer | Scenario | Objective | Preconditions / Test Data | Steps Summary | Expected Result | Automation Target | Priority | Owner | Status | Source Ref | Tracking Ref | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TP-001 | Sales | Workflow | Confirm quotation | Validate normal confirmation flow | Demo customer, valid lines, salesperson user | Create quotation -> confirm | State changes correctly, downstream docs created, log/audit behavior correct | Automated | High |  | Ready | FD-xx / SD-xx / TD-xx | T-xxx |  |

Layer examples:
- Unit
- Function / Method
- Workflow
- Security
- Integration
- UI
- Report
- Data Migration
- Performance
- Regression
- UAT

Automation Target values:
- Automated
- Manual
- Mixed
- Future Automation

## 5. Automation Code Coverage Map

| TP ID | Planned Test Code File | Test Class / Method | Framework / Base Class | Status | Notes |
|---|---|---|---|---|---|

## 6. Security And Access Coverage

| TP ID | Role / Group | Operation | Expected Access Result | Multi-company / Record Rule Notes | Status |
|---|---|---|---|---|---|

## 7. Integration And Interface Coverage

| TP ID | System / Interface | Direction | Trigger | Expected Payload / Behavior | Error / Retry Expectation | Status |
|---|---|---|---|---|---|---|

## 8. Regression Scope

| Area | Why Sensitive | Core Existing Flow | Regression Focus | Owner | Status |
|---|---|---|---|---|---|

## 9. Defect And Retest Loop

| TP ID | Defect / Gap | Root Cause Hypothesis | Fix Owner | Fix Status | Retest Status | Notes |
|---|---|---|---|---|---|---|

Fix Status examples:
- Open
- In Fix
- Ready For Retest
- Closed

Reopen rule:
- if a previously passed scenario fails after regression, reopen the same TP ID and update both `Test Plan.md` and `Project Tracking.md`

## 10. Execution Status Summary

| TP ID | Last Run / Review Date | Result | Evidence / Defect Ref | Next Action | Status |
|---|---|---|---|---|---|

## 11. Open Risks And Blockers

| ID | Related TP ID / Area | Risk / Blocker | Impact | Owner | Target Resolution Date | Status |
|---|---|---|---|---|---|---|

## 12. Exit Criteria

- [ ] Critical business flows passed
- [ ] Security-sensitive cases passed or explicitly waived
- [ ] Integration failure/retry paths covered
- [ ] Regression-sensitive existing flows covered
- [ ] Failed cases have owner and next action
- [ ] Bug/fix/retest loop is reflected in Test Plan and Project Tracking
- [ ] Final status is consistent with Project Tracking
```

## Planning rules

1. Break coverage down by real modules, workflows, functions/methods, and risk areas, not generic "functional test" buckets.
2. Cover business logic, security, integration, error handling, reporting, and regression where they materially apply.
3. Keep every test case traceable to Functional Design, Solution Design, Technical Design, or Project Tracking items.
4. Distinguish planned coverage from executed results; use the status model consistently.
5. Mark missing environments, data, or decisions as blockers instead of pretending the case is ready.
6. When a case should become automated test code, map it into the automation coverage section explicitly.
7. Track defects and retest loops in the dedicated section instead of hiding them in notes.
8. Use `Test Plan.md` for detailed QA/QC status; use `Project Tracking.md` for delivery-level status.
