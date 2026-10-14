# Canonical native handoffs — schema2 carrier

Read full current `protocols/role-returns.md`, `flow/phases.md`, `flow/run-state.md` and this runtime before dispatch/acceptance. These owners define the unmodified canonical return fields, statuses and conditional payloads; this document declares only package-local transport context. No copied reduced schema, ordinal scan map, new RETRY role status or worker control fields are accepted.

Each role returns one canonical object with phase, role, status, nonempty summary, runId, inputIdentity, candidateIdentity, contractVersion and real evidence; every phase/status requires its full owner payload. Parent extracts then validates shape/types/conditional fields, current identities, actual artifact containment/content, scope, independence and semantic acceptance before writing accepted state. Optional genuinely absent facts are omitted. Status aliases are not used in canonical records. The actual package helper binds contractVersion to `methodology-codex/2.0.0` and canonical phase spelling to lowercase bootstrap/architect/code/qa/review/debug/finalize; this is the declared package parsing/binding profile, not a change of neutral statuses or envelope fields.

Package record input:

```json
{"kind":"role","result":{"phase":"code","role":"coder","status":"SUCCESS","summary":"example only; replace with actual complete canonical return"},"context":{"sourceChange":{"mayEdit":["target-relative-owned-path"],"artifacts":["/absolute/real/authorized/artifact"]}}}
```

This schematic shortened result is NOT a valid phase return and authenticates no action. `result` must contain the full actual canonical owner-defined envelope and conditional payload. `context.sourceChange` is required on Code SUCCESS and Debug FIXED, and on parent-scoped observed partial Code BUG_REPORT/BLOCKED or Debug BLOCKED that records changed target bytes: target-relative exact granted mayEdit and actual absolute artifacts. It supplies scope evidence, not permission; parent verifies changes against the authentic grant and helper derives the fresh resulting target digest. Other judged phases use the latest accepted target digest. inputIdentity is the immutable state binding digest; candidateIdentity is the actual post-edit derived target digest on Code/Debug, not the stale pre-edit digest. First Architect plan binding allows only the declared pending plan creation/change, updates its actual digest once; unexpected drift refuses. Input/rules/framework/spec/adapter identities stay immutable.

Observed partial Code failure keeps its canonical BUG_REPORT or BLOCKED status; Debug may retain observed partial work with canonical BLOCKED. PARTIAL describes completeness and is not a new phase status or wire field. Only the parent can authorize changed candidate history through context.sourceChange, within persisted accepted Architect mayEdit and authentic current scope. Supply actual surviving partial/failure/regression evidence in context.sourceChange.artifacts plus original failure evidence; if a Code result includes artifacts, its list must agree with that context. Debug filesTouched, including deletions, remains separately compared with actual observed before/after source paths; a deleted path is not fabricated as a surviving artifact. All actual changes must fit the intersection of saved Architect scope and supplied mayEdit. Use freshly derived resulting candidateIdentity and retain old/new inventory/history, never the pre-edit digest or a phase-success claim. Helper checks actual containment/inventory/scope; parent judges authority, completed effects and failure meaning. Partial changes invalidate prior QA/Review and preserve baseline/immutable inputs. Code BUG_REPORT enters the shared causal Debug route with spend recorded before dispatch or exhaustion recorded at the cap; Code/Debug BLOCKED retains partial history and stops without a new success or extra Debug spend/refund. Worker flags provide no sourceChange authority, terminal restart or budget reset.

A parent response-correction event is separate from a role result:

```json
{"kind":"control","event":"response-correction","phase":"qa","reason":"actual extraction/schema failure","evidence":["/absolute/real/diagnostic"],"unknownEffect":false}
```

This parent control may optionally include context.sourceChange with the same mayEdit/artifacts shape, ONLY during Code or Debug after an explicit parent investigation establishes known completed effects. Record its real investigation and surviving artifacts; the helper validates the same persisted scope intersection and records observed candidate/history without accepting phase success. It has no canonical role candidateIdentity field: the helper derives the resulting digest from actual bytes. A worker flag cannot authenticate that investigation or supply parent control authority. unknownEffect=true refuses before accepting source change or replay, preserving the unresolved investigation dependency; it neither spends nor refunds Debug. Other phases cannot carry this sourceChange control. The exact implementation schema and measured limits are owned by the current tests/test_guide.md; no unsupported transport/extraction replay mechanism is introduced.

One correction per phase attempt, preserving errors/session/cost. Second unusable return stops BLOCKED or ESCALATED_FINALIZE; true unknownEffect blocks replay pending actual investigation. Neither wrapper alters shared return schema/enums. Parent-owned control is not worker consent, budget injection or repair authority.

Bootstrap SUCCESS supplies actual isEmpty/classificationHint/fileCount/files with path/summary/structure/relevance/recommendations and map. Architect SUCCESS supplies classification/projectType/taskType/planPath/slices/scope/ACs/deficiencies/specBlocked/visualGate and actual semantically ready plan; visual activation needs actual componentNodes/testsOnly, PASS actual command/exit/output/evidence/scannedNodes>=1. Human unresolved spec and required visual failure refuse Code. Code SUCCESS needs actual artifacts/testGuidePath/testSummary/deviations/AC/logs and applicable current final Code Doxygen command/exit/output/evidence/mapPath/identities. 
The legitimate written-host-prohibition Code Doxygen arm is exactly:

```text
doxygen={status:'NOT_APPLICABLE',reason,prohibition:{path,quote},evidence,candidateIdentity,inputIdentity}
```

Fill reason with actual applicability, path with the real contained target rule file, quote with its exact nonempty written prohibition, evidence with actual contained readable artifacts including that rule path, and identities with the current input and resulting candidate. The helper checks exact record fields/types, real rule/evidence containment, quote presence in actual rule bytes, current identities and bounded explicit denial syntax naming Doxygen. Such syntax recognition establishes only its finite text condition; the parent still judges actual controlling authority and applicability. Bare absence, a missing tool/configuration or “not needed” is not an exception. The accepted prohibition retains its actual whole-rule identity and is revalidated through QA, Review, Finalize and affected Debug changes against current input/candidate and unchanged rule bytes. A changed rule needs renewed parent authority/applicability judgment; old permission or a surviving quote cannot silently waive that check. Finalize doxygenPath may be genuinely omitted only under that currently verified retained prohibition, never null or a placeholder. Normal M19 package and inventory smoke remain map-applicable and require actual successful build/current XML evidence; this conditional arm cannot waive their promised maps.

Code/QA actionable BUG_REPORT carries populated goal, actual, logAnalysis, dataAnalysis, hypothesis, recommendation. BLOCKED names reason/limitations/evidence of requirement gap.

QA scans is a LIST, exactly eight objects, each id, status PASS/FAIL/N/A/BLOCKED, nonempty reason and actual evidence list:

- green-test-trap
- quantitative-ac
- semantic-trace
- infra-dod
- side-effect-channel
- secret-leak
- real-path-shape
- discriminating-test

No dict, ordinals, duplicate/missing/extra identity or new applicability boolean. Parent judges governing trigger, required AC and producing evidence/timing; false-trigger N/A cannot waive required coverage. QA also returns actual testSummary/findings/limitations; findings retain scan/code/severity/message/evidence and applicable path/line, secrets redacted. Full suite, whole log audit, every applicable PASS and every measured met criterion are owed. Review separately returns independent complete diff/scope/correctness/regression/side-effect findings/evidence/limits; accepted current Review precedes Finalize. Debug FIXED includes rootCause/fix/filesTouched/postFixAudit/testSummary/current origin/regression and consumed entry, renewed QA always. Finalize full RETURN-801–803 report/classification/plan/tests/log/applicable map/testSummary/AC/QA/Review/live/blastRadius/scopeDeviations/limitations/identities is required; doxygenPath is genuinely omitted only under the retained current verified prohibition described above, never null/placeholder; assigned Architect is producer, root consumer. Late repair is ESCALATED_FINALIZE, never silent edit.

Actual helper API:
`initialize(project, spec, approval, run_id, max_debug=4, *, framework, adapter, plan)` returns `(state_path,state)`; `advance(state,result)` returns a new state, preserves input on refusal; `save(path,state)` atomically stores accepted state or separately constructed diagnostic refusal record; `main` supplies CLI. Single root writer only.

```text
python3 FRAMEWORK_ROOT/skills/feature-dev/scripts/run_state.py init --project TARGET --spec SPEC --approval AUTHENTIC_APPROVAL_REFERENCE --framework FRAMEWORK_ROOT --adapter ADAPTER --plan PLAN --run-id RUN_ID --max-debug 4
python3 FRAMEWORK_ROOT/skills/feature-dev/scripts/run_state.py show --state STATE
python3 FRAMEWORK_ROOT/skills/feature-dev/scripts/run_state.py record --state STATE --result VERIFIED_PHASE_JSON
```

Resolve placeholders to actual authorized paths before execution; proposals are NOT_RUN. State `.methodology/runs/RUN_ID/state.json`, schema2. show validates current locks/resume without writes. Success0 JSON stdout, refusal2 with safe diagnostics stderr; record may retain refusal chronology while accepted progress/counters stay unchanged. No unreadable ledger replacement. Debug cap plain nonnegative int/strict decimal CLI default4, zero valid, bool/negative/fraction/unsupported extension refuse. Root persists spend before each Code/QA/Review-origin entry, retained once on failure/resume. Retry units separate; terminal/schema1/stale/malformed/unsafe artifacts refuse, never reset. The helper cannot authenticate an arbitrary approval string or judge mental reading/isolation; actual parent evidence remains required.

Source release is package3.0.0 over neutral3.0.0; contractVersion remains methodology-codex/2.0.0 and schema2. Source release and wire identity are separate; old input locks are not migrated.

## Historical C2 consumer route (retained scope)

Source2.2 adds the opt-in methodology-consumer-pm/1.0.0 carrier at references/consumer-pm-profile.md,13 seeds/four entries/shared consumer_files + orient/codemap/markup_migrate (six total helpers,27skills/73members/sixroles). Read full current owners and selected profile before native effects. Historical47/23/two input capacity remains historical; no input-lock migration. Explicit commands/grammars/authority/receipt/unknown-effect contracts live in the profile and package README. C3 automatic hooks/trust, C4 SDK/import/ingest/ledger comparison, C5 autonomous/resume proof and C6 loader activation remain held. Wire2.0/schema2/neutral1.1 remain unchanged. Claude runtime/version and the other58 of its59 package files remain unchanged; the sole source exception is the exact owner-approved one-line parity predicate in implementations/claude/tests/test_package_contract.py. Its shared23/Claude28 and all29 assertions are retained.

## Consequential decision packet

At the consequential-open trigger load full `prompting/brainstorm.md` through the current adapter binding. The authorized root coordinates its independent packet using the actual native collaboration mechanism; inner roles request it. Carry existing evidence references in the brief/plan/DEC/task, never a new canonical field or phase. Missing required proof holds dependent readiness; preserve reasoned routine/settled/forced exclusions and actual actor/source limits.

Current M30 binding: neutral2.0.0/source2.4.0; wire2.0/schema2 and C2 consumer mechanisms remain unchanged. The historical C2 paragraph above describes its accepted1.1/2.2 release, not current version acceptance. Consequential decisions load the current full brainstorm owner.
