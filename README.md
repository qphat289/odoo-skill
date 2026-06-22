# Odoo Development Skill Pack

Reusable Odoo skill pack for Codex, Claude Code, and other coding agents.

This repository is designed so another agent can set it up with minimal guessing: keep the repo available, point the runtime at `SETUP.md`, and let the agent choose native-skill mode or project-instruction mode for that host.

For repository behavior, `AGENTS.md` is the canonical instruction file. Host-specific files such as `CLAUDE.md`, `GEMINI.md`, `.cursorrules`, and similar wrappers should point back to `AGENTS.md` instead of duplicating the full workflow.

## Quick start

If you want another agent to install and use this pack correctly:

1. keep this repository available in the target workspace
2. tell the agent to use `SETUP.md`
3. tell the agent which runtime or IDE you are using
4. after setup, start work from `AGENTS.md` and the routed workflow

The shortest safe setup prompt is:

```text
Use SETUP.md in this repository and set up the Odoo skill pack for my IDE or agent runtime.
Detect whether it supports native skills or only project instructions.
Prefer project-scoped setup unless I ask for user-scoped reuse.
After setup, tell me the exact path or instruction file used and give me one smoke-test prompt.
```

## What this repo is

- `skills/odoo-development/`
  - Shared Odoo router.
- `skills/odoo-14.0/` through `skills/odoo-19.0/`
  - Version-specific Odoo skill packs.
- `skills/odoo-module-generation/`, `skills/odoo-models/`, `skills/odoo-security/`, `skills/odoo-views/`, `skills/odoo-owl/`, `skills/odoo-upgrade/`, `skills/odoo-quality/`
  - Core engineering domain skills.
- `skills/odoo-integrations/`, `skills/odoo-automation/`, `skills/odoo-business-domains/`, `skills/odoo-operations/`, `skills/odoo-presales/`
  - Extended domain skills that hold the main reusable references.
- `agents/`
  - Reusable subagent prompts for planning, review, testing, upgrade analysis, and context gathering.
- `workflows/`
  - End-to-end execution playbooks for generate, review, and upgrade tasks.
- `docs/correct-log/`
  - Correction log used to capture recurring mistakes and promote them into the canonical skills or rules.
- `rules/`
  - Cross-version coding and security rules used by skills, agents, and review flows.
- `scripts/`
  - Generic installer, platform wrappers, version detection, and validation helpers.
- `SETUP.md`
  - Agent-executable setup playbook.

## What `AGENTS.md` does

- `AGENTS.md` is the canonical repository instruction file.
- It explains the meaning of the main folders and the mandatory repository workflow.
- It tells the agent to detect the Odoo version, read the router skill, load the smallest matching domain skill, then load the correct workflow and rules.
- Host-specific files such as `CLAUDE.md`, `GEMINI.md`, `HERMES_SETUP.md`, `.cursorrules`, `.clinerules`, `.windsurfrules`, and `.github/copilot-instructions.md` are thin wrappers that should point back to `AGENTS.md`.

In practice:

- `AGENTS.md` = repository behavior
- `SKILL.md` = project-mode router entry
- `skills/.../SKILL.md` = packaged skill logic
- `workflows/...` = execution playbooks
- `agents/...` = helper roles or subagent prompts

## Design goals

- Keep `skills/` clean: only native skill folders.
- Keep the Odoo knowledge base split into discoverable domain skills.
- Keep a correction loop so repeated runtime mistakes can become reusable guidance.
- Keep `workflows/` as the primary execution standard.
- Let another agent read `SETUP.md` and install this pack without guessing paths.
- Support both project-scoped installs and user-scoped installs.
- Keep shared `agents/`, `workflows/`, `rules/`, and `scripts/` adjacent to the installed skill root because the packaged skills reference them directly.

## Canonical structure

```text
skills/
  odoo-14.0/
  odoo-15.0/
  odoo-16.0/
  odoo-17.0/
  odoo-18.0/
  odoo-19.0/
  odoo-development/
    SKILL.md
    agents/openai.yaml
    references/
  odoo-module-generation/
  odoo-models/
  odoo-security/
  odoo-views/
  odoo-owl/
  odoo-upgrade/
  odoo-quality/
  odoo-integrations/
  odoo-automation/
  odoo-business-domains/
  odoo-operations/
  odoo-presales/
rules/
agents/
workflows/
docs/correct-log/
scripts/
```

## Design standard

- `skills/` contains only native skill folders.
- Shared knowledge is split into domain skills instead of one oversized central pack.
- `skills/odoo-development/references/` is reserved for router and skill-authoring references, not the main execution knowledge base.
- `workflows/` are the canonical execution layer for task flows.
- `agents/`, `workflows/`, and `rules/` stay runtime-agnostic and can be reused by different hosts.
- `scripts/install_skill_pack.py` is the platform-neutral installer contract.

## Full Pipeline Artifacts

- `01-business-to-implementation-spec.md`
  - Business-facing scope artifact that merges mature presales output into delivery-ready requirements.
- `02-implementation-plan.md`
  - Technical execution artifact that turns the confirmed scope into ordered build work.

Template sources:

- `skills/odoo-presales/references/business-to-implementation-spec-template.md`
- `skills/odoo-module-generation/references/implementation-plan-template.md`

Repeat-bug prevention source:

- `skills/odoo-quality/references/common-bug-patterns.md`

## Full workflow

The normal end-to-end flow is:

1. `workflows/presales-discovery.md`
2. `workflows/fit-gap.md`
3. `workflows/proposal-handoff.md`
4. `01-business-to-implementation-spec.md`
5. `workflows/implementation-planning.md`
6. `02-implementation-plan.md`
7. `workflows/generate-module.md`
8. `workflows/review-module.md`
9. `workflows/test-module.md`
10. optional specialized passes such as:
    - `workflows/security-module.md`
    - `workflows/frontend-owl.md`
    - `workflows/generate-tests.md`
    - `workflows/upgrade-module.md`

Use `workflows/orchestrator.md` when the task is still broad and the agent must choose the right branch first.

## Available agents

These helper prompts live under `agents/` and are meant to support the main workflow, not replace it.

- `odoo-planner.md`
  - turns confirmed scope into `02-implementation-plan.md`
- `odoo-presales-consultant.md`
  - turns business-facing work into discovery, fit-gap, proposal, and `01-business-to-implementation-spec.md`
- `odoo-code-reviewer.md`
  - systematic review helper for correctness, security, and maintainability
- `odoo-upgrade-analyzer.md`
  - upgrade and migration analysis helper
- `odoo-tester.md`
  - test-focused helper for validating module behavior
- `odoo-context-gatherer.md`
  - gathers only the smallest useful context before implementation
- `odoo-code-tracer.md`
  - follows execution paths or bug traces through the codebase
- `odoo-domain-selector.md`
  - helps choose the smallest relevant Odoo domain skill
- `odoo-skill-finder.md`
  - finds the right skill or reference fragment quickly

## Available workflows

The current workflow set is:

- `orchestrator.md`
- `presales-discovery.md`
- `fit-gap.md`
- `proposal-handoff.md`
- `implementation-planning.md`
- `generate-module.md`
- `review-module.md`
- `test-module.md`
- `generate-tests.md`
- `security-module.md`
- `frontend-owl.md`
- `upgrade-module.md`
- `skill-maintenance.md`

## Support matrix

### Native skill installs

- Claude Code project skills: `.claude/skills/odoo-development/`
- Claude Code user skills: `~/.claude/skills/odoo-development/`
- Codex repo skills: `.agents/skills/odoo-development/`
- Codex user skills: `~/.agents/skills/odoo-development/`
- Any runtime with a native skill root can use `python scripts/install_skill_pack.py <that-skill-root>`

### Project-instruction support

- Cursor via `.cursorrules`
- GitHub Copilot via `.github/copilot-instructions.md`
- Gemini or Antigravity via `GEMINI.md`
- Windsurf via `.windsurfrules`
- Cline and Roo via `.clinerules`
- Hermes via `HERMES_SETUP.md` and `hermes-agent.json`
- OpenClaw via `openclaw-agent.json`

For Hermes and OpenClaw, the JSON agent configs now point to `AGENTS.md` as the canonical repository instruction, while `SKILL.md` stays the router for packaged skill discovery.

### Optional packaging

- Codex plugin packaging: `.codex-plugin/plugin.json`
- Claude plugin packaging: `.claude-plugin/plugin.json`

## Next step

Read `SETUP.md` and use the matching installer or host instruction file for the target runtime.

## Agent setup prompts

Use one of these prompts when you want another agent to install this pack for you.

### Generic prompt

```text
Use SETUP.md in this repository and set up the Odoo skill pack for my IDE or agent runtime.
Detect whether it supports native skills or only project instructions.
Prefer project-scoped setup unless I ask for user-scoped reuse.
Do not invent paths or claim auto-discovery that is not verified.
After setup, tell me the exact installed path or instruction file used, then give me one smoke-test prompt.
```

### Claude Code prompt

```text
Use SETUP.md and install this Odoo skill pack for Claude Code in this project.
Prefer native project skills under .claude/ unless something is unsupported.
After setup, tell me the exact path populated and give me one smoke-test prompt.
```

### Codex prompt

```text
Use SETUP.md and install this Odoo skill pack for Codex in this repository.
Prefer repo-scoped native skills under .agents/ unless something is unsupported.
Keep AGENTS.md active for repo-level guidance.
After setup, tell me the exact path populated and give me one smoke-test prompt.
```

### Project-instruction host prompt

```text
Use SETUP.md and configure this repository for my IDE in project-instruction mode.
Do not claim native skill installation unless the host actually supports it.
Point me to the exact instruction file I should use and give me one smoke-test prompt.
```

## Setup guidance by runtime

- If the runtime supports native skill folders, prefer native installation first.
- If the runtime only supports project instructions, keep this repository in the workspace and point the runtime to the correct wrapper file.
- For Codex and Claude Code, project or repo scope is usually the safest default.
- For cross-project reuse, use user scope only when the user explicitly wants it.
- For any runtime-specific uncertainty, `SETUP.md` is the source of truth for installation behavior.

## What a correct setup looks like

- The agent chose the right mode: native skill install or project-instruction mode.
- The target path or instruction file is stated explicitly.
- `agents/`, `workflows/`, `rules/`, and `scripts/` stay adjacent where the selected runtime expects them.
- The agent gives you one prompt to confirm the skill pack is discoverable and usable.

## Working model

The intended usage model is:

1. setup the pack with `SETUP.md`
2. let the runtime or wrapper point into `AGENTS.md`
3. let `AGENTS.md` route into `SKILL.md`, the right version skill, the right domain skill, and the right workflow
4. use helper agents only when the active workflow benefits from a specialized role
