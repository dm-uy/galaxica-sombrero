---
id: flow.finalize
title: Finalization
status: draft
---

# Finalization

Finalize assembles and verifies the concrete result through {{cap:workflow-orchestration}}. It has authority to regenerate declared outputs for the judged candidate; it does not acquire implementation repair authority from an earlier green verdict.

<!-- anchor: flow.finalize.entry -->

## Entry and current evidence

- **FINAL-101** MUST: Enter Finalize only with full independent QA and required Review evidence for the same current candidate and approved inputs. Verify role identity, all eight scan judgments, test results, measurable acceptance criteria and required live delivery evidence; earlier green status alone is insufficient.
- **FINAL-102** MUST: Reconcile the actual specification, plan, code, tests, logs/data, required map and scope. Confirm that the map lists each new entity by qualified name and that authored change/version annotations are appropriate. Preserve the design graph in the plan and the post-code map as distinct artifacts; do not create a third competing graph copy. The qualified entity inventory and change metadata follow [semantic markup](../code/exoskeleton.md); design graph details follow [graphs](../protocols/graph.md), with these concrete outputs required at this boundary. Inspect the artifact contents and producing commands/exits rather than merely the return shape or path. Required skipped, failed, deferred or unavailable evidence prevents SUCCESS and carries its honest limitation.
- **FINAL-103** MUST: Confirm every applicable declared check and delivery sink completed, including real entry-point/artifact-shape tests, infrastructure and side-effect probes where required. A mock/capture proves an API call and cannot satisfy real sink delivery. Bind actual commands through {{cap:check-runner}} and retain outputs without private values.
- **FINAL-104** MUST: Check current run/input/candidate identities again before producing the final report; include unchanged baseline provenance and the exact judged scope. A candidate change since QA requires renewed verification rather than approval of a surviving report path.

<!-- anchor: flow.finalize.outputs -->

## Declared outputs and map

- **FINAL-201** MAY: Regenerate only declared outputs when their generation leaves the judged source and configuration unchanged. Record actual command, exit, output paths and resulting hashes, verify generated contents and preserve the same candidate identity; generation is not permission to seed or repair source/configuration.
- **FINAL-202** MUST: For a product with authored code, Doxygen is mandatory unless its own written instructions explicitly prohibit it; otherwise determine applicability from actual project configuration and declared deliverables. Run mandatory applicable Doxygen through {{cap:code-map-build}} and retain the actual exit code, stdout/stderr and per-file XML checks for changed/new code and its declared contracts. The build must finish without errors and its ignored output must not enter the source commit. Inspect the generated map rather than accepting a producer statement that it exists.
- **FINAL-203** MUST: Treat a missing or incomplete required Doxygen configuration, invalid source syntax, missing required annotations or other implementation prerequisite as a Finalize repair failure under FINAL-401. Missing configuration cannot silently waive the check. Any allowed nonapplicability or explicit written project prohibition requires actual quoted rule and applicability evidence; absence of existing markup is not a prohibition.
- **FINAL-204** MUST: Verify required plan, test guide, tests, log, report, code-map and other deliverables actually exist and match their declared contents and roles, including new/untracked paths. Use actual project paths rather than default filenames; absent required artifacts or unreadable outputs must be reported as failure or unavailability.

<!-- anchor: flow.finalize.blast-radius -->

## Blast radius and scope

- **FINAL-301** MUST: Compare the actual candidate against the acquired baseline and enumerate staged, unstaged, added, modified, deleted and untracked paths with their content identities. Inspect both the full diff and new files; a diff command alone omits untracked content. Account for generated/ignored outputs separately without concealing candidate changes.
- **FINAL-302** MUST: Cross-check every changed path and side effect against authorized ownership, MAY EDIT and DO NOT TOUCH, specification constraints, the plan and approved deviations. Report an unauthorized touched path as SCOPE_DEVIATION and investigate unexpected paths; the debugger filesTouched list or producer artifact list alone cannot establish the actual blast radius.
- **FINAL-303** MUST: Report the actual added, modified, deleted and untracked paths, deviations and their reasons, regressions considered and residual risks. Preserve observed unexpected changes and their ownership rather than deleting, resetting or committing them to make the report clean.

- **FINAL-304** MUST: In a non-repository exception explicitly authorized at entry, enumerate the filesystem delta against the acquired run-start snapshot and its content identities, excluding declared output/cache directories; never anchor this delta on the map configuration timestamp. State the weaker available evidence and preserve every added/deleted path. Brownfield scope checking remains mandatory and greenfield changes remain visible in the report.

<!-- anchor: flow.finalize.failure -->

## Repair and continuation boundary

- **FINAL-401** MUST: If completing Finalize requires a source, configuration, syntax or annotation repair, return explicit ESCALATED_FINALIZE with the required repair and evidence. Obtain an owner continuation decision before that work; do not edit source/configuration in Finalize and do not automatically return to Debug.
- **FINAL-402** MUST: Preserve the candidate, causal history, spent Debug entries and other applicable budgets on Finalize failure. Identify the unresolved obligation, expected/actual evidence, attempted output generation and specific continuation decision; missing/malformed Finalize responses also cannot yield SUCCESS.
- **FINAL-403** MUST: After an authorized continuation changes implementation, reconcile approved inputs/scope and renew full independent QA plus affected Review before Finalize. Record the linked continuation identity and preserved spend; never reuse stale green evidence or implicitly restart a terminal run.

<!-- anchor: flow.finalize.report -->

## Result report and gate

- **FINAL-501** MUST: Return an explicit final status and actual report/artifact paths with candidate and input identities, classification, plan/test/log/map paths, test summary, acceptance evidence map, independent QA/Review, live evidence, blast radius, deviations and limitations. Report failed/unavailable obligations and E2E warnings plainly; a non-null object or existing report path is not a successful result.
- **FINAL-502** MUST: The root verifies all produced artifacts, real command outputs and actual scope before accepting Finalize SUCCESS and overall SUCCESS. Any unsatisfied mandatory obligation prevents success; retain BLOCKED or ESCALATED_FINALIZE with the operative reason and owner decision.
- **FINAL-503** MUST: Present the concrete result for the separate owner decision under [gates](../process/gates.md), using {{param:dialog-language}} in dialog and the project artifact convention in files. Include actual absolute paths to the development plan, test guide, logs and code map where applicable. Do not automatically merge, publish, deploy or treat a phase verdict as integration approval. When the adopted project document convention requires the three-heading report form, place every owner-facing claim inside the headings Blocked on the owner, Changed and Found, on their own lines in that order; place no owner-facing claim outside them, and mark each unconfirmed claim with where the agent looked. The finalizer produces this prescribed enclosure/order and provenance for the root to verify, with detailed template/convention at [document conventions](../documents/conventions.md). This conditional project obligation preserves the original report binding; GATE-1008 remains the general SHOULD for the result-decision order.
