---
id: process.specification
title: Specification
status: draft
---

# Specification

A specification connects an actual request and measured input to a bounded, verifiable result. The author establishes intent; Architect independently validates it before planning/delegating implementation. A form, a status or a source template cannot manufacture authorization or replace required evidence.

<!-- anchor: process.specification.route -->

## Authoring, classification and record identity

- **SP-101** MUST: Read the actual brief, instructions and current records, and use [reconnaissance](reconnaissance.md) before a new specification. Compare relevant task/backlog/tracker requirements with project records; surface conflicts or omissions instead of deleting one because another is the preferred authoring home. Comparing an external tracker grants no permission to write to it.
- **SP-102** MUST: Classify by existing implementation/interfaces/artifacts, not missing durable documents. Use [greenfield](../protocols/spec-greenfield.md) for a genuine first implementation, [brownfield](../protocols/spec-brownfield.md) for preserving an existing surface, and state preservation boundaries for mixed work. Carry Input RECON and evidence limits into either profile.
- **SP-103** MUST: Keep the specification at a stable project-selected path; state changes in actual project metadata rather than draft prefixes or approval renames. Distinguish project spec states such as draft/approved/rework/rejected/abandoned from FORMAT's neutral stub/draft/stable card status. Use the project's declared header/input/approval convention; do not add project keys to a neutral card.
- **SP-104** MUST: Record the exact scope/decision reference and near-top Done when / Stop and ask when conditions. Follow [gates](gates.md) for an own decision or inherited approved batch within its exact scope. Approval is actual matching authority, not the string approved; integration remains a separate decision. Where current convention records integration with the batch, do not force merged/gate2 onto specs or destructively migrate retained legacy metadata.
- **SP-105** MUST: Keep spec authoring distinct from technical Architect ownership. Drafting a spec does not activate Architect or authorize a development plan/Code. Architect reads the applicable full profile and document contract, checks readiness and only then plans under the granted scope using existing [roles](../roles/architect.md) and [phases](../flow/phases.md).

<!-- anchor: process.specification.consistency -->

## Checks before implementation delegation

- **SP-201** MUST: For both GREENFIELD and BROWNFIELD, sweep numeric and enumeration consistency across the complete actual input before delegating implementation: counts, thresholds, exact quantifiers, ranges, numbered lists, declared memberships and AC/BR references. Compare narrative with actual enumerated population and measured evidence; distinguish a dated measurement from a binding future threshold. Record each contradiction and its disposition, not merely a token scan.
- **SP-202** MUST: Verify every explicitly named required external identifier, including inherited spec identifiers: images, packages (including applicable package ecosystems), API names/URLs and required versions. Use actual installed/documented project interfaces or primary source evidence through available capabilities. Record identifier, method/command, source/time/result and access limits. A partial HTTP response establishes only that response, not full operational compatibility. Do not install a dependency merely to look up its identity.
- **SP-203** MUST: Validate the complete applicable profile, including purpose/scope/BR/AC/delivery, graph authority, scope lists, boundaries and full document readiness. Brownfield validation explicitly checks BR-1 compatibility/authorized exceptions, MAY EDIT / DO NOT TOUCH and measurable ACs. Inspect coupled test/doc/plan/checker consumers; successful format/lint output alone does not prove completeness or architecture equality.
- **SP-204** MUST: Treat literal verification promises as obligations with the applicable [development plan](../protocols/dev-plan.md) commitments: token → actual symbol/operation → bounded expected result. Keep AC and volunteered promises visible without inventing a new commitment schema or checker. Source-section headings are a prose contract unless an actual documented consumer proves a particular parser rule.

<!-- anchor: process.specification.deficiencies -->

## Deficiencies and bounded reconstruction

- **SP-301** MUST: For missing mandatory sections, contradiction or deficient constraints, record a SPEC_DEFICIENCY block naming the concrete omission/conflict, source/evidence, affected requirement, chosen interpretation and rationale. Reconstruct best effort only from measured APIs, invariants, graph or other actual evidence inside the existing approval/authority. Do not edit the approved spec in the implementation loop or invent an approval/protection boundary.
- **SP-302** MUST: Propagate every complete deficiency/interpretation block verbatim to Code for both classifications, together with the actual scope. A greenfield classification cannot suppress a block. Validate transport at the producer and receiving prompt; a deficiency list left in an upstream report alone is insufficient.
- **SP-303** MUST: Code records a Deviations section explicitly: `(none)` if no reinterpretation/narrowing/replacement occurred, otherwise all such changes to BR/AC, including beneficial changes and the received evidence-grounded interpretations. A departure's record is not authorization to make an out-of-scope change.
- **SP-304** MUST: Where the applicable source/adapter profile requires `# SPEC_DEFICIENCY_RESOLVED: <id> <choice> <rationale>` and target code-surface permissions allow it, retain that source resolution annotation. It is conditional encoding, not a universal new comment mandate; absence of permission for that encoding does not waive existing role/code annotations or verbatim transport/Deviations.
- **SP-305** MUST: When correctness requires a human decision, including equally valid conflicting quantitative interpretations or ambiguous protection authority, report SPEC_BLOCKED through existing role returns, stop dependent implementation and prepare the concrete amendment/question for the owner. Independent authorized work may continue. When required evidence is unavailable, report BLOCKED under the existing vocabulary; it is not a fabricated human intent fork, PASS or a new status/schema.
- **SP-306** MUST: Predeclare genuine deferred checks with criterion mapping, exact command, prerequisite and reason. TEST_DEFERRED is disclosure and fulfills no criterion or coverage until actual execution supplies proof. Missing required evidence cannot be hidden by converting it into discretionary deferred work.

[Role returns](../protocols/role-returns.md), [delegation](../flow/delegation.md), [phases](../flow/phases.md) and gates retain their current ownership and status semantics. The source producer promises deficiency transport for both classifications; some donor consumers transported it only for brownfield. Universal transport above preserves the duty rather than copying that consumer defect. Donor repairs and runtime implementation are separate work.

For BROWNFIELD, the existing source-to-final and converse review is recorded in the
specification receipt's `Task/tracker comparison`, with source pointers in `Input RECON`.
For each substantive obligation in the declared, relevant input population, identify its
source location and wording or a faithful bounded summary, then its exact BR, AC or boundary
location in the specification. Preserve conditions, quantifiers, prohibitions and exceptions;
a source can contain several obligations, and citing that source once does not account for
all of them. A combined BR may cover several obligations only while retaining their meaning.

If an obligation is not carried into the specification, record its disposition and the
actual basis or decision reference: superseded, deferred, excluded within authorized scope,
or unresolved. A disposition does not grant authority to drop an obligation. Conversely,
identify the source or existing derivation/assumption basis for substantive BRs and boundaries;
agent-authored additions do not become approved intent through this correspondence.

Use the receipt's existing author/validator, input limits and readiness outcome to state who
checked this correspondence, its actual extent, unresolved mappings and unavailable inputs.
Apply the existing deficiency and human-decision routes to unresolved items; do not claim
complete correspondence merely because every source was opened or every BR has a citation.
This clarifies the existing review result, not a new register, requirement-ID scheme, role,
mandatory blind-extraction pass, owner gate or implementation-stage QA obligation. Reuse existing
source references and project homes rather than copying the requirements into parallel documents.

<!-- anchor: process.specification.form -->

## Full authoring and validation receipt form

This receipt accompanies the full selected specification; it never replaces its content. Project state/header encoding follows the project convention. Each supplied bracketed field must contain actual evidence or an explicit limit.

```markdown
$START_SPECIFICATION_RECEIPT
PURPOSE: Establish readiness of the exact bounded specification for its granted next action.
SCOPE: [Exact spec identity and validation population]
KEYWORDS: specification, consistency, deficiency, authority
$START_DOCUMENT_PLAN
$DOCUMENT_PLAN
GOAL Validate the specification input and transport => GOAL_READY
DECISION Dispose recorded deficiencies within authority => DECISION_DEFICIENCIES
$END_DOCUMENT_PLAN
$START_SECTION_VALIDATION
$START_ARTIFACT_GOAL_READY
TYPE: GOAL
KEYWORDS: classification, numeric checks, identifiers, readiness
$START_CONTRACT
$CONTRACT
PURPOSE: [Correct bounded delegation]
DESCRIPTION: [Actual spec identity, classification and next action]
RATIONALE: [Why validation is necessary for this input]
ACCEPTANCE_CRITERIA: [All applicable form/authority/evidence/transport checks closed or explicit refusal]
$END_CONTRACT
$START_BODY
Spec home/status/identity: [Stable path, actual metadata, byte/revision identity]
Author / validator: [Actual responsibilities and evidence]
Input RECON: [Measured source/consumer population and limits]
Approval: [Exact authority/scope/reference; separate integration state]
Task/tracker comparison: [Compared inputs, differences or none; write authorization is separate]
[BROWNFIELD: each relevant source obligation/location → exact BR/AC/boundary, or disposition
with authority/basis; reverse source/derivation links; reviewer, extent and unresolved/access limits
use the existing Author / validator, Input RECON and Readiness outcome fields]
Classification/profile: [Actual source basis and architecture authority]
Done when / Stop and ask when: [Actual finish line and task-specific edges]
Complete-profile/document check: [Contracts/markers/links/BR/AC/scope/graph/delivery and limits]
Numeric/enumeration sweep: [Each count/threshold/list/quantifier comparison and disposition]
External identifiers: [Every required identifier incl. inherited; method/command, source/time/result]
Verification promises: [Actual commitment references and token→operation→result mapping]
Deferred proof: [Exact command/prerequisite/reason/criterion; unfulfilled status or none]
Readiness outcome: [Evidence-grounded ready input, SPEC_BLOCKED human decision, or BLOCKED proof]
$END_BODY
$START_LINKS
IMPLEMENTS: (none)
IMPACTS: DECISION_DEFICIENCIES
REQUIRES: DECISION_DEFICIENCIES
$END_LINKS
$END_ARTIFACT_GOAL_READY
$END_SECTION_VALIDATION
$START_SECTION_DISPOSITIONS
$START_ARTIFACT_DECISION_DEFICIENCIES
TYPE: DECISION
KEYWORDS: deficiency, interpretation, delegation, deviations
$START_CONTRACT
$CONTRACT
PURPOSE: [Retain every omission/conflict and actual authorized interpretation]
DESCRIPTION: [Recorded disposition or explicit none]
RATIONALE: [Evidence and authority for the disposition]
ACCEPTANCE_CRITERIA: [Exact full blocks delivered to Code, Code Deviations and refusal when needed]
$END_CONTRACT
$START_BODY
SPEC_DEFICIENCY_[ID]: [Issue, evidence, affected requirement, choice and rationale]
[Repeat full blocks for the entire population or explicit none]
Human-dependent choices: [Exact competing options, concrete amendment/question; or none]
Transport: [Actual receiving prompt/receipt identity, identical blocks, complete scope]
Source-resolution annotation: [Applicable profile/encoding/permission or justified N/A]
Code Deviations: [Exact explicit-none/full list evidence; pending until Code actually reports]
Remaining work/status: [Dependent stop or permitted continuation, no new return enum]
$END_BODY
$START_LINKS
IMPLEMENTS: GOAL_READY
IMPACTS: GOAL_READY
REQUIRES: (none)
$END_LINKS
$END_ARTIFACT_DECISION_DEFICIENCIES
$END_SECTION_DISPOSITIONS
$END_SPECIFICATION_RECEIPT
```

Fictional brownfield correspondence in that same receipt, not a separate ledger:

| Source obligation | Specification location or disposition | Basis / check |
|---|---|---|
| Brief paragraph 2: export all records, including archived records | BR-2; AC-EXPORT-1 explicitly includes archived records | Validator compared the full obligation and its qualifier with both locations |
| Brief paragraph 3: retain the existing file format | BR-1; AC-REGRESSION-1 names the preserved format | Compatibility is not inferred from an unrelated green suite |
| Earlier decision D1: CSV output | Superseded by D2 selecting JSON | Actual authorized decision D2; no silent deletion or agent-selected replacement |

If BR-2 instead says only “export active records”, the archived-record obligation is still
unaccounted for even when the brief is marked read and every BR has a source citation. Record
the mismatch through the existing deficiency/readiness procedure before claiming the spec ready.
An inaccessible appendix remains an explicit coverage limit, not an assumed empty obligation set.

<!-- anchor: process.specification.example -->

## Complete worked example: validation with a recoverable omission

This fictional receipt uses a constraint-led first specification for local title search. The evidence and decisions are illustrative and do not certify a real run. Negative variants after it show refusal conditions rather than a new automated prose oracle.

```markdown
$START_SEARCH_RECEIPT
PURPOSE: Validate the local title-search MVP before bounded implementation delegation.
SCOPE: specs/title-search.md and its actual illustrative input/scope/AC population.
KEYWORDS: search, greenfield, validation, deficiency transport
$START_DOCUMENT_PLAN
$DOCUMENT_PLAN
GOAL Validate a bounded first specification => GOAL_SEARCH_READY
DECISION Retain a measured document metadata interpretation => DECISION_SEARCH_METADATA
$END_DOCUMENT_PLAN
$START_SECTION_VALIDATION
$START_ARTIFACT_GOAL_SEARCH_READY
TYPE: GOAL
KEYWORDS: classification, counts, identifier sweep
$START_CONTRACT
$CONTRACT
PURPOSE: Give Code a consistent input with its original scope and interpretation intact.
DESCRIPTION: Validate a first local title-search spec with two declared behaviors and no external package.
RATIONALE: Even a greenfield input can contain deficiencies that downstream implementation must know.
ACCEPTANCE_CRITERIA: The full profile is checked, both behavior declarations match their summary,
required identifiers are accounted, and the exact metadata deficiency is retained in Code's input.
$END_CONTRACT
$START_BODY
Spec home/status/identity: specs/title-search.md stays at its stable path; project metadata says
approved with a matching illustrative owner reference. Input identity is the recorded snapshot in
notes/title-search-input.md; no present real hash or operational PASS is invented by this example.
Author / validator: spec author drafted intent; a separate Architect read the full input/profile.
Input RECON: the illustrative repository has a brief/current records and no implementation/tests.
Brief fixes local search, two behaviors and standard-library-only execution; external facts are not
load-bearing. Unknown wider source coverage is not claimed as complete.
Approval: owner approved that local MVP and constraints, not publication or the unseen result.
Task/tracker comparison: local task and brief agree; there is no external tracker in this context.
Classification/profile: GREENFIELD, constraint-led. Outcomes/local CLI/input-text seam fixed;
Architect owns technical component graph/layout. No nonexistent regression guard is imposed.
Done when: search returns matching titles for declared inputs, meaningful positive/error tests and
real local entrypoint probe pass within allowed homes. Stop and ask: network/dependency expansion,
conflicting owner intent or unknown protection authority. Missing required proof is BLOCKED.
Complete-profile/document check: Context, observable build/default/error behavior, justified stack,
architecture authority, MVP BR-1, boundaries, exclusions/deferred return conditions, behavior/test/
scope/delivery ACs, actual local probe route and risks are present. Document contract/markers/links
are complete except artifact metadata described in the deficiency below. Scope includes search/,
tests/, README.md, scripts/probe_search.py and plans/title-search.md; current brief/spec are protected.
Numeric/enumeration sweep: summary declares exactly two behaviors, search and help; enumerated
build/BR entries contain those two behaviors. Empty query rejects with exit 2; valid query matches
case-insensitively. No incompatible threshold/count or unnamed third behavior exists. AC references
resolve to the declared behavior/test/scope/probe checks; no stale suite count is required.
External identifiers: no image, package or API URL is required, including in inherited input.
The selected local interpreter is inspected by the run and its actual version recorded before Code;
no package installation serves as identity lookup. A later explicitly required package would need
primary verification and actual compatibility limits rather than this N/A statement.
Verification promises: the planned probe promise maps to scripts/probe_search.py → actual module
CLI invocation/output/exit → declared search/error observations. The actual plan commitment must
retain this mapping; promise presence alone is not successful execution.
Deferred proof: none. The eventual behavior/probe results are NOT RUN at this authoring receipt.
Readiness outcome: ready for planning/delegation within existing approval after the full deficiency
block below is carried verbatim; this is input readiness, not implementation or acceptance PASS.
$END_BODY
$START_LINKS
IMPLEMENTS: (none)
IMPACTS: DECISION_SEARCH_METADATA
REQUIRES: DECISION_SEARCH_METADATA
$END_LINKS
$END_ARTIFACT_GOAL_SEARCH_READY
$END_SECTION_VALIDATION
$START_SECTION_DISPOSITIONS
$START_ARTIFACT_DECISION_SEARCH_METADATA
TYPE: DECISION
KEYWORDS: missing artifact metadata, evidence-grounded interpretation, greenfield transport
$START_CONTRACT
$CONTRACT
PURPOSE: Preserve the metadata omission and its bounded resolution across delegation.
DESCRIPTION: The approved goal artifact has a goal outline/contract but omits its TYPE and KEYWORDS.
RATIONALE: The declared goal and document-level keywords determine the missing metadata without
changing requirements, authority or approved spec bytes.
ACCEPTANCE_CRITERIA: Full exact block is in the Code prompt; Code Deviations retains its interpretation.
$END_CONTRACT
$START_BODY
SPEC_DEFICIENCY_SEARCH_METADATA: The approved goal artifact omits TYPE and KEYWORDS. Its outline
and contract identify a GOAL; interpret TYPE: GOAL and KEYWORDS: local title search, MVP, validation.
Do not edit the approved spec. This interpretation changes no BR, AC, scope or authorization.
Human-dependent choices: none; the recorded artifact meaning supports this one reconstruction.
Transport: the same full block above is copied into the illustrative Code prompt together with the
entire approved scope; greenfield classification does not omit it. The actual run must record both
producer/receiving identities and compare bytes before claiming transport succeeded.
Source-resolution annotation: N/A in this document-only metadata interpretation; no new source code
comment mandate is imposed. Existing authored-code annotations remain required if code is written.
Code Deviations: the illustrative completion would state the metadata interpretation above and
"Other reinterpretations/narrowings/replacements: (none)" only after Code checks its actual work.
At this pre-Code receipt that report is pending, not fabricated evidence of completion.
Remaining work: technical plan, bounded Code, independent checks and separate result acceptance.
$END_BODY
$START_LINKS
IMPLEMENTS: GOAL_SEARCH_READY
IMPACTS: GOAL_SEARCH_READY
REQUIRES: (none)
$END_LINKS
$END_ARTIFACT_DECISION_SEARCH_METADATA
$END_SECTION_DISPOSITIONS
$END_SEARCH_RECEIPT
```

If the same input says “exactly two behaviors” but lists search/help/export, the validator must compare the actual enumeration and record the conflict. An explicit approved exclusion of export can support a documented reconstruction; equally valid two-versus-three intent requires SPEC_BLOCKED and a concrete amendment. An explicitly required package with unavailable primary lookup instead yields BLOCKED for missing evidence. An omitted greenfield transport block violates SP-302 even if Code independently guesses the same choice. A real operator-gated probe may be TEST_DEFERRED only with its exact command, prerequisite, reason and criterion; the delivery criterion remains unfulfilled.

<!-- anchor: process.specification.limits -->

## Coverage and retained ownership

- **SP-401** MUST: Keep source qualification and remaining duties explicit. Full bytes/hash freshness establish observed identity, not clean revision, whole-source applicability or runtime adoption. Missing-source coverage cannot be claimed absent or complete. Review source-to-final and converse meaning, actual examples and exact result evidence before closure.
- **SP-402** MUST: Preserve general decision lifecycle and full generic graph detail at their current owning bodies; completing the authoring/profiles/validation subjects alone does not discharge DEC01 history/status/register obligations or expanded graph grammar. Existing [decisions](decisions.md), [graph](../protocols/graph.md), [learning](learning.md) and [lints](../checks/lints.md) keep their owning obligations and limits.

The lesson2/lesson3/shared development roles provide consistency, deficiency and refusal duties; product conventions provide stable spec/input/approval encoding. The PM harness, native PM adaptation and standalone development distribution compose those duties under actual project authority. Detailed prompting/policies, learning/evaluation, donor engine repair, runtime adoption and publication remain outside this authoring slice.
