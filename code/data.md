---
id: code.data
title: Data transformation
status: draft
---

# Data transformation

This contract covers data-heavy ETL and relational transformations. Native stack choices, queries, schema access and
transaction mechanisms belong to the target and its adapter; this document supplies no database or staging engine.
Python dataframe examples illustrate one source profile, not a mandatory dependency or a benchmark.

<!-- anchor: code.data.strategy -->

## Measure before choosing a strategy

- **DATA-101** MUST: Before planning data-heavy work, load the applicable transformation contract through {{cap:skill-loading}}. Measure the actual schema, key types, population/window, input shape, row and byte volume, available memory, operation complexity and existing stack. Read the real schema through authorized read-only tools; never guess columns or keys. Record unavailable inputs and their effect on the strategy.
- **DATA-102** SHOULD: Prefer transparent dataframe steps when the actual project uses Python and measured data fits memory. This source-profile preference makes intermediate results inspectable; it is not proof that every model performs better in a particular library. Large inputs can exhaust in-memory processing, and row-wise iteration or a query per row can make a functional solution impractical.
- **DATA-103** MUST: Evaluate volume and complexity before loading full tables or choosing an iterative calculation. When memory or iteration limits defeat the dataframe strategy, choose an appropriate database-first or bounded strategy from actual target evidence. Obtain specialized help only through the parent's authorized delegation; a strategy change does not grant new tooling or schema authority.

<!-- anchor: code.data.loading-joins -->

## Loading, keys and immediate join diagnostics

- **DATA-201** SHOULD: Prefer a filtered single-table load when it supplies the required inputs. A one-level join still requires immediate diagnostics; its simple syntax does not prove safe cardinality.
- **DATA-202** MUST: Immediately after loading a join, expose source row counts and actual result length, then check expected key/cardinality/type/null/duplicate/unmatched conditions and row multiplication or loss. Source-profile examples are source `COUNT(*)` and result `len(df)`. Equal aggregate counts alone can conceal both lost and duplicated records; compare the relevant keyed populations and intended join relationship.
- **DATA-203** MUST: Avoid string-key joins and use integer keys in the applicable relational source profile. Inspect the real key schema first; the original guide treats string joins as an architectural warning, not a license to invent conversions, coerce keys or migrate a schema. If the actual required schema conflicts with that directive, expose the conflict for its owning decision instead of silently weakening it or forcing a migration.
- **DATA-204** SHOULD: For low-cardinality string columns in the dataframe profile use the stack's category representation where appropriate, checking actual values and semantics. The source example `astype('category')` is memory/processing guidance, not permission to change stored types or discard values.

<!-- anchor: code.data.iteration -->

## Vectorization and bounded loops

- **DATA-301** MUST: Use the applicable stack's vectorized or set-oriented transformations rather than an avoidable row loop. The dataframe source examples include column arithmetic, grouping, merge and its fuller apply profile; selecting one of these names alone does not prove vectorization or performance. Measure the actual operation shape and intermediates.
- **DATA-302** MUST: In the retained dataframe source profile, restrict row iteration to small inputs, approximately 5000 rows or less. Treat SQL inside a row loop as the N+1 anti-pattern; only when unavoidable retain the source's 100–200-iteration bound, document why it is unavoidable and measure actual rows, queries and iterations. These approximate source-profile limits are not universal measured performance thresholds or an unlimited exception. A conflicting required workload needs an explicit strategy/authority resolution.

<!-- anchor: code.data.staging -->

## Authorized transactional staging and persistence

- **DATA-401** MUST: For an authorized job that writes transformed results, build the result with explicit insert/update/delete intent, represented by I/U/D in the staging source profile. Export that staging result in ONE transaction and apply the intended destination changes atomically using actual target mechanisms. The example insert/update statements do not implement the delete case: verify each applicable D outcome or state explicitly that deletion is unsupported or missing; do not claim all three operations delivered.
- **DATA-402** MUST: Define staging and destination ownership, transaction boundary, rollback behavior and key/null/duplicate acceptance. Verify actual persisted destination outcomes and diagnostic staging content when a database sink is a deliverable. A mocked connection or export call proves only invocation; [tests](tests.md), [LDD](ldd.md) and the plan's delivery contract retain real-sink obligations.
- **DATA-403** MUST: Preserve the staging table and its diagnostic trace after the run; the retained profile clears its owned staging contents at the beginning of the next owned run. Apply that lifecycle only within explicit job ownership and authorization. Never drop or clear shared/production data without permission; an authorization conflict is a disclosed prerequisite, not an automatic cleanup step. Temporary intermediates also need an authorized lifecycle.

<!-- anchor: code.data.decomposition -->

## Observable simple steps

- **DATA-501** MUST: Decompose a complex transformation into observable Filter → Enrich → Aggregate stages with inspectable intermediate results. When problems arise, immediately split the logic into individual diagnostic steps. Source SQL examples create filtered, joined/enriched and grouped intermediate tables; actual dialect, names, permissions and persistence belong to the target.
- **DATA-502** MUST: Keep individual blocks logically simple; avoid short dense expressions that obscure conditions and intermediate evidence. Follow the [exoskeleton](exoskeleton.md) and [navigation](navigation.md) containers under target rules, and log authored meaningful flow through [LDD](ldd.md).
- **DATA-503** SHOULD: Prefer understandable linear steps with modest repetition over over-engineered abstraction when that helps agent inspection. This preference does not prohibit the constitution's authorized DRY or modularity, impose a universal line count or require duplication of every operation.
