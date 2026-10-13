---
id: process.gates
title: Gates
status: draft
skill-name: gates
skill-when: a specification is ready for the owner's approval, or a run ended with a verdict or another terminal status
---

# Gates

<!-- anchor: process.gates.decisions -->

## Decisions

- **GATE-101** MUST: Require two owner decisions for every change: its specification or recorded batch scope before implementation, and its concrete result after a verdict and live probe before merge, publish or deploy; record both in files.
- **GATE-102** MUST NOT: Skip a gate or auto-approve it, even when the verdict appears obvious; both decisions require explicit owner consent and durable records, because treating the gate as a formality transfers ownership of the goal to the executor.
- **GATE-103** MUST: Keep the human as the owner of the goal and the agent as its executor.
- **GATE-104** MUST: Load this gate protocol whenever a specification is ready for the owner's approval and whenever a run ends with a verdict or another terminal status, using {{cap:skill-loading}} or the resolved subject file.

<!-- anchor: process.gates.channel -->

## Channel

- **GATE-201** MUST: Pass a gate through a structured owner question using {{cap:ask-owner-structured}}, or the explicit approved exit of {{cap:plan-mode}}, subject to the declared fallback in GATE-203.
- **GATE-202** MUST NOT: Treat a free-form chat message as approval where the adapter declares a structured question mechanism; agreement inside plan mode also does not exit that mode.
- **GATE-203** MAY: Accept explicit chat approval only where the adapter has no structured mechanism and names it as a declared fallback; record the owner's words verbatim, artifact version or hash, scope, who and when, and ask again on ambiguous wording instead of recording consent.
- **GATE-204** MUST: Prepare the concrete artifact when a decision is missing, ask through the supported channel, then wait; never demand a nonexistent structured tool or repeat an already answered question whose approval still matches the artifact and scope.
- **GATE-205** MUST NOT: Infer approval from silence, a timeout, a default option, another agent or a tool result; an unanswered gate blocks dependent work.

<!-- anchor: process.gates.waiting -->

## Waiting

- **GATE-301** MUST: Wait for the pending owner answer before any dependent action or crossing the gate; independent and reversible work may continue only under GATE-302.
- **GATE-302** MAY: Continue independent research and reversible preparation inside the approved scope while the gate waits, provided neither depends on the pending answer nor proceeds past the gate.
- **GATE-303** MUST: Match existing approval to the current specification or concrete result; changed scope needs renewed authorization.
- **GATE-304** MUST NOT: Infer acceptance of newly invented requirements from a broad product idea.
- **GATE-305** MAY: Use an existing explicit owner authorization for the exact scope as the decision, record its scope and source, and continue without asking it again when its channel satisfies GATE-201 through GATE-203.

<!-- anchor: process.gates.cadence -->

## Cadence

- **GATE-401** MUST: In batch cadence, obtain approval before code for tasks that record class, finish line, stop conditions and scope; a specification inside the approved scope inherits that approval, while a specification outside it stops the run for renewed authorization.
- **GATE-402** MAY: Let the owner mark any batch task for a separate specification decision before that task runs.
- **GATE-403** MUST: Inside an approved batch, stop when a task leaves its approved scope, changes a contract, decision or vision, needs an irreversible or outside-repository action without existing authorization, meets an unexplained check failure, or meets its own stop conditions.
- **GATE-404** MUST NOT: Use change size to waive the applicable ceremony, measured input or gate; the class determines ceremony rather than an agent's claim that a task is too small.
- **GATE-405** MUST: For each checkpoint, obtain the measured reconnaissance and specification required by its cadence, develop within the approved scope, seek the concrete result decision, and move and commit the roadmap only when the checkpoint's finish line including required integration is met.
- **GATE-406** MUST: Use {{param:gate-cadence}} to select per-change or batch for the first of two owner decisions: what will be built before any code; the second is the concrete result after the verdict and live probe before merge, publish or deploy.
- **GATE-407** MUST: Apply batch ceremony by class: S has a task entry with finish line, stop conditions and touched-code map; M has reconnaissance, specification and full cycle; L is cut into M tasks; in per-change cadence every change has reconnaissance and a specification.
- **GATE-408** MUST NOT: Grant the result decision in advance or waive its evidence under either cadence.

<!-- anchor: process.gates.record -->

## Record

- **GATE-501** MUST: Record every gate decision in the specification or its approved batch record and the durable notes, rather than keeping the sole record in chat.
- **GATE-502** MUST: Write the decision immediately when the answer arrives, before launch, merge, deploy or commit, through {{cap:run-state-persist}}; a later handoff only summarizes it, because a session can end between action and handoff.
- **GATE-503** MUST: Include in the record the decision, mechanism used, what was approved, who and when.
- **GATE-504** MUST: Keep approval evidence in specification front matter and notes, with artifact identity and version or hash, scope, owner identity, timestamp and the owner's answer verbatim.
- **GATE-505** MUST: Encode specification gate state in its front-matter status; where the project's convention records integration in the batch, use that record for the result decision without giving the filename a second state encoding.
- **GATE-506** MUST: Keep the specification path stable on approval and follow the project's specification naming convention.

<!-- anchor: process.gates.spec-decision -->

## Spec decision

- **GATE-601** MUST: Present a specification containing its measured reconnaissance input, goal, scope with MAY EDIT and DO NOT TOUCH or an MVP boundary, business requirements and acceptance criteria, delivery contract and live-probe requirements.
- **GATE-602** MUST: Resolve specification contradictions before coding.
- **GATE-603** MUST: For a brownfield specification, require a reconnaissance input in its header; if absent, return to read-only reconnaissance through {{cap:spawn-role-isolated}} or its declared fallback and resubmit rather than approve an unmeasured specification.
- **GATE-604** MUST: Present a compact digest of the concrete specification: goal, scope, measurable acceptance criteria, delivery contract and side-effect channel, deficiencies and risks.
- **GATE-605** SHOULD: State runtime credential readiness in the digest using {{cap:launch-environment}}: compare required key names with permitted credential-source and session presence, report keys present but not exported without values, and flag missing access that would block a promised live criterion.
- **GATE-606** MUST: Ask one supported owner question offering approve and launch, rebuild with the requested changes, or cancel the feature.
- **GATE-607** MUST: Route to implementation only on explicit approval; record the decision and its mechanism in the specification and notes before launching anything.
- **GATE-608** MAY: For a large or risky specification, submit it as the complete plan through {{cap:plan-mode}}; explicit owner approval of that exit satisfies the first decision, while a conversational yes inside plan mode does not.
- **GATE-609** MUST: Offer cancellation as a real choice; a known deficiency is approvable only when the approval record names that deficiency, and the measured-reconnaissance prerequisite is still mandatory.

<!-- anchor: process.gates.plan-mode -->

## Plan mode

- **GATE-701** MUST: Stay in {{cap:plan-mode}} until its explicit exit succeeds or the owner switches session mode; an imperative request to implement means plan the implementation while this mode remains active.
- **GATE-702** MUST NOT: Treat conversational agreement, including an answer to a planning question, as approval or an exit from plan mode; incorporate the confirmed choice and submit the full plan through its exit channel.
- **GATE-703** MUST NOT: Mutate in plan mode: use non-mutating reads, searches, static analysis and checks rather than file writes, configuration changes, rewriting formatters or generators, or commits.
- **GATE-704** SHOULD: Prefer existing functions and established project patterns over new machinery when planning.
- **GATE-705** MUST NOT: Use {{cap:todo-list}} to track the planning phase; it tracks implementation after the approved plan.
- **GATE-706** MUST: Inspect discoverable facts and ask the owner only for owner-controlled choices or material ambiguity; locate code and current behavior from the files.
- **GATE-707** MUST: Make the plan decision-complete: goal and success criteria, changes by subsystem, public API, schema and data flow, edge cases, failure modes, tests, acceptance criteria and explicit assumptions, concise to review and sufficient for another engineer to implement.
- **GATE-708** MUST: Send the exit-plan call through {{cap:plan-mode}} with the complete plan starting with a title as the only and final tool call of that response; do not substitute a plain plan reply or a prose or question-tool request to proceed.
- **GATE-709** MUST: After a rejected plan, incorporate feedback and resubmit; if the review channel is unavailable or aborted, stay in plan mode and ask for a manual mode switch rather than start implementation.
- **GATE-710** SHOULD: Apply the active plan-mode restrictions even when a later tool description suggests a mutating action.

<!-- anchor: process.gates.result-evidence -->

## Result evidence

- **GATE-801** MUST: Before the result decision, run and record a minimal end-to-end live probe on the path named in the specification and actually used by the product, including asynchronous or streaming execution when applicable; a slower synchronous path is not substitute evidence.
- **GATE-802** MUST: State plainly when live verification is unavailable, use only authorized destinations and label that check unverified rather than passed.
- **GATE-803** MUST: Present test summary, full blast-radius inventory, acceptance results, deviations including scope or business-requirement deviations, live-probe output, finalize report and independent review as result evidence.
- **GATE-804** MUST: Record git HEAD, branch, dirty paths and untracked paths before work as the blast-radius baseline.
- **GATE-805** MUST: Build the complete changed-file inventory from `git status --porcelain -uall`, `git diff --name-only HEAD` and `git diff --stat HEAD`; inspect staged, unstaged and new files explicitly, preserve spaced and renamed paths when parsing, and anchor any filesystem-delta fallback on the run-start revision rather than a documentation-generator configuration.
- **GATE-806** MUST: Show a discriminating check failing before the fix, recording the command and observed RED failure as evidence that the check can reject the regression.
- **GATE-807** MUST: Where the adapter supplies a guard through {{cap:check-runner}}, record its exit before commit and label it PRE-COMMIT; a post-commit empty diff is vacuous evidence, and an unavailable guard is reported as guard not run.
- **GATE-808** MUST: Identify the exact judged state: commit hash when the run committed on its own branch, otherwise base revision plus a hash of the diff and new-file contents so untracked work is identified too.
- **GATE-809** MUST: For an applicable guard, demonstrate that its intended regression makes it fail, then remove only that owned regression; this is evidence and not a third owner decision.
- **GATE-810** MUST: Run an available guard over the work tree with specification, plan and explicit run-start base revision through {{cap:check-runner}}; interpret 0 as clean, 1 as loosening and 2 as could-not-run, avoiding an implicit HEAD base that hides earlier changes in the slice.
- **GATE-811** MUST: Surface every BAR_WEAKENED hit to the owner, report the count of exit-neutral ADVISORY lines and do not silently waive them because the suite is green.
- **GATE-812** MUST NOT: Report guard exit 2 as clean; the result must say guard not run.

<!-- anchor: process.gates.review -->

## Review

- **GATE-901** MUST: Obtain an independent review through {{cap:spawn-role-isolated}} over the whole blast-radius diff before the result gate; the reviewer verifies without fixing in place.
- **GATE-902** MUST: Add security review to the independent review for authentication or token slices.
- **GATE-903** MUST: List merge-blocking review problems with file and line, why each blocks integration, and how to reproduce the failure.
- **GATE-904** MUST: Route actionable review findings as a Bug Report to the debugger through {{cap:workflow-orchestration}} within the existing loop budget, rerun independent QA and refresh the report; never repair silently in the reviewer phase.
- **GATE-905** MUST NOT: Weaken acceptance criteria to obtain approval.

<!-- anchor: process.gates.result-decision -->

## Result decision

- **GATE-1001** MUST: Ask the supported result question with merge, rework with a concrete Bug Report, and reject; recommend merge only when the live probe and required evidence are green, and preserve artifacts on rejection.
- **GATE-1002** MUST: Ask only for the ungranted merge, publish or deploy decision over the concrete result; specification approval is not blanket integration approval.
- **GATE-1003** MUST: Treat commit and merge as distinct operations, each requiring its own applicable authorization.
- **GATE-1004** MUST NOT: Let inner role phases commit or merge; integration belongs to the parent.
- **GATE-1005** MUST: Commit named files only, excluding unrelated changes and secrets.
- **GATE-1006** MUST NOT: Treat rejection as authorization for a destructive rollback; preserve work and artifacts until that separate action is authorized.
- **GATE-1007** MUST: After authorized integration, update roadmap checkboxes, position marker and notes, record actual results in the handoff and commit through the authorized parent; do not mark integration complete before the result decision.
- **GATE-1008** SHOULD: Present the result decision in this order: what waits for the owner, what changed, what was found.

<!-- anchor: process.gates.git-hygiene -->

## Git hygiene

- **GATE-1101** MUST: Review git diff HEAD for staged and modified content and enumerate all new paths with git status --porcelain -uall; preserve spaces and rename destinations when parsing, and read untracked content explicitly because diff alone does not include it.
- **GATE-1102** MUST: After exposing owned new files with intent-to-add, remove only those entries with git reset -- followed by their explicit paths; leaving the empty-blob index entries can let a later restore destroy their contents.
- **GATE-1103** MUST NOT: Use unqualified git reset or blanket volume deletion, or touch another run's changes.
- **GATE-1104** MUST NOT: Treat a dirty tree as permission to commit, stash, reset or discard someone else's work; preserve it and use {{cap:worktree}} for isolation only where necessary and permitted.
- **GATE-1105** MAY: Perform read-only reconnaissance without a clean tree.
- **GATE-1106** MUST: Clean up only resources created by this run.

<!-- anchor: process.gates.terminal -->

## Terminal

- **GATE-1201** MUST: Return any non-success terminal status to the owner and wait for the next decision rather than loop the runner.
- **GATE-1202** MUST NOT: Automatically rerun or merge after a terminal status; bounded retries inside a phase may run only within its per-kind budget and approved cost ceiling before termination.
- **GATE-1203** MUST: Use the terminal vocabulary SUCCESS, SPEC_BLOCKED, VISUAL_GATE_FAIL, ESCALATED, BLOCKED, ERROR and ESCALATED_FINALIZE; phase faults and their routes map to these through the declared phase policy.
- **GATE-1204** MUST: Use SUCCESS only for completed implementation, QA and Finalize; it does not assert merge or deployment.
- **GATE-1205** MUST: Return status, goal, plan and report paths, important validation and deviations through {{cap:structured-output}} or its declared fallback, routing any ungranted integration decision through the result gate.
- **GATE-1206** MUST: Update durable notes and handoff honestly through {{cap:run-state-persist}} even when the run is blocked.
- **GATE-1207** MUST: Close a roadmap checkpoint only when its own completion criterion holds, including integration where required.
- **GATE-1208** MUST: Before repeating a side-effecting push, migration, deploy or send with unknown fate, inspect whether it already applied; if still UNKNOWN, record intent durably and ask the owner rather than repeat it, because timeout proves nothing about delivery.
- **GATE-1209** MUST: At escalation, offer grant or abort; range-check extra iterations in 1..20, default 1, and extra cost ceiling in USD 0..1000, default 0, capping each grant at 20 iterations and USD 1000; reject invalid ranges rather than blindly coerce them and record explicit owner consent before spending again.

- **GATE-1210** MUST: If the traceability lint exits 1 for SCOPE_CREEP, UNKNOWN_BR or UNCOVERED_REQUIREMENT, stop the cycle as VISUAL_GATE_FAIL and return to the owner for a decision.

<!-- anchor: process.gates.surfaces -->

## Surfaces

- **GATE-1301** MUST: Have the frontend relay the gate to the owner and return its answer through the declared mechanism; a one-shot smoke route is not evidence of a full human session.
- **GATE-1302** MUST NOT: Read a headless or unattended run as owner approval; label unmeasured no-human behavior UNMEASURED and do not transfer results between different routes, including a route that exits 0 with an unanswered-question error.
- **GATE-1303** MUST: Treat a frontend unable to relay a structured question and answer as unable to satisfy that channel; only a valid declared fallback can replace it.

<!-- anchor: process.gates.answer-handling -->

## Answer handling

- **GATE-1401** MUST: Reject bad owner payloads with an error value and re-ask through a fresh answer opportunity rather than terminate or replay the rejected input indefinitely.
- **GATE-1402** MUST: Explain a rejected answer with its type or field locations and validation messages as applicable, and log the rejection at high importance without sensitive values.
- **GATE-1403** MUST: Tolerate unknown annotation keys and supported equivalent spellings in owner input while rejecting unknown decision actions; machine verdicts forbid unknown fields so contract drift fails loudly.
- **GATE-1404** MUST: Block after three malformed answers at one gate by default; an adapter override must state its reason, and a valid answer is recorded immediately and never asked again.
