# WORKFLOW: Implementation Planning

## Purpose

Guide the agent from a confirmed business-to-implementation scope into an execution-ready implementation plan.

## When to use

Use this workflow when `01-business-to-implementation-spec.md` or an equivalent confirmed handoff artifact exists and the next step is build planning.

## Inputs

- confirmed `01-business-to-implementation-spec.md`
- target Odoo version
- target module technical name

## Required reads

- `agents/odoo-planner.md`
- `skills/odoo-module-generation/references/implementation-plan-template.md`
- `skills/odoo-module-generation/references/odoo-module-checklist.md`
- `skills/odoo-module-generation/references/odoo-manifest-data-order.md`
- `skills/odoo-quality/references/common-bug-patterns.md`
- `rules/security.md`
- `rules/coding-style.md`

## Optional reads

- smallest relevant version skill
- matching business-domain, automation, integration, OWL, or operations references
- `skills/odoo-presales/references/business-to-implementation-spec-template.md` when the input scope is still uneven

## Steps

1. Confirm the scope document is specific enough for build planning.
2. Read the implementation-plan template, module checklist, and common bug patterns.
3. Verify the technical baseline against the target Odoo version and touched standard modules.
4. Turn relevant common bug patterns into explicit plan checks, risks, or task notes.
5. Produce or update `02-implementation-plan.md`.
6. Keep the plan ordered by dependency and implementation sequence.
7. Record blockers, assumptions, and validation work in the plan itself.
8. Hand off to code generation or review work only after the plan is coherent.

## Outputs

- `02-implementation-plan.md`
- short note of unresolved blockers if any

## Validation gates

- the plan maps back to confirmed scope rather than loose presales prose
- version-specific checks are visible before coding starts
- repeat bug risks are translated into explicit implementation checks
- task order is clear enough to drive implementation without extra replanning
