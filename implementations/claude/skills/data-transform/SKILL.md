---
name: data-transform
description: "Сложная трансформация данных: «ETL», «джойн таблиц на Pandas или SQL», «перелить данные между схемами». Use when planning or writing a complex data transformation, join or other data-heavy change (ETL, Pandas, SQL) and the choice of approach depends on the real schema and population."
---

# data-transform

Choose and verify a data transformation from the real schema and measured volumes, not from assumptions.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../code/data.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Read the actual schema or API first (`information_schema`, the database client's describe command, or the API definition) and measure the real population: row counts, key uniqueness, null and duplicate rates. Never guess a column or table name.
2. Choose Pandas-first or SQL-first from that evidence (where the data lives, its size, what must be transactional). Prefer vectorized operations and small named stages over row loops.
3. Count source and result rows at each stage and diagnose join expansion or loss explicitly; record the counts as evidence.
4. Test against read-only reference data and against isolated resources created through the API under test. Transactional staging with insert, update and delete, and its lifecycle, apply only inside granted jobs.
5. Report the measured counts and any stage you could not verify.

Limits:
- Do not clear shared data, mutate a shared database for a test, or invent universal volume benchmarks.
- Credentials follow the credentials policy: names and presence only, never values in artifacts.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.
