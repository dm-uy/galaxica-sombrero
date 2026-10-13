---
id: process.batch
title: Current task or bounded batch
status: draft
---

# Current task or bounded batch

<!-- anchor: process.batch.packet -->

## Work packet and autonomy

- **BATCH-101** MUST: Each runnable task has goal/route, actual grant, deliverable, scope/artifact owner, necessary inputs, finish conditions, exceptional stops, state/dependencies, result evidence and next disposition. One task and a bounded batch use the same fields.
- **BATCH-102** MUST: Continue ordinary steps within the grant without repeated approval. Reserve consequential ungranted forks and release actions for their owner; silence, default choices, tool results and other agents do not create consent.
- **BATCH-103** MUST: Preserve the original packet and result before replacing TASKS. Blocked, deferred and dropped tasks retain reasons and next disposition. Resume preserves pending decisions, unfinished work and cumulative failures.
- **BATCH-104** MUST: Assess the real deliverable against finish conditions and attribute author claims, self-review and independent review. Negative research may answer its question without proving an undelivered capability; done is distinct from separately reserved integration/release.
- **BATCH-105** MUST: Record substantive scope changes against the actual grant. A status update cannot enlarge authority. Unknown consequential action completion retains intent/observations and is investigated before replay.

<!-- anchor: process.batch.planning -->

## Plan one task or a bounded packet

The packet custodian reads the entry/profile, current outcome, necessary requirements/source inputs, relevant decisions and open choices, the old packet and its actual results. A single task uses the same contract as a batch. The deliverable is a reviewable proposed packet with concrete finish/stop conditions, dependency order, ownership and authentic grant provenance; drafting it alone does not activate it.

- **BATCH-106** MUST: Partition execution by actual dependencies and unresolved go/no-go decisions; do not treat approval of a decision task as approval of work contingent on its unknown result.
- **BATCH-107** MUST: On activation reconcile task, route and handoff with the matching actual grant; reserve decision IDs only under an existing project registry and its allocation authority.
- **BATCH-108** MUST: Before cleanup verify the resource belongs to the run, inspect ignored and uncommitted content, preserve nonregenerable state and obtain the applicable integration/cleanup authority; a clean status alone is insufficient.

1. Locate the current route focus and the actual question/result it requires. If direction, an authoritative input or a required owner choice is missing, describe the blocker before scheduling dependent execution. Read only the relevant requirements, decisions and evidence links; do not turn planning into a whole-history read.
2. Cut work into bounded tasks, each with goal/route ID, actual grant or pending decision, deliverable, allowed artifacts and writer, inputs, observable finish conditions, exceptional stops, state/dependencies, result evidence and next disposition. Express a finish as something a reviewer can observe, rather than “work on review.” Identify the selected execution method; use its established checks and limits.
3. Partition by prerequisite and shared write surface. Independent tasks may run concurrently only under the project's collision/isolation rules and available authority. Give each assigned writer exact allowed paths and inputs; a shared current-state document has one custodian. Separate branches/copies can isolate work but do not create permission to write shared artifacts. Name dependencies that prevent parallel execution.
4. Separate a go/no-go question from contingent work. The packet can include a bounded decision/research task and describe the possible later action, but that action stays pending unless an authentic grant explicitly covers the applicable conditional branch. In the ordinary case plan it after the result, in a later packet. Silence or elapsed time does not settle the decision.
5. Size the packet to a credible work horizon under the chosen method. Carry unfinished previous tasks explicitly before replacing the current file; retained dropped/blocked/deferred rows keep their reasons, evidence and return conditions. Do not present a rewritten packet as if the original had all succeeded.
6. Present the outcome, tasks/finish lines, exclusions and owner-only choices. Record a real approval's who/when/channel and exact covered packet/specification identity. Existing clear matching human consent counts under applicable authority; a filled form, status flag, agent claim or default answer does not. If approval is required and unresolved, keep the packet proposed and continue only independent already granted work.

For the existing software specialization, S is a small change without a contract/direction change, M requires the project's recon/specification and development cycle, and L is divided before execution. Classification follows the actual changed surface, not a desire to skip checks. This conditional profile preserves the established software-role/QA/repair interfaces; general document/research tasks do not acquire mandatory code maps or feature-dev phases from the letters.

<!-- anchor: process.batch.execution -->

## Activate, dispatch and track

**Activation.** The custodian checks the recorded human grant against the actual packet, current inputs and prerequisites. Set the permitted tasks/packet active using project vocabulary, reflect approved started work in the route, and rewrite the baton in the same state update: what the packet is for, its pointer and next eligible task. If project policy requires a commit, these related records are committed together when authorized. Otherwise report the saved state and ownership honestly. Activation does not expand scope or waive a separate result decision.

**Conditional decision reservations.** When the project already uses numbered decision records, the designated allocator examines existing recorded and reserved IDs before assigning a new one. A known decision task reserves its number during planning; other required reservations are allocated at activation, and an unexpected decision receives an allocation before its writer creates the record. Parallel writers do not independently select numbers. References resolve either to a real record or an explicit reservation. A reservation has no accepted decision body until its authority actually decides. Projects using local task decisions need no new numbered registry.

**Dispatch.** Resume unfinished active/review work before opening the next eligible task, subject to actual dependencies and ownership. Send the assignee its full contract: goal, inputs, allowed paths, finish line, method/checks, exceptional stops and required result evidence. Follow the host's authorized delegation and routing policy. Keep current packet updates under its one writer; other contributors report results to that custodian. A correction inside the existing grant is a follow-up to the same work, not a fresh run that loses failure history. A changed specification/scope follows its actual change authority.

**Track.** Record start, meaningful observation, block and finish promptly. Route a local choice to the task/notes; a future-binding decision to its existing owning home with authentic provenance; errors to existing notes with relevant task/context or evidence. No additional learning program, experiment or metric process follows from recording an error. Preserve the existing task's root-cause repair and QA obligations. When a stop condition fires, record the reason, affected dependencies, owner action or missing input and return condition. Other independent granted tasks can continue. When an effect's fate is unknown, preserve the intended action and observed response, investigate actual effects and do not replay blindly.

**Verification and assessment.** Inspect the actual artifact/input identity and every claimed result. Distinguish author claim, self-review and independent review; verify that the declared checks ran on the relevant candidate. A “success” label covers only the work actually checked. List each skipped, not-run, deferred or blocked check with its reason, required input/environment, recovery action and criterion affected. Required unavailable proof prevents claiming that criterion met. For research quotations verify against the fetched source, not a search summary; for a local formatting check do not claim semantic or operational delivery. Keep verification read-only over the candidate; any check that needs mutations uses an authorized isolated copy, not the author's working state. The chosen software method retains its independent QA, scans and live-channel obligations. A document comparison can use an independent source/claim review; no software machinery is inferred.

The assessment output is a task result linked from TASKS: actual deliverable, evidence, reviewer attribution, failures/limits, whether each finish condition is met, and next disposition. Negative research can complete a question with a supported negative answer; it cannot prove the proposed capability works. “Done” does not authorize an owner-reserved integration, publication, deployment or send.

<!-- anchor: process.batch.closure -->

## Close, archive and carry forward

At packet end, inspect every row and present owner blockers first, then actual changes/evidence and confirmed findings/limits. Prepare the concrete result for any reserved result decision. Rework sends findings back to the same task with retained counters/history; rejection or cancellation retains the reason and the actual artifacts. No terminal engine status silently substitutes for the owner decision.

Before replacing TASKS, retain the original packet, authentic grant and results in the project's established archive/notes home. At the event specified by the profile—often accepted integration—archive the final packet with all task states, not just done rows. Each unfinished task has one explicit destination: the next packet, the outcome route or deferred work, with original ID/state, dependencies, reason and return condition. The new current packet links to that lineage; the route closes only achieved outcomes and the baton points to the next actual permitted task. If integration is still pending, state that fact and keep recoverable current work instead of pretending it merged.

Cleanup is a separate ownership and preservation check. Enumerate only resources created by this run and verify actual merge/integration evidence where the profile requires it. Inspect ignored files as well as visible status; a supposedly clean worktree may hold the only nonregenerable input or configuration. Preserve required state in an authorized destination before removal. Confirm resource ownership, absence of another active writer, branch/result lineage and the actual cleanup grant. Foreign or shared resources remain untouched; record their owner and blocker. Use the project's safe removal mechanism only after these checks. Conflicting source-specific destructive commands provide no general permission to force-delete a branch, reset a tree or erase data. Record what was preserved/removed and why, then complete [session closure](session.md).

<!-- anchor: process.batch.cases -->

## Worked packet and refusal cases

Every Meadow document review row, consent and observation here is fictional. The [TASKS form](../documents/templates/TASKS.md) provides the full editable packet and separate filled examples; no example grants execution.

In an imagined B-002 packet under outcome P2, T-201 inventories supplied policy definitions and T-202 drafts a checked comparison from that inventory. The imagined owner's local-review grant covers these two tasks and their named records, not external sharing. T-202 depends on T-201's source inventory. T-203 would assess an absent appendix; it is blocked with reason “appendix unavailable,” preserved original ID and return condition “owner supplies a usable appendix.” A sharing task is future work under P3, pending a go/no-go decision on the completed packet and a separate sharing grant. B-002 activation updates TASKS, P2's active row and HANDOFF together. The inventory writer and draft writer use distinct artifacts; the custodian alone updates TASKS.

The fictional inventory result records which inputs were examined; the draft assessment identifies checked and unchecked claims. An independent reviewer verifies the available-text claims. T-201 is done only with its actual inventory evidence; T-202 remains in review if a required source check is missing. T-203 remains blocked in the archived packet and is carried to the next packet with the same ID and appendix return condition. T-204 remains held for interviews under deferred outcome P4; the earlier B-001/T-101 failed review remains linked as history. The new TASKS points to B-002's retained result. The owner decision about sharing stays pending even if the local draft is done.

If a contributor deletes T-203 or an earlier failed review row, closure restores it from the retained packet and records the change; omission cannot manufacture success. If an input link is missing, dependent comparison stops until the source is recovered. If a filled fictional record says “Gate A approved,” the activation check rejects it as authority and consults the real project gate record. If delivery timed out, the custodian checks the intended destination before any retry because the effect may already exist. If a cleanup list includes an ignored directory used by another session, ownership prevents deletion even when status is clean. These refusals preserve the approved local work while keeping ungranted or unverified actions blocked.
