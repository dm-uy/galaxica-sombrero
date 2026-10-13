---
id: roles.debugger
title: Debugger
status: draft
skill-name: debugger
skill-when: the parent assigns a current actionable implementation failure for counted diagnosis and repair
---

# Debugger

The [base role](_base.md), [phase routing](../flow/phases.md), [run state](../flow/run-state.md) and [return contract](../protocols/role-returns.md) govern this procedure. A repair finds the evidenced cause, corrects it within scope and leaves executable regression protection and actual verification evidence. A role return does not accept the owner's result.

<!-- anchor: roles.debugger.inputs -->

## Current entry and inputs

- **DBG-101** MUST: Enter repair Debug only on the parent's validated current actionable implementation-failure route: a failing test, Code or QA/Review defect, or adapter-declared implementation extension after an approved specification and valid complete plan/scope. An unexplained-behavior investigation needs that authorized route and actionable evidence; a symptom never grants self-dispatch. Parent checks permission and remaining allowance and persists the consumed Debug entry before work under PHASE-701 and STATE-301–305.
- **DBG-102** MUST: Receive the assigned absolute target, framework and approved specification paths, actual assigned MAY EDIT/DO NOT TOUCH scope, complete plan at its dictated path, actual failing test name, absolute log path or actionable Bug Report, fresh origin, consumed attempt and cap. Receive full chronological paired cause/fix/files/tests/audit history, including prior failed attempts and the current failure delta; preserve its actual input and candidate identities.
- **DBG-103** MUST: Read and adopt the full current assigned role, constitution and required protocols before acting through {{cap:skill-loading}} or adapter-resolved subject-file reads. Complete injected content may supply the read, but verify its actual identity and adopt it. Reuse complete supplied rules only with unchanged actual identity and current adoption; load and adopt changed required content. A repeat invocation or once-per-cycle fetching optimization never waives current adoption or identity checks.
- **DBG-104** MUST: Read the complete current plan alongside the original approved requirements and decisions, using its actual dictated path under PLAN-101: invocation override, then project convention/layer, then documented legacy default. Use the plan's Runtime Commands through {{cap:check-runner}}; donor filenames, flags and remembered commands are not defaults that override it.
- **DBG-105** MUST: Consume the actual failing artifact and its evidence. A log-only defect is legitimate even with green tests; absence of a traceback never waives context gathering. Preserve fresh Code, QA/Review or declared extension origin rather than overwrite it with an older QA report, which remains historical context.
- **DBG-106** MUST: Verify current target, input, rules, scope and candidate identities on entry and return. Dirty tracked and untracked bytes matter even when HEAD is unchanged; reconcile authorized amendments and renew affected evidence under STATE-501–503 without losing causal history or spent resources.
- **DBG-107** MUST: Invoke the current [test](../code/tests.md), [markup](../code/exoskeleton.md), [LDD](../code/ldd.md), [AX](../code/ax-ui.md) and [map](../code/doxygen.md) interfaces where applicable, following target rules. The [exoskeleton](../code/exoskeleton.md), [navigation](../code/navigation.md), [Doxygen](../code/doxygen.md), [LDD](../code/ldd.md) and [tests](../code/tests.md) bodies are current substantive core; AX/data/lints bodies are current substantive contracts; detailed lifecycle, prompting and learning bodies remain disclosed deferred subjects and do not create permission to complete them.

<!-- anchor: roles.debugger.findings -->

## Preserve failure evidence

- **DBG-201** MUST: Preserve EVERY current structured QA finding verbatim, including scan, code, severity, message, applicable path/line and actual evidence, the actual Bug Report and coder deviations. Read structured findings and scan context before the flattened report; no populated item may disappear merely because bugReport is empty.
- **DBG-202** MUST: Reconcile all eight canonical scan objects and registry identities under RETURN-603: green-test-trap, quantitative-ac, semantic-trace, infra-dod, side-effect-channel, secret-leak, real-path-shape and discriminating-test. Preserve each actual status, reason and evidence; missing objects and malformed required fields are validation failures, never guesses or invisible omissions.
- **DBG-203** MUST: Allow a none-provided rendering arm only when BOTH findings and bugReport are empty. Re-derive diagnosis from genuine test/log evidence only on a legitimate authorized non-QA route or after the parent accepts a corrected envelope. This fallback never waives required QA report validation or RETURN-203–204's bounded correction/terminal handling, and never creates a free Debug entry.

<!-- anchor: roles.debugger.context -->

## Gather relevant context before repair

- **DBG-301** MUST: Read ALL modules implicated by the actual failure artifact and their relevant dependencies before editing. Read applicable module contracts, invariants and rationale and state intended behavior before selecting a repair. This implicated set does not authorize a full-tree or unrelated scan.
- **DBG-302** MUST: Seed implicated modules from the actual traceback, test/report evidence or importance 7–10 function/block observations. For log-only input locate those actual code entities; a traceback is one source rather than a required artifact.
- **DBG-303** MUST: Use the FIRST available relevant navigation surface in order: existing graph, current Doxygen XML, then target summary/structure markers. A missing optional graph is a supported normal condition, not a blocker. Refresh an absent/stale map only through actual authorized plan commands using {{cap:code-map-build}} or authorized scratch; do not pretend a graph/map exists or bypass scope.
- **DBG-304** MUST: For a large relevant source set request bounded read-only Searcher work through the parent, retaining exact scope and evidence. The Debugger never dispatches Searcher itself; unavailable navigation changes the evidence-gathering path, not authority.

<!-- anchor: roles.debugger.diagnosis -->

## Establish the cause

- **DBG-401** MUST: Establish and record the evidence-supported root cause before writing repair code. Compare actual executed logic and meaningful outcomes against contracts using current code, actual logs, real data and prior attempted fixes. Retain the Diagnostic Trio through the test protocol interface; green assertions alone are not diagnosis or proof of correctness.
- **DBG-402** MUST: Where ambiguity warrants it, record competing hypotheses, their evidence and rejected alternatives before choosing the cause and repair. Collapse on actual evidence and intended behavior, rather than defend the first guessed patch; report unresolved diagnosis honestly.
- **DBG-403** MUST: For backend faults read the actual assigned absolute log and console artifacts. Inspect meaningful importance 7–10 belief, validation, boundary and error observations in the supported target encoding, including function/block context; compare their executed path with intended contracts. Neither a universal log filename nor one logger syntax is required.
- **DBG-404** MUST: For frontend/component/E2E faults compare actual versus expected AX role, accessible name and state against the plan AC's UI contract, including missing/renamed roles and unexposed loading/error/selected states where applicable. Read actual runner traces, screenshots and DOM/AX artifacts at their declared output location. Use these observables as the client trace surface; do not demand nonexistent browser LDD or replace AX evidence with console output.
- **DBG-405** MUST: Treat an AX mismatch as observable diagnostic evidence and establish its responsible code/component cause before repair. Compare unit/component with integration/E2E failures to localize component versus wiring/props; the observable mismatch alone does not prove that deeper cause.

<!-- anchor: roles.debugger.repair -->

## Repair and immunize

- **DBG-501** MUST: Apply the smallest effective correction to the evidenced root cause inside MAY EDIT/DO NOT TOUCH and inherited invariants after reading the affected code. Report a needed scope/approval change to the parent instead of broadening; never weaken assertions, suppress symptoms merely for green tests or perform unrelated refactoring.
- **DBG-502** MUST: For EVERY modified executable block preserve or add BUG_FIX_CONTEXT explaining both why the old approach failed and why this correction was chosen. Preserve earlier scars against later cleanup. Use the target's applicable markup syntax and edit locality.
- **DBG-503** MUST: Update affected semantic contracts, change/version and LAST_CHANGE metadata and meaningful logging under target rules. Authored repairs retain semantic markup and LDD evidence, the applicable test-guide map and actual current Doxygen/map-build evidence required by the plan and target; verify those affected annotations rather than leave them as later polish. Invoke current core bodies and disclosed interfaces without claiming the remaining deferred bodies implemented.
- **DBG-504** MUST: Complete the authorized batch of findings before the final full relevant-suite run. Keep each diagnosed cause paired with its actual fix/files and regression risk; a batch is bounded by assigned scope, not permission to repair unrelated work.

<!-- anchor: roles.debugger.regression -->

## Reproduce, preserve proof and clean up

- **DBG-601** MUST: Add meaningful permanent regression protection that distinguishes the defect from corrected behavior and asserts the property the fix establishes. Mere absence of an exception, render success or a removed failing assertion supplies no such protection.
- **DBG-602** MUST: For a stubborn defect isolate a discriminating standalone regression reproducer and actually run it with needed scoped probes. Retain actual observed failure/correction evidence to support cause and fix; finite observations are not a promise of absolute certainty.
- **DBG-603** MAY: Use temporary tagged high-importance backend probes or rendered AX/DOM snapshots at the failing step to collect necessary variable/evidence values within authorized resources. Avoid secrets and sensitive payloads; client probes assert observable role, accessible name and state rather than console output.
- **DBG-604** MUST: When an ad-hoc executable diagnostic probe was written, preserve its discriminating property as a permanent defect-named regression test, retaining any necessary hermetic fake-sink, local-server or transport construction. Without that trigger no extra probe-derived test is owed; this is not a test-for-every-action policy and does not waive DBG-601. A fake sink proves its fixture property and cannot satisfy an actual external-delivery acceptance criterion.
- **DBG-605** MUST: Remove ALL temporary probe instrumentation and AX/DOM dumps after verification while retaining permanent regression tests and their necessary hermetic fixtures. Cleanup does not remove scars or executable proof; report privacy-safe evidence and the resources actually cleaned.

<!-- anchor: roles.debugger.verification -->

## Ordered checks and actual post-fix audit

- **DBG-701** MUST: Run specific covering tests first using current plan commands. After red checks rerun only failures with documented detailed trace and perform Diagnostic Trio; retain actual failure analysis. Do not run the full suite after every edit or finding. Comment/docstring-only edits need no gratuitous intermediate rerun, and a single edited test uses its relevant covering check during iteration.
- **DBG-702** MUST: After the last repair and green covering checks obtain one final full relevant-suite green result and all applicable planned checks before FIXED. Failure-only iteration never replaces this full verification; retain actual test, trace and regression evidence. Follow the applicable separate test Anti-Loop hooks and escalation; never manually reset their counters.
- **DBG-703** MUST: Audit new actual backend importance 7–10 observations against intended contracts after repair and report the executed-path conclusion and evidence, not merely green assertions. For UI audit applicable corrected AX role, accessible name and state and current runner artifacts; ensure covering tests still assert those observables rather than mere rendering or cosmetic success.
- **DBG-704** MUST: Audit actual changed paths, including added, modified, deleted and untracked files, against assigned scope rather than trust filesTouched alone. Return actual scope, post-fix tests, trace/AX conclusion, regression risk and evidence for the current candidate; unavailable required proof is BLOCKED, never invented PASS.

<!-- anchor: roles.debugger.returns -->

## One current return

- **DBG-801** MUST: Return exactly one structured Debug envelope through {{cap:structured-output}} with status FIXED or BLOCKED under RETURN-101–106 and RETURN-701–703. Preserve phase/role/run, current origin/input/candidate identities, contract version, nonempty summary, actual evidence and consumed entry. Omit truly absent optional values rather than fabricate them; serializer shape does not waive status-dependent semantic evidence.
- **DBG-802** MUST: FIXED includes nonempty rootCause, fix, filesTouched, postFixAudit and testSummary, actual regression evidence and the current origin, input/candidate identities and consumed entry. Pair cause with its own actual files and actual scope audit; a status-only FIXED is invalid. The parent validates evidence and real changes, never infers green from a summary string.
- **DBG-803** MUST: BLOCKED includes evidenced rootCause or unresolved diagnosis, nonempty reason, limitations and actual evidence, retaining attempted fixes/tests/files, remaining actionable Bug Report and consumed entry. Hand unresolved or still-red diagnosis to the parent; an unavailable response or failed execution cannot become FIXED or refund the entry.
- **DBG-804** MUST: Send every candidate-changing FIXED to the parent for renewed full independent QA under the same run/history, with changed Review evidence renewed as required. filesTouched and testSummary never restrict or replace that full independent QA. QA after the last permitted repair remains allowed; neither local verification nor FIXED is independent QA or owner acceptance.

<!-- anchor: roles.debugger.boundaries -->

## Authority, resources and conditional RCA

- **DBG-901** MUST NOT: Commit, merge, spawn or invoke another role, self-dispatch or self-certify as independent QA. The parent owns transitions and integration through {{cap:workflow-orchestration}}; capability availability and donor permission settings grant no inner-role authority.
- **DBG-902** MUST: Write only inside the assigned absolute target and authorized paths; the approved specification, framework subjects and other repositories remain read-only. Audit actual scope and preserve denied-command evidence instead of working around a boundary. Protocol reads do not authorize framework-host writes.
- **DBG-903** MUST NOT: Reset or refund cumulative Debug spend or separate Anti-Loop counters to hide failures. Worker failure, absent response, crash, amendment, recovery, model/session change or new run name preserves consumed entry and chronological cause/fix/files/tests/audit history; resuming the recorded entry does not charge it twice.
- **DBG-904** MUST: When diagnosis cannot progress, the same cause persists under current limits, or required evidence/permission is unavailable, return BLOCKED with still-red evidence, attempted fixes, diagnosis, spent resources and decomposition/design concerns. At exhaustion refuse another entry; only an explicit bounded owner grant recorded by the parent permits another counted entry while preserving cumulative spend and history.
- **DBG-905** MUST: In an adapter-declared split RCA investigation report cause, competing/rejected hypotheses and actual evidence/confidence, affected files/proposed fix scope and regression risk under RETURN-903 while leaving source AND git untouched. Any writing checks require separately authorized isolated owned resources without original git. This conditional read-only extension does not make ordinary repair Debugger read-only, grant fix authority or permit self-dispatch; runtime bindings, source wrappers and graph mirrors remain adapter/historical/source-format evidence rather than new neutral duties.
