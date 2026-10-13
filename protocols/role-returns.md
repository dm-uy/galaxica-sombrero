---
id: protocols.role-returns
title: Role returns
status: draft
---

# Role returns

A role return is the producer's evidence-bearing claim, not an instruction to advance. Bind structured delivery through {{cap:structured-output}} and keep producer and authoritative consumer contracts aligned. Field names below are neutral interface names; an adapter declares any serializer/alias spelling and exposes one versioned canonical contract.

<!-- anchor: protocols.role-returns.envelope -->

## Common envelope

- **RETURN-101** MUST: Every return includes `phase`, `role`, `status`, nonempty `summary`, `runId`, `inputIdentity`, `candidateIdentity`, `contractVersion` and actual `evidence` references. Match the assigned current phase and role and the locked run/inputs/candidate; evidence paths identify real readable artifacts in authorized roots.
- **RETURN-102** MUST: Use only declared phase statuses: Bootstrap and Architect use SUCCESS or BLOCKED; Code, QA and Review use SUCCESS, BUG_REPORT where actionable, or BLOCKED; Debug uses FIXED or BLOCKED; Finalize uses SUCCESS, BLOCKED or ESCALATED_FINALIZE. Missing, null, empty or unknown statuses are rejected, never normalized to success. Reject unsupported phase/status pairs before choosing a route; Bootstrap/Architect refusals map to the canonical SPEC_BLOCKED, VISUAL_GATE_FAIL, BLOCKED or ERROR outcomes as applicable under GATE-1203. An adapter may declare PASS as the alias for role SUCCESS and FAIL as the actionable QA BUG_REPORT alias at its parsing boundary.
- **RETURN-103** MUST: Distinguish role SUCCESS from overall completion. A phase SUCCESS satisfies only that phase's validated predicate and goes to the next declared consumer; overall SUCCESS requires Finalize and the concrete result still needs its separate owner decision.
- **RETURN-104** MUST: Reject unknown fields unless an adapter extension explicitly declares their type, meaning, producer, consumer, required conditions and version before use. Compatibility aliases are accepted only at the declared parsing boundary; canonical serialization has one spelling, preserves every typed field and exposes exactly the agreed contract surface.
- **RETURN-105** MUST: Keep return schemas and their exposed serializer/import surface versioned and deliberately frozen against drift. A declared contract change is visible as a version/hash update and reviewable regeneration action; a test must not heal its own freeze fixture. Do not impose a particular package, field-case convention or serialization library on every adapter.

- **RETURN-106** MUST: Omit genuinely absent optional fields rather than emitting null or placeholder strings for missing facts, unless the explicitly declared field type permits null with its stated meaning. A declared adapter contract uses one public serializer/schema surface and explicit exports; its freeze record covers that exact surface deterministically, with count/path evidence from deliberate regeneration.

<!-- anchor: protocols.role-returns.validation -->

## Consumer validation

- **RETURN-201** MUST: Extract the candidate payload, validate shape/types, validate status-dependent required fields, then verify semantics and evidence before writing accepted state. Reject absent, malformed or ambiguous payloads. Tolerating declared fences/surrounding prose does not authorize guessing beyond an unambiguous object or accepting unvalidated text.
- **RETURN-202** MUST: Check phase/role/run/input/candidate identities, required artifact existence, authorized path containment and real producing evidence. Check the actual dictated plan path rather than basename similarity; relative adapter paths resolve against the declared target root. Examples, a file count or path existence alone do not establish correctness or delivery.
- **RETURN-203** MUST: Validate required and conditional payloads for the actual phase/status against the norms below before continuation. A BUG_REPORT without its populated report is MALFORMED_VERDICT; a type-valid SUCCESS with stale or incomplete evidence is rejected. Genuine environment/authorization gaps use BLOCKED with reason and limitations rather than an unactionable defect.
- **RETURN-204** MUST: Route response/extraction/schema failures through their bounded correction and terminal handlers, preserving last errors, session identity and all-turn costs. At most one response-level correction applies per phase attempt; its second failure is BLOCKED, or ESCALATED_FINALIZE for Finalize. Preserve typed transport errors without recategorization; only a real actionable implementation defect enters counted Debug.
- **RETURN-205** MUST: The consumer owns counters, budgets, approval, routing and freshness. A return cannot inject those control values or reconstruct approval from model text. Semantic acceptance independently establishes scope, independence, acceptance satisfaction and delivery; serializer validation alone proves none of them.

<!-- anchor: protocols.role-returns.bootstrap -->

## Bootstrap payload

- **RETURN-301** MUST: Bootstrap SUCCESS includes `isEmpty`, `classificationHint` as GREENFIELD or BROWNFIELD, integral nonnegative `fileCount`, `files` and `recommendations`, plus actual map evidence. Each mapped file has `path`, `summary`, `structure` and `relevance`; fileCount matches the list. Capture the actual bounded inventory scope and limitations.
- **RETURN-302** MUST: Treat empty/classification hints and recommendations as reconnaissance facts for Architect, not authority to create a product or waive approval. BLOCKED includes the unavailable input/mechanism and evidence. An embedded Bootstrap returns equivalent inventory/boundary evidence before its Architect consumer acts.

<!-- anchor: protocols.role-returns.architect -->

## Architect payload

- **RETURN-401** MUST: Architect SUCCESS includes `classification`, `projectType`, `taskType`, `planPath`, `featureSlices`, `mayEdit`, `doNotTouch`, `acceptanceCriteria`, `specDeficiencies`, `specBlocked` and `visualGate`. Each slice has id, description, files and actual UI applicability; optional business-requirements path names its real artifact. Classifier vocabulary is adapter-declared and preserves its actual meaning.
- **RETURN-402** MUST: Each acceptance criterion has `id`, `text`, `measurable` and the applicable `threshold` attached to that criterion. Preserve exact approved scope, constraints and deficiency evidence in the plan. specBlocked is true only for deficiencies requiring human input and then `blockReason` is required and nonempty; ordinary resolved deficiencies remain recorded with deviations.
- **RETURN-403** MUST: visualGate carries status and output plus actual activation facts. PASS requires real `command`, `exitCode`, `output` and `evidence`; NOT_APPLICABLE or SKIPPED requires `reason` and activation/applicability evidence. A required failing/missing visual result refuses Code, regardless of an otherwise parseable Architect SUCCESS. Activation evidence includes nonnegative integral `componentNodes` and boolean `testsOnly`: the mechanical gate activates at componentNodes greater than or equal to three unless testsOnly is true. PASS additionally requires integral `scannedNodes` greater than or equal to one, established by the real output; zero-node PASS is rejected. The adapter may encode these observations differently at its declared boundary but must preserve their meanings and thresholds.
- **RETURN-404** MUST: Verify that planPath exists at the dictated location and the plan is semantically ready for its declared slice, tests, scope, commands and delivery sinks. Architect BLOCKED states the human-dependent deficiency or unavailable evidence and its required decision; a return shape alone cannot authorize Code.

<!-- anchor: protocols.role-returns.code -->

## Code payload

- **RETURN-501** MUST: Code SUCCESS includes nonempty actual `artifacts`, `testGuidePath`, `testSummary`, `deviations`, measured acceptance evidence and actual logs/map evidence as applicable. Record `detectedUi` and its classifier evidence when relevant; the consumer reconciles it with authorized UI scope before changing routing. When Doxygen is applicable, Code SUCCESS also requires a `doxygen` build record with command, exitCode, output, evidence, mapPath, and current candidate/input identities. The record establishes the real successful build as the final Code check before SUCCESS, with current per-file XML checks; a previous map cannot substitute for that build. A nonapplicable record supplies its reason and actual applicability or written-prohibition evidence. Requiredness follows PHASE-502 and the actual project/specification facts, not the producer's unsupported claim.
- **RETURN-502** MUST: Code BUG_REPORT requires a populated `bugReport` containing nonempty `goal`, `actual`, `logAnalysis`, `dataAnalysis`, `hypothesis` and `recommendation`, plus actual failure evidence. QA BUG_REPORT requires the same six fields. Recommendation supplies a specific actionable fix; actual records the failure class, including Import, Transformation, UI or Infra as applicable. A missing conditional field rejects the return before continuation.
- **RETURN-503** MUST: Code BLOCKED includes `reason`, `limitations` and evidence identifying the missing required environment, input or authorization. Failed external lookup, declared deferred tests and unverified quantitative criteria remain visible; they cannot be converted into covered acceptance or invented SUCCESS.

<!-- anchor: protocols.role-returns.qa-review -->

## QA and Review payloads

- **RETURN-601** MUST: QA returns `testSummary`, `scans`, `findings`, `limitations` and the common envelope for the same candidate, preserving QA-703 and QA-704 of [QA](../roles/qa.md). Every applicable criterion includes measured or real evidence; SUCCESS satisfies QA-602 and rejects FAIL/BLOCKED required scans and unmet required criteria.
- **RETURN-602** MUST: QA BUG_REPORT contains the six populated fields required by RETURN-502 and the actual report/evidence path. Findings include `scan`, `code`, `severity`, `message`, and path/line where applicable; use stable registry codes and LOW/MEDIUM/HIGH severity by actual impact, with secrets represented only by redacted class and location.
- **RETURN-603** MUST: The `scans` list contains exactly all eight named identities: `green-test-trap`, `quantitative-ac`, `semantic-trace`, `infra-dod`, `side-effect-channel`, `secret-leak`, `real-path-shape` and `discriminating-test`. Every entry has `id`, `status` as PASS/FAIL/N/A/BLOCKED, nonempty `reason` and actual `evidence` paths. N/A requires trigger-based applicability rationale and cannot waive a required acceptance criterion; unknown or omitted scans are rejected.
- **RETURN-604** MUST: Review returns independent `findings`, evidence, complete diff/scope judgment and limitations for the current candidate. SUCCESS records verified requirements, boundaries, regression and side-effect assessment; an actionable defect returns BUG_REPORT and invalidates affected QA/Review evidence when fixed. BLOCKED identifies missing judgment/authority. Preserve read-only and independence evidence even when Review is embedded in QA.

<!-- anchor: protocols.role-returns.debug -->

## Debug payload

- **RETURN-701** MUST: Debug FIXED includes `rootCause`, `fix`, `filesTouched`, `postFixAudit`, `testSummary`, actual regression evidence and current origin/candidate identity. Pair the cause with its own actual files and consumed entry; the audit compares real changes with authorized scope rather than trusting the reported list.
- **RETURN-702** MUST: Debug BLOCKED includes nonempty `rootCause` or its unresolved diagnosis, `reason`, evidence and limitations, retaining attempted fixes, tests, files and the consumed entry. A failed execution or unavailable response cannot refund the entry or become FIXED.
- **RETURN-703** MUST: Treat filesTouched as scope-audit and diagnostic evidence, not permission to skip full independent QA. FIXED proceeds to renewed QA under the same run/history; the consumer verifies actual changes and never infers green from the testSummary string alone.

<!-- anchor: protocols.role-returns.finalize -->

## Finalize payload

- **RETURN-801** MUST: Finalize SUCCESS includes the actual `report` artifact, `classification`, `planPath`, `testsPath`, `logPath`, applicable `doxygenPath`, `testSummary`, `acceptanceEvidence`, `qaEvidence`, `reviewEvidence`, required `liveEvidence`, `blastRadius`, `scopeDeviations`, `limitations` and current identities. blastRadius accounts for added, modified, deleted and untracked paths; the consumer verifies actual existence, contents and candidate consistency. The report also preserves the conditional project document-convention enclosure, ordered headings and unconfirmed-claim provenance required by FINAL-503, with actual formatting/evidence supplied to the root consumer.
- **RETURN-802** MUST: Finalize BLOCKED identifies unavailable required evidence with reason and limitations. ESCALATED_FINALIZE includes `requiredRepair`, failure evidence and the owner continuation decision needed when source/configuration/syntax/annotation repairs are necessary; preserve history and budgets and do not route automatically to Debug.
- **RETURN-803** MUST: Accept Finalize SUCCESS only after the actual report, independent judgment, full acceptance/live/map/test evidence and blast radius are verified for the current candidate. A non-null final object, absent status or report path alone is rejected; failed or unavailable mandatory obligations remain unsatisfied and the result gate remains pending.

<!-- anchor: protocols.role-returns.extensions -->

## Optional diagnostic, recheck and E2E interfaces

- **RETURN-901** MUST: An adapter-declared intake return identifies `source`, `symptom`, redacted `logExcerpt`, `severity`, `affectedArea` and `reproHint` from actual supplied incident evidence. This diagnostic input does not grant production writes or fix authority; permissions and original evidence provenance remain explicit.
- **RETURN-902** MUST: A reproduction return includes `reproduced`, actual `failingTestPath` when reproduced and `notes`/evidence. The reproducer is the proposed fix acceptance criterion. Nonreproduction disables automatic fix approval and requires an explicit investigation/owner route rather than an invented failing test.
- **RETURN-903** MUST: A root-cause return includes `rootCause`, `hypothesesConsidered`, `evidence`, `confidence`, `affectedFiles`, `proposedFix` and `regressionRisk`. Retain rejected hypotheses with their evidence and confidence; numeric hypothesis confidence lies from zero through one and the overall confidence label is declared. affectedFiles proposes the fix MAY EDIT scope subject to authorization, not blanket rights.
- **RETURN-904** MUST: A supplemental recheck return includes actual `passed`, `summary` and evidence for its current candidate. Red creates the fresh recheck failure stamp with its own summary; green does not replace full renewed independent QA. Its producer/consumer declaration keeps retry and Debug accounting distinct.
- **RETURN-905** MUST: An E2E return includes `outcome` as passed/failed/flaky, `totals`, actual `reportPath`, `tracePaths` and `warnings`. Traces feed current diagnosis and flaky warnings remain in final reporting. A required acceptance criterion cannot be satisfied by flaky; failed actionable evidence uses counted Debug and unavailable required execution uses BLOCKED, as [phase extensions](../flow/phases.md) require.
