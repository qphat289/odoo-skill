# Odoo Profiling Guide

Measure first, optimize second.

## Profiling ladder

| Tool | Best use |
|---|---|
| Access logs | First pass for query count and response split |
| Odoo.sh monitoring | Hosted environments and production-safe observation |
| Stack dump / hang inspection | Production hangs or blocked workers |
| Embedded profiler | Local reproduction and deeper call analysis |

## What to look for

- High SQL count: usually batching or N+1 problem
- Low SQL count but high SQL time: missing index or poor query plan
- Low SQL time but high Python time: compute-heavy or serialization-heavy code

## Good workflow

1. Reproduce the same action reliably.
2. Capture baseline timing and query count.
3. Apply one focused change.
4. Measure again with the same setup.
5. Keep the proof in the review note or commit message.

## Practical rules

- Profile warm requests, not only the first cold request.
- Use realistic data volume before concluding a fix worked.
- Prefer scriptable reproduction over manual clicking when possible.
- Pair this guide with `postgresql-indexing-guide.md` when SQL time dominates.

