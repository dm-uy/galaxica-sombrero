Candidate **A — Versioned operational successor with coordinated release hold**

This is one unranked integrated proposal for the bounded two-to-three-alternative packet. It addresses Q-REPRESENTATION and Q-ROLLOUT together. No fallback, scores, selection or implementation is proposed.

**Essence.** Introduce a Codex schema3 operational ledger in which cumulative accounting, grant consumption, successor identities and dispatch reservations belong to one authoritative causal lineage. A historical predecessor is read through a narrowly supported importer, then remains immutable. The successor binds current approved inputs and current package identities independently. Deliver the resulting Codex candidate for review in isolation; hold shared-neutral main integration until separately authorized Claude/DSH compatibility work is accepted.

**Representation and trust boundary**

The schema3 ledger contains the active successor’s ordinary run state plus:

- Causal-lineage identity and exact predecessor references.
- Imported accounting provenance and reconciliation result.
- Original allowance, cumulative spend and individually bounded additional grants.
- Consumed grant identities and exclusive outstanding dispatch reservation.
- Retained retry episodes, completion identities and historical references.

This is one accounting authority inside the operational ledger, not a second wallet or a new project-wide register. Ordinary initialization retains default4 and cannot be used to replace an existing causal lineage with fresh spend0.

Historical validation is separate from current operational validation. The importer initially admits only:

1. The motivating Codex3.2/schema2 shape, paired with its identified parent aggregate-accounting record.
2. Current Codex4.0/schema2 terminal records with sufficient native accounting, requiring a parent reconciliation input whenever their provenance says accounting occurred outside that native state.
3. Successors produced by the new schema3 contract.

It does not execute the old helper, rewrite old bindings or assert that historical inputs satisfy current operational requirements. It validates strict supported structure, version/contract identity, terminal status, contained source locations, recorded identities and exact source bytes; root authenticates provenance and matching human authority.

For the motivating pair, imported cumulative spend is4 and original ceiling4. Native0/0 is retained as its distinct historical allowance, not added again and not substituted for aggregate spend. Reconciliation must identify whether native amounts are already included in the parent total; conflicting, ambiguous or incomplete relationships block import. A caller cannot supply an arbitrary aggregate number without the supported parent record and its provenance.

The old native ledger and parent accounting record remain byte-for-byte unchanged on success and every refusal path. Rejections go to the new operation’s receipt or stderr, never through the old `record` diagnostic path. Historical hashes establish byte identity, not authenticity of every original cost or turn.

**Current successor and history**

The successor has a new run identity, explicit continuation reason and authentic approval references. It separately locks the current specification, dictated plan, framework/adapter, approved scope and actual candidate inventory. Historical baseline, failures, causes, costs and evidence stay linked and distinguishable from the successor’s acquired baseline and current evidence.

No earlier phase receives invented SUCCESS. A parent-authenticated entry assessment identifies the earliest phase whose real predicate must be performed. Unaffected historical evidence can remain informative or reusable for its original property; affected QA/Review/Finalize evidence must be renewed under STATE-501–504.

For later schema3 successions, terminal run records become immutable snapshots before a successor is authorized. Snapshot creation alone supplies no execution authority. The active lineage checkpoint is the sole place that authorizes a new successor and carries accounting forward. Interruption between snapshot creation and that checkpoint may leave an unreferenced snapshot; it must not create another active allowance. Exact storage layout and safe snapshot publication belong to Architect, but the one-authority invariant belongs in the specification.

**Supported terminal and reentry population**

The supported status population is the existing seven terminal outcomes, with conditional reentry rather than a status-only reopen command:

| Terminal predecessor | Permitted successor entry after matching resolution/authority |
|---|---|
| SPEC_BLOCKED | Bootstrap or Architect to establish missing or amended specification/design predicates. |
| VISUAL_GATE_FAIL | Architect to repair the actual plan/visual deficiency. |
| BLOCKED or ERROR | Earliest incomplete applicable phase after the blocking prerequisite or unknown completion is resolved. |
| ESCALATED | QA without source repair when eligible; otherwise a charged causal repair within remaining allowance or a bounded extension. |
| ESCALATED_FINALIZE | Current Finalize only when no source repair is required and its current prerequisites hold; source repair returns through a charged producer and renewed QA/Review. |
| SUCCESS | Explicitly authorized same-cause continuation, such as renewed verification or newly discovered defects; a separate new feature uses its own approved task, not this importer. |

Additional constraints apply across every row:

- Entry to Bootstrap/Architect performs real work and creates no fake earlier verdict.
- Entry to Code requires an actual current approved plan/scope. When that Code work repairs the inherited cause, it consumes the same pre-entry causal unit as Debug.
- Entry to QA requires actual eligible authored artifacts and current input/candidate validation. It needs no positive additional repair allowance.
- Review requires applicable current independent QA; Finalize requires current QA and affected Review.
- Unsupported phase/status combinations, insufficient evidence and unresolved unknown effects refuse.
- The motivating Jeni BLOCKED/code record establishes completed terminal Code work, not an unfinished worker. Its proposed new source repair cannot reuse repair4 for free.

**Allowance, exclusivity and recovery**

The specification fixes this sequence before any repair dispatch:

1. Check actual required helper capabilities, supported versions/import shape, current inputs, candidate, authority, allowance and scoped retry limits.
2. Reconcile the historical accounting and continuation grant.
3. In the one authoritative checkpoint, record the successor/phase entry, causal charge, grant allocation and unique dispatch reservation together.
4. Read back that reservation and current identities before the parent releases the worker.
5. Bind accepted output or investigated completion to that dispatch identity.

Additional grants retain GATE-1209’s actual entry/cost constraints. An additional grant is not required for eligible no-repair QA, and the helper cannot authenticate consent merely because a reference is populated. Unknown costs remain unknown; the existing resource contract determines whether they prevent another dispatch.

A lineage admits one authoritative writer and one outstanding repair reservation. Reusing a consumed grant, opening a competing successor or replaying a completed dispatch refuses within that declared storage/lineage domain. All supported continuation operations consult that same ledger. Copying its files or introducing another writer/host is outside the enforcement guarantee; this proposes no distributed lock service or adversarial clone protection.

Interruption treatment is deliberately bounded:

- Before the accepted reservation checkpoint, no worker release is permitted.
- After reservation but before release, spend remains charged. Once actual nonrelease is established, the same reservation can be released without another charge.
- After possible release, missing acknowledgment means unknown completion. Investigate worker identity, artifacts and actual effect/completion evidence before any replay.
- A validated completed result may be accepted through current recovery predicates. An already entered unfinished worker may resume under its existing reservation when supported and safe.
- An absent/corrupt ledger, uncertain release or unexplained changed candidate blocks dependent work.
- A failed or BLOCKED entry retains its charge. A terminal completed entry is not relabeled interrupted recovery.

Checkpoint replacement does not prove atomic worker launch, exactly-once transport or power-loss durability. Stronger guarantees would require new evidence and, if materially broader, matching authority.

**Retry scopes**

Preserve response-correction, extraction, transport and test-session histories and costs separately from causal repair spend. An unfinished episode carries its original identity, used allowance and cap into recovery. Renaming the successor does not reopen an exhausted episode.

A genuinely new phase attempt or authorized test session may start a new episode only under that unit’s existing scope rules, with an explicit predecessor/closure relationship. This proposal does not add transport or extraction retries where the current Codex profile permits none. Response correction remains at most one per phase attempt.

**API and compatibility boundary**

Schema3 is an explicit incompatible persistent-state contract. Proposed Codex package version: **5.0.0**, with a separately identified state contract3. Existing canonical role-return wire2.0 remains unchanged unless a later approved specification identifies a concrete necessity to change it; persistent schema version and role-return wire must not be conflated.

The public helper needs an explicit continuation operation, read-only capability reporting and reservation/reconciliation operations consumed by the actual parent dispatch path. Exact command spelling and function decomposition are Architect details. Ordinary `record` cannot become a disguised terminal-reopen operation.

Old schema2 ledgers remain readable historical inputs, not silently upgraded operational files. Existing schema2 ordinary runs remain usable through their unchanged complete old package snapshot. Moving an active old run to the new package is not promised by this terminal-continuation contract.

The root compatibility test `test_release_bridge_keeps_wire_and_helper_algorithms` currently pins the whole normalized Codex helper AST and explicitly detects schema/default drift. The new specification must authorize the exact Codex algorithm/schema exception and retain meaningful old-regression controls. Broadening normalization or replacing a pin merely to obtain green is unacceptable. Claude’s original algorithm protection remains outside this Codex exception; later sibling compatibility changes need their own scoped review.

**Rollout**

Treat the shared-neutral clarifications conservatively as new explicit duties where ordering was previously implicit. Proposed neutral version: **4.1.0**, assuming the final wording adds requirements without changing existing meanings. Any actual meaning change instead follows FMT-23’s MAJOR requirement; “clarification” is not a version exemption.

The Codex candidate and neutral4.1 proposal can be implemented and reviewed in an isolated complete checkout under a future specification/run grant. That candidate checkout is not advertised as an operationally compatible package for untouched Claude/DSH helpers. Canonical main and existing installed snapshots remain at their current versions while the release dependency is held.

Transfer instructions ask separately authorized Claude/DSH agents for two distinguishable outcomes:

- Required compatibility with the selected shared-neutral version, including their ordinary initialization/validation, adapters, runtime/adoption/layout claims and affected tests.
- Separately scoped native continuation implementation if and when the owner grants it. Full continuation parity is not a prerequisite merely to preserve ordinary operation, provided advertised limits remain truthful.

Shared-neutral main integration waits for accepted sibling compatibility changes and ordinary-operation checks on the final combined candidate. This task does not edit sibling code or presume those grants. If that compatibility work is absent, the concrete deliverable remains a tested Codex candidate plus transfer packet; common-source release stays held.

After compatible source acceptance, publication, complete-snapshot packaging, installed profile updates and fresh binding/discovery checks each follow their future matching grant. Existing in-place Claude/DSH consumers make source integration consequential even before an explicit installer runs. This candidate does not solve the dependency by silently repointing them to older snapshots.

Withheld actions are therefore explicit: sibling source changes; shared-neutral main integration before compatibility acceptance; publication; installed snapshot/profile activation; Jeni import or continuation; and any additional Jeni repair/resource grant.

**Exactly two principal side effects**

1. Schema3 introduces a persistent-format and caller migration boundary, increasing validation and compatibility-test work even though role wire and software phases remain unchanged.
2. Coordinated release preserves ordinary sibling availability but couples main delivery of the Codex feature to external agents’ separately authorized compatibility work.

**Strongest objection**

The representation centralizes accounting cleanly but is a substantial native contract change for a bounded capability gap, and the release hold can delay practical Jeni applicability. Its viability depends on keeping schema3 limited to the stated continuation/accounting requirements rather than using it to redesign orchestration.

**Future verification and falsifier**

Future authorized verification must exercise production helper functions, the real CLI and the actual parent reservation/release path in isolated resources. Required differentiating cases include:

- Jeni-shaped parent4/native0 reconciliation; double-counting, missing-parent and inconsistent-parent controls.
- Byte-identical predecessor preservation after accepted import and each refusal, including malformed CLI input.
- Each supported terminal/reentry class; no-repair QA at exhausted allowance; repair through Code; new repair refusal at the extended ceiling.
- Duplicate grants, competing successors, completed-dispatch replay, wrong scope and candidate/input drift.
- Interruption before checkpoint, after checkpoint/before release, and after uncertain release; no duplicate charge and no blind replay.
- Retained exhausted retry episodes and legitimate new scoped episodes.
- Renewed current QA/Review/Finalize predicates and existing negative regression controls.
- Ordinary Codex/Claude/DSH initialization and validation against the final coordinated source, alongside explicit unsupported sibling continuation claims.

A decisive falsifier is a real supported-domain sequence that releases two causal workers using one reserved entry/grant, or imports the motivating pair as fresh0/default4. Another release-level falsifier is ordinary sibling initialization refusing solely because the combined accepted source has advanced neutral version without its required compatibility closure.

These checks are **NOT RUN**.

**Evidence and limits**

Source-backed premises: strict schema2/cap≤4, current full binding validation, zero-spend initialization, terminal refusal and diagnostic mutation behavior, pre-entry Debug charging, temporary-file replacement, the four retry units, neutral state/gate/preflight/plan/test/lifecycle duties, sibling hard pins, and the root AST compatibility control. I directly read the motivating parent record and relevant native identity window, plus its full continuation assessment.

Design judgments: schema3 centralization, proposed versions, the conditional reentry matrix and coordinated release hold. Exact schema fields, serialization, storage layout and command names remain specification/Architect work. Historical authenticity beyond the inspected records, runtime durability, installed-profile freshness and all behavioral efficacy remain unproved.

Inputs read included the same complete brief, complete RECON, source manifest, original completeness/delta reports, full brainstorm and superposition owners, decisions owner, relevant runtime/adoption material and actual claim-bearing source windows. Some broad combined reads truncated; relevant bodies/windows were fetched separately. Archived current-record history and the large native ledger were not exhaustively reread. No peer outputs or later evaluation were inspected.

**Writes: none.** No tests, builds, helper/probe execution, delegation, network/provider calls, configuration changes or Git mutation occurred.
