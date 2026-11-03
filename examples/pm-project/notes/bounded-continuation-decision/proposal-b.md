Candidate B — Authoritative continuation envelope; Codex delivery first, shared-neutral delivery held

This is one unranked integrated candidate for the bounded two-to-three-alternative population. It addresses Q-REPRESENTATION and Q-ROLLOUT together. It contains no scores, selection or implementation authority.

**Essence and mechanism**

Introduce a separately versioned Codex continuation envelope. Ordinary fresh runs retain their existing schema2 format and default cap4. A continued lineage has one authoritative envelope containing historical predecessor references, aggregate resource accounting, bounded grants, dispatch reservations and its current successor’s operational state.

The envelope’s embedded successor is a new explicitly typed continuation representation, **not a schema2 object with extra fields**, and never masquerades as the original terminal run. Its phase/input/candidate/evidence predicates follow the existing native workflow and current role-return wire. Current-state validation applies to the successor; historical validation applies separately to the frozen predecessor.

Keep all authority-bearing continuation information in one checkpointed envelope. Do not split grant consumption, aggregate accounting and the active successor between independently authoritative files. Human-readable exports or receipts may exist, but cannot authorize dispatch.

The envelope belongs at one deterministic, contained lineage location under the target’s existing `.methodology` footprint. Supported sibling continuation requests address that same envelope and serialize through the single parent writer. Subsequent terminal successors are retained in the envelope’s chronological history before another successor becomes active. The original external predecessor and imported parent record remain unchanged.

**Inputs, legacy reconciliation and outputs**

Admit an explicit bounded historical population:

- Original Codex3.2/schema2 with its identified parent accounting bridge, including the motivating native0/root4 case.
- Current Codex4.0/schema2 terminals with sufficiently complete causal accounting.
- Later successors produced by this envelope contract.

Historical validation checks the admitted format/version, terminal status, target/run/causal identity, complete readable chronology, retained locks and bound source digests. It does not run ordinary current `_bindings` against old3.2 inputs or rewrite their version/hash locks.

The parent authenticates the real approval and historical provenance. The helper checks that the supplied reconciliation structurally binds the actual predecessor, actual parent accounting bytes, causal scope, counters and grant reference. This is a named bridge for the admitted parent-accounting shape, not arbitrary ingestion of user-supplied sidecars.

For Jeni’s observed population, import aggregate spend4 and existing ceiling4, record native0/0 as that predecessor’s local allowance interpretation, and identify their overlapping accounting. **Do not sum4+0 as independent budgets or initialize a new default4.** An unexplained discrepancy, ambiguous overlap, missing causal link or incomplete accounting refuses admission. Unknown historical costs remain unknown.

Output is a current-bound successor identity plus a complete accounting reconciliation and permitted next action. Original terminal bytes, historical locks and parent ledger remain immutable on success **and refusal**. Refusals use stderr and, once available, the owned envelope’s diagnostic history; they never append diagnostics to the frozen predecessor.

**Supported terminal and reentry population**

A terminal status alone selects no next phase. The following matrix also requires authentic continuation authority, reconciled inputs/scope, current candidate facts and actual phase evidence.

| Predecessor population | Supported successor entry |
|---|---|
| SPEC_BLOCKED or VISUAL_GATE_FAIL before implementation | Architect after the relevant approved amendment; no invented Code/QA success |
| BLOCKED or ERROR in Bootstrap/Architect | The first unmet prerequisite/phase after its cause is resolved |
| BLOCKED, ERROR or ESCALATED in Code/Debug/QA/Review | Existing interrupted entry, a newly counted repair, or QA, according to retained completion/candidate/accounting evidence |
| ESCALATED_FINALIZE | Current Finalize if only final checks remain; candidate-changing repair requires counted work followed by renewed independent QA and affected Review |
| SUCCESS | Explicitly approved amendment within the linked causal scope; integration-only work remains the separate result-decision route |
| Unsupported status/phase combination, RUNNING predecessor, unknown effects or irreconcilable evidence | Refuse continuation; investigate or obtain the missing decision |

Three resource cases remain distinct:

1. **No source repair:** Eligible QA, Review or Finalize needs no positive additional Debug grant. Applicable current predicates still govern.
2. **Remaining allowance:** A new causal repair consumes existing reconciled remaining allowance; no extension is manufactured.
3. **Additional allowance:** After exhaustion, a new repair requires a separately recorded bounded owner extension satisfying GATE-1209.

A new Code phase repairing the same cause is charged before dispatch just as a new Debug entry is. After the last authorized repair, QA remains eligible. Candidate-changing work invalidates prior QA and affected Review; the successor does not inherit a green flag as current acceptance. Unaffected evidence is reusable only after the existing freshness/applicability checks.

The exact representation of the matrix and error messages is an Architect detail; the admitted population, refusal cases and resource distinctions belong in the specification.

**Counters, grants and dispatch sequence**

The envelope retains aggregate spend, original allowance and additional grants separately. Each grant has its authentic authority reference, canonical identity, causal scope, entry allowance, cost terms and consumption history. Range and cost rules remain GATE-1209’s existing rules, without a new ceiling or default increase.

Preserve response-correction, extraction, transport and test-session histories independently. Each episode retains its phase attempt/session identity, cap, spent turns and available costs. An unfinished episode follows the same interrupted attempt across successor naming; an exhausted correction episode cannot become fresh merely through continuation. A genuinely new authorized phase attempt may open its own episode, with its relationship to the closed attempt recorded. Existing unsupported extraction/transport retry mechanisms do not become supported through the envelope.

Before releasing a worker, the parent:

1. Validates actual helper/version capabilities and current bindings, candidate, approval, scope and relevant episode state.
2. Resolves any existing reservation or unknown completion.
3. Checkpoints one reservation binding successor, phase, causal entry, candidate/input identity and grant consumption. A new repair increments cumulative spend in that same checkpoint.
4. Reads back the committed reservation, then releases only its named dispatch.
5. Checkpoints actual worker/session identity, returned evidence, observed effects, costs and accepted/refused outcome before another dispatch.

A competing successor or repeated grant claim consults the same authoritative envelope and refuses while its lineage has an active reservation/successor or exhausted grant. Grant uniqueness and sibling-spend protection apply **only within the declared authoritative target/lineage/storage domain and supported API under one writer**. Files copied elsewhere, older executables, manual edits and independent hosts are outside this enforcement claim. A parent cannot introduce a different lineage identity to conceal the same admitted parent causal chain; ambiguous identity reconciliation blocks.

**Interruption and recovery**

Before reservation commit, no dispatch is permitted. After commit, the recorded charge survives interruption.

A reservation with no recorded release is not automatically proof that release never occurred. On recovery, the parent investigates the actual worker/session and effect sink. Known unlaunched work may use the same reservation; an already entered interrupted worker retains its existing charge. Known completed work follows current result-validation/recovery rules. Unknown completion blocks replay. Completed dispatch identities cannot be replayed as fresh repair entries.

Historical interrupted entry reuse requires evidence identifying that same already charged entry; a bare native counter or narrative assertion is insufficient. Otherwise the mechanism cannot claim a free recovered entry.

The bounded durability promise is a complete checkpoint plus conservative investigation after parent/process interruption. Current temp-file replacement does not establish power-loss durability, atomic worker release or exactly-once transport. Storage rollback or corrupt/missing authority records supplies no permission to advance.

**API, version and compatibility boundary**

Add explicit historical-inspection, successor-creation and reservation/recovery operations through the actual Codex helper/caller surface. Names and function decomposition are local design details. Ordinary schema2 `init/show/record` stays recognizable; it cannot mutate a frozen terminal predecessor or bypass an enrolled lineage’s authority.

Proposed version semantics:

- Additive continuation envelope contract `methodology-codex-continuation/1.0.0`.
- Retain existing ordinary schema2 and role-return wire2.0.0.
- A proposed Codex package4.1.0 can identify additive support **only if** old supported nonterminal APIs remain compatible. Any necessary incompatible public API/state replacement must be explicitly classified before specification approval, rather than silently introduced during implementation.
- Keep neutral `SPEC_VERSION`4.0.0 in the independently deliverable Codex stage because shared-neutral source bytes remain unchanged in that stage.

The existing whole-helper AST protection in `tests/test_c1_review_and_routing.py` is a genuine affected compatibility consumer. The specification must authorize the exact Codex algorithm/package exceptions and retain unrelated drift controls and old behavioral regressions. Broad normalization or silently replacing its pin is not an adequate compatibility change. Claude’s protected implementation stays outside this executable scope.

**Rollout arrangement**

Prepare two reviewable delivery units under the same bounded specification.

The first contains Codex executable support, actual callers/CLI/tests, package/runtime/adoption declarations and Codex-specific applications of existing preflight/plan/test/lifecycle duties. It can be tested and considered for source integration against unchanged neutral4.0.0 without changing sibling bindings. Actual source integration still needs its matching result decision. No install, profile activation or consumer continuation follows.

The second contains the proposed shared-neutral clarifications in their existing owners. It remains held from canonical integration until separately authorized Claude/DSH agents provide compatible ordinary-operation bindings and acceptance evidence.

For this second unit, propose neutral4.1.0 if the final text **adds explicit duties**, including the earlier real-premise ordering. Use4.0.1 only for wording demonstrated to preserve every meaning; use5.0.0 if an existing norm’s meaning changes. Do not classify by the label “clarification.” Corresponding Codex bindings are part of this task; sibling binding/code changes remain those agents’ separately authorized work.

Ordinary sibling operations therefore remain against unchanged neutral4.0.0 during the first stage. After the shared-neutral bump, untouched hard-pinned sibling helpers cannot be advertised as operational. Compatibility-only sibling adoption need not claim terminal-continuation parity, but must prove their ordinary route works against the exact new neutral bytes.

The owner’s full requested shared-neutral delivery is consequently **not independently releasable within this executable grant**. Its precise held dependency is accepted sibling compatibility work, followed by matching integration/publication authority. Drafting that unit and transfer instructions remains possible now.

Installed complete snapshots remain unchanged. Canonical in-place consumers receive no protection from a snapshot that was never configured; therefore the shared-neutral hold applies before canonical integration. Snapshot rebuild/reinstallation, installed-profile changes, consumer migration/Jeni execution and sibling continuation implementation are explicitly withheld pending their own grants.

**Exactly two principal side effects**

1. Maintaining ordinary schema2 and a separate continuation-envelope format increases validation/caller complexity and creates a risk that an unupdated caller consults the wrong authority.
2. Staged delivery leaves a temporary difference between Codex’s concrete application guidance and shared-neutral text, while completion of the shared-neutral deliverable depends on external agents.

**Strongest objection**

The envelope creates another persistence contract and an authority-selection boundary. If every real caller cannot reliably distinguish ordinary state from an enrolled continuation lineage, it could bypass accounting or treat an exported phase view as authoritative. A unified successor schema may offer a smaller proof surface. This candidate is viable only if caller coverage and refusal behavior establish one authority per enrolled lineage.

**Future verification obligations and falsifier**

Meaningful future evidence must combine direct helper logic with actual shipped CLI and parent dispatch in isolated owned resources. It must cover the original3.2/native0+root4 import; contradictory or missing parent accounting; unchanged predecessor bytes after every success/refusal; no-repair QA at zero remaining; repair using remaining allowance; bounded extension and exhaustion; Code precharge; duplicate/sibling grant use; retained exhausted retry episodes; interruptions around reservation/release/completion; unknown-effect blocking; and renewed current QA/Review/Finalize.

Use representative retained historical artifacts as well as constructed fixtures. Preserve all applicable old regressions and inspect explicit AST-contract exceptions independently. Verify sibling ordinary-operation compatibility separately before shared-neutral integration; inspect actual installed/profile bindings only under a future grant.

A decisive falsifier is **any supported caller releasing a second causal repair without a distinct authorized charge, or releasing work from a stale/exported schema2 view while the authoritative envelope blocks it**. Additional falsifiers include Jeni’s aggregate4 becoming fresh0/default4, mutation of frozen predecessor bytes on refusal, or ordinary sibling initialization failing after a supposedly compatible shared release.

**Source basis and limits**

Source-backed premises include strict schema2 fields/cap, current package-neutral binding, terminal refusal/diagnostic behavior, initialization/advance/save/CLI behavior, STATE accounting/recovery/freshness requirements, PREFLIGHT-203, GATE-1209 and FMT version rules. I directly inspected those relevant helper bodies and owners, the runtime/adoption procedure, transfer brief and exact whole-AST compatibility-test logic. The actual Jeni values/hashes and historical profile observations are attributed to the shared RECON and independent completeness/delta evidence; I did not independently reread Jeni’s external ledgers or re-audit historical costs.

The envelope’s feasibility, caller completeness, correct scope reconciliation and two-stage delivery practicality remain design judgments requiring implementation evidence. No runtime, efficacy, host durability or native sibling parity claim is made.

Inputs read: full shared brief, full RECON, source manifest and original completeness/delta reports; full brainstorm/superposition/decision owners, with overlapping reads to recover truncated output; relevant current source/runtime/adoption and compatibility-test bodies. Some broad combined reads were truncated; claim-bearing portions were reread. This was bounded source inspection, not a whole-package audit or execution.

Writes: **none**, including scratch and Git. No tests, builds, helper/probe execution, network/provider calls, installation, configuration mutation, delegation or peer-output inspection occurred.
