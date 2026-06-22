# Business-to-Implementation Spec Template

Use this template when presales output is mature enough to become delivery-ready scope.

Suggested filename: `01-business-to-implementation-spec.md`

## Template

```markdown
# Business-to-Implementation Spec

## Document Control

- Customer or project:
- Target Odoo version:
- Primary business owner:
- Primary delivery owner:
- Status: draft | confirmed

## Business Context

- Background:
- Problem to solve:
- Why now:

## Goals And Success Criteria

- Goal 1:
- Goal 2:
- Success signal:

## Scope Summary

- In scope:
- Out of scope:
- Phase split if relevant:

## Requirement Traceability

| ID | Requirement | Source | Fit-gap class | Priority | Status |
|---|---|---|---|---|---|
| R1 |  |  | Fit / Config / Custom / Integration / Process / Out | High / Medium / Low | Confirmed / Open |

## Selected Solution Approach

- Chosen direction:
- Why this approach:
- Rejected alternatives:

## Odoo App And Module Mapping

| Business area | Standard Odoo app or module | Custom module or extension | Notes |
|---|---|---|---|
|  |  |  |  |

## User Roles

- Role:
  Responsibility:

## Process And User Flows

1. Trigger:
2. Main flow:
3. Decision points:
4. Exceptions:

## Functional Requirements

### Requirement R1

- Business rule:
- Expected behavior:
- Key fields or data:
- User-facing outputs:

## Security And Approval Notes

- Access groups:
- Record visibility:
- Approval rules:
- Multi-company constraints:

## Views, Reports, And Documents

- Form or tree views:
- Reports:
- Email or PDF outputs:
- Wizards:

## Automation And Integrations

- Cron or scheduled jobs:
- Notifications:
- External systems:
- Data exchange direction:

## Non-Functional Constraints

- Performance:
- Auditability:
- Compliance:
- Usability:

## Assumptions

- Assumption 1:

## Open Questions

- Question 1:

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2

## Handoff Notes For Planning

- Recommended module technical name:
- Expected custom models:
- Standard modules to inherit:
- Known technical risks:
```

## Guardrails

- Keep open questions visible instead of mixing them into confirmed scope.
- Keep phase-2 backlog outside the confirmed in-scope sections.
- Preserve fit-gap traceability so planning can map each confirmed customization or integration.
