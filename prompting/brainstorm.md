---
id: prompting.brainstorm
title: Brainstorm
status: draft
skill-name: brainstorm
skill-when: Generate and compare alternatives for a genuinely open product or design choice.
---

# Brainstorm

<!-- anchor: prompting.brainstorm.scope -->

## Choose the generation profile

Brainstorming expands the space before preference narrows it. It is useful when different feasible approaches could satisfy the goal; it adds little to a settled decision or obvious small edit. Existing decisions and actual constraints remain authoritative. Generation, evaluation, selection and implementation are separate duties even when a single authorized participant performs them sequentially.

- **BRAIN-101** MUST: State whether the task is a broad five-proposal exploration, a generator-only five-to-ten variant exploration, or a bounded two-to-three alternative choice; do not pad a settled choice or silently give a generator selection authority.
- **BRAIN-102** MUST: Present each proposal's essence and two possible side effects before comparison or preference. In generator-only mode do not score, select or implement.

Broad five-proposal work includes conventional, unconventional and one deliberately wild approach. Generator-only five-to-ten work expands further: conventional, counterintuitive, wild and cross-domain/inverted variants are useful categories, not artificial quotas for duplicate ideas. Its artifact is a hypothesis list for an authorized selector. Bounded decisions use the actual plausible two or three alternatives, without five-item padding. Specifying a profile does not authorize spawning agents or implementing a selected idea.

<!-- anchor: prompting.brainstorm.procedure -->

## CONSULT → PROPOSE → HOLD → EVALUATE → COLLAPSE

CONSULT relevant accepted decisions and experience as short pointers/priors. Record why each prior colors an alternative, where it applies and what changed evidence could reopen a rejection. A prior is context, not a veto; a previous rejection without new evidence should not be disguised as a novel candidate. “No priors matched” is an honest outcome with no penalty. Do not copy an entire experience archive into the answer. Permanent retirement or changes to a decision use its actual owning process.

PROPOSE under the declared profile. Concretize the audience and constraints; invert an assumption, borrow a cross-domain pattern or give a complete contrasting example to avoid generic answers. Research may widen the space if actually available and authorized. Search ranking or popularity does not choose the solution.

HOLD each candidate without a favorite: essence, two side effects, dependency assumptions and applicable prior. Clean context removes irrelevant implementation history, not governing instructions, constraints or grants. A separately authorized generator/selector can receive a compact hypothesis handoff; a single-session phased prompt is also valid.

EVALUATE only in a selecting profile. Name criteria before assigning feasibility, impact and risk scores from 1 to 10. Explain each score and its evidence/uncertainty; optional cost and technical-debt axes reflect the actual decision. These are reasoned judgments, not measured probabilities. Declare weights, score direction and tie-breaker; verify pivotal factual claims using [verification](verification.md), not a fluent guess or search result ranking.

COLLAPSE under the real decision authority: a human-owned scope/constraint fork waits for the matching decision; a routine choice delegated within an approved scope proceeds on its criteria. Reuse existing approval and do not manufacture a second gate. Record selected alternative, allowed tradeoffs, why others lost/were deferred, next action and reopening evidence using the actual [decision record](../process/decisions.md). Selection does not authorize implementation outside the grant.

- **BRAIN-103** MUST: Keep priors, score reasons, weights, tie-breaker, decision authority and rejected/reopening reasons visible in the comparison artifact; unsupported empirical claims remain uncertain.

<!-- anchor: prompting.brainstorm.form -->

## Complete reusable form

Placeholder template; instantiate candidate records for the declared population.

```text
$START_BRAINSTORM
$START_SCOPE
[Goal, audience, hard constraints, generation profile and selection authority]
$END_SCOPE
$START_PRIORS
[Matched decision pointers and applicability; or no priors matched]
$END_PRIORS
$START_PROPOSALS
[For every candidate: ID; essence; side effect A; side effect B; dependencies; prior influence]
$END_PROPOSALS
$START_COMPARISON
[Selecting profile only: criteria, direction, weights, each score/reason/source, tie-breaker]
[Generator-only profile: omit comparison and state that omission explicitly]
$END_COMPARISON
$START_DECISION
[Actual selected/held result and authority; rejected/deferred reasons; reopening evidence; next action]
[Generator-only profile: hand off candidates without a favorite or implementation]
$END_DECISION
$END_BRAINSTORM
```

<!-- anchor: prompting.brainstorm.example -->

## Filled broad exploration and authorized selection

Illustrative scenario: a volunteer reading club needs attendees to find a session room. The organizer delegates reversible communication-format selection, with no new software/service or attendee tracking. No priors matched. All effects and scores below are design judgments, not observed outcomes.

| ID / category | Essence | Side effect A | Side effect B |
|---|---|---|---|
| A / conventional | Put the room on the existing invitation | Late room changes require correction | Long invitations can bury the location |
| B / conventional | Add a single entrance notice | People may miss the entrance board | Someone must update it when rooms change |
| C / unconventional | Print a small route diagram on invitations | A diagram needs a readable legend | Layout changes make it stale |
| D / counterintuitive | Ask attendees to meet at one named desk first | Queueing can delay the start | A volunteer must remain at the desk |
| E / wild | Use a volunteer walking guide from the entrance | It depends on that volunteer being present | Different arrivals need repeated walks |

Weights: feasibility 0.4, impact 0.4, low-risk contribution 0.2; utility is 0.4F + 0.4I + 0.2(11−R). Higher feasibility/impact and lower risk are preferred. The tie-breaker is lower volunteer dependency, consistent with the grant. Scores are illustrative judgments; arithmetic is simple and explicitly shown, not a model performance claim.

| ID | F / reason | I / reason | R / reason | Utility |
|---|---|---|---|---|
| A | 9: invitation already exists | 6: location can be overlooked | 3: correction dependency | 7.6 |
| B | 8: a board already exists | 8: arrival location is relevant | 3: single update point | 8.0 |
| C | 6: diagram authoring needed | 7: route can clarify | 5: layout staleness | 6.4 |
| D | 7: known desk | 7: one meeting point | 6: queue/staff dependency | 6.6 |
| E | 4: repeated volunteer work | 8: direct guidance | 7: availability dependency | 5.6 |

Selected B within the organizer's delegated scope. A is a useful later supplement, not selected because the arrival notice more directly addresses the scenario. C loses on authoring/staleness; D on staffing/queueing; E on repeated labor. Reopen if the entrance board is unavailable, inaccessible or attendees cannot reliably pass it. Next action is to draft the notice for review; this comparison does not claim that anyone installed it. A human-owned change to registration or attendee tracking would remain held for its separate owner decision.

<!-- anchor: prompting.brainstorm.generator -->

## Filled generator-only handoff

For the same fictional goal, a generator delivers six unranked complete variants:

| Variant | Essence | Side effect A | Side effect B |
|---|---|---|---|
| Invitation label | Put the room in the existing message | Corrections need redistribution | Detail may be buried |
| Entrance notice | State the room at arrival | Board can be missed | Someone maintains it |
| Route diagram | Show a spatial path | Legend needs explanation | Layout changes make it stale |
| Meeting desk | Start everyone at one desk | Queueing may delay arrival | Staff must be present |
| Walking guide | Escort attendees from the entrance | Volunteer availability dependency | Repeated walks for late arrivals |
| Color route cards | Match a route color to a room card | Color accessibility needs care | Cards need maintenance |

The artifact hands these six alternatives to the authorized selector. There are no scores, favorite, implementation steps or claim that constraints were waived to generate wild ideas.

For a bounded real fork, use the [two-to-three comparison](superposition-collapse.md) instead. Complete the profile, full candidate population, effects, priors, selecting authority and durable outcome before handoff. Self-consistency voting is a different verification technique, not a brainstorm selection or external truth check.
