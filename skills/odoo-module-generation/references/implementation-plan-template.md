# Implementation Plan Template

Use this template after `01-business-to-implementation-spec.md` is confirmed enough to guide build work.

Suggested filename: `02-implementation-plan.md`

## Template

```markdown
# Implementation Plan

## Source Spec

- Input document: `01-business-to-implementation-spec.md`
- Target Odoo version:
- Target module technical name:

## Objective

- Delivery goal:
- Build boundary:

## Technical Approach

- New module vs extension:
- Inherit vs new models:
- Key architecture choices:

## Technical Verification

- Standard modules reviewed:
- Core models reviewed:
- Core views reviewed:
- Version-specific checks:

## Delivery Breakdown

| Step | Area | Deliverable | Dependency | Status |
|---|---|---|---|---|
| 1 | Scaffold | Manifest and file tree | None | Todo |

## Model And Data Plan

- Models to create:
- Models to inherit:
- Key fields:
- Data files:

## View And UX Plan

- Menus and actions:
- Form or tree views:
- Reports or wizards:
- OWL or frontend work if any:

## Security Plan

- Access groups:
- ACL files:
- Record rules:
- Multi-company checks:

## Automation And Integration Plan

- Cron jobs:
- Mail or activities:
- Controllers or APIs:
- External dependencies:

## Testing Plan

- Unit or transaction tests:
- Security checks:
- User-flow checks:
- Regression focus:

## Risks And Notes

- Risk 1:
- Mitigation:

## Progress Log

| Task | Owner | Status | Notes |
|---|---|---|---|
|  |  | Todo / Doing / Done / Blocked |  |

## Completion Checklist

- [ ] Manifest and dependency order verified
- [ ] Security reviewed
- [ ] Tests added or updated
- [ ] Version-specific syntax verified
- [ ] Open blockers resolved or recorded
```

## Guardrails

- The plan should only contain confirmed build work, not unresolved business discovery.
- Keep one ordered task flow so implementation status can be updated without relying on chat history.
- Record blockers in the plan, not only in agent messages.
