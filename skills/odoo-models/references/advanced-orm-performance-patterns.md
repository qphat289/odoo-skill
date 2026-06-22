# Advanced ORM Performance Patterns

Use this reference when standard model patterns are not enough and the task depends on ORM internals, batching, cache behavior, or large-recordset performance.

## Recordset iteration

- Iterate directly over recordsets instead of indexing `self[i]`.
- Batch reads and writes whenever possible.
- Avoid per-record `search_count()` inside compute methods.

## Prefetch awareness

- First field access can prefetch stored fields for the full recordset.
- `fetch()` is useful when you need a narrow field subset on large recordsets.
- Be careful when inherited logic later touches fields outside the fetched set.

## Compute method discipline

- Do not mix stored and non-stored fields in the same compute method.
- Keep stored compute logic user-independent when `compute_sudo=True` is involved.
- Prefer batch aggregation with `_read_group()` over repeated per-record counts.

## Raw SQL safety

- Flush ORM state before raw `SELECT` that depends on pending writes.
- Invalidate cache after raw `UPDATE` or `DELETE`.
- Treat raw SQL as a performance escape hatch, not the default.

## Domain scaling patterns

- Prefer `any` domains for parent-child existence checks.
- Prefer `_search()` query objects over large intermediate ID lists when chaining searches.
- Review `_order` carefully when it traverses `Many2one` chains because it can introduce expensive joins.

