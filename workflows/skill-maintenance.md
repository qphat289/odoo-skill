# WORKFLOW: Skill Maintenance

## Purpose

Guide the agent through improving the skill pack itself after real usage reveals stale guidance, repeated mistakes, or weak instructions.

## When to use

Use this workflow when the repository knowledge needs correction or strengthening, not when building or reviewing a client module.

## Inputs

- correction-log entries
- affected area such as models, views, security, upgrade, or presales
- optional routing failure, pressure scenario, or loophole report

## Required reads

- `docs/CORRECTIONS_LOG.md`
- `skills/odoo-development/references/skill-pack-harness-guide.md`
- `skills/odoo-development/references/eval-campaign-guide.md`
- `skills/odoo-development/references/route-pressure-scenarios.md`
- `evals/routing-workflow-evals.json`
- `docs/HARNESS_EVAL_LOG.md`
- `docs/HARNESS_EVAL_RUNBOOK.md`

## Optional reads

- the smallest relevant skill, rule, workflow, or agent file affected by the correction
- `skills/odoo-quality/references/common-bug-patterns.md` when the issue is a repeat bug candidate
- official Odoo docs or source when the claim is uncertain

## Steps

1. Read the correction log and work only from `Pending` rows.
2. Verify each correction against the smallest relevant existing source.
3. Use official Odoo docs or source when the claim is time-sensitive or uncertain.
4. Patch the canonical destination:
   - version skill
   - domain skill
   - `skills/odoo-quality/references/common-bug-patterns.md` for repeatable pre-build or review bugs
   - `rules/security.md`
   - `rules/coding-style.md`
   - workflow or agent only when operationally necessary
5. If the issue is about routing, artifact forcing, or agent rationalization:
   - update or add a pressure scenario
   - update eval coverage in `evals/routing-workflow-evals.json` when scenario coverage is missing or stale
   - update the harness guidance or validator rule
   - capture the loophole in `docs/CORRECTIONS_LOG.md`
   - record the RED/GREEN/REFACTOR result in `docs/HARNESS_EVAL_LOG.md`
6. Update the correction log immediately:
   - move fixed items to `Applied`
   - mark uncertain items `needs-verify`
   - mark obsolete items `superseded`
7. Run:
   - `python scripts/run_harness_eval_campaign.py --ids <scenario IDs>` when the change needs a focused campaign brief
   - `python scripts/validate_layout.py`
   - `python scripts/validate_skill_pack_contracts.py`
   - `python scripts/validate_harness_evals.py`
   - `python scripts/validate_no_stale_refs.py`

## Outputs

- updated canonical repository files
- updated correction log status
- short report of applied and still-unverified items

## Validation gates

- no already-fixed item remains in `Pending`
- fixes land in canonical files, not only in the log
- repeat bugs are promoted into `common-bug-patterns.md` when they are broad enough to justify reuse
- repository layout still validates after the maintenance pass
- routing or loop fixes update the harness layer when needed
- harness eval coverage and log stay aligned with meaningful routing changes
