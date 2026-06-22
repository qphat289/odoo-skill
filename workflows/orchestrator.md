# WORKFLOW: Orchestrator

## Purpose

Act as the top-level router for workflow selection inside this repository.

## When to use

Use this file first when the task type is still broad and the agent must decide which specialized workflow to load.

## Inputs

- request type
- target Odoo version if known
- module path or business context if available

## Required reads

- `SKILL.md`
- `skills/odoo-development/SKILL.md`

## Optional reads

- `skills/odoo-upgrade/references/odoo-version-routing.md`
- `skills/odoo-module-generation/references/odoo-manifest-data-order.md`
- `rules/security.md`
- `rules/coding-style.md`

## Steps

1. Identify the request type.
2. Detect or confirm the Odoo version before any code generation, review, or upgrade work.
3. Load the matching version skill from `skills/odoo-14.0/` through `skills/odoo-19.0/`.
4. Route to the matching specialized workflow:
   - create or extend module -> `workflows/generate-module.md`
   - review or audit module -> `workflows/review-module.md`
   - upgrade or migrate module -> `workflows/upgrade-module.md`
   - generate or audit security -> `workflows/security-module.md`
   - run or debug tests -> `workflows/test-module.md`
   - generate tests -> `workflows/generate-tests.md`
   - OWL or frontend work -> `workflows/frontend-owl.md`
   - discovery workshop -> `workflows/presales-discovery.md`
   - fit-gap work -> `workflows/fit-gap.md`
   - proposal, SOW, or handoff -> `workflows/proposal-handoff.md`
   - confirmed scope to build plan -> `workflows/implementation-planning.md`
   - skill-pack self-maintenance -> `workflows/skill-maintenance.md`
5. Load only the smallest relevant domain skill and references for that workflow.
6. Apply `rules/security.md` and `rules/coding-style.md` for generation, review, and upgrade tasks.

## Outputs

- selected workflow
- selected version skill
- minimal reference set to load next

## Validation gates

- request type is mapped to exactly one primary workflow
- version is not guessed when it materially affects syntax or rules
- shared rules are loaded for code-facing work
- only needed references are loaded after routing
