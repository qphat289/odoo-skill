# Example Project Tracking: Sale Approval, CRM Handoff, and API Sync

Use this file as a realistic reference when drafting a full `Project Tracking.md`. It is paired with:

- `skills/odoo-quality/references/test-plan-example-sale-approval.md`

The goal is to show how delivery tasks, review, testing, defect fixing, retest, and final reporting can stay synchronized with `Test Plan.md`.

## Scenario summary

- Target Odoo version: `18.0`
- Business area: Sales, CRM, Approval, Customer sync
- Custom modules:
  - `x_sale_approval`
  - `x_crm_sale_bridge`
  - `x_sale_sync_api`
- Main delivery loop:
  - implement
  - review
  - test
  - bug or gap found
  - fix
  - retest
  - update status
  - close

## Example artifact

```markdown
# Project Tracking

## 1. Source Artifacts

| Artifact | Path / Version | Status | Notes |
|---|---|---|---|
| Requirement Analysis | `docs/analysis/Requirement Analysis.md` | Approved | normalized requirement rows and phase boundaries |
| Clarification Register | `docs/analysis/Clarification Register.xlsx` | Approved | clarification baseline locked before delivery planning |
| Fit/Gap Analysis | `docs/analysis/Fit-Gap.xlsx` | Approved | core gap decisions locked for phase 1 |
| Functional Design | `docs/design/Functional Design.docx` | Approved | business scope signed off |
| Solution Design | `docs/design/Solution Design.docx` | Approved | approval and API approach confirmed |
| Technical Design | `docs/design/Technical Design.md` | Approved | implementation baseline locked |
| Test Plan | `docs/qa/Test Plan.md` | In Execution | TP-001 to TP-018 in use |

## 2. Phase Summary

| Phase | Goal | Scope | Entry Criteria | Exit Criteria | Status |
|---|---|---|---|---|---|
| Phase 1 | Approval core build | `x_sale_approval` models, workflow, security, UI | Technical Design approved | approval flow implemented, reviewed, and critical tests green | In Fix |
| Phase 2 | CRM bridge | `x_crm_sale_bridge` mapping and opportunity handoff | Phase 1 stable enough for downstream build | opportunity mapping implemented and covered | In Progress |
| Phase 3 | API sync | `x_sale_sync_api` payload, sync log, retry flow | approval flow available for approved orders | sync success and retry/idempotency cases passed | Testing |
| Phase 4 | UAT and closure | end-to-end business verification | SIT stable and critical bugs resolved | UAT complete, evidence captured, final report updated | Ready |

## 3. Module / Workstream Summary

| Module / Area | Owner | Scope Summary | Key Dependencies | Status |
|---|---|---|---|---|
| `x_sale_approval` | Dev A | approval threshold, manager approval, credit and margin rules | `sale`, `mail`, security groups | In Fix |
| `x_crm_sale_bridge` | Dev C | opportunity-to-quotation mapping and qualification control | `crm`, `sale`, approval module defaults | In Progress |
| `x_sale_sync_api` | Dev B | outbound API sync, log, retry, idempotency | approved order state, controller patterns, API credentials | Ready For Retest |
| Cross-module QA/QC | QA lead | regression pack, UAT coordination, artifact updates | all modules, SIT env, key users | Testing |

## 4. Task Breakdown

| Task ID | Phase | Module / Area | Part | Task | Description | Source Ref | Dependencies | Owner | Priority | Status | Acceptance / Done Criteria | Test Plan Ref | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T-001 | Phase 1 | `x_sale_approval` | Models | Add approval fields and state | add approval status, approver, approval timestamp, threshold flags | FD-2.1 / TD-5.2 / TD-6.1 | none | Dev A | High | Done | fields stored, upgrade-safe, no broken base flow | TP-002, TP-003 | merged |
| T-002 | Phase 1 | `x_sale_approval` | Business Logic | Override confirm for approval gate | move high-value quotation into `pending_approval` | FD-2.1 / TD-6.1 | T-001 | Dev A | High | Done | above-threshold orders do not confirm directly | TP-002 | covered by automated test |
| T-003 | Phase 1 | `x_sale_approval` | Business Logic | Implement manager approve action | allow manager to approve and continue standard flow | FD-2.1 / TD-6.2 | T-001, T-002 | Dev A | High | In Fix | approval resumes confirm exactly once | TP-003 | duplicate downstream action bug |
| T-004 | Phase 1 | `x_sale_approval` | Business Logic | Recompute approval requirement on line change | keep threshold logic correct after edits | FD-2.1 / TD-5.4 | T-001 | Dev A | High | In Fix | approval flag updates after price and quantity changes | TP-004 | compute/onchange issue |
| T-005 | Phase 1 | `x_sale_approval` | Security | Add manager-only approval protection | enforce role checks in UI and server method | FD-4.3 / TD-8.2 | T-003 | Dev A | Critical | Done | salesperson cannot approve through button or direct call | TP-005, TP-014 | |
| T-006 | Phase 1 | `x_sale_approval` | Business Logic | Credit limit validation | block confirm when customer exceeds credit policy | FD-2.4 / TD-6.4 | T-002 | Dev A | High | Done | blocked with business message, no side effects | TP-006 | |
| T-007 | Phase 1 | `x_sale_approval` | Tests | Automated approval baseline tests | add tests for under/over threshold and recompute | TD-13 / QA plan | T-001, T-002, T-004 | QA + Dev A | High | In Fix | green automated tests for TP-001, TP-002, TP-004 | TP-001, TP-002, TP-004 | recompute test still red |
| T-008 | Phase 1 | `x_sale_approval` | Tests | Approval action test | add automated test for approve flow | TD-13 / QA plan | T-003 | QA + Dev A | High | Ready For Retest | TP-003 passes after fix | TP-003 | rerun pending |
| T-009 | Phase 1 | `x_sale_approval` | Review | Review approval rule set | review margin and credit paths | TD-6.4 / TD-6.5 / TD-8 | T-006, T-010 | Reviewer | High | In Review | no bypass, no obvious regression risk | TP-006, TP-007 | |
| T-010 | Phase 1 | `x_sale_approval` | Business Logic | Margin floor rule | enforce low-margin approval or block path | FD-2.5 / TD-6.5 | T-002 | Dev A | High | In Progress | expected low-margin behavior implemented and tested | TP-007 | |
| T-011 | Phase 2 | `x_crm_sale_bridge` | Business Logic | Opportunity default mapping | copy approved CRM fields into quotation defaults | FD-3.1 / TD-6.8 | T-001 | Dev C | High | In Progress | quotation contains mapped data correctly | TP-008 | |
| T-012 | Phase 2 | `x_crm_sale_bridge` | Business Logic | Qualification guard | restrict quotation creation to allowed lead statuses | FD-3.1 / TD-6.8 | T-011 | Dev C | Medium | Ready For Test | invalid lead statuses blocked with clear message | TP-009 | |
| T-013 | Phase 2 | `x_crm_sale_bridge` | Tests | CRM bridge tests | add automated tests for mapping and qualification | QA plan / TD-13 | T-011, T-012 | QA + Dev C | High | Ready | tests created and runnable | TP-008, TP-009 | |
| T-014 | Phase 3 | `x_sale_sync_api` | Integration | Build sync payload and log | construct outbound payload and persist sync log | SD-4.2 / TD-9.2 / TD-9.3 | T-002 | Dev B | Critical | Done | sync payload valid, log created, external ID stored on success | TP-010, TP-013 | |
| T-015 | Phase 3 | `x_sale_sync_api` | Integration | Happy-path API sync | push approved orders to external API | SD-4.2 / TD-9.2 | T-014 | Dev B | Critical | Done | approved order sync passes in mock and SIT | TP-010 | |
| T-016 | Phase 3 | `x_sale_sync_api` | Integration | Retry and idempotency logic | prevent duplicates across retry cycles | SD-4.2 / TD-9.4 | T-014 | Dev B | Critical | Ready For Retest | duplicate-safe retry behavior passes | TP-011 | defect `BUG-016` |
| T-017 | Phase 3 | `x_sale_sync_api` | Security | Service-user isolation | protect sync actions and technical fields | SD-4.4 / TD-8.5 / TD-9.1 | T-014 | Dev B | High | Done | sales users cannot access protected sync actions | TP-012 | |
| T-018 | Phase 3 | `x_sale_sync_api` | Tests | API sync automated tests | create success, payload, and retry tests | QA plan / TD-13 | T-014, T-016 | QA + Dev B | Critical | In Fix | TP-010 and TP-011 automation green | TP-010, TP-011, TP-013 | retry suite still failing |
| T-019 | Phase 1 | `x_sale_approval` | Views | Approve button and approval fields UI | manager-only button visibility and approval block | FD-4.3 / TD-7.2 / TD-8.2 | T-003, T-005 | Dev A | Medium | Testing | UI visibility verified in XML and SIT | TP-014 | manual check pending |
| T-020 | Phase 3 | Cross-module | Regression | Standard sale flow regression pack | protect base quotation confirm path | TD-13 / regression scope | T-002, T-014 | QA | Critical | Done | standard sale flow remains green | TP-015 | |
| T-021 | Phase 4 | Cross-module | UAT | Manager approval + sync end-to-end | execute business UAT across CRM, approval, and sync | FD-2 / FD-3 / SD-4 | T-003, T-011, T-016, T-019 | QA + PM + Key User | High | Ready | key users validate end-to-end scenario | TP-016 | waiting on retest closure |
| T-022 | Phase 4 | Cross-module | Reporting | Update Test Plan and final evidence | sync final pass/fail and bug closure into QA artifact | QA workflow | T-021 | QA lead | High | In Progress | Test Plan reflects latest evidence and statuses | TP-001 to TP-018 | |
| T-023 | Phase 4 | Cross-module | Reporting | Update Project Tracking final closure | mark final task statuses with evidence | delivery workflow | T-022 | PM / QA lead | High | In Progress | tracker aligned with Test Plan and release decision | all linked TP IDs | |
| T-024 | Phase 4 | Cross-module | Deployment | Release readiness review | confirm no open critical blocker before deployment | TD / QA / tracking | T-022, T-023 | PM + Tech Lead | Critical | Blocked | no critical defects open, UAT complete | TP-016, related | blocked by T-003 and T-016 |

## 5. Blockers And Decisions

| ID | Related Task | Blocker / Decision | Impact | Owner | Due / Review Date | Status |
|---|---|---|---|---|---|---|
| B-001 | T-003 / T-008 | `action_approve()` currently triggers downstream confirm twice | approval release blocked | Dev A | 2026-06-26 | Open |
| B-002 | T-016 / T-018 | retry path still risks duplicate outbound sync | integration release blocked | Dev B | 2026-06-26 | Open |
| B-003 | T-021 | business UAT cannot start until approval and retry defects close | final sign-off delayed | PM | 2026-06-28 | Blocked |
| D-001 | T-010 | low-margin quotations require approval instead of hard block | changes expected TP-007 acceptance | Product owner | 2026-06-25 | Approved |

## 6. Review And Test Queue

| Task ID | Review Needed | Test Needed | Reviewer / Tester | Status | Notes |
|---|---|---|---|---|---|
| T-003 | Yes | Yes | Reviewer / QA | In Fix | rerun TP-003 after patch |
| T-004 | Yes | Yes | Reviewer / QA | In Fix | rerun TP-004 with `Form` scenario |
| T-007 | No | Yes | QA | Testing | suite partially green |
| T-008 | No | Yes | QA | Ready For Retest | waiting for code patch |
| T-011 | Yes | Yes | Reviewer / QA | Ready For Test | execute TP-008 |
| T-012 | No | Yes | QA | Ready For Test | execute TP-009 |
| T-016 | Yes | Yes | Reviewer / QA | Ready For Retest | rerun TP-011 in mock + SIT |
| T-018 | No | Yes | QA | In Fix | retry test suite still red |
| T-019 | No | Yes | QA / Key User | Testing | manual SIT step pending |
| T-021 | No | Yes | QA / Key User | Ready | UAT after critical retests close |

## 7. Change Notes

| Date | Change | Reason | Impacted Tasks |
|---|---|---|---|
| 2026-06-25 | Marked T-003 `In Fix` | TP-003 failed with duplicate confirmation behavior | T-003, T-008, T-021, T-024 |
| 2026-06-25 | Marked T-016 `Ready For Retest` | idempotency patch prepared after TP-011 failure | T-016, T-018, T-021, T-024 |
| 2026-06-25 | Kept T-024 blocked | UAT and critical retest not complete | T-021, T-022, T-023, T-024 |
```

## Why this example is useful

1. It uses the same scenario and IDs as the QA/QC example, so the relationship between `Test Plan.md` and `Project Tracking.md` is obvious.
2. It shows how delivery tasks can stay granular without turning the tracker into a vague backlog.
3. It makes `In Fix` and `Ready For Retest` visible at task level, not just at test-case level.
4. It keeps the upstream requirement-analysis and fit-gap chain visible all the way to task status.
5. It demonstrates how blockers and release readiness should depend on evidence from both implementation and QA/QC.
6. It gives the agent a concrete model for the full loop, while still allowing narrower requests to use smaller workflows.
