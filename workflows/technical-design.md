# WORKFLOW: Technical Design

## Purpose

Guide the agent from Functional Design and Solution Design into a detailed `Technical Design.md` for devs, technical reviewers, and coding agents.

## When to use

Use this workflow when customer-facing design artifacts are ready enough to define how the Odoo solution will be implemented.

## Inputs

- `Requirement Analysis.md` when available
- `Functional Design.docx` or equivalent functional design content
- `Solution Design.docx` or equivalent solution design content
- `Fit-Gap Analysis.xlsx` or equivalent fit-gap analysis workbook
- target Odoo version
- target module technical name

## Required reads

- `agents/odoo-technical-planner.md`
- `skills/odoo-module-generation/references/technical-design-template.md`
- `skills/odoo-module-generation/references/odoo-module-checklist.md`
- `skills/odoo-module-generation/references/odoo-manifest-data-order.md`
- `skills/odoo-quality/references/common-bug-patterns.md`
- `rules/security.md`
- `rules/coding-style.md`

## Optional reads

- smallest relevant version skill
- `skills/odoo-module-generation/references/technical-design-example-sale-approval.md` when a realistic sample would help shape the artifact
- matching business-domain, automation, integration, OWL, or operations references
- `skills/odoo-presales/references/design-artifact-handoff-guide.md`

## Steps

1. Confirm Functional Design and Solution Design are specific enough for technical design.
2. Read the technical-design template, module checklist, and common bug patterns.
3. Verify the technical baseline against the target Odoo version and touched standard modules.
4. Preserve requirement-analysis IDs and fit-gap IDs in the traceability chain when they exist.
5. Map functional requirements and solution decisions into technical sections.
6. Turn relevant common bug patterns into explicit technical checks, risks, or test notes.
7. Produce or update `Technical Design.md`.
8. Keep the design ordered by dependency and implementation sequence where useful.
9. Record blockers, assumptions, technical risks, and prerequisites in the document, while keeping business-facing clarifications upstream in `Clarification Register.xlsx`.
10. Hand off to `workflows/test-plan.md`, `workflows/project-tracking.md`, code generation, or review work only after the technical design is coherent.

## Outputs

- `Technical Design.md`
- short note of unresolved blockers if any
- recommended next step: `Test Plan.md` for detailed QA coverage or `Project Tracking.md` for delivery breakdown/status tracking

## Validation gates

- the design maps back to Functional Design and Solution Design
- version-specific checks are visible before coding starts
- repeat bug risks are translated into explicit technical checks
- the document contains test-planning notes, but the full scenario matrix lives in `Test Plan.md`
- devs or coding agents can implement from the design without rereading all presales prose
