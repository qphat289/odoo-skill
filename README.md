# Odoo Development Skill Pack

Reusable Odoo skill pack for Codex, Claude Code, and other coding agents.

## What this repo is

- `skills/odoo-development/`
  - Shared Odoo router.
- `skills/odoo-14.0/` through `skills/odoo-19.0/`
  - Version-specific Odoo skill packs.
- `skills/odoo-module-generation/`, `skills/odoo-models/`, `skills/odoo-security/`, `skills/odoo-views/`, `skills/odoo-owl/`, `skills/odoo-upgrade/`, `skills/odoo-quality/`
  - Core engineering domain skills.
- `skills/odoo-integrations/`, `skills/odoo-automation/`, `skills/odoo-business-domains/`, `skills/odoo-operations/`
  - Extended domain skills that hold the main reusable references.
- `agents/`
  - Reusable subagent prompts for planning, review, testing, upgrade analysis, and context gathering.
- `workflows/`
  - End-to-end execution playbooks for generate, review, and upgrade tasks.
- `rules/`
  - Cross-version coding and security rules used by skills, agents, and review flows.
- `scripts/`
  - Generic installer, platform wrappers, version detection, and validation helpers.
- `SETUP.md`
  - Agent-executable setup playbook.

## Design goals

- Keep `skills/` clean: only native skill folders.
- Keep the Odoo knowledge base split into discoverable domain skills.
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
rules/
agents/
workflows/
scripts/
```

## Design standard

- `skills/` contains only native skill folders.
- Shared knowledge is split into domain skills instead of one oversized central pack.
- `skills/odoo-development/references/` is reserved for router and skill-authoring references, not the main execution knowledge base.
- `agents/`, `workflows/`, and `rules/` stay runtime-agnostic and can be reused by different hosts.
- `scripts/install_skill_pack.py` is the platform-neutral installer contract.

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

### Optional packaging

- Codex plugin packaging: `.codex-plugin/plugin.json`
- Claude plugin packaging: `.claude-plugin/plugin.json`

## Next step

Read `SETUP.md` and use the matching installer or host instruction file for the target runtime.
