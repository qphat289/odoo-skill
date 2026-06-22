# PostgreSQL Indexing Guide for Odoo

Use this reference when search domains, joins, or report queries are slow.

## Baseline rule

Run `EXPLAIN` or `EXPLAIN ANALYZE` before adding indexes. Indexes are not free.

## Common index choices

| Pattern | Good default |
|---|---|
| Equality, ranges, ordering | B-tree |
| Optional sparse field | partial or not-null B-tree |
| `ILIKE` / fuzzy name search | trigram |
| Frequent multi-column filter | compound index |

## Odoo-specific hints

- Index `Many2one` fields used in search domains, rules, and joins.
- Use `index='trigram'` for text fields used in name search or contains search.
- Use compound indexes when the same columns are filtered together repeatedly.
- Avoid indexing low-value booleans blindly; partial indexes are often better.

## Review checklist

- Does the slow query filter on unindexed fields?
- Does the plan still use `Seq Scan` after the new index?
- Will the new index hurt a hot write path?
- Is the query really better, or just differently expensive?

