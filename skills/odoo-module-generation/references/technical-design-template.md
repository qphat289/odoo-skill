# Odoo Technical Design Template

Use this template when Functional Design and Solution Design are ready enough to guide implementation.

Suggested filename: `Technical Design.md`

## Template

```markdown
# Technical Design

## 1. Source Artifacts

| Artifact | Path / Version | Status | Notes |
|---|---|---|---|
| Requirement Analysis |  | Draft / Approved |  |
| Clarification Register |  | Draft / Approved |  |
| Functional Design |  | Draft / Approved |  |
| Solution Design |  | Draft / Approved |  |
| Fit/Gap Analysis |  | Draft / Approved |  |

## 2. Technical Summary

- Target Odoo version:
- Target module technical name:
- Existing modules to depend on:
- Standard modules to inherit:
- Custom module(s):
- Implementation sequencing notes:

## 3. Requirement Traceability

| Req ID | Fit/Gap ID | Functional Section | Solution Decision | Technical Section | Test Plan Hint | Tracking Hint | Build Treatment |
|---|---|---|---|---|---|---|---|

## 4. Module And Dependency Design

### 4.1 Build order / dependency order

- module creation sequence:
- security/data/view loading sequence:
- cross-module dependency risks:

## 5. Model And Data Design

### 5.x Model: `model.name`

- Purpose:
- `_name` / `_inherit`:
- Key fields:
- Computed fields:
- Constraints:
- Onchange / CRUD behavior:
- Company behavior:
- Data loading:

## 6. Business Logic Design

## 7. View, Menu, Action, Wizard, And Report Design

## 8. Security Design

- Groups:
- ACL:
- Record rules:
- Server-side permission checks:
- Multi-company notes:

## 9. Integration Design

- External systems:
- Direction:
- Payload/data mapping:
- Authentication:
- Error handling:
- Retry/reconciliation:

## 10. Automation And Notification Design

## 11. Data Migration And Configuration Design

## 12. Performance, Logging, And Operations

## 13. Test Planning Notes

- Unit / transaction tests:
- Security tests:
- Workflow tests:
- Integration tests:
- Data migration or cutover validation:
- UAT support notes:
- Full case-by-case coverage and status: see `Test Plan.md`

## 14. Technical Risks And Preconditions

| ID | Topic | Risk / Precondition | Impact | Owner |
|---|---|---|---|---|

## 15. Build Readiness Checklist

- [ ] Functional Design source is identified
- [ ] Solution Design source is identified
- [ ] target Odoo version is confirmed
- [ ] dependencies are known
- [ ] every persistent model has ACL plan
- [ ] security-sensitive flows have server-side checks
- [ ] tests are identified for non-trivial logic
```

## Rules

1. Base this document on Functional Design and Solution Design, not loose chat notes.
2. Keep business rationale traceable, but write for devs and coding agents.
3. Preserve upstream traceability back to requirement-analysis IDs and fit-gap IDs when they exist.
4. Do not use this as a progress tracker or full test tracker; status/backlog belongs in `Project Tracking.md`, and detailed case coverage belongs in `Test Plan.md`.
5. Keep business-facing clarifications upstream in `Clarification Register.xlsx`; use this section for technical risks, prerequisites, and explicitly waived assumptions only.
6. Apply Odoo version-specific rules before finalizing.
