# Example Test Plan: Sale Approval, CRM Handoff, and API Sync

Use this file as a realistic reference when drafting a full `Test Plan.md`. It shows how to cover module behavior, function/method logic, integration, security, regression, automation mapping, defect handling, and status tracking in one coherent artifact.

The scenario below is illustrative but grounded in common Odoo 18 custom-delivery patterns.

## Scenario summary

- Target Odoo version: `18.0`
- Business area: Sales, CRM, Approval, Customer sync
- Custom modules:
  - `x_sale_approval`
  - `x_crm_sale_bridge`
  - `x_sale_sync_api`
- Standard dependencies:
  - `sale`
  - `sale_management`
  - `crm`
  - `mail`
- Core custom behaviors:
  - quotation above approval threshold must enter `pending_approval`
  - sales manager approves and confirmation resumes
  - credit limit and margin rules must be enforced server-side
  - approved quotation can be pushed to an external order-sync API
  - CRM opportunity qualification data must flow into quotation defaults

## Example artifact

```markdown
# Test Plan

## 1. Source Artifacts

| Artifact | Path / Version | Status | Notes |
|---|---|---|---|
| Requirement Analysis | `docs/analysis/Requirement Analysis.md` | Approved | requirement rows normalized and phase boundaries confirmed |
| Clarification Register | `docs/analysis/Clarification Register.xlsx` | Approved | business clarifications resolved before fit-gap and design lock |
| Fit/Gap Analysis | `docs/analysis/Fit-Gap.xlsx` | Approved | approval, CRM bridge, and API sync classified |
| Functional Design | `docs/design/Functional Design.docx` | Approved | Customer sign-off completed |
| Solution Design | `docs/design/Solution Design.docx` | Approved | Integration and approval approach confirmed |
| Technical Design | `docs/design/Technical Design.md` | Approved | Build-ready |
| Project Tracking | `docs/tracking/Project Tracking.md` | In Use | Task IDs T-001 to T-024 |

## 2. QA/QC Strategy Summary

- Target Odoo version: `18.0`
- Target module(s): `x_sale_approval`, `x_crm_sale_bridge`, `x_sale_sync_api`
- Test Plan status: `In Execution`
- In-scope business flows:
  - opportunity to quotation
  - quotation approval
  - confirmation after approval
  - outbound sync to external API
- In-scope integrations:
  - outbound REST sync for approved sale order
  - email notification for approval request
- In-scope security / roles:
  - salesperson
  - sales manager
  - integration service user
- Out of scope for this phase:
  - invoice posting
  - stock picking customization
- Test environments:
  - DEV for automated tests
  - SIT for integration and manual verification
  - UAT for business validation
- Test data strategy:
  - one company baseline
  - one secondary company for multi-company checks
  - customer under credit limit
  - customer over credit limit
  - product with normal margin
  - product with low margin
- Automation target summary:
  - server-side logic: automated
  - controller/API sync: automated + SIT verification
  - manager approval UI visibility: mixed
  - customer-facing UAT flow: manual
- Key risks:
  - approval bypass through direct server call
  - margin computation mismatch after line update
  - integration retry duplicates
  - multi-company visibility leak
- Artifact sync rule:
  - whenever TP status changes because of execution, fix, or retest, update linked tracking tasks in `Project Tracking.md`
- Reporting rule:
  - update `Test Plan.md` and `Project Tracking.md` after each meaningful execution cycle

## 3. Coverage Matrix

| Module / Area | Business Flow | Logic | Security | Integration | UI / Report | Regression | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| `x_sale_approval` | quotation approval | threshold, margin, credit rules | manager-only approval | approval email | quotation form buttons | sale confirm flow | QA lead | Testing |
| `x_crm_sale_bridge` | opportunity to quotation | default mapping, qualification sync | salesperson access | none | CRM to quotation action | CRM lead flow | QA lead | Ready |
| `x_sale_sync_api` | approved order sync | payload builder, retry, idempotency | service user isolation | outbound REST | sync status smart button | order update after sync | QA lead | Testing |

## 4. Detailed Test Cases

| TP ID | Module / Area | Layer | Scenario | Objective | Preconditions / Test Data | Steps Summary | Expected Result | Automation Target | Priority | Owner | Status | Source Ref | Tracking Ref | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TP-001 | `x_sale_approval` | Workflow | Confirm quotation under threshold | Verify normal confirmation path is unchanged | quotation total below approval limit | create quotation -> confirm | state becomes `sale`, no approval state used | Automated | High | QA | Passed | FD-2.1 / SD-3.2 / TD-6.1 | T-007 | covered by test `test_confirm_under_threshold` |
| TP-002 | `x_sale_approval` | Workflow | Confirm quotation over threshold | Verify approval gate is enforced | quotation total above approval limit | create quotation -> confirm | state becomes `pending_approval`, confirmation is not completed | Automated | High | QA | Passed | FD-2.1 / SD-3.2 / TD-6.1 | T-007 | server-side must enforce |
| TP-003 | `x_sale_approval` | Function / Method | `action_approve()` resumes confirmation | Verify manager approval continues standard flow | order in `pending_approval`, manager user | approve order | approver fields set, order confirmed once | Automated | High | QA | Ready For Retest | FD-2.1 / SD-3.2 / TD-6.2 | T-008 | duplicate confirm found in prior run |
| TP-004 | `x_sale_approval` | Function / Method | `_compute_requires_approval()` after line update | Verify threshold recalculates when line values change | draft quotation with editable lines | add line / edit price / recompute | approval flag reflects latest total | Automated | High | QA | Failed | FD-2.1 / TD-5.4 | T-007 | stale compute after onchange suspected |
| TP-005 | `x_sale_approval` | Security | Salesperson cannot approve | Prevent approval by unauthorized user | order in `pending_approval`, salesperson user | call button and direct method | `AccessError` or guarded `UserError`, no state change | Automated | Critical | QA | Passed | FD-4.3 / SD-5.1 / TD-8.2 | T-010 | verify both UI and direct call |
| TP-006 | `x_sale_approval` | Function / Method | Credit limit block on confirm | Verify credit limit rule is enforced server-side | partner over credit limit | confirm quotation | confirm blocked with clear error | Automated | High | QA | Passed | FD-2.4 / TD-6.4 | T-009 | |
| TP-007 | `x_sale_approval` | Function / Method | Margin floor validation | Verify low margin line requires approval or blocks as designed | one low-margin product line | save or confirm quotation | expected approval/block behavior occurs | Automated | High | QA | In Progress | FD-2.5 / TD-6.5 | T-009 | |
| TP-008 | `x_crm_sale_bridge` | Workflow | Opportunity creates quotation with mapped defaults | Verify CRM bridge maps approved fields correctly | qualified opportunity with budget, timeline, notes | create quotation from opportunity | quotation partner, notes, tags, and reference fields copied correctly | Automated | High | QA | Designed | FD-3.1 / TD-6.8 | T-012 | |
| TP-009 | `x_crm_sale_bridge` | Function / Method | Qualification status filter | Verify only allowed lead statuses can create quotation | lead in non-qualified status | trigger create quotation action | action blocked with business message | Automated | Medium | QA | Designed | FD-3.1 / TD-6.8 | T-012 | |
| TP-010 | `x_sale_sync_api` | Integration | Push approved order to API | Verify happy-path outbound sync | approved order, API mock returns 200 | trigger sync | sync log created, external ID stored, status updated | Automated | Critical | QA | Passed | SD-4.2 / TD-9.2 | T-015 | mock + SIT evidence |
| TP-011 | `x_sale_sync_api` | Integration | Retry on temporary API failure | Verify retry path does not create duplicate outbound state | API mock returns 500 then 200 | trigger sync twice or scheduler retry | one final success, no duplicate external record, retry count increments | Automated | Critical | QA | Failed | SD-4.2 / TD-9.4 | T-016 | duplicate payload risk |
| TP-012 | `x_sale_sync_api` | Security | Service user isolation | Verify normal sales users cannot use admin sync action or see technical tokens | salesperson user | open sync view / invoke route | access denied or protected fields hidden | Automated | High | QA | Passed | SD-4.4 / TD-8.5 / TD-9.1 | T-017 | |
| TP-013 | `x_sale_sync_api` | Function / Method | Payload builder omits forbidden fields | Verify API payload structure and redaction | approved order with internal notes | build payload | payload includes required fields only, excludes internal-only data | Automated | High | QA | Passed | SD-4.3 / TD-9.3 | T-015 | |
| TP-014 | `x_sale_approval` | UI | Approve button visibility | Verify button visible only for managers in `pending_approval` | one manager, one salesperson, order in each state | open quotation form | button visibility matches role and state | Mixed | Medium | QA | Testing | FD-4.3 / TD-7.2 / TD-8.2 | T-010 | manual UI check plus XML assertion |
| TP-015 | Cross-module | Regression | Existing standard sale confirmation remains stable | Protect standard order flow not using custom approval | plain order, no special CRM or sync data | confirm standard quotation | base sale flow still works | Automated | Critical | QA | Passed | TD-13 / regression scope | T-020 | |
| TP-016 | Cross-module | UAT | Manager approval and sync end-to-end | Verify business users can complete the designed flow | SIT/UAT env, manager and salesperson users | create opportunity -> quotation -> approval -> sync | flow completes with expected audit and status updates | Manual | High | QA / Key User | Ready | FD-2 / FD-3 / SD-4 | T-021 | |

## 5. Automation Code Coverage Map

| TP ID | Planned Test Code File | Test Class / Method | Framework / Base Class | Status | Notes |
|---|---|---|---|---|---|
| TP-001 | `x_sale_approval/tests/test_sale_approval.py` | `TestSaleApproval.test_confirm_under_threshold` | `TransactionCase` | Done | |
| TP-002 | `x_sale_approval/tests/test_sale_approval.py` | `TestSaleApproval.test_confirm_over_threshold_sets_pending` | `TransactionCase` | Done | |
| TP-003 | `x_sale_approval/tests/test_sale_approval.py` | `TestSaleApproval.test_action_approve_confirms_once` | `TransactionCase` | In Fix | duplicate confirmation bug found |
| TP-004 | `x_sale_approval/tests/test_sale_approval_compute.py` | `TestSaleApprovalCompute.test_requires_approval_recompute_after_line_change` | `Form` + `TransactionCase` | In Fix | onchange + compute interaction |
| TP-005 | `x_sale_approval/tests/test_sale_approval_security.py` | `TestSaleApprovalSecurity.test_salesperson_cannot_approve` | `TransactionCase` | Done | |
| TP-010 | `x_sale_sync_api/tests/test_sync_api.py` | `TestSaleSyncApi.test_push_order_success` | `TransactionCase` + patcher | Done | |
| TP-011 | `x_sale_sync_api/tests/test_sync_api_retry.py` | `TestSaleSyncApiRetry.test_retry_is_idempotent` | `TransactionCase` + patcher | In Fix | idempotency gap |
| TP-014 | `x_sale_approval/tests/test_sale_form_view.py` | `TestSaleApprovalView.test_approve_button_visibility` | `TransactionCase` | Planned | supplement with manual UI proof |
| TP-015 | `x_sale_approval/tests/test_regression_sale_flow.py` | `TestSaleApprovalRegression.test_standard_sale_confirm_unchanged` | `TransactionCase` | Done | |

## 6. Security And Access Coverage

| TP ID | Role / Group | Operation | Expected Access Result | Multi-company / Record Rule Notes | Status |
|---|---|---|---|---|---|
| TP-005 | Salesperson | approve quotation | denied | no manager group, no bypass through direct method | Passed |
| TP-012 | Salesperson | trigger technical sync | denied | service-only fields/actions hidden | Passed |
| TP-014 | Sales Manager | approve quotation | allowed only in `pending_approval` | same-company only | Testing |
| TP-017 | Secondary-company salesperson | search quotations from main company | denied | record rules and company isolation respected | Designed |

## 7. Integration And Interface Coverage

| TP ID | System / Interface | Direction | Trigger | Expected Payload / Behavior | Error / Retry Expectation | Status |
|---|---|---|---|---|---|---|
| TP-010 | External order API | outbound | manual sync action | order header, lines, customer ref, approved metadata | success marks synced | Passed |
| TP-011 | External order API | outbound | scheduler retry | same logical order must not duplicate remote record | 500 retried, duplicate prevented | Failed |
| TP-018 | Mail template | outbound | approval request creation | manager receives notification with order info | failure logged and visible | Designed |

## 8. Regression Scope

| Area | Why Sensitive | Core Existing Flow | Regression Focus | Owner | Status |
|---|---|---|---|---|---|
| Standard sale confirm | custom override of `action_confirm()` | quotation -> sale order | avoid blocking normal orders | QA | Passed |
| CRM opportunity conversion | bridge adds default mapping | lead -> opportunity -> quotation | no broken default mapping | QA | Designed |
| Sale sync retry | scheduler / manual retry overlap | approved order sync | no duplicate outbound record | QA | Failed |

## 9. Defect And Retest Loop

| TP ID | Defect / Gap | Root Cause Hypothesis | Fix Owner | Fix Status | Retest Status | Notes |
|---|---|---|---|---|---|---|
| TP-003 | approval resumes confirmation twice | custom `action_approve()` and inherited confirm both trigger downstream action | Dev A | In Fix | Pending | retest after patch on `action_approve()` |
| TP-004 | approval flag stale after line amount change | missing depends or onchange refresh path | Dev A | In Fix | Pending | retest with `Form` scenario |
| TP-011 | duplicate sync on retry | idempotency key not persisted before retry cycle | Dev B | Ready For Retest | Pending | rerun automated retry test and SIT sync |

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
| TP-001 | 2026-06-25 | Pass | automated suite run `sale_approval_green_01` | keep in regression pack | Passed |
| TP-003 | 2026-06-25 | Fail | defect `BUG-014` | patch approval resume logic, rerun | In Fix |
| TP-004 | 2026-06-25 | Fail | defect `BUG-015` | patch recompute logic, rerun with `Form` flow | In Fix |
| TP-010 | 2026-06-25 | Pass | mock API log + SIT screenshot | include in release evidence | Passed |
| TP-011 | 2026-06-25 | Fail | defect `BUG-016` | rerun after idempotency fix | Ready For Retest |
| TP-014 | 2026-06-25 | Partial | XML inspection done, manual UI pending | run manager/salesperson UI pass in SIT | Testing |

## 11. Open Risks And Blockers

| ID | Related TP ID / Area | Risk / Blocker | Impact | Owner | Target Resolution Date | Status |
|---|---|---|---|---|---|---|
| R-001 | TP-011 | external sandbox sometimes delays duplicate-check response | integration retest may be noisy | Integration lead | 2026-06-27 | Open |
| R-002 | TP-016 | UAT users not yet available for approval scenario | business sign-off delayed | PM | 2026-06-28 | Blocked |

## 12. Exit Criteria

- [ ] Critical business flows passed
- [ ] Security-sensitive cases passed or explicitly waived
- [ ] Integration failure/retry paths covered
- [ ] Regression-sensitive existing flows covered
- [ ] Failed cases have owner and next action
- [ ] Bug/fix/retest loop is reflected in Test Plan and Project Tracking
- [ ] Final status is consistent with Project Tracking
```

## Why this example is useful

1. It separates module flow coverage from function/method coverage.
2. It shows how to map test-plan cases into actual Odoo test files and test classes.
3. It treats failures as part of the artifact, not as a chat-only side note.
4. It keeps the upstream requirement-analysis and fit-gap chain visible instead of starting traceability only at technical design.
5. It keeps UAT, automated tests, and integration verification in one place without mixing them up.
6. It demonstrates how `Test Plan.md` and `Project Tracking.md` can work together during retest loops.
