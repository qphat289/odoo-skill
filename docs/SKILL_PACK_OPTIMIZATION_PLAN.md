# Odoo Skill-Pack Optimization Plan

## Purpose

This document captures the intended optimized architecture of the Odoo skill pack after strengthening it with presales routing, design artifacts, QA/QC loops, project tracking, and harness-driven validation.

It is not a customer delivery artifact. It is the operating plan for the pack itself.

## Target outcome

Make the pack:

- strong enough for large customer-requirement-to-delivery loops
- flexible enough for narrow tasks
- explicit enough for presales, technical, QA/QC, and tracking handoffs
- testable enough that routing and artifact behavior can be pressure-tested over time

## What was weak before

- routing language leaned too hard toward development work
- presales and business-facing ambiguity were not first-class enough
- workflows could be interpreted as rigid rails
- office-file handling risked being treated as an afterthought or as a separate workflow
- the large delivery loop existed conceptually but was not strong enough as a maintained harness

## Design principles adopted

### From Superpowers-style skill building

- treat skill design like process TDD
- capture realistic failure patterns, not only ideal instructions
- use RED -> GREEN -> REFACTOR for skill behavior, not only code behavior
- close rationalization loopholes explicitly

### From Anthropic-style agent design

- keep routing flexible and context minimal
- preserve hard gates for high-risk work
- make validators and evals carry real discipline
- separate broad workflow guidance from concrete reusable references

## Optimized architecture

### 1. Router layer

Canonical files:

- `AGENTS.md`
- `SKILL.md`
- `skills/odoo-development/SKILL.md`

Responsibilities:

- classify the task shape
- choose the smallest correct route
- keep presales as the first stop for business ambiguity
- enforce version, security, and test gates for technical work

### 2. Workflow layer

Canonical files under `workflows/`.

Responsibilities:

- define default playbooks
- keep formal artifact chain for end-to-end delivery
- allow narrow or hybrid execution when the task is narrower than the full chain

### 3. Artifact layer

Canonical delivery artifacts:

- `Requirement Analysis.md`
- `Fit-Gap Analysis.xlsx`
- `Functional Design.docx`
- `Solution Design.docx`
- `Technical Design.md`
- `Test Plan.md`
- `Project Tracking.md`

Responsibilities:

- preserve traceability from customer input to tested output
- separate business-facing artifacts from technical artifacts
- keep QA/QC and tracking state outside of chat-only reporting

### 4. Support capability layer

Canonical files under:

- `skills/odoo-documents/`
- `skills/odoo-spreadsheets/`

Responsibilities:

- attach DOCX handling to the real presales, design, QA/QC, or tracking route
- attach workbook handling to the real presales, fit-gap, QA/QC, or tracking route
- keep office-file support project-owned and license-safe

### 5. Helper-agent layer

Canonical files under `agents/`.

Responsibilities:

- presales analysis and handoff
- technical design planning
- QA/QC planning and test loop support
- review, trace, context gathering, and execution support

### 6. Harness layer

Canonical files:

- `skills/odoo-development/references/skill-pack-harness-guide.md`
- `skills/odoo-development/references/eval-campaign-guide.md`
- `skills/odoo-development/references/route-pressure-scenarios.md`
- `docs/CORRECTIONS_LOG.md`
- `docs/HARNESS_EVAL_LOG.md`
- `evals/routing-workflow-evals.json`

Responsibilities:

- encode routing pressure
- record loopholes
- keep repeated maintenance evidence-based
- stop the pack from drifting back into rigid or under-specified behavior

### 7. Validator layer

Canonical files:

- `scripts/validate_layout.py`
- `scripts/validate_skill_pack_contracts.py`
- `scripts/validate_harness_evals.py`
- `scripts/validate_no_stale_refs.py`

Responsibilities:

- ensure required files exist
- ensure core contracts stay present
- ensure eval coverage stays machine-checkable
- ensure removed or renamed canonical files do not leak back into active guidance

## Operating modes

### Narrow technical mode

Examples:

- fix code
- review module
- run tests
- generate tests

Rule:

- do not force the full artifact chain

### Presales / business mode

Examples:

- analyze customer requirement file
- fit-gap
- customer-facing FSD / Solution Design

Rule:

- do not jump into technical implementation detail too early

### Full delivery loop mode

Examples:

- customer requirement to analyzed, designed, implemented, tested, fixed, retested, and reported output

Rule:

- keep the whole loop explicit and synchronized through `Test Plan.md` and `Project Tracking.md`

## Office-file capability rule

`.docx`, `.xlsx`, `.xls`, `.csv`, and `.tsv` are treated as route-attached capabilities.

This means:

- requirement workbook analysis stays a presales route with spreadsheet capability
- customer-facing FSD or Solution Design stays the correct business/design route with DOCX capability
- a DOCX export of QA/QC content stays a QA/QC route with DOCX capability

This prevents office-file handling from distorting the primary workflow choice.

## Current proof points

Validated by:

- `python scripts/validate_layout.py`
- `python scripts/validate_skill_pack_contracts.py`
- `python scripts/validate_harness_evals.py`
- `python scripts/validate_no_stale_refs.py`

The current pack now has:

- flexible routing contracts
- harness references
- eval manifest coverage
- maintenance logging for loopholes and eval campaigns

## Recommended next upgrades

### Near-term

- build richer scenario replay support around `routing-workflow-evals.json`
- add more loop-sync pressure cases when real failures appear
- continue tightening helper-agent handoff language

### Medium-term

- add project-level delivery templates or stubs generated from artifacts
- add optional evidence schemas for test execution and defect reporting
- add richer route coverage for upgrade-specific and integration-heavy work

### Long-term

- semi-automated eval replay against controlled prompt fixtures
- version-specific pressure scenarios where Odoo 14-19 differences materially affect routing or code guidance

## Success definition

The pack is optimized when:

- the agent can handle both small and large tasks without overbuilding
- presales, technical, QA/QC, and tracking routes feel coherent
- artifacts remain traceable without becoming bureaucratic
- workflow changes are validated by harness thinking rather than trust alone
