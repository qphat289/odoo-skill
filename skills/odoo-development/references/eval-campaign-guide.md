# Skill-Pack Eval Campaign Guide

Use this guide when validating whether routing, workflow selection, artifact handling, and helper-agent behavior still hold under realistic pressure.

## Purpose

Turn the Odoo skill pack into something that is not only well-written, but repeatedly testable.

This guide complements:

- `skill-pack-harness-guide.md` for overall harness philosophy
- `route-pressure-scenarios.md` for human-readable scenario design
- `../../../evals/routing-workflow-evals.json` for machine-checkable eval coverage
- `../../../docs/HARNESS_EVAL_LOG.md` for recording RED/GREEN/REFACTOR runs
- `../../../docs/HARNESS_EVAL_RUNBOOK.md` for operator steps
- `../../../scripts/run_harness_eval_campaign.py` for rendering campaign briefs

## Why this exists

Superpowers-style skill design is strong because it does not stop at "write better instructions."

It asks:

1. what failure happens without the guidance
2. what minimal patch makes the agent behave better
3. what loophole still remains after the patch

Anthropic-style harness thinking pushes the same idea further:

- test the agent on realistic tasks
- preserve the smallest useful context
- keep routing flexible
- move discipline into validators and repeated checks

## What to evaluate in this repository

Run eval campaigns when any of these change:

- top-level routing rules
- workflow boundaries
- canonical artifact rules
- presales vs technical handoff rules
- QA/QC and tracking loop rules
- document or spreadsheet handling rules
- helper-agent responsibilities

## Eval layers

### 1. Routing eval

Question:

- did the agent choose the right primary workflow?
- did it keep the task narrow when the request was narrow?

### 2. Guardrail eval

Question:

- did the agent preserve hard constraints such as version detection, security review, and test validation?

### 3. Artifact eval

Question:

- did the agent create only the artifacts that materially fit the task?
- did it preserve traceability when artifacts already existed?

### 4. Loop eval

Question:

- after plan -> build -> test -> fix -> retest, did the agent update `Test Plan.md` and `Project Tracking.md` correctly?

### 5. Office capability eval

Question:

- when a task touches `.docx` or `.xlsx`, did the agent treat document/spreadsheet handling as a capability tied to the task instead of ignoring it or forcing a file conversion workflow too early?

## Campaign rhythm

### RED

Use the scenario set before the patch or against the old wording.

Record:

- wrong workflow chosen
- over-forced artifact chain
- skipped guardrail
- ignored `.docx` / `.xlsx` handling need
- missing loop synchronization

### GREEN

Patch only the smallest canonical files needed:

- router
- workflow
- helper agent
- template/example
- validator

Re-run the same scenarios and confirm the failure is gone.

### REFACTOR

Ask:

- what new rationalization still lets the agent fail?
- should this become a pressure scenario?
- should this become a validator rule?
- should this be logged in `CORRECTIONS_LOG.md`?

## Minimum evidence per eval run

For each scenario, capture:

- scenario ID
- expected route
- actual route
- failure mode, if any
- patch applied
- validator or log update
- remaining risk

Do not write "passed" without enough detail to explain why.

## Campaign support

Use:

```powershell
python scripts/run_harness_eval_campaign.py --list
python scripts/run_harness_eval_campaign.py --ids RP-002,RP-007,RP-013
python scripts/run_harness_eval_campaign.py --all
```

to render a reusable campaign brief before running the scenarios manually.

## When an eval fails

1. patch the canonical file, not only the log
2. update `route-pressure-scenarios.md` if the failure exposed a new pattern
3. update `routing-workflow-evals.json` if coverage is missing
4. update `HARNESS_EVAL_LOG.md`
5. run the validator scripts again

## Good outcomes

- narrow task stays narrow
- full customer requirement still routes through the complete loop
- presales is not skipped for business ambiguity
- technical work still enforces version/security/test gates
- `.docx` and `.xlsx` handling is recognized when relevant
- loop artifacts stay synchronized after test/fix cycles
