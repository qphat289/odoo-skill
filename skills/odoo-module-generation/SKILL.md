---
name: odoo-module-generation
description: Domain skill for Odoo module scaffolding, manifest design, install order, file tree conventions, and module skeletons across Odoo 14-19.
---

# Odoo Module Generation

Use this skill when the task is about creating a module, shaping the file tree, writing `__manifest__.py`, or validating install/data ordering.

## Quick reference

| Topic | File | When to use |
|---|---|---|
| Shared overview | `references/odoo-module-generator.md` | Pick the right version file |
| Checklist | `references/odoo-module-checklist.md` | Pre-flight or handoff checklist |
| Manifest/data ordering | `references/odoo-manifest-data-order.md` | Security, data, views ordering |
| XML and CSV data files | `references/xml-data-loading-patterns.md` | `record`, `ref`, `eval`, `noupdate`, CSV `:id` |
| Templates | `references/common-module-templates.md` | Reusable skeletons and file stubs |
| Technical Design | `references/technical-design-template.md` | Turn Functional Design and Solution Design into dev-ready implementation design |
| Technical Design example | `references/technical-design-example-sale-approval.md` | See a realistic technical design that matches the QA/QC and tracking examples |
| Project Tracking | `references/project-tracking-template.md` | Break Technical Design into phase/module/task status tracking |
| Project Tracking example | `references/project-tracking-example-sale-approval.md` | See a realistic delivery tracker that matches a full QA/QC loop |
| Version files | `references/odoo-module-generator-<version>.md` | Real scaffold and manifest rules per version |
| Upgrade deltas | `references/odoo-module-generator-<from>-<to>.md` | Migration-sensitive module changes |

## Rules

1. Load the exact version file before generating a module.
2. Use `references/odoo-manifest-data-order.md` whenever XML or CSV ordering matters.
3. Use `references/xml-data-loading-patterns.md` when authoring install/demo/security data files.
4. Pair this skill with `odoo-models`, `odoo-security`, and `odoo-views` for full implementation work.
