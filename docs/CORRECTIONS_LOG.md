# Skill Correction Log

Use this log to capture mistakes, stale claims, and recurring bugs found while using the Odoo skill pack.

## Purpose

- Keep active correction work in one visible place.
- Make it easy to promote repeat issues into the right canonical skill, rule, or workflow.
- Ensure that once a correction is absorbed, the pending entry is removed or moved so the log stays trustworthy.

## Status tags

- `pending`: identified and waiting to be applied
- `needs-verify`: suspected issue, but source verification is still missing
- `applied`: already promoted into the canonical repository source
- `superseded`: no longer relevant because another change replaced it

## Maintenance rule

After a correction is applied to the real source of truth:

1. remove it from `Pending`
2. move it to `Applied`
3. or edit it to `superseded` if another change made it irrelevant

Do not leave an already-fixed item in `Pending`.

## Row format

```markdown
| ID | Status | Date | Area | Version | Target file | Topic | Problem | Correct guidance or bug pattern | Evidence | Resolution |
```

## Repeat-bug entry guideline

Use this when the issue looks like a candidate for `skills/odoo-quality/references/common-bug-patterns.md`.

```markdown
| CB-CAND-001 | pending | YYYY-MM-DD | models/views/security/performance/etc. | all / 14-15 / 16 / 17+ / 18+ | skills/odoo-quality/references/common-bug-patterns.md | short bug title | short statement of the recurring mistake | preferred prevention rule in one sentence | failing example, review finding, or source link | promote if the same bug repeats across modules |
```

## Loophole / routing entry guideline

Use this when the problem is not mainly a code bug, but an agent-behavior loophole such as over-forcing a workflow, skipping traceability, jumping to code too early, or failing to keep artifacts synchronized.

```markdown
| LOOP-001 | pending | YYYY-MM-DD | router/workflow/agent/harness | all | target canonical file | short loophole title | what the agent rationalized or skipped | preferred counter-rule in one sentence | failing scenario, prompt, or observed behavior | add or update pressure scenario, harness guidance, and validator if the loophole is broad |
```

## Pending

| ID | Status | Date | Area | Version | Target file | Topic | Problem | Correct guidance or bug pattern | Evidence | Resolution |
|---|---|---|---|---|---|---|---|---|---|---|

## Applied

| ID | Status | Date | Area | Version | Target file | Topic | Problem | Correct guidance or bug pattern | Evidence | Resolution |
|---|---|---|---|---|---|---|---|---|---|---|
