# Transaction Safety Patterns

Use this reference when the task touches batch processing, cron jobs, duplicate-key handling, raw SQL, locking, or retry logic.

## When to load this file

- `savepoint()` or rollback behavior matters
- code may hit `IntegrityError`, `UniqueViolation`, or concurrency conflicts
- the task mixes ORM writes with raw SQL
- cron or batch flows must continue after partial failures

## Core rule

If a database statement fails, the PostgreSQL transaction is aborted until rollback.
Do not keep issuing ORM or SQL calls after a DB error unless the failing code was isolated by `savepoint()`.

## Safe patterns

### Per-record isolation in batches

```python
for row in rows:
    with self.env.cr.savepoint():
        try:
            record = self.create(row)
            record._post_create_checks()
        except ValidationError:
            raise
        except Exception as exc:
            _logger.warning("Skipping row %s: %s", row.get("name"), exc)
```

Use this for import jobs, cron processors, and upgrade scripts that must continue after one bad record.

### Unique key handling

```python
from psycopg2 import IntegrityError

with self.env.cr.savepoint():
    try:
        self.create({"code": code, "name": name})
    except IntegrityError:
        existing = self.search([("code", "=", code)], limit=1)
```

Prefer check-then-create when the key is cheap to search.
Use `savepoint()` when races are still possible.

### Lock before processing

```python
from psycopg2.errors import LockNotAvailable

with self.env.cr.savepoint(flush=False):
    try:
        self.env.cr.execute(
            "SELECT id FROM %s WHERE id = %%s FOR UPDATE NOWAIT" % self._table,
            (record.id,),
        )
    except LockNotAvailable:
        _logger.info("Record %s is locked elsewhere, skipping", record.id)
        return

record._process_locked_record()
```

Use this for cron workers or queue-like logic where parallel workers may grab the same record.

### Retry on serialization conflict

```python
import time
from psycopg2.errors import SerializationFailure

for attempt in range(3):
    try:
        return self.write(vals)
    except SerializationFailure:
        self.env.cr.rollback()
        if attempt == 2:
            raise
        time.sleep(0.05 * (2 ** attempt))
```

Use this only when the operation is safe to retry.

## Raw SQL rules

### Flush before SQL reads of ORM-managed fields

```python
self.env["sale.order"].flush_model(["state", "amount_total"])
self.env.cr.execute(
    """
    SELECT state, SUM(amount_total)
      FROM sale_order
     WHERE state IN %s
     GROUP BY state
    """,
    (("sale", "done"),),
)
```

### Invalidate cache after SQL writes

```python
self.env.cr.execute(
    "UPDATE my_model SET state = %s WHERE id = %s",
    ("done", record.id),
)
self.env.invalidate_all()
```

Do not trust cached ORM values after manual SQL writes.

## Commit discipline

- Do not call `commit()` inside ordinary business methods.
- Manual `commit()` is acceptable in long cron jobs, migration scripts, or controlled batch runners.
- If you manually commit, do it at stable checkpoints after the data is internally consistent.

### Safe cron checkpoint

```python
for chunk in self._iter_chunks():
    self._sync_chunk(chunk)
    self.env.cr.commit()
```

### Unsafe business-flow commit

```python
order = self.create(vals)
self.env.cr.commit()  # Avoid this inside request-driven business logic
order.action_confirm()
```

This can persist half-finished state that later steps cannot roll back.

## Common anti-patterns

### Swallowing DB errors without isolation

```python
try:
    self.create(vals)
except Exception:
    pass

self.search([])  # dangerous if the earlier exception was a DB error
```

### Mixing partial rollback assumptions with no savepoint

```python
try:
    self._write_many_records()
except IntegrityError:
    # Wrong assumption: outer transaction is still healthy
    self._continue_work()
```

### Committing before all dependent steps are done

```python
record = self.create(vals)
self.env.cr.commit()
record._generate_children()
```

## Checklist

- [ ] Any DB failure path is wrapped in `savepoint()` or followed by explicit rollback
- [ ] batch jobs isolate per-record failure
- [ ] lock-sensitive flows use `FOR UPDATE NOWAIT` when appropriate
- [ ] raw SQL reads flush first
- [ ] raw SQL writes invalidate ORM cache
- [ ] manual commits happen only at stable checkpoints
