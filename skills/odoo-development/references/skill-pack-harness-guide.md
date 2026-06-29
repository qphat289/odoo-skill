# Odoo Skill-Pack Harness Guide

Use this guide when improving the Odoo skill pack itself, especially when the issue is not only missing content but weak routing, weak validation, or agent rationalization under pressure.

## Purpose

Keep the pack flexible in routing but strict in validation.

This guide is inspired by:

- Anthropic skill-authoring guidance on progressive disclosure, feedback loops, and validators
- superpowers-style RED -> GREEN -> REFACTOR thinking for agent behavior
- harness/context-engineering patterns for long-running agent work

## Core stance

1. Workflows are default playbooks, not rigid rails.
2. Validators and feedback loops are where discipline becomes real.
3. Narrow tasks should stay narrow.
4. Full-chain delivery should stay traceable.
5. When the pack fails, patch the canonical source and the harness layer together.

## What the harness is in this repository

The harness is not one file. It is the combination of:

- routers: `AGENTS.md`, `SKILL.md`, `skills/odoo-development/SKILL.md`
- workflows
- helper agents
- canonical artifacts
- validation scripts in `scripts/`
- pressure scenarios
- correction log and loophole tracking

## Design rules

### 1. Soft route, hard gate

Use soft wording for route selection:

- "default route"
- "closest workflow"
- "when useful"
- "preserve traceability where practical"

Keep hard wording only for high-risk constraints:

- version detection before version-sensitive work
- security validation
- manifest/data ordering
- test validation before claiming completion

### 2. Default artifact, not forced artifact

Canonical artifacts are the default for formal delivery work:

- `Requirement Analysis.md`
- `Fit-Gap Analysis.xlsx`
- `Functional Design.docx`
- `Solution Design.docx`
- `Technical Design.md`
- `Test Plan.md`
- `Project Tracking.md`

Do not force the whole artifact chain for:

- fix-only requests
- review-only requests
- quick comparisons
- targeted planning
- status-only updates

### 3. Preserve traceability without overloading the task

For narrow tasks, preserve only the traceability that materially matters.

Examples:

- quick fit-gap review: keep source file and requirement IDs visible
- test-plan update: keep linked `TP ID` and tracking references synchronized
- fix-only code task: keep related `Technical Design`, `Test Plan`, or `Project Tracking` refs if they already exist

### 4. Patch behavior, not only content

If the agent fails because it rationalizes, over-routes, or skips a loop:

- update the router or workflow wording
- add or update a pressure scenario
- add or update a validator if possible
- log the loophole in `docs/CORRECTIONS_LOG.md`

## Preferred maintenance loop

### RED

Observe a real or simulated failure:

- wrong workflow selected
- artifact chain forced when not needed
- business request jumped into code too early
- test/tracking status drift
- presales/technical/QA handoff loses traceability

### GREEN

Patch the smallest canonical files that fix the behavior:

- router
- workflow
- agent
- template/example
- validation script

### REFACTOR

Close loopholes:

- what rationalization would let the agent fail again?
- can the validator catch it?
- can a pressure scenario expose it quickly?

## What to validate

Use machine-checkable validation where possible:

- repository layout
- presence of critical harness files
- presence and coverage of the eval manifest
- presence of required contract phrases in canonical router/workflow files
- presence of source-artifact and traceability sections in core templates

Use human review where needed:

- whether the route is too rigid
- whether outputs match the user's actual intent
- whether examples still feel realistic

## Common failure modes

- full delivery loop forced onto a narrow request
- business-facing input routed straight into code generation
- artifact created just because the workflow mentions it, not because the task needs it
- test status updated without syncing project tracking
- technical design written without preserving upstream requirement or fit-gap traceability
- correction log updated without patching canonical files

## Files to use together

- `skills/odoo-development/references/route-pressure-scenarios.md`
- `skills/odoo-development/references/eval-campaign-guide.md`
- `../../../evals/routing-workflow-evals.json`
- `workflows/skill-maintenance.md`
- `docs/CORRECTIONS_LOG.md`
- `docs/HARNESS_EVAL_LOG.md`
- `scripts/validate_layout.py`
- `scripts/validate_skill_pack_contracts.py`
- `scripts/validate_harness_evals.py`
