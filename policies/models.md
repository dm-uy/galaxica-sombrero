---
id: policies.models
title: Model tiers
status: draft
---

# Model tiers

Model selection contributes to a verified task result. The tiers retain their meanings in the
[parameter registry](../runtime/parameters.md); concrete selections and supported controls belong in the
[adapter](../runtime/adapters.md), under the existing [delegation authority](../flow/delegation.md).

<!-- anchor: policies.models.selection -->

## Adequate selection

- **MODEL-101** MUST: Prefer a deterministic tool or script when it completely performs the required mechanical operation and its applicable checks with adequate reliability. Use a model when the remaining required work needs one; a partial mechanical result does not complete a judgment task.
- **MODEL-102** MUST: Select a sufficient tier, supported effort/settings and context by the hardest necessary step of the assigned task, rather than its average or role label. Use {{param:model-mechanical}} for mechanical work, {{param:model-routine}} for routine work of a known shape and {{param:model-judgment}} for judgment through {{cap:model-tier}}. Fixed role/phase defaults are starting bindings, never substitutes for task adequacy; do not choose the largest model automatically without task justification.
- **MODEL-103** MUST: Split mixed work only into independently meaningful slices when separation reduces total work while preserving relevant context, dependencies and explicit ownership of the combined result. Assign each slice sufficient capability for its own hardest necessary step; otherwise retain the whole task's requirement.

<!-- anchor: policies.models.economy -->

## Total work to a verified result

- **MODEL-201** MUST: Compare adequate authorized choices by total cost and time to a verified result, including delegation/setup, context size and rereading, queue/response latency, retries, repair and verification effort. Cheapest token price alone cannot decide selection when required capability, reliability or verification would suffer; use observed task performance where available and label estimates.
- **MODEL-202** MUST: Avoid redundant agents and unjustified repeated checks while retaining every approved acceptance criterion, required independent review and valid verification of changed work. Identify why a repetition or extra worker is needed before treating it as useful economy; a shorter run that omits required work is not a verified result.

<!-- anchor: policies.models.context -->

## Sufficient relevant context

- **MODEL-301** MUST: Give each worker relevant sufficient inputs, actual constraints and known limitations through {{cap:context-management}} or its declared fallback. Prefer narrow self-contained fresh briefings and the applicable handoff/delta over unnecessary accumulated history, following DELEG-401 through DELEG-404 in the [briefing contract](../flow/delegation.md). Reduced context must retain the facts needed to perform and verify the assigned slice.

<!-- anchor: policies.models.binding -->

## Actual runtime bindings

- **MODEL-401** MUST: Discover actual model choices, selection/effort controls, concurrency and permission restrictions through {{cap:capability-discovery}} before selection. Bind choices under DELEG-201 in the [activation contract](../flow/delegation.md): availability does not authorize an override, and overrides remain unset absent an explicit selection under existing policy/owner authority. An explicit declared adapter selection need not imply permission for a tool-level override.
- **MODEL-402** MUST: Keep concrete models, providers and supported effort/settings in adapter mappings of the existing three model parameters and model-tier capability. Choose mappings using available capabilities and observed task performance, assessing unfamiliar choices for required fit; runtime-specific aliases, pins, inheritance and configuration precedence are adapter facts, not universal tier rules.
- **MODEL-403** MUST: Declare limitations and the actual authorized fallback when model selection, dynamic routing or effort controls are unavailable. One available model may serve multiple tiers if adequate for their tasks. Declare absent controls explicitly and do not claim a mechanism or dynamic selection the runtime cannot perform.

<!-- anchor: policies.models.reassessment -->

## Reassess inadequacy

- **MODEL-501** MUST: Reassess and raise capability for unresolved judgment, ambiguity or demonstrated inadequacy, selecting an authorized adequate judgment tier for the affected work when available. Preserve usable work and record the reason, affected part and result; reassessment remains subject to existing failure and approval routes.
- **MODEL-502** MUST: Diagnose an ordinary mechanical slip and repair it within the current limits; the slip alone does not require tier escalation. A task type that verifies adequately on its current tier may stay there; unresolved judgment or evidence of inadequate capability invokes MODEL-501.
- **MODEL-503** MUST: Use the existing blocked/escalation route when authorized available capability cannot adequately complete or verify required work. A stronger available model supplies no additional authority. Investigate unknown side-effect completion before retry or replay under DELEG-504 in the [return contract](../flow/delegation.md).

<!-- anchor: policies.models.continuity -->

## Continuity and independent verification

- **MODEL-601** MUST: Preserve scope, authority, outstanding effects, work/evidence history and all spent phase, retry, response-correction and repair budgets when switching model, worker or context. A switch grants no fresh attempt or reset; use the actual pre-entry spend and remaining allowance under DELEG-204, DELEG-405 and DELEG-503 in the [delegation contract](../flow/delegation.md) and STATE-303 in the [run-state contract](../flow/run-state.md).
- **MODEL-602** MUST: Reuse evidence only when unchanged input/code/configuration identity and current applicability establish its validity. Name the evidence and its retained scope explicitly; verify changed artifacts and perform required review. Prior passing evidence does not prove a changed candidate or waive renewed QA required by the flow.
- **MODEL-603** MUST: Keep an independent actor wherever the [QA contract](../roles/qa.md) requires independent verification, with capability adequate to check the judgment involved. Cost reduction cannot make author self-review equivalent to independent QA, or structural conformance equivalent to semantic verification; routine checks alone cannot establish an architectural, legal, privacy or security judgment.

<!-- anchor: policies.models.records -->

## Honest run records

- **MODEL-701** MUST: Record the requested tier, concrete model and supported effort/settings with a concise task reason in existing run records available through {{cap:run-record-access}}. Record the observed model/settings separately when exposed, including relevant issuer/inheritance observations; a requested selection is not proof of the identity that ran.
- **MODEL-702** MUST: Preserve available usage, duration, retries and outcome with the selection/reassessment evidence. Identify unavailable observations as unknown and distinguish estimates from measured facts; do not invent model identity, effort support, usage or execution results.
- **MODEL-703** MUST: Assess economy per verified task using available total-work evidence and its limitations. Distinguish structural checks, finite scenario interpretation and live runtime adoption; do not claim monetary, time or token savings from unmeasured assumptions or policy conformance alone.
