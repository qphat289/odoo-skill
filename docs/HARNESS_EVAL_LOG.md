# Harness Eval Log

Use this file to record meaningful RED/GREEN/REFACTOR runs for the skill pack itself.

Do not use it for customer project test execution. That belongs in project-level artifacts such as `Test Plan.md` and `Project Tracking.md`.

## How to use

For each meaningful routing, artifact, or loop-behavior change:

1. record the scenario IDs exercised
2. note the failure or risk that triggered the change
3. note the canonical files patched
4. note the validator updates
5. record the final verification result

## Eval entries

| Eval ID | Date | Scenario IDs | Focus | RED failure or risk | GREEN patch | REFACTOR closure | Validation | Status |
|---|---|---|---|---|---|---|---|---|
| EVAL-001 | 2026-06-26 | RP-001 to RP-010 | Flexible routing + harness baseline | Workflow wording was still too easy to over-force into the full chain | Router, workflow, harness guide, pressure scenarios, contract validator | Added loophole guidance and machine-checkable contract phrases | `validate_layout.py`, `validate_skill_pack_contracts.py` | Applied |
| EVAL-002 | 2026-06-26 | RP-002, RP-004, RP-005, RP-007, RP-011, RP-012 | Routing eval layer + office capability handling | No reusable eval campaign layer existed for narrow tasks, office-file tasks, and loop-sync checks | Added eval campaign guide, routing eval manifest, eval validator, and router/workflow references | Added office-capability scenarios and eval log discipline | `validate_layout.py`, `validate_skill_pack_contracts.py`, `validate_harness_evals.py` | Applied |

## Open eval ideas

| Candidate | Why it matters | Suggested scenarios | Status |
|---|---|---|---|
| Hybrid route drift after future workflow edits | Flexible routing can regress back into hard routing | RP-003, RP-007, RP-008 | Open |
| Test/fix/retest artifact sync drift | Large-loop delivery can claim completion before tracking is updated | RP-005, RP-013 | Open |
| Presales to technical handoff clarity | Technical Design can become vague if upstream traceability weakens | RP-009, RP-010 | Open |
