---
id: concepts.glossary
title: Glossary
status: draft
---

# Glossary

This is the canonical neutral vocabulary for declared methodology protocol surfaces: assignments, specifications/plans, execution and assessment records, adapter/adoption descriptions and their public methodology references. It does not govern ordinary-language synonyms in explanatory prose or a target project's domain vocabulary. Detailed operational meanings remain at the linked current owners; this table does not create new wire enums or schemas.

<!-- anchor: concepts.glossary.scope -->

## Authority, scope and maintenance

- **GLOSS-101** MUST: Use each applicable canonical term below verbatim when naming its protocol concept on the declared surface under [language](../policies/language.md). Reference this authority rather than copying a competing table. Preserve target-domain vocabulary and authentic unpublished-history language under their actual destination rules.
- **GLOSS-102** MUST: Resolve a new applicable protocol concept in the selected duties to a source-backed owning entry in the same authorized change rather than inventing a local synonym. Preserve existing owner authority; report unknown/conflicting terms and actual table membership without claiming universal corpus vocabulary or extending scope to deferred knowledge content.
- **GLOSS-103** MUST: Check canonical-term uniqueness, any recorded source-form uniqueness and escaped-source/code-point equality separately under LANG-201/203. Check actual consumer use as a separate operation with named population, identities, readable inputs and limits. A unique reversible table does not prove consumer vocabulary use, execution adoption or enforcement.

This body contains exactly forty canonical entries in the following table. The number describes that finite table, not all historical words, all markers or complete source transfer. Full original house glossaries used source-language marker translations; their private population and detector counts are not the neutral population here. Public and unpublished destinations retain their actual [language scope](../policies/language.md); old donor exceptions are not new exclusions.

<!-- anchor: concepts.glossary.terms -->

## Canonical terms and current owners

| Canonical term | Neutral meaning and distinction | Current owning reference |
|---|---|---|
| owner | Human authority for goals and matching bounded decisions; not a worker/tool claiming consent. | [Gates](../process/gates.md), [role authority](../roles/_base.md) |
| assigned role | Explicitly invoked responsibility with its full contract and scope; reading another role does not assign it. | [Shared role contract](../roles/_base.md) |
| orchestrator | Parent coordinating actual transitions, one-writer state and integration, distinct from inner roles. | [Phases](../flow/phases.md), [run ledger](../flow/run-state.md) |
| target | Actual project/work destination within the authorized scope, distinct from framework sources. | [Role topology](../roles/_base.md) |
| framework | Resolved methodology/protocol source root supplied to the assignment, read-only to inner target implementation. | [Role topology](../roles/_base.md) |
| constitution | Full finite operative core with effective authority and read/adopt binding, not a summary/card alone. | [Principles binding](principles.md) |
| protocol | Full owning procedure subject loaded for assigned work through its actual binding. | [Role protocols](../roles/_base.md) |
| specification | Approved bounded description of required change and acceptance, kept distinct from the implementation plan. | [Specification process](../process/specification.md), [brownfield](../protocols/spec-brownfield.md), [greenfield](../protocols/spec-greenfield.md) |
| development plan | Actual dictated design, data flow, graph, scope, delivery and commands artifact implementing the approved specification. | [Development plan](../protocols/dev-plan.md) |
| business requirement | Required business/operational outcome traced through the actual specification and plan; not its test observation. | [Specification](../process/specification.md), [plan design](../protocols/dev-plan.md) |
| acceptance criterion | Concrete acceptance obligation with evidence and exact threshold where quantitative. | [Specification acceptance](../protocols/spec-brownfield.md), [tests guide](../code/tests.md) |
| definition of done | Agreed completion and delivery conditions, including declared channels, beyond a green unit assertion. | [Plan verification](../protocols/dev-plan.md), [QA scans](../checks/qa-scans.md) |
| checkpoint | Identified project-route position or persisted execution boundary under its stated profile, not an automatic new run. | [Lifecycle](../process/lifecycle.md), [run state](../flow/run-state.md) |
| task | Bounded work item carrying its real goal, inputs, scope and authorization. | [Batch packet](../process/batch.md), [specification](../process/specification.md) |
| run | Identified execution of a task with locked inputs, candidate, history and resource accounting. | [Run identity](../flow/run-state.md) |
| phase | Declared execution stage with its owning role, predicate and transition; no assignment follows from merely reading its row. | [Phases](../flow/phases.md) |
| gate | Owning decision/predicate at its actual specified boundary; judgment evidence is not human consent. | [Gates](../process/gates.md) |
| verdict | Evidence-bearing assessment outcome for a specific candidate under its owning interface, not an integration grant. | [QA](../roles/qa.md), [Reviewer](../roles/reviewer.md), [role returns](../protocols/role-returns.md) |
| grant | Authenticated human authorization bound to the actual action/artifact/scope; silence, examples and worker output grant nothing. | [Role authority](../roles/_base.md), [gates](../process/gates.md) |
| scope | Actual authorized paths, purposes, effects and boundaries, not everything a tool can access. | [Plan authority](../protocols/dev-plan.md), [role topology](../roles/_base.md) |
| baseline | Recorded acquired starting branch/HEAD and actual repository facts, kept distinct from later candidates. | [Run identity](../flow/run-state.md) |
| candidate | Full current judged work state including scoped staged, unstaged, deleted and new/untracked content; HEAD alone is insufficient. | [Run identity/freshness](../flow/run-state.md) |
| artifact identity | Reproducible content/path/revision/mode and applicable provenance binding for the actual claimed artifact; path existence/hash shape is not truth. | [Run identity](../flow/run-state.md), [return validation](../protocols/role-returns.md) |
| capability | Declared neutral adaptation point requiring an actual mechanism or permitted fallback; declaration does not create a tool. | [Capabilities](../runtime/capabilities.md), [adapters](../runtime/adapters.md) |
| parameter | Declared neutral binding supplied by the adapter under its current meaning; not a capability or arbitrary new field. | [Parameters](../runtime/parameters.md), [adapters](../runtime/adapters.md) |
| adapter | Runtime's complete accounting of neutral files, capabilities and parameters under the existing adapter contract/schema. | [Adapters](../runtime/adapters.md) |
| mechanism | Declared actual implementation/read/action path supplying a capability or assessment within its authority and limits. | [Adapter mechanisms](../runtime/adapters.md), [role runtime](../roles/_base.md) |
| fallback | Declared alternative used only under its actual absence/availability condition; never a generic semantic policy override. | [Adapters](../runtime/adapters.md), [role runtime](../roles/_base.md) |
| semantic adoption deviation | Actual anchored departure with reason, owning authority and applicable end date/trigger; different from an absent-tool fallback. | [Adapter adoption](../runtime/adapters.md), [role runtime](../roles/_base.md) |
| source assertion | Attributed claim from an identified source, retained with scope and qualification rather than presented as current measurement. | [Verification dimensions](../prompting/verification.md), [model claims](../policies/models.md) |
| measured finding | Observation obtained from an actual identified artifact/command/query within a declared population and unit. | [Verification](../prompting/verification.md), [quantitative acceptance](../code/tests.md) |
| computed finding | Derived result from declared authentic inputs and an explicit calculation; not independent measurement of those inputs. | [Verification](../prompting/verification.md) |
| estimated finding | Qualified approximation with assumptions and uncertainty; not a measured threshold satisfaction. | [Verification](../prompting/verification.md), [model policy](../policies/models.md) |
| unverified finding | Claim whose required evidence/access/inspection is missing or incomplete, carrying its limit rather than a fabricated PASS. | [Lint evidence](../checks/lints.md), [role returns](../protocols/role-returns.md) |
| check applicability | Actual trigger/profile determination with evidence; justified false trigger permits N/A where its owning interface allows it. | [QA scans](../checks/qa-scans.md), [lint evidence](../checks/lints.md) |
| Debug entry | Parent-counted causal entry into Debug, charged before entry and never refunded by local greens/retries or renaming. | [Run repairs](../flow/run-state.md) |
| QA visit | Initial or renewed independent QA assessment of the current candidate; it consumes no Debug entry itself. | [Phases](../flow/phases.md), [run repairs](../flow/run-state.md) |
| test-session attempt | Actual framework/session failure-counter unit under its declared hook/profile, separate from run-level Debug spend. | [Tests counter](../code/tests.md), [run retries](../flow/run-state.md) |
| terminal SUCCESS | Accepted terminal run outcome after current applicable phase/evidence predicates; does not itself authorize result integration. | [Run terminal](../flow/run-state.md), [gates terminal](../process/gates.md) |
| integration acceptance | Authentic owner decision over the concrete verified current result and matching integration action, separate from specification approval and run success. | [Gates result decision](../process/gates.md), [run terminal](../flow/run-state.md) |

<!-- anchor: concepts.glossary.profiles -->

## Scoped markers and status dialects

- **GLOSS-201** MUST: Interpret markers and statuses only in their owning interface/profile; preserve exact spelling, case, condition and meaning. Never normalize a suite pass, check PASS, role SUCCESS, terminal SUCCESS or integration acceptance into one substitute result, and never invent a wire value from descriptive prose.

The table names existing profiles and points to their full owners; it is a navigation aid, not a second registry or parser. Examples in code spans are quoted syntax, not live calls or declarations.

| Surface/profile | Existing markers/statuses | Interpretation and current owner |
|---|---|---|
| Neutral card | `id`, `title`, `status`; `stub`, `draft`, `stable` | Body maturity; draft is not runtime adoption. [FORMAT](../FORMAT.md) owns exact card grammar. |
| Neutral section/norm | `<!-- anchor: dotted.id -->`; `PREFIX-101`, `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY` | Anchored rule identity/force; heading or line number is not the anchor. [FORMAT](../FORMAT.md) owns grammar. |
| Adaptation call | `{{cap:name}}`, `{{param:name}}` | Actual declared runtime binding; quoted forms are examples. [FORMAT](../FORMAT.md), [capabilities](../runtime/capabilities.md), [parameters](../runtime/parameters.md) own declarations. |
| Adapter file | `reference`, `vendored`, `not-applied`; `overrides` | Accounting/adoption modes and actual conditional override evidence, not completeness from a reason string. [Adapters](../runtime/adapters.md) owns schema. |
| QA scan | `PASS`, `FAIL`, `N/A`, `BLOCKED` | All eight named scan rows with evidence/reason; required unknown proof cannot be N/A. [QA scans](../checks/qa-scans.md), [QA returns](../protocols/role-returns.md) own exact statuses. |
| Visual result | `PASS`, `NOT_APPLICABLE`, `SKIPPED` | Actual graph activation/threshold and verdict evidence; nonactivation needs reason. [Plan visuals](../protocols/dev-plan.md), [Architect return](../protocols/role-returns.md) own profile. |
| Role result | `SUCCESS`, `BUG_REPORT`, `BLOCKED`; Debug `FIXED`; Finalize `ESCALATED_FINALIZE` | Phase-dependent actual required payloads; parseable shape is not verified correctness. [Role returns](../protocols/role-returns.md) owns conditional values. |
| Terminal run | `SUCCESS`, `SPEC_BLOCKED`, `VISUAL_GATE_FAIL`, `ESCALATED`, `BLOCKED`, `ERROR`, `ESCALATED_FINALIZE` | Preserved terminal history; no automatic resume or erased spend. [Gates](../process/gates.md), [run state](../flow/run-state.md) own complete vocabulary. |
| Optional E2E return | `passed`, `failed`, `flaky` | Exact extension outcome; required AC cannot be satisfied by flaky. [Role returns](../protocols/role-returns.md) owns it. |
| Test guide/deferred observation | `TEST_DEFERRED`, `NOT_RUN` and explicit applicability explanation | Acceptance burden/observation remains unavailable or deferred, never covered by skipped tests. [Tests](../code/tests.md) owns evidence duties; these labels do not extend scan enums. |
| Code regions and contracts | `MODULE_CONTRACT`, `FUNC_`, `CLASS_`, `METHOD_`, region/end-region; `GREP_SUMMARY`, `STRUCTURE` | Actual language/host/locality profile, paired nesting and semantic meaning. [Exoskeleton](../code/exoskeleton.md) owns detailed field/placement rules. |
| LDD event | `[IMP:1-10][FUNCTION_NAME][BLOCK_NAME]`; structured `imp`, `func`, `block` | Host encoding of owned importance/function/block/event semantics, not a new universal operation field. [LDD](../code/ldd.md) owns levels/profiles. |
| Document/graph/prompt | paired `$START_`/`$END_`, `$DOCUMENT_PLAN`, `$CONTRACT`; DraftCodeGraph and `satisfies` | Actual collision-safe document/prompt or graph grammar; not interchangeable code regions. [Document](../protocols/document.md), [graph](../protocols/graph.md), [prompt markup](../prompting/prompt-markup.md) own profiles. |
| Project route/task | stable checkpoint/task identity and current-position convention | Actual adopted [lifecycle](../process/lifecycle.md), [conventions](../documents/conventions.md) and [batch](../process/batch.md); no imported private house marker or tracker. |

<!-- anchor: concepts.glossary.procedure -->

## Vocabulary assessment and reusable form

Actor: the scoped author/reader assesses meaning; its parent/owning authority resolves a conflicting rule or unapproved addition. Inputs: actual surface/population, destination language/privacy rules, glossary/current owner identities, source forms where applicable and actual readable consumers. Output: an authorized prose assessment with distinct table, notation, consumer and adoption conclusions. Assessment does not rewrite a consumer or broaden a scanner's scope by itself.

1. Declare the actual governed surface and distinguish published methodology, permitted unpublished history and target-domain terms.
2. Map every applicable protocol concept to its canonical entry and current owner. Preserve names/statuses at their real interfaces. Report unknown or duplicate competing authority; add a genuinely required source-backed entry only within authorized scope.
3. Check table term uniqueness. If source forms are recorded, separately check source uniqueness and exact reversibility: decode escape tokens while preserving literal separators/spaces and compare every ordered code point. Apply only the three contextual no-column classes under LANG-301; compare actual/declared population both ways and retain missing/stale/unparsed inputs.
4. Independently read the named consumer population and compare its actual protocol uses. Record synonym/conflict/unknown cases and access limits. Table success or reporter exit0 cannot imply consumers were read or that a second ignored declaration list was checked.
5. Report actual counts/units, evidence identity and both independent conclusions. Resolve contradictions through the existing owner; withhold an unsupported completeness/adoption claim. Unrelated authorized assessment may continue while missing access or approval is routed.

```text
VOCABULARY ASSESSMENT
Task/actor/authority: <actual assignment and bounded permitted action>
Surface/population: <protocol carriers and units; destination rules; domain/history exclusions>
Authority identity: <current glossary and each applicable owning subject/revision>
Term mapping: <actual source concept/use -> exact canonical term -> owning reference>
Table checks: <term uniqueness; source uniqueness if applicable; actual rows/readability>
Notation checks: <escaped source; full ordered code points; exact separators; equality; applicable exception and measured/declaration differences>
Consumer checks: <actual readable paths/occurrences; canonical/conflicting/unknown uses; unavailable/skipped scope>
Status/marker interpretation: <actual interface/profile; exact value; predicate and evidence; no cross-interface substitution>
Findings/provenance: <source/measured/computed/estimated/unverified category and actual basis>
Disposition/limits: <per-check results; required resolution; permitted next action; no inferred runtime enforcement/integration>
```

<!-- anchor: concepts.glossary.cases -->

## Complete supplied fictional cases

These exercises use declared inputs and expected outcomes; they supply no actual scanner/runtime/approval evidence. The forty entries above remain the real table; example-local strings below do not add canonical protocol terms.

**Valid bounded use with separate consumer proof.** Supplied task V1 permits read-only assessment of two public protocol records at revision v3. Both use `grant`, `candidate`, `QA visit` and `integration acceptance` with their meanings above. The supplied table has all forty distinct entries and linked owner identities. A translation input additionally supplies an example-local source mapping with a literal slash. The complete expected assessment is:

```text
VOCABULARY ASSESSMENT — fictional valid case
Task/actor/authority: V1; read-only assessor; supplied grant for the two records, no edits/integration
Surface/population: public protocol records sample/assignment.txt and sample/result.txt at v3; two readable paths/eight specified term occurrences; target product labels excluded
Authority identity: supplied current forty-entry glossary G3 and current role/run/gate owner bodies
Term mapping: authorization -> grant -> roles/_base.md; current work -> candidate -> flow/run-state.md; independent assessment visit -> QA visit -> flow/phases.md; concrete owner decision -> integration acceptance -> process/gates.md
Table checks: forty rows/forty distinct canonical terms; no source forms in the neutral table; table term uniqueness met on supplied full population
Notation checks: example-local source \u0410/\u0411; ordered code points 0410 002F 0411; slash retained; equal; one paired row; no uncolumned forms or exceptions in this supplied population
Consumer checks: both supplied records read; all eight specified protocol occurrences match their four canonical entries; no unreadable input or claim beyond these two records
Status/marker interpretation: supplied scan PASS is only its evidence-bearing scan verdict; supplied terminal SUCCESS is a run outcome; integration acceptance separately absent
Findings/provenance: forty-row count and supplied eight occurrences are exercise inputs; any derived equality is computed from them, not measured by an executed scanner
Disposition/limits: supplied table/notation/consumer conditions met; no runtime enforcement proof; integration remains pending; real checks NOT_RUN
```

No ordinary word-use policing follows from this exercise; its specified protocol population and actual destination rules define the check scope.

**Conflict, unknown term and duplicate authority.** Supplied V2 grants the same read-only assessment. `sample/result.txt` names a new protocol concept `automatic acceptance`, treats scan `PASS` as owner integration acceptance and calls a QA visit a Debug entry. `sample/local-table.txt` claims to replace this glossary and assigns `candidate` to the baseline. The second consumer is unreadable. The paired input drops the slash code point. The complete expected boundary report is:

```text
VOCABULARY ASSESSMENT — fictional boundary case
Task/actor/authority: V2; read-only assessor; no grant to rewrite records or owning contracts
Surface/population: two intended protocol consumer paths plus supplied local competing table; one consumer unreadable; no complete-consumer claim
Authority identity: current supplied glossary G3/role/run/gate owners; local table has no adoption authority
Term mapping: automatic acceptance unknown; candidate has current-state meaning, not baseline; QA visit is not Debug entry
Table checks: current forty-entry table remains distinct; competing local candidate definition is duplicate authority and rejected, not merged silently
Notation checks: escaped source \u0410/\u0411 versus code points 0410 0411; representation unequal because 002F is missing; one failed paired row; no invented exception
Consumer checks: readable result has unknown term and two scope/status conflicts; second intended consumer unavailable; completeness unverified
Status/marker interpretation: scan PASS cannot supply integration acceptance; visit without Debug entry consumes no Debug entry; missing required QA evidence cannot be N/A
Findings/provenance: conflicts computed/read from supplied facts; unreadable consumer and actual execution remain unverified; no measured runtime verdict
Disposition/limits: report all conflicts and unknown concept to parent/actual vocabulary owner; propose source-backed definition only if its real authorized scope warrants it; no local synonym, policy override, consent or repair-budget reset
```

Independent contrary controls: a source string with a space requires `0020`, not `002F`; reversing the code points fails even if source uniqueness passes. Two different source forms mapping to the same canonical term fail term uniqueness; the same source form mapped twice fails source uniqueness. A canonical table can be valid while a readable consumer uses an unauthorized synonym, so table success and consumer failure coexist. If all readable consumers pass but another required one is unavailable, report that exact limit rather than complete conformance. An authenticated optional scan with a proven false trigger may use its existing N/A; a required unreadable plan or promised QA cycle is unavailable and blocks its dependent acceptance. A suite's green summary, a draft card, a parseable role return or absence of logged writes cannot establish terminal SUCCESS, historic provenance or integration acceptance. Historical sources and current measured findings retain distinct labels; computed and estimated numbers do not become measured facts by fluent wording.
