# Odoo Skill Pack Setup

Use this file as an execution playbook.

If you are an AI agent asked to install this Odoo pack for a user, do not improvise the layout. Detect the target runtime, choose the matching install mode below, run the generic installer or a platform wrapper, then validate the result.

## Goal

Install the packaged Odoo skills into the user's preferred runtime with the correct combination of native skill discovery and adjacent support folders.

## Source of truth

- Shared router skill: `skills/odoo-development/`
- Version skills: `skills/odoo-14.0/`, `skills/odoo-15.0/`, `skills/odoo-16.0/`, `skills/odoo-17.0/`, `skills/odoo-18.0/`, `skills/odoo-19.0/`
- Skill metadata: `skills/odoo-development/agents/openai.yaml`
- Shared workflows: `workflows/`
- Shared helper prompts: `agents/`
- Shared cross-version rules: `rules/`
- Generic installer: `scripts/install_skill_pack.py`
- Platform wrappers: `scripts/install_for_claude.ps1`, `scripts/install_for_codex.ps1`
- Version detector: `scripts/detect_odoo_version.py`
- Validator: `scripts/validate_layout.py`

## Preflight

Before installing:

1. Identify the target runtime.
2. Identify whether the user wants project-scoped or user-scoped installation.
3. Identify the target project path when using project scope.
4. Run `python scripts/validate_layout.py` in this repository.
5. Use `python scripts/detect_odoo_version.py` when the user also wants runtime Odoo-version detection guidance.
6. Only then run the installer.

## Runtime matrix

### Generic native skill host

- Required concept: one filesystem root that contains `skills/<skill-name>/SKILL.md` or equivalent per-host skill folders
- Required adjacency: sibling `agents/`, `workflows/`, `rules/`, and `scripts/` next to that skill root
- Preferred installer: `python scripts/install_skill_pack.py <skill-root>`
- Use this when the runtime is not Claude/Codex but still supports file-based skill discovery

Install command:

```powershell
python scripts/validate_layout.py
python scripts/install_skill_pack.py C:\path\to\skill-root --force
```

### Claude Code

- Native project skill path: `.claude/skills/<skill-name>/SKILL.md`
- Native user skill path: `~/.claude/skills/<skill-name>/SKILL.md`
- Required adjacency: `.claude/agents/`, `.claude/workflows/`, `.claude/rules/`, `.claude/scripts/`
- Best default for one repository: project scope
- Best default for reuse across many repositories: user scope
- Plugin mode is optional and secondary; prefer native skill install first

Install commands:

```powershell
python scripts/validate_layout.py
powershell -ExecutionPolicy Bypass -File scripts/install_for_claude.ps1 -Scope project -TargetPath C:\path\to\target-repo
```

```powershell
python scripts/validate_layout.py
powershell -ExecutionPolicy Bypass -File scripts/install_for_claude.ps1 -Scope user
```

### OpenAI Codex

- Native repo skill path: `.agents/skills/<skill-name>/SKILL.md`
- Native user skill path: `~/.agents/skills/<skill-name>/SKILL.md`
- Required adjacency: `.agents/agents/`, `.agents/workflows/`, `.agents/rules/`, `.agents/scripts/`
- Best default for one repository: repo scope
- Best default for reuse across many repositories: user scope
- Plugin mode is optional and secondary; prefer native skill install first

Install commands:

```powershell
python scripts/validate_layout.py
powershell -ExecutionPolicy Bypass -File scripts/install_for_codex.ps1 -Scope repo -TargetPath C:\path\to\target-repo
```

```powershell
python scripts/validate_layout.py
powershell -ExecutionPolicy Bypass -File scripts/install_for_codex.ps1 -Scope user
```

### Project-instruction hosts

- Cursor: use `.cursorrules`
- GitHub Copilot: use `.github/copilot-instructions.md`
- Gemini or Antigravity: use `GEMINI.md`
- Windsurf: use `.windsurfrules`
- Cline and Roo: use `.clinerules`
- Hermes: use `HERMES_SETUP.md` and `hermes-agent.json`
- OpenClaw: use `openclaw-agent.json`

For these hosts, do not claim native skill installation unless their current documentation explicitly supports a matching skill root. The safe default is project-instruction mode: keep this repository available in the workspace, then follow the host-specific instruction file above.

## Agent procedure

When a user says "use SETUP.md and install this Odoo pack for my IDE", follow this exact procedure:

1. Detect the IDE or runtime.
2. Decide whether that runtime supports native skills or only project instructions.
3. If it exposes a generic native skill root, prefer `python scripts/install_skill_pack.py`.
4. Otherwise map it to `Claude Code` or `OpenAI Codex` if applicable.
5. Otherwise keep the repository in project mode and rely on the host-specific instruction file.
6. Prefer native skill installation over plugin installation when native support exists.
7. Prefer project or repo scope unless the user explicitly wants cross-project reuse.
8. Run `python scripts/validate_layout.py`.
9. Run the generic installer or the matching wrapper when native skill install is supported.
10. Confirm that the destination now contains `odoo-development/SKILL.md` and the adjacent support folders.
11. Tell the user the exact discovery path or project instruction file that was populated.
12. Give the user one smoke-test prompt.

## Validation criteria

An installation is correct only if all of the following are true:

- Destination folder contains `odoo-development/SKILL.md`
- Destination folder contains version skills from `odoo-14.0` through `odoo-19.0`
- Shared router skill contains `references/`
- Adjacent support folders exist for `agents/`, `workflows/`, `rules/`, and `scripts/`
- Root skill repo still validates with `python scripts/validate_layout.py`
- The runtime-specific discovery path matches the matrix above

## Smoke tests

Use one of these after install:

- "Use the Odoo development skill and review this addon for Odoo 18 security issues."
- "Use the Odoo development skill and scaffold a new Odoo 18 module with one model and access rights."
- "Use the Odoo development skill and tell me which reference file to load for OWL work in Odoo 19."

## Notes

- Do not claim that the knowledge base is auto-loaded from arbitrary folders.
- Do not treat `agents/` or `workflows/` as native runtime registries unless that runtime explicitly supports them.
- Prefer the generic installer when the runtime exposes a simple skill root and does not need a host-specific wrapper.
- For Codex project behavior, keep `AGENTS.md` in the working repository when you want additional repo-level instructions.
- For Claude project behavior, keep `CLAUDE.md` in the working repository when you want additional repo-level instructions.
- For project-instruction hosts, keep the repository in the workspace and point the runtime at the matching host instruction file instead of claiming a native install that has not been verified.
