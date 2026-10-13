---
id: prompting.decomposition
title: Decomposition
status: draft
skill-name: prompting-decompose
skill-when: Author bounded semantic steps with explicit inputs, outputs, checks and recoverable handoffs.
---

# Decomposition

<!-- anchor: prompting.decomposition.boundaries -->

## Split at a real change of responsibility

A useful step does one coherent transformation: inspect supplied information, design a plan, author an artifact, or verify a result. Mixing uncertainty resolution with irreversible execution hides the boundary at which a real grant or evidence is needed. Step count alone does not make a decomposition good. The source's approximately five-to-seven consecutive steps is a planning heuristic; longer work can group steps and hand off compact state without erasing progress or spending.

- **DECOMP-101** MUST: Give each step a specific input, owner, allowed effects/tools, output schema/artifact, acceptance/consistency check and failure route. Sequence dependencies; parallelize only independent authorized work with explicit path/state ownership.
- **DECOMP-102** MUST: Distinguish authoring/planning outputs from actual execution outputs and preserve the accepted software phase/gate/role order when describing software work. Source phase labels are conditional illustrations.

A plan is a reviewable artifact, not a completed side effect. A status such as PENDING, IN_PROGRESS, DONE, FAILED or HELD denotes operational task state backed by artifacts. It is not a request to reveal hidden beliefs or private chain-of-thought. A concise decision summary, observable calculations and evidence explain the result. Generated explanatory chains can be wrong, so [verification](verification.md) and independent checks remain necessary when applicable.

<!-- anchor: prompting.decomposition.procedure -->

## Build, cross-check and hand off

Start with the actual goal, grant, inputs and stop points. List natural modes and their dependency edges, then define input/output contracts at each transition. A later phase receives a checked output plus the necessary source references, not an entire irrelevant history. Check a transition before advancing: structure/type, goal fit, required source/evidence, constraints, completed artifact and unresolved effects. A failure routes to its bounded owning repair step or a held terminal state; a changed context does not silently retry all work.

For design, reconcile static components, scenario data flow and measurable acceptance criteria using [solution design](solution-design.md) and the actual [graph](../protocols/graph.md)/[plan](../protocols/dev-plan.md) contracts. Every relevant component is accounted for across the declared scenarios; every flow step uses established components. Do not demand that optional/error-only nodes appear in every happy path. Resolve inconsistency before an execution consumer treats the plan as ready.

- **DECOMP-103** MUST: Persist completed/failed state, attempt units and spend, authorization, unknown effects and next action across handoff/reset; a new worker, model or session never resets a budget or confers permission.

Placeholder phase form:

```text
$START_PHASE
ID: [Unique phase ID and coherent mode]
OWNER: [One owner; exact writable paths/state fields]
INPUT: [Checked upstream artifact identities and relevant facts]
ALLOWED_EFFECTS: [Tools/effects granted, or authoring only]
OUTPUT: [Exact artifact/schema and terminal status]
CHECK: [Observable completion and consistency conditions]
FAILURE_ROUTE: [Bounded repair owner or HELD/FAILED with reason]
NEXT: [Dependency and condition to advance]
$END_PHASE
```

Placeholder compressed handoff:

```text
$START_HANDOFF
GOAL_AND_GRANT: [Actual scope, authority and stop points]
CURRENT: [Phase, owner, exact artifact paths/identities]
DONE: [Completed checked outputs and evidence]
FAILED_OR_HELD: [Failures, unresolved findings, unknown effects]
BUDGETS: [Each counted unit, spent/max and terminal constraints]
NEXT: [One next authorized action, required inputs and failure route]
$END_HANDOFF
```

<!-- anchor: prompting.decomposition.example -->

## Filled illustrative multi-stage task

Fictional task: author a plain-text session schedule from two supplied workshop entries. The owner permits local drafting and review, with no invitations or publication. Supplied entries: “Reading, room A, 09:00” and “Discussion, room B, 10:00”. No dates or live room availability are known; the artifact says so.

| Phase / owner | Input | Allowed effects | Output / check | Failure route |
|---|---|---|---|---|
| Inspect / author | Two literal entries and drafting grant | Read supplied data | Entry records with title/room/time; neither entry omitted | HELD if an entry lacks a required field |
| Plan / author | Checked entry records | Author text only | Proposed layout including unknown-date note; plan uses both entries | Return to Inspect for inconsistent data |
| Draft / author | Checked layout and records | Write only the authorized draft artifact | Full two-line schedule plus unknown-date note; no invented times | One bounded drafting correction if a line differs |
| Verify / reviewer | Draft plus original records | Read and report only | Both source entries match; date limitation present; no publication claim | Report exact mismatch to author; preserve failed attempt |

These names describe this nonsoftware authoring task; they do not reorder the software flow. The illustrated draft is complete:

```text
Session schedule — date not supplied
09:00 — Reading — room A
10:00 — Discussion — room B
Room availability has not been independently checked. This is a draft for the coordinator.
```

Filled handoff:

```text
$START_HANDOFF
GOAL_AND_GRANT: Draft and review the supplied schedule only; invitations/publication need their own grant.
CURRENT: Verify; reviewer owns the read-only review; author owns schedule.txt.
DONE: Two source entries inspected; layout and complete schedule authored.
FAILED_OR_HELD: None observed in this fictional case; date and live availability remain unknown.
BUDGETS: Draft correction 0/1; no software Debug cycle has been started.
NEXT: Compare both draft entries to supplied records; report mismatch or approve the draft for coordinator review.
$END_HANDOFF
```

The example describes expected artifact handling, not an actual independent review or file-delivery receipt. If a real step requires an unavailable tool, missing source or new effect, its output remains HELD/FAILED with the missing requirement; no invented “DONE” replaces the artifact. The prompt author hands the completed decomposition and assumptions to its separately authorized executor.
