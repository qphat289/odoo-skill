# Odoo Implementation Handoff Guide

Use this reference when a presales package must become delivery-ready input.

## Goal

Turn discovery and fit-gap outputs into `01-business-to-implementation-spec.md` without losing business intent.

## Required inputs

- Discovery notes
- Current fit-gap table
- Proposal or SOW scope notes if they exist

## Mapping rules

| Fit-gap classification | Handoff destination |
|---|---|
| Fit | `Business Context` or assumptions only |
| Configuration | `Configuration Notes` |
| Customization | `Functional Requirements`, `Process And User Flows`, `Security And Approval Notes`, `Views, Reports, And Documents` |
| Integration | `Integrations` section or explicit workflow/report notes |
| Process change | `Business Context` assumptions |
| Out of scope | `Out of Scope` |

## Minimum handoff structure

```markdown
# Business-to-Implementation Spec

## Scope Summary

## Requirement Traceability

## Selected Solution Approach

## Odoo App And Module Mapping

## Process And User Flows

## Functional Requirements

## Security And Approval Notes

## Views, Reports, And Documents

## Automation And Integrations

## Business Context

## Out of Scope

## Assumptions

## Open Questions

## Acceptance Criteria

## Handoff Notes For Planning
```

## Handoff checklist

- Each custom or integration row appears somewhere in the business-to-implementation spec.
- Out-of-scope items remain visible.
- Open questions are listed explicitly.
- Business context explains why the feature matters, not only what to build.
- The implementation team can start planning without rereading long presales prose.
