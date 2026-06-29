# Design Artifact Handoff Guide

Use this reference to move from customer requirements into Functional Design, Solution Design, Technical Design, Test Plan, and delivery tracking without losing traceability.

## Artifact chain

```text
Scope of Work / Requirements
-> Requirement Analysis.md
-> Clarification Register.xlsx
-> Fit-Gap Analysis.xlsx
-> Functional Design.docx
-> Solution Design.docx
-> Technical Design.md
-> Test Plan.md
-> Project Tracking.md
-> Build / Review / Test
```

## Ownership model

| Artifact | Format | Main audience | Main owner |
|---|---|---|---|
| Requirement Analysis | `.md` | FC, solution owner, PM, delivery lead | FC / solution owner |
| Clarification Register | `.xlsx` | FC, PM, solution owner, customer owner, key stakeholders | FC / solution owner |
| Fit-Gap Analysis | `.xlsx` | FC, PM, solution owner, delivery lead | FC / solution owner |
| Functional Design | `.docx` | customer, FC, PM, QA, key users | FC |
| Solution Design | `.docx` | customer, PM, FC lead, solution owner, tech lead | FC / solution owner |
| Technical Design | `.md` | dev, technical lead, coding agent, reviewer | technical planner / dev |
| Test Plan | `.md` | QA/QC, dev, reviewer, tester, PM | QA/QC lead / dev lead |
| Project Tracking | `.md` | PM, dev lead, QA lead, delivery team | PM / delivery owner |

## Handoff rules

1. Requirement Analysis normalizes the customer input into a traceable working baseline.
2. Clarification Register captures the necessary pre-fit-gap and pre-design answers in one place.
3. Fit-Gap Analysis classifies each requirement row into fit, configuration, customization, integration, process change, or out of scope.
4. Functional Design explains what users and business processes need.
5. Solution Design explains the selected overall Odoo solution and why.
6. Technical Design explains how the solution will be implemented in Odoo.
7. Test Plan explains how the solution will be validated across module behavior, business logic, integration, security, and regression scope.
8. Project Tracking explains implementation and QA execution status.
9. Technical Design must cite Functional Design and Solution Design as source inputs.
10. Do not scatter unresolved questions across downstream artifacts; resolve or waive them in the clarification register first.

## Traceability matrix

```markdown
| Req ID | Fit/Gap ID | Functional Section | Solution Decision | Technical Section | Test Plan Ref | Tracking Ref | Status |
|---|---|---|---|---|---|---|---|
```

For ID meanings such as `RQ`, `CL`, `FG`, `FR`, `TD`, `TP`, and `T`, see `docs/ARTIFACT_ID_GLOSSARY.md`.

## Handoff checklist

- each custom or integration requirement appears in Functional Design and Technical Design
- each major decision appears in Solution Design
- each major test case can cite the requirement or design source that justifies it
- each tracked delivery task can cite the requirement, design, or test source that drives it
- out-of-scope and later-phase items remain separate
- acceptance criteria exist or are marked as needing confirmation
- technical risks are not hidden in customer-facing prose only
