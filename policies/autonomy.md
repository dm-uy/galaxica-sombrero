---
id: policies.autonomy
title: Autonomy
status: draft
---

# Autonomy

Autonomy describes how an executor continues inside an actual grant. It does not grant a task,
select a software role or change the [two owner decisions](../process/gates.md). A launch switch
and a sentence saying "work autonomously" are profile inputs, not evidence of approval or an
enforced permission boundary. This policy is also an input to [agent prompt authoring](../prompting/agent-prompt-design.md);
authoring that contract does not launch its consumer.

<!-- anchor: policies.autonomy.profile -->

## Declare the operating profile

- **AUTO-101** MUST: Identify the actual task, approved scope, required outputs, success criteria, stop points and applicable owner decision before describing interactive or unattended work; record the grant's source and artifact identity rather than invent approval from the chosen mode.
- **AUTO-102** MUST: Resolve actual launch/autonomy controls and answer mechanism or declared fallback through {{cap:launch-environment}} and {{cap:capability-discovery}}; distinguish a documented profile, an available mechanism and observed runtime behavior.
- **AUTO-103** MUST NOT: Treat an autonomy switch, permissive tool configuration, absent question tool, silence, timeout, default selection or exit 0 as owner consent; apply the existing gate channel and matching-approval rules.
- **AUTO-104** MUST: State what an unattended route cannot complete when an owner answer or unavailable mechanism is required; report that boundary honestly rather than claim the process necessarily halts or the gate passed.

Declare mode by the work actually permitted, rather than its launcher name. Interactive work
can continue autonomously through routine steps between owner decisions. Unattended work can
prepare an authorized artifact but cannot supply the missing owner decision. A runtime that
returns an unanswered-question error and exits successfully supplies output, not approval.
Its observed behavior belongs to that exact route and binding; another surface needs its own evidence.

<!-- anchor: policies.autonomy.choice -->

## Continue or hold a choice

- **AUTO-201** MUST: Use the task's declared criteria for routine delegated selections and preserve already accepted decisions; generate and compare meaningful alternatives under [superposition and collapse](../prompting/superposition-collapse.md) when an actual open choice needs it.
- **AUTO-202** MUST: In an interactive strategic fork requiring the owner's choice, hold the alternatives and present their effects before collapse; in an authorized unattended routine selection, record the criteria, selected alternative and rejected reasons without inventing a new owner decision.
- **AUTO-203** MUST: Label criteria extracted from the task separately from proposed operational criteria; use synthesized criteria only where the existing grant delegates that decision and they do not change the goal, scope, contract or acceptance criteria. Missing strategic criteria remain an owner question.
- **AUTO-204** MUST NOT: Manufacture an unresolved choice or reopen a settled answer merely to satisfy a ritual; identify new contradictory evidence when reopening is justified.

Some source profiles synthesize a minimum criterion set and collapse without interaction.
That profile is conditional on delegated decision authority; its criterion count is not a new
universal requirement. A choice of equivalent output serialization under an approved schema
can be routine. Changing the product's audience or accepting a lower finish line is an owner
choice even if an agent calls it an implementation detail.

<!-- anchor: policies.autonomy.execution -->

## Carry the authorized work through

- **AUTO-301** MUST: Continue necessary steps inside the existing grant until the declared output and finish line are complete, providing concise status with the next action; do not request a second approval for a decision whose channel, scope and artifact still match.
- **AUTO-302** MUST: Stop dependent work at an applicable gate, task stop point, scope departure, specification that cannot be met as written or contradicts measured inputs, unexplained check failure, exhausted allowance or action lacking required authority; identify the actual reason and use the accepted failure/terminal route.
- **AUTO-303** MAY: Continue independent research or reversible preparation within the grant while an answer waits, only when that work neither depends on the pending answer nor crosses the gate.
- **AUTO-304** MUST NOT: Use autonomous prose to disable tool permission checks or authorize destructive, irreversible or outside-scope actions; inspect an unknown side effect before considering a repeat under the [existing gate contract](../process/gates.md).
- **AUTO-305** MUST: Preserve cumulative spend, errors, unknown effects and valid artifact evidence across context, worker, model or session changes, using [run state](../flow/run-state.md) and [model policy](models.md); a fresh context is not a fresh allowance.
- **AUTO-306** MUST: Carry owner corrections through the actual supported follow-up mechanism or next applicable gate; reconcile changed scope with matching authorization and retain prior failure/held history rather than silently resetting it.

A source proposal for a spend supervisor, notification bridge or deterministic driver is not a
current implementation. A declared ceiling and stop condition can exist even when automatic
supervision is unavailable: name who observes it and the limitation. Do not promise monitoring,
goals, notifications or runtime isolation merely because a source describes them. Existing role,
phase and retry contracts own the execution sequence and counted units.

<!-- anchor: policies.autonomy.forms -->

## Profile form and worked decisions

This is an authoring form, not a new run-state schema. Fill every slot, using an explicit
not-applicable reason where the task has no corresponding effect.

```text
AUTONOMY PROFILE
Task/artifact identity: <actual task and version or hash>
Goal and grant: <owner authority, exact scope and approval source>
Mode/route: <interactive or unattended; actual runtime route>
Allowed writes/effects: <paths, destinations and permissions>
Outputs/finish line: <complete artifacts and observable success criteria>
Criteria: <task-sourced criteria; separately labelled delegated operational criteria>
Choice authority: <routine choices delegated; strategic choices held>
Stops: <task conditions plus applicable gates and exhausted allowances>
Answer channel: <actual mechanism or declared fallback; unavailable limitation>
Independent work while waiting: <admissible work and dependency boundary>
Continuity: <spent units, errors, unknown effects and retained evidence>
Outcome record: <completed work, pending decision, evidence and next action>
```

The following supplied fictional input grants a local report, but no publication. Its derived
output is a manual illustration, not a runtime receipt.

```json
{
  "task": "summarize supplied inventory revision r3",
  "grant": "owner approved writing reports/inventory.md from supplied inventory r3",
  "mode": "unattended",
  "allowed_writes": ["reports/inventory.md"],
  "allowed_effects": ["read supplied inventory", "write local report"],
  "outputs": ["complete report with unresolved rows identified"],
  "finish_line": ["each supplied row appears exactly once", "no invented row values"],
  "criteria": {"task_sourced": ["exact row coverage", "source-backed fields"], "delegated_operational": ["sort by supplied stable row ID"]},
  "choice_authority": {"routine": "choose stable ordering", "strategic": "publication destination remains owner-controlled"},
  "stops": ["missing supplied row", "new output destination", "publication decision"],
  "answer_channel": "declared explicit owner chat fallback when owner returns",
  "independent_work_while_waiting": "prepare the local report before any publication decision",
  "continuity": {"prior_failures": 0, "unknown_effects": [], "allowance_reset": false},
  "outcome": {"local_report": "may complete within grant", "publication": "pending matching result decision", "runtime_evidence": "NOT_RUN"}
}
```

Boundary decisions use the supplied conditions below, rather than asserted tool outputs:

| Supplied condition | Expected decision and reason |
|---|---|
| Same report grant, owner present, two equivalent allowed orderings | Use the declared routine criterion; no renewed strategic approval is needed. |
| Unattended route has no answerer and returns exit 0 after a question error | Preserve the report as unapproved output; do not publish or declare the gate passed. |
| Requirement needs choosing a new audience, with no delegated criteria | Hold alternatives for the owner; continue only independent preparation. |
| Required answer is pending, but report formatting is independent | Format within approved paths; the pending answer still blocks dependent work. |
| Retry changes model after a failed attempt | Retain spent allowance and failure; changing model alone grants no retry. |
| Tool can delete a remote dataset, report grant names only a local file | Capability availability does not authorize deletion; use the actual stop/decision route. |

Review checks the grant against every allowed effect, the finish line against every output, the
criteria against actual delegated authority, and the answer mechanism against the route's known
limits. A populated form proves declared intent; runtime enforcement and completed delivery
require their own evidence.
