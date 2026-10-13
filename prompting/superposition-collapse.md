---
id: prompting.superposition-collapse
title: Superposition and collapse
status: draft
skill-name: superposition-collapse
skill-when: Hold and compare two or three viable hypotheses before an authorized bounded decision.
---

# Superposition and collapse

<!-- anchor: prompting.superposition-collapse.scope -->

## Preserve alternatives before choosing

“Superposition” is a source metaphor for keeping distinct possibilities available. The procedure works at the artifact level: enumerate viable hypotheses, unfold what each requires and compare them against explicit criteria. It makes discarded alternatives and uncertainty reviewable; it does not claim quantum mechanics, native feature geometry or guaranteed optimality.

- **SUPER-101** MUST: For a genuinely unresolved bounded decision hold two or three viable alternatives before selecting, describe each against the same actual goal/constraints, and retain contrary evidence instead of writing the winner first and inventing losing options afterward.
- **SUPER-102** MUST: Collapse only under the actual authority and criteria, preserving accepted decisions, rejected/deferred reasons, assumptions, tradeoffs and reopening evidence. Use broader [brainstorm](brainstorm.md) only when exploration is needed.

An interactive comparison can be concise because the owner is present to discuss a real fork. An autonomous handoff needs durable paragraph-depth rationale for each serious hypothesis; source profiles sometimes suggest 200 or more words, but relevance and complete reasoning/evidence decide adequacy, not a universal word minimum. Neither profile requires private chain-of-thought. The existing software [Architect](../roles/architect.md) and [development plan](../protocols/dev-plan.md) own their detailed decision duties and phase order; historical THINK/TECH_STACK/PROPOSE/EVALUATE/COLLAPSE/DELEGATE labels are source illustrations, not a replacement software flow.

<!-- anchor: prompting.superposition-collapse.procedure -->

## Comparison and result

PROPOSE names actual distinct alternatives, including a valid reuse/do-less option when it meets the goal. HOLD explains how each would work, dependencies, two side effects, evidence and uncertainties, with no favorite. EVALUATE compares criterion by criterion: feasibility, impact, risk and any relevant cost/scale/debt axes. Declare weights, direction and tie-breaker, separate estimates from observations and externally check pivotal facts. COLLAPSE records the selected or held outcome and its matching decision authority. The next step remains bounded by the task grant; selection alone does not execute.

If evidence changes, revisit the specific rejected reason. A prior does not veto measured contrary evidence; unchanged facts do not make an old rejection a new discovery. An unavailable external check leaves an uncertainty or held result, not a fabricated score source. Repeating the same hypothesis in another context does not provide independent evidence.

Placeholder comparison form:

```text
$START_COMPARISON
$START_DECISION_SCOPE
[Goal, constraints, actual decision authority and known prior decisions]
$END_DECISION_SCOPE
$START_ALTERNATIVES
[Each ID: mechanism; evidence; assumptions; two effects; strongest benefit; strongest objection]
$END_ALTERNATIVES
$START_CRITERIA
[Criteria/direction/weights; score reasons; source qualification; tie-breaker]
$END_CRITERIA
$START_RESULT
[Selected or held; why; losing/deferred reasons; authority; reopen facts; next authorized action]
$END_RESULT
$END_COMPARISON
```

<!-- anchor: prompting.superposition-collapse.example -->

## Filled bounded comparison

Illustrative goal: keep a workshop's correction log usable by two editors who already share one document. Grant: choose a reversible log layout; no service acquisition, automation or publication. Prior: a shared document is accepted for this workshop; no evidence calls for changing it.

A — append-only dated paragraphs. Each correction adds the source statement, replacement and editor. This uses the existing document and keeps chronological context intact. Two possible effects are a long navigation trail and inconsistent wording across entries. Its strongest benefit is minimal structural work; its strongest objection is weak scanability once entries accumulate. The assumption is that the editors can find a date using the document's existing search.

B — a table with date, statement, correction, source and editor. Each correction occupies one row, retaining the evidence alongside the replacement. Two effects are wider rows on small screens and a need to agree concise cell wording. The strongest benefit is consistent comparison; the objection is poorer readability for a long explanation. It assumes short workshop corrections, not long investigations.

C — one page per correction plus an index. Each page can explain a complex issue and the index gives its status. Two effects are maintaining two records per correction and orphan-page risk. The benefit is ample explanation space; the objection is extra coordination for only two editors. It assumes the volume/complexity will justify an index, which is currently unmeasured.

Criteria are clarity and low maintenance, equally weighted; a tied choice favors existing single-document simplicity. Judgments: A clarity6/maintenance9; B clarity9/maintenance8; C clarity8/maintenance4. Means are A7.5, B8.5, C6.0; they are transparent design judgments, not empirical performance. Within the delegated scope B is selected: both editors can compare evidence and corrections in one record. A loses on scanability; C is deferred until long corrections justify the extra records. Reopen B if real corrections repeatedly require multi-page explanations or table access proves unsuitable. Next authorized artifact is a proposed table layout. No live editor behavior or service result has been observed in this example.

An interactive rendering could compress each paragraph into essence, two effects and criterion rationale, leaving the same authority/rejected/reopen record. Autonomous delivery retains the expanded explanation because the next participant cannot rely on unstored chat.

<!-- anchor: prompting.superposition-collapse.consistency -->

## Self-consistency is a separate technique

Self-consistency samples separately produced answers to a verifiable question and compares/votes on their results. It does not compare architectural tradeoffs and grants no delegation rights. Define the question, actual sampling independence, finite number of attempts, aggregation/tie policy and a checkable reference before using it. Correlated model mistakes or repeated donor adaptations can all agree; majority voting does not replace external factual proof. The ledger still counts all attempts and retains failures after a fresh context or model change.

- **SUPER-103** MUST NOT: Treat self-consistency agreement, repeated source copies or an articulate fourth explanation as independent external truth or renewed authority; pivotal facts follow [verification](verification.md).
