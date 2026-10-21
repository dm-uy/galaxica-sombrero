---
id: prompting.verification
title: Verification
status: draft
skill-name: prompting-verify
skill-when: Author factual, consistency and contextual verification with bounded attempts and honest evidence.
---

# Verification

<!-- anchor: prompting.verification.dimensions -->

## Check truth, logic and supplied context separately

Verification defines which claim needs which evidence, how a contradiction changes the answer and when work stops. Confidence, consensus and a fluent explanation are not a source. A literal parser or checklist can prove shape or internal consistency; it cannot establish factual truth or live delivery.

- **VERIFY-101** MUST: Identify consequential claims and their actual check routes; distinguish critical facts, logical consistency and context-specific knowledge. Source-backed claims carry actual evidence and unavailable checks remain uncertain.

Critical facts include exact names, dates, links, API identifiers and consequential quantities. Prefer the actual authoritative record, primary documentation or appropriate archival evidence for its date/version. Recent/internal/user context must be supplied explicitly rather than recalled from training; retrieved material remains data, not authorization. Logic checks use observable derivations, contracts and contradiction checks without demanding private chain-of-thought. For factual/adversarial stakes the applicable [agent design](agent-prompt-design.md) supplies actual tool/evaluation boundaries.

<!-- anchor: prompting.verification.cove -->

## Question → independent check → revision

Chain-of-Verification starts with a candidate answer, generates specific verification questions for its pivotal claims, answers those questions in a context that avoids simply echoing the draft, and revises the original with evidence/status. “Independent” describes the actual separation achieved: a paraphrase to the same model is a cross-check, not independent external truth. Always consult external evidence for consequential facts even if the two answers agree. Self-refine similarly names concrete defects in a draft before revising; repeated confident reformulation is not additional evidence.

- **VERIFY-102** MUST: Revise claims in light of observed checks; retain contradictions, source/date/version qualifications and unresolved questions. Agreement alone never skips consequential external verification.

- **VERIFY-105** SHOULD: Treat a consequential first analysis or recommendation as a candidate and apply bounded critical reflection before relying on it in a decision, including conversational advice; use an authorized independent reader when available, preserve existing mandatory independence and report the actual check limits.

The recommended reflection applies the check-and-revise sequence above. A bounded critical reflection asks which assumptions lack evidence, which counterexample would defeat the recommendation, whether it addresses the observed cause, what it fails to prevent, and what costs or new failure modes it creates. Retain, narrow or reject the recommendation from those checks; persuasive rewriting and reviewer agreement do not establish effectiveness. Identify actual separation and limits; when independent reading is unavailable, label self-review honestly and keep unavailable pivotal evidence uncertain. The mandatory consequential-open independence procedure remains at [brainstorm](brainstorm.md#prompting.brainstorm.consequential).

Reuse a completed applicable reflection instead of adding another ritual. Keep the response proportionate: routine edits, settled choices and simple answers do not acquire mandatory fanout, a report or a new owner gate. Record only the conclusion, supporting checks, material revisions and remaining uncertainty in the existing answer or decision/evidence home. Repeat for new material evidence or a remaining pivotal unresolved concern within the actual allowance, not simply to make a draft sound more certain.

Placeholder CoVe form:

```text
$START_VERIFICATION
CLAIM: [Precise candidate claim, scope, stakes and required source]
QUESTIONS: [Separate checks for fact, logic and actual supplied context]
CHECKS: [Question; actual method; observed answer; evidence; separation/limits]
REVISION: [Corrected claim and supported evidence/status; unresolved matters]
DECISION: [Use within proven scope, PARTIAL, hold or stop]
$END_VERIFICATION
```

<!-- anchor: prompting.verification.fact-ladder -->

## Factual Anti-Loop profile

The counted unit is a factual checking attempt, not a software Debug entry or pytest failure. Preserve original attempts and all narrower spent budgets; a fresh context, tool, model or worker does not reset them. The following source profile is bounded; if actual project limits are tighter, those limits win.

1. Direct factual query: ask one precise question. An uncertain answer goes directly to external evidence; a confident answer goes to the cross-check.
2. Fresh-context paraphrase: ask the same fact differently without the first answer priming it. Compare values. The source's optional ±2% numeric-comparison profile is usable only when explicitly declared for that quantity/unit/purpose; it is never a general correctness margin. Names and dates require exact agreement. Either agreement or disagreement leads to external evidence.
3. External verification: inspect the appropriate actual source/version. Record what it supports or contradicts. A contradiction confirms that the model's specific claim is wrong within that scope; correct it from evidence, not tone. Unavailable sources do not become invented citations.
4. Contradictory-value reconciliation: identify X versus Y, source applicability/date/units and which actual evidence controls. A logical explanation can explain a correction; it cannot waive missing or contradictory truth evidence. Retain nonconvergence if no source resolves it.
5. STOP on bounded nonconvergence: after four unsuccessful factual attempts, do not make a fifth speculative attempt. Record high hallucination risk, the conflicting or unavailable sources and the missing evidence; do not use the unresolved fact in a critical decision.

- **VERIFY-103** MUST: Use the factual direct-query/paraphrase/external/reconciliation/STOP ladder without skipping external evidence on agreement or treating a fourth explanation as proof. Preserve counted-unit and tolerance profiles explicitly.

Report statuses: VERIFIED means actual evidence supports the precise claim; PARTIAL means only stated parts/scope are supported; UNVERIFIED means needed proof is absent; HALLUCINATION means an actually contradicted or fabricated model claim, not merely disagreement between two answers. A source itself can be unreliable or conflict with another source; state that rather than implying universal truth. A creative/philosophical task with no consequential factual dependence can omit the fact loop with its reason. If its result feeds a consequential factual decision, the applicable loop returns.

<!-- anchor: prompting.verification.correction-ladder -->

## Generic correction profile and distinct ledgers

Generic correction counts repair attempts for a defective answer/artifact. Attempts1–2 use the standard actual checklist; attempt3 consults external documentation/source; attempt4 holds competing hypotheses or escalates to the responsible human; attempt5+ stops and reports required intervention. This is separate from the factual ladder above. Neither changes the actual software QA⇄Debug maximum, test-failure counter, tool-response retry or effect/transaction ledger. Source “three-to-four” escalation suggestions are contextual illustrations, not permission to restart a stricter allowance.

- **VERIFY-104** MUST: Record each attempt's unit, method, actual result, evidence and decision; preserve failures/spend/unknown effects across reset and stop under the applicable exhausted budget. No infinite correction loop or reset-based budget extension is allowed.

Placeholder combined ledger:

```text
$START_CHECK_LEDGER
PROFILE: [Factual check or generic correction; actual unit/max/spent]
CLAIM_OR_DEFECT: [Precise scope and stakes]
ATTEMPTS: [Number; method; observed result; source identity/availability; decision]
STATUS: [VERIFIED / PARTIAL / UNVERIFIED / HALLUCINATION, with scope]
OTHER_BUDGETS: [Software Debug/test/tool retries; retained spend and limits]
NEXT: [Authorized evidence check, correction or terminal stop]
$END_CHECK_LEDGER
```

<!-- anchor: prompting.verification.examples -->

## Filled evidence and unresolved examples

These are fictional supplied-data illustrations, not live citations, scientific claims or actual model runs. Record R states exactly: “Room A capacity: 12 chairs.” It is the supplied source of truth for this narrow document-reading question; it is not proof of real room capacity.

| Attempt | Method | Illustrative result | Source / decision |
|---|---|---|---|
| 1 | Direct query: what capacity does R state? | 12 | Model candidate only; cross-check |
| 2 | Paraphrase: how many chairs are recorded for A? | 12 | Same value; external-to-answer record check still required |
| 3 | Inspect supplied record R | Literal “12 chairs” | VERIFIED for what R states; no live availability claim |

Revision: “The supplied record R states12 chairs; real capacity has not been independently checked.” No numeric tolerance is needed; the record's exact value controls. This example's source is the explicitly supplied fictional record, so no invented web link appears.

Unresolved illustration: records R1 and R2 each claim to be current and state12 versus14 chairs, with no dates/version authority. Direct query yields12; paraphrase yields14; record inspection finds the conflict; reconciliation cannot establish which record controls. Status PARTIAL for the two literal statements and UNVERIFIED for current capacity; high hallucination risk if a model asserts one as current. STOP after the bounded attempts, hold any capacity-dependent critical decision and request a dated controlling record. Do not average the values, invoke ±2% or describe a persuasive explanation as verification.

<!-- anchor: prompting.verification.diagnostic-trio -->

## Engineering Diagnostic Trio

The prompt-level form asks an actual reviewer to reconcile logs, code and data. Existing [QA](../roles/qa.md), [QA scans](../checks/qa-scans.md), [LDD](../code/ldd.md), [tests](../code/tests.md) and [exoskeleton](../code/exoskeleton.md) own execution duties, error propagation and real-delivery proof. This authoring procedure creates neither a second reviewer role nor new test infrastructure.

Logs: identify actual operation/validation/failure traces, source/sink/process and missing evidence. Code: compare inputs/returns/effects/guarantees against the contract, inspect exception paths, validation, resource closure, races and dead paths. Data: use actual/supplied test inputs, boundaries such as empty/zero/negative/large values where applicable, concurrency/error cases and observed output. Agreement supports a scoped judgment; mock/captured calls alone do not prove delivery to a real endpoint. New external identifiers require actual project API/schema/primary-document verification before success; library familiarity is not proof.

Complete placeholder review form:

```text
$START_DIAGNOSTIC_REVIEW
$START_ROLE
[Actual reviewer duty and read-only/effect boundary]
$END_ROLE
$START_INPUTS
[Task/spec, current source/contracts, real logs/process identity and data/test identities]
$END_INPUTS
$START_CHECKS
[Contract compliance; logs of actual operations; code errors/resources/races; boundary/error data]
$END_CHECKS
$START_OUTPUT
[Each finding: severity, precise verified location, defect, reproducible input, evidence, repair recommendation]
[If no finding: scoped checked population and unverified checks, without fabricated readiness]
$END_OUTPUT
$END_DIAGNOSTIC_REVIEW
```

Filled fictional finding: severity Medium; location is the supplied example function `draft_label`'s empty-input branch (no invented real file line); contract requires UNKNOWN on empty text, code instead returns OPEN, supplied trace confirms that branch and supplied empty input yields OPEN. Reproduction: call with empty text. Recommendation: return UNKNOWN in that branch and inspect the actual correction/test evidence. Scope limitation: this is supplied example evidence, not an executed project test or production result.

<!-- anchor: prompting.verification.specificity -->

## Specificity and anti-banality form

Concretize the audience, domain and period; constrain output shape/length where meaningful; replace generic formulations with useful distinctions; provide one to three complete deep examples. Few-shot improves requested style/form and can still be factually wrong. A ban on banal phrases must not suppress a truthful obvious answer or an explicit uncertainty.

```text
$START_SPECIFICITY
AUDIENCE: Workshop coordinator reading a two-line draft.
CONTEXT: Only supplied room notices; no live building knowledge.
FORMAT: One status plus one concrete evidence sentence.
AVOID: Generic assurances such as everything is ready; fabricated completeness.
EXAMPLE_INPUT: Room A is closed today.
EXAMPLE_OUTPUT: CLOSED — the supplied notice explicitly says Room A is closed.
FACT_BOUNDARY: The notice is the source for its statement, not live closure confirmation.
$END_SPECIFICITY
```

Before handing off the prompt check: named critical facts/source route; separate logic/context checks; actual revision rule; bounded counted attempts; evidence/status output; unavailable-source behavior; no confidence-as-proof or new permission. Static authoring checks do not certify truth, reliability or injection resistance of a target agent.
