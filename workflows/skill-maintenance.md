# WORKFLOW: Skill Maintenance

## Purpose

Guide the agent through improving the skill pack itself after real usage reveals stale guidance, repeated mistakes, or weak instructions.

## When to use

Use this workflow when the repository knowledge needs correction or strengthening, not when building or reviewing a client module.

## Inputs

- correction-log entries
- affected area such as models, views, security, upgrade, or presales

## Required reads

- `docs/correct-log/CORRECTIONS_LOG.md`

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
5. Update the correction log immediately:
   - move fixed items to `Applied`
   - mark uncertain items `needs-verify`
   - mark obsolete items `superseded`
6. Run `python scripts/validate_layout.py`.

## Outputs

- updated canonical repository files
- updated correction log status
- short report of applied and still-unverified items

## Validation gates

- no already-fixed item remains in `Pending`
- fixes land in canonical files, not only in the log
- repeat bugs are promoted into `common-bug-patterns.md` when they are broad enough to justify reuse
- repository layout still validates after the maintenance pass
