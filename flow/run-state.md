---
id: flow.run-state
title: Run state
status: draft
---

# Run state

The ledger connects actions to the inputs and repository bytes they judge. Persist it through {{cap:run-state-persist}}; the orchestrator owns the authoritative state and checks evidence before accepting any transition.

<!-- anchor: flow.run-state.identity -->

## Identity and input locks

- **STATE-101** MUST: Record runId, task identity, absolute target and framework roots, baseline branch/HEAD and actual baseline acquisition evidence, specification/plan/rules/adapter versions and hashes, approved scope and authentic approval references. Keep the original baseline distinct from later candidate identities and record whether required repository preflight actually ran.
- **STATE-102** MUST: Identify the full candidate with its baseline/HEAD and a reproducible content digest that covers tracked staged, unstaged, modified and deleted paths plus new/untracked content within scope. Record path inventory and scope alongside hashes; unchanged HEAD alone cannot prove an unchanged candidate.
- **STATE-103** MUST: Lock each approved input version when the run begins and reconcile any amended specification, plan, rules, adapter or scope with applicable approval before advancing. Never overwrite a locked hash merely to suppress mismatch; preserve prior versions and their provenance.
- **STATE-104** MUST: Record the dictated plan path and actual artifact/evidence roots and role return contract version. Associate every accepted role result with its run, phase, task, input identity and judged candidate; path existence and a correctly shaped hash do not establish its truth.
- **STATE-105** MUST: Keep feature-design and optional diagnostic continuations explicitly identified with their own applicable phase inputs. Do not infer a plan phase, fix authority or new scope from the presence of a compatible state object; shared typed structures do not confer authorization.

<!-- anchor: flow.run-state.ledger -->

## Ledger and resource history

- **STATE-201** MUST: Use one durable state writer. Append each accepted or refused event with a recorded timestamp, phase/status, current identities, evidence, error/route and applicable counter delta; checkpoint atomically so partial writes cannot authorize progress. Preserve append-only diagnostic/fix history and monotonic resource totals even when ordinary current-result fields are replaced.
- **STATE-202** MUST: Keep accepted phase evidence beside the work in the declared run footprint or an explicitly authorized private evidence home. Ignore generated runtime bookkeeping as the project requires, without concealing source changes. Record completion when it occurs with the repository facts that made it true; the ledger is evidence about those facts, not proof by its own existence.
- **STATE-203** MUST: Pair every chronological attempt number and root cause directly with its own files touched, audit, fix, tests and origin. Retain the entire diagnostic history, including failed attempts and costs; do not render an unordered collection or pair a fresh failure with stale unrelated evidence.
- **STATE-204** MUST: Retain worker/session identities, cost/time/resource provenance and retry costs for all turns, including failed validation and transport turns. Declare any wallet/time/recursion guard and its unit before execution and check available resource allowance at phase entry before spending. Pin the actual persistence/durability mechanism so a hard interruption cannot leave a completed worker turn detached from its checkpoint. Size declared orchestration recursion to the longest segment between owner resumes, not an invented number of all loops. Defaults and enforcement mechanisms are adapter choices that cannot erase spent resources or replace the Debug-entry cap.
- **STATE-205** MUST: Derive replay and briefing facts from checkpointed inputs and declared current-event stamps. A missing, unreadable, truncated, corrupt or incomplete ledger supplies no authority to advance; record the condition and perform honest work only when safe, otherwise BLOCKED. A state validator cannot authenticate approval, independence, artifact semantics, scope or real delivery; the orchestrator and independent judges must establish those facts.

- **STATE-206** MUST: Declare the checkpoint encoding and durable worker-turn boundary so inputs and complete outputs round-trip without field loss. Choose the return model from the declared phase registry; replay arguments derive only from checkpointed state, while live repository validation remains at the phase boundary. Distinguish current operational scratch flags from the frozen public state/return contract and keep their reducers and persistence settings explicit.

<!-- anchor: flow.run-state.repairs -->

## Debug-entry accounting

- **STATE-301** MUST: The default Debug-entry cap is four; {{param:debug-entry-cap}} binds the adapter cap. The counted unit is entry into Debug, not QA visits, successful fixes, subprocess retries or response corrections; the root orchestrator owns cumulative accounting on both automated and direct-delegation paths.
- **STATE-302** MUST: An adapter cap must be a nonnegative integer; boolean, negative and nonintegral values are invalid. Where the adapter schema stores parameters as text, the adapter declares strict decimal parsing to this semantic integer and rejects ambiguous coercion. An adapter may lower the default cap. An increase above the current allowance requires an explicit bounded owner grant under GATE-1209 recorded with scope, reason and additional allowance before the next entry; declaration alone cannot silently raise the default.
- **STATE-303** MUST: Record the Debug entry spend before entering the phase; an initial or renewed QA consumes no Debug entry. Code-origin BUG_REPORT, QA/Review defects and extension-origin actionable failures share this unit; recovered work inside an already entered Debug retains its original spend and does not create a free entry.
- **STATE-304** MUST: A failed or BLOCKED Debug preserves the consumed entry. Missing responses, crashes, changed candidates, amendments and recovery neither refund nor reset the cumulative spend; resuming the already recorded entry does not charge that same entry twice.
- **STATE-305** MUST: When spent Debug entries reach the authorized cap, refuse the next Debug entry and escalate with still-red evidence, attempted fixes, full causes/files history, diagnosis and decomposition concerns. A recorded bounded owner grant extends permission while preserving cumulative spend and causal history. QA after the last permitted repair remains allowed; exhaustion is not success and a new run name cannot evade the cap.

<!-- anchor: flow.run-state.retries -->

## Separate retry units

- **STATE-401** MUST: Maintain distinct response-correction, extraction/schema-validation, transport/error and test Anti-Loop counters with declared finite caps, episode/phase/session scope and increment rules. Response correction is at most one per phase attempt as PHASE-904 requires. No retry kind resets Debug spend or substitutes for an unrecorded Debug entry.
- **STATE-402** MUST: Bound schema/extraction re-prompts in the same live worker context and accumulate every attempted turn and cost. Declare total-turn bound as one initial turn plus permitted corrections; use resume only for the initial attempt where supported, then a normal correction prompt with bounded errors and required schema. Preserve the last validation errors and session identity at exhaustion; do not emit a default success.
- **STATE-403** MUST: Preserve the typed transport/error cause and declared retryability rather than recategorizing it as a parse defect. Charge each attempted retry once and retain failed turn costs; retry only a declared retryable phase within its bound. Exhaustion, fatal errors and unavailable resources invoke their declared abort/escalation route exactly once.
- **STATE-404** MUST: Keep test Anti-Loop/session failure counters separate from run repair allowance. Do not reset them to conceal a red run. For an unknown side-effect outcome, investigate actual completion and sink state before replay; checkpointed completion may avoid duplicate work only after the authoritative freshness and recovery checks.

<!-- anchor: flow.run-state.freshness -->

## Freshness and amendments

- **STATE-501** MUST: Changes to the specification, plan, rules, adapter, approved scope or candidate invalidate affected approval/verification evidence. Dirty tracked changes and untracked bytes are candidate changes even if HEAD is unchanged; compare actual current identities before accepting any continuation.
- **STATE-502** MUST: After an authorized input amendment, reconcile applicable owner approval, re-establish the current input locks and renew verification of affected work. Preserve valid unaffected evidence, chronological history and spent budgets; hand the next producer the precise old/new delta and actual amended plan path instead of repeating unchanged bootstrap work.
- **STATE-503** MUST: Every candidate-changing fix invalidates the earlier QA verdict and requires full renewed independent QA before Finalize, including UI-only changes. Renew changed Review evidence as PHASE-605 requires; a stored qaPassed or prior-green value cannot waive this predicate.
- **STATE-504** MUST: Compare evidence contents, producing commands/results, input/candidate identity and applicability. An earlier status, surviving artifact path, schema-valid return, HEAD-only check or debugger filesTouched list alone cannot establish freshness, coverage or delivery. A declared decomposition restart explains the changed slice boundary and reconciles approval while retaining applicable spent resources.

<!-- anchor: flow.run-state.recovery -->

## Safe recovery

- **STATE-601** MUST: Accept a recovered phase result only for the same run/task, current return schema, approved inputs/scope and actual candidate facts. Revalidate its role payload, evidence/artifact existence and containment, producer identity, timestamps and phase predicate through the authoritative consumer; reject stale or mismatched records and investigate unknown completion before replay.
- **STATE-602** MUST: Recovery may supply only a validated phase result. A worker record must not set counters, budgets, approval, phase routing or authoritative freshness flags. The consumer derives permitted state changes from current verified facts; counter injection or claimed approval from a return is rejected before state mutation.
- **STATE-603** MUST: When recoverable Bootstrap, Architect, Code or QA evidence is absent/corrupt/mismatched, treat it as no recoverable result with a diagnostic, not success. Perform the phase honestly when safe and authorized, otherwise BLOCKED. Architect recovery verifies its real plan; Code recovery verifies nonempty actual artifacts; QA recovery verifies the complete current candidate and its acceptance evidence.
- **STATE-604** MUST NOT: Recover Debug or Finalize as cached deliverables to skip counted repair work or current final checks. A resumed already entered Debug may reuse checkpointed completed work only with its spend and cause preserved; it must not replay one old verdict into another attempt slot. Finalize must verify the current candidate and current report.
- **STATE-605** MUST: Distinguish delivery record recovery from resuming one interrupted worker. Record the original completion identity, cost and recovered outcome so verified completed work is neither charged twice nor assumed complete without evidence. Durable replay does not authorize an automatic scheduler, new goal or implicit fresh run.

<!-- anchor: flow.run-state.terminal -->

## Terminal and continuation

- **STATE-701** MUST NOT: Automatically resume or advance a terminal run. The canonical SUCCESS, SPEC_BLOCKED, VISUAL_GATE_FAIL, ESCALATED, BLOCKED, ERROR and ESCALATED_FINALIZE outcomes of GATE-1203 retain their artifacts, history, pending decisions and applicable spent resources; a terminal flag cannot be cleared by a worker result.
- **STATE-702** MUST: Owner-approved continuation records a successor or continuation identity, explicit authorization/reason and linked causal history before work resumes. Preserve applicable cumulative budgets and reconcile changed input/scope approval; a changed name, clean checkout or decomposition restart does not grant a budget reset.
- **STATE-703** MUST: Record the concrete result decision separately from phase/run success. Keep failed/unavailable obligations and outstanding integration authority visible; only the actual owner decision under [gates](../process/gates.md) authorizes the applicable irreversible action.
