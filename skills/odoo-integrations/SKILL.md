---
name: odoo-integrations
description: Domain skill for Odoo controllers, external APIs, import/export, website integrations, attachments, and source-verification patterns across Odoo 14-19.
---

# Odoo Integrations

Use this skill when the task involves HTTP controllers, JSON routes, third-party APIs, file exchange, website behavior, or binary attachment flows.

## Quick reference

| Topic | File | When to use |
|---|---|---|
| Controllers and routes | `references/controller-api-patterns.md` | HTTP endpoints, JSON controllers, request handling |
| API version notes | `references/api-version-notes-17.md` to `references/api-version-notes-19.md` | Version-sensitive route/auth differences |
| External APIs | `references/external-api-patterns.md` | Third-party service calls and sync jobs |
| Import and export | `references/import-export-patterns.md` | CSV, Excel, batch sync, import pipelines |
| Website integration | `references/website-integration-patterns.md` | Website forms, portal-facing flows, site hooks |
| Binary attachments | `references/attachment-binary-patterns.md` | Files, images, `ir.attachment`, downloads |
| GitHub fetch patterns | `references/github-fetch-patterns.md` | Pulling official source examples for verification |
| GitHub verification | `references/github-verification-guide.md` | Verifying syntax against official Odoo code |

## Rules

1. Pair this skill with the active version skill before copying route, request, or asset syntax.
2. Use `odoo-security` when a controller or integration exposes access-sensitive data.
3. Use `odoo-operations` when the task also needs validation, logging, or debugging guidance.
4. When the target is 17, 18, or 19, load the matching `api-version-notes-<version>.md` before finalizing route/auth choices.
