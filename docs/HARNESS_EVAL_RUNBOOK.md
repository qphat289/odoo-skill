# Harness Eval Runbook

Use this runbook to execute a routing/workflow eval campaign for the skill pack.

## Purpose

Turn the eval manifest and pressure scenarios into a repeatable operator workflow.

## Inputs

- `evals/routing-workflow-evals.json`
- `skills/odoo-development/references/route-pressure-scenarios.md`
- `skills/odoo-development/references/eval-campaign-guide.md`
- `docs/HARNESS_EVAL_LOG.md`

## Quick start

List available scenarios:

```powershell
python scripts/run_harness_eval_campaign.py --list
```

Render a full campaign brief:

```powershell
python scripts/run_harness_eval_campaign.py --all
```

Render a focused campaign:

```powershell
python scripts/run_harness_eval_campaign.py --ids RP-002,RP-007,RP-013
```

Write the campaign brief to a file:

```powershell
python scripts/run_harness_eval_campaign.py --ids RP-002,RP-007 --output docs/tmp-harness-campaign.md
```

## Operator flow

1. Choose scenario IDs.
2. Render the campaign brief.
3. Run the scenarios manually against the relevant router/workflow change.
4. Capture:
   - expected route
   - actual route
   - over-routing or under-routing behavior
   - skipped guardrails
   - artifact or loop-sync drift
5. Patch the smallest canonical files.
6. Update:
   - `docs/CORRECTIONS_LOG.md`
   - `docs/HARNESS_EVAL_LOG.md`
   - `evals/routing-workflow-evals.json` when coverage changes
7. Re-run:
   - `python scripts/validate_layout.py`
   - `python scripts/validate_skill_pack_contracts.py`
   - `python scripts/validate_harness_evals.py`

## When to use a focused campaign

Use a focused campaign when:

- only one route changed
- one helper agent was tightened
- one office-file rule was added
- one loop-sync bug was patched

## When to use the full campaign

Use the full campaign when:

- the top-level router changed
- multiple workflows were refactored
- artifact rules changed
- the harness or validators changed significantly
