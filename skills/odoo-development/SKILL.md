---
name: odoo-development
description: Odoo development router for Odoo 14-19. Use when the version is unknown at first or when the task spans multiple domains such as module scaffolding, models, security, views, OWL, upgrade, testing, or performance.
---

# Odoo Development

Use this skill as the top-level router for the Odoo pack. Once the version and domain are known, switch to the matching version skill and domain skill.

## Mandatory procedure

1. Detect or confirm the target Odoo version before writing code. If needed, run `python ../../scripts/detect_odoo_version.py`.
2. Switch to the matching version-specific skill:
   - `../odoo-14.0/SKILL.md`
   - `../odoo-15.0/SKILL.md`
   - `../odoo-16.0/SKILL.md`
   - `../odoo-17.0/SKILL.md`
   - `../odoo-18.0/SKILL.md`
   - `../odoo-19.0/SKILL.md`
3. Load the matching domain skill:
   - `../odoo-module-generation/SKILL.md`
   - `../odoo-models/SKILL.md`
   - `../odoo-security/SKILL.md`
   - `../odoo-views/SKILL.md`
   - `../odoo-owl/SKILL.md`
   - `../odoo-upgrade/SKILL.md`
   - `../odoo-quality/SKILL.md`
   - `../odoo-integrations/SKILL.md`
   - `../odoo-automation/SKILL.md`
   - `../odoo-business-domains/SKILL.md`
   - `../odoo-operations/SKILL.md`
4. Read the matching workflow in `../../workflows/`.
5. Read only the references needed for the version and domain.
6. Read `../../rules/security.md` and `../../rules/coding-style.md` when generating or reviewing code.
7. Use helper prompts from `../../agents/` only when they materially improve the task.
8. Verify uncertain syntax against official Odoo docs or source.
9. Validate security, manifest order, and tests before finishing.

## Quick reference

| Domain | Skill | When to use |
|---|---|---|
| Version routing | `odoo-14.0` to `odoo-19.0` | Choose exact version before coding |
| Module scaffolding | `odoo-module-generation` | Manifest, file tree, scaffold, install order |
| ORM and model logic | `odoo-models` | Fields, domains, computes, inheritance, CRUD |
| Security | `odoo-security` | ACL, record rules, groups, multi-company |
| XML and reports | `odoo-views` | Views, QWeb, actions, menus, reports, wizards |
| OWL and frontend | `odoo-owl` | OWL components, assets, web client changes |
| Upgrade and migration | `odoo-upgrade` | Version deltas, migration references, troubleshooting |
| Testing and performance | `odoo-quality` | Tests, review checks, performance and validation |
| Integrations | `odoo-integrations` | Controllers, import/export, APIs, website, attachments |
| Automation | `odoo-automation` | Cron jobs, sequences, mail, background flows |
| Business flows | `odoo-business-domains` | Sales, stock, accounting, HR, project, pricing patterns |
| Operations | `odoo-operations` | Settings, validation, debugging, error handling, i18n |

## Router-only references

Keep `references/` under this skill for repository routing and skill-authoring material only.
Do not treat it as the main implementation knowledge base when a domain skill already exists.

## Hard rules

- Never guess the Odoo version when the manifest is missing or unclear.
- For Odoo 17+, use direct XML attributes such as `invisible="expr"` instead of `attrs`.
- For Odoo 16+, prefer `Command` for x2many operations.
- For Odoo 17+, use `@api.model_create_multi` for `create()`.
- For Odoo 18+, use `_check_company_auto = True`, `check_company=True`, keep record rules on `company_ids`, and use `allowed_company_ids` only for Python/context propagation when needed.
- Every model needs access rights in `security/ir.model.access.csv`.
