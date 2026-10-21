# Historical independent document/source review — QA reflection clarification

Reviewed source at the original review stage: saved uncommitted content in repository `dm-uy/galaxica-sombrero`, branch `codex/qa-reflection-clarification`, base `9f95453`. The source was subsequently committed in `f72798d`; `ad5a72c` and `dc25ea4` changed only the four maintainer records. This report is historical, not a claim that the later PR head was uncommitted or newly reviewed here. The original absolute checkout path was intentionally omitted for publication; repository, base, source commit and branch supply its portable identity. No software QA verdict, tests, live probes or installation checks were performed by this original reviewer.

## Findings

1. **P2 — Reflection text adds an obligation while release claims a meaning-preserving patch.** `prompting/verification.md:29` says to apply the entire sequence before relying on every consequential analysis/recommendation, including conversational advice, and to use an authorized independent reader whenever available. Existing VERIFY-101/102 required check routes, evidence-sensitive revision and external factual verification; BRAIN-104/106 required independent actors only at their more specific consequential-open trigger. A source-grounded recommendation outside that trigger could previously satisfy the duties without obtaining another reader. The added imperative now makes that insufficient when a reader is available. Preserving numbered norm lines therefore does not establish FMT-25 (`FORMAT.md:110`). Either make the added paragraph genuinely explanatory, with optional questions/readers outside already mandatory procedures, and retain patch classification, or state the additive duty as a separately identified norm and use the FMT-24 minor version cascade. Do not silently redefine existing VERIFY-102 or create unnumbered new requirements while claiming no new norms. The same issue is mirrored in the three native prompting-verify carriers. This is about contract/version honesty, not a recommendation to add roles, phases or owner gates.

2. **P2 — Example adapter version was omitted from cascade.** `examples/adapter.example.json:4` still declares `3.0.2`; changed `tests/test_first_layer.py:287` now requires `3.0.3` for that same file, and the changed LDD allocation checker also expects it. Source comparison establishes the contradiction without executing tests. Synchronize the example adapter to the selected neutral release, preserving all other fields and the negative controls.

3. **P2 — Historical DSH measurement is now attributed to the new candidate.** `implementations/dsh/tests/test_guide.md:3` changes the current-source label to 3.0.3 but retains “Measured on the delivered candidate ...146 passed in145.52s”. That was the prior source's result; no new measurement provenance is supplied in this candidate, whose note says checks pending. Mark it explicitly as reused historical evidence for its original identity/limits, or replace the claim using the actual completed candidate check and evidence. Do not relabel the old elapsed time as a new observation.

## Checked scope and observations

Read complete changed neutral owner contexts (QA, tests, preflight, verification, decisions, session), FORMAT, complete brainstorm owner and safety owner; complete three native QA and verification carriers; task/source note and current-record deltas. Reviewed all tracked diff populations; version-only native/test hunks were also normalized for exact comparison, leaving only documented prose, pins/receipts and one inert Python continuation-space edit. New source note read directly because it is untracked. The remaining executable source edits are release literals, not helper algorithms. Tests were inspected for version selectors/pin refresh and retained negative control intent, not executed.

The strict QA-602 gate is retained, baseline count does not become proof, masked assertions remain unverified, BUG_REPORT/BLOCKED routing remains authentic, and matching real scope consent is reused without retroactively recoloring failures. Scenario guidance bounds actual resources and includes read-triggered/background effects and applicable nonempty fixtures; it disclaims exhaustive source census. Failed preparation withholds dependent launch and helpers explicitly do not sandbox arbitrary child writes. Repeat-assignment evidence does not inherit independent reading or runtime validity from a source hash and does not waive fresh full QA after repair. Reflection retains brainstorm independence at its existing trigger and excludes routine ritual/fanout/gates. Public notes abstract the private consumer incident rather than copying payloads. No observed weakened scan, status, budget, gate or source-protection control.

## Limits and write audit

This review proves only the checked document/source relationships and identified contradictions. It does not establish future agent compliance, comparative effectiveness, runtime safety, whole-methodology quality, installation or live delivery. No private-source reinspection was authorized/performed. Root is running separate checks in an owned Git-free copy; those results are not claimed here. Source was read-only; no Git state, tests/runtime/settings or delegation changed. Only write: `[original private scratch report]`. No outside writes.

## Revised freeze rereview — 3.1.0 / Claude2.2.0

All three initial findings are resolved in the inspected revised source. VERIFY-105 SHOULD is explicit at prompting/verification.md:29, recommendations retain proportionality and the complete BRAIN-104–110 trigger remains mandatory. FMT-24 MINOR is justified as an added recommendation without altering the earlier norm meanings; 3.1.0 neutral/Codex/DSH and2.2.0 Claude communicate that addition honestly. The mirrored carriers refer expressly to the neutral recommendation. The example adapter now binds3.1.0. DSH test guide explicitly labels the146/145.52s observation historical3.0.2 evidence, not a new execution. The remaining bridge-pin rationale's phrase “patch identity” is loose wording about a file patch rather than the release classification; all actual selected versions and source note correctly say MINOR, so this is not a blocking defect.

Read the updated complete verification owner/source note and latest full diff population. Exact version normalization showed no residual executable/test edits beyond version selectors and justified pin/oracle changes; the initial inert continuation-space edit is removed. Source note preserves initial failures and corrections, does not assert pending checks passed, and explains the transient product/history substring correction. Source note initial counts were checked directly against original stdout tails: root601passed/4failed126.33s, native Codex2, DSH2, selected Claude158. No false private-source or efficacy assertion found.

Read root preservation receipt and independently compared every tracked path plus the new note to final/source:425 files, no byte differences at inspection. Thus final check snapshot matches reviewed source at that time; this comparison is not execution evidence. Root preservation.json reports original norms/fences preserved, only added VERIFY105, four source ASTs unchanged except versions and50 path-bound QA receipt updates. Existing control code retains its original contrary cases. No unresolved document/source findings in this bounded rereview. Final runtime/package checks remain pending and are required before closure claims.

Write audit unchanged: only [original private scratch report] written.

## Final execution-receipt and oracle delta verification

Verified final/root.stdout:602passed/3failed126.76s. All three failure locations are exact current-population assertions expecting1242 against actual1243, consistent with the single added VERIFY105. Reviewed tests/test_format.py and tests/test_report.py delta: only those three exact expected integers plus the matching purpose count change to1243; protection siblings, population-key checks, capability/parameter/anchor checks and verdict/log checks remain. Reviewed bridge rationale edit: “patch identity” becomes “version identity”, with the same current carrier hash and negative controls. All three beforeimage and afterimage hashes in oracle-correction.json match actual saved beforeimages and latest source; corrected scratch and source bytes match for these three files.

Verified oracle-recheck.stdout:6passed1.07s. This is the three formerly failing cases plus the bridge module, not a fresh entire-root-suite run. Root full-suite result must remain reported as602passed/3failed followed by affected-case6passed; neither this reviewer nor the note should call the complete suite freshly green. This bounded rerun is justified because only exact expected population constants and an inert rationale changed after the full run; no production or methodology source changed.

Verified final native stdout tails:Codex2passed0.02s, DSH2passed0.02s, selected Claude package/hook/profile/run-state158passed57.77s. Verified all three adapter stdout SUMMARY rows:exit0,pass76,warn0,fail0,neutralfiles71,anchors447,norms1243,specversion3.1.0. Native package subsets must be named as such, not described as full native suites. These are source/package consistency results; no efficacy, future compliance, live probe or installed-profile acceptance follows.

No unresolved document/source finding. Previously reported three defects remain retained as corrected history. Current-record closure edits and future commit/PR identities are root-owned subsequent operations and were not certified by this precommit source review. Audit: only exact scratch report written; no other writes or tests/probes run by reviewer. A read-only attempt to parse the textual adapter output as JSON failed locally; direct SUMMARY inspection above resolved that reading-format error without changing any artifact.


## Custody

Root imported this independent report into the existing project notes. Only local absolute-path presentation was normalized; findings, resolutions and evidence limits are retained. The original scratch report remains on the owner machine.


## Later PR review provenance

Two owner-supplied independent reviews inspected committed head `dc25ea4957044e8eb3e7bc84b1396d439c0fcd83`; their findings and measured checks are reconciled in [the follow-up record](qa-reflection-clarification.md#pr17-independent-review-follow-up). The old DSH timing discussed above was inherited by the3.0.2 guide from source e959e66 (DSH3.0.1), not measured anew on3.0.2. The original review observations above remain history.


## PR17 bounded correction review — 2026-10-21

Disposition: no actionable document/source finding in the inspected follow-up. This is a bounded documentation review, not a software-flow QA verdict or integration approval.

## Identity and scope

Reviewed `dm-uy/galaxica-sombrero`, branch `codex/qa-reflection-clarification`, delta from `dc25ea4957044e8eb3e7bc84b1396d439c0fcd83` to the current uncommitted correction. Twelve changed paths match the assigned population: four test files, three QA carriers and five maintainer records. Original neutral owners are unchanged in this delta. No tests, application runtime, database, Git mutations or delegation were performed by this reviewer.

## Findings resolved

- Independently parsed all four before/after test ASTs: identical. Exactly five comment lines change (2+1+1+1), now aligned with the existing 3.1.0/2.2.0 assertions. No algorithm or assertion was altered.
- The PR creation readback is explicitly historical; committed snapshot dc25ea4 is identified separately from source f72798d and the record-only successors. Git history confirms both successors touch only the four stated maintainer records. A self-referential current-commit hash is correctly avoided.
- Original source review remains accurately identified as precommit review, with later source provenance supplied rather than rewriting the original event as postcommit review. Repository/base/branch/source identity is portable; an owner-local absolute path is unnecessary.
- The historical author results (601/4, 602/3 and focused 6-pass correction) remain recorded. Fresh full-suite results are attributed to the first independent review at dc25ea4; second-report timing is explicitly attributed without claiming unavailable raw streams.
- HANDOFF has one current baton/next action. GRACE-Q2, M37 migrations/retirement, DSH probe and profile boundaries, exhausted C3, incomplete M30 and deferred route remain recoverable through existing links. Local HANDOFF and note targets resolve; M37 explicitly records both run-state limitations. Main merge/install/release are still withheld.
- All three QA carriers now point to the full neutral verdict/test-guide owners. Launch/repeat triggers require full preflight/session reads. Their existing complete-owner, eight-scan, strict-verdict and independent-role duties remain intact. Anchor targets exist; a separate duplicated-prose pin would add no needed policy protection here.
- The owner-directed gh account switch is directly present in the inherited human conversation and is now explicitly distinguished from the original settings exclusion. Optional rule redesign and extra status/pin machinery are reasonably excluded.

## Receipt readback

Personally read the first reviewer’s original report and raw stdout/exit receipts: root605/128.29s, baseline605/127.03s, Claude545/179.46s, Codex146/62.74s, DSH146/63.39s; all exits0. These match the updated result note and retain the reviewed dc25ea4 identity.

Read follow-up raw stdout presently available: Claude7/0.17s, Codex2/0.02s, DSH2/0.02s, root package checks13/30.34s. Independently verified every one of426 entries in the follow-up source manifest against its Git-free copy: zero hash mismatches. The preservation receipt’s five comment lines and unchanged ASTs agree with this reviewer’s own comparison. These bounded checks are not a fresh full-suite execution.

## Limits and custody

No live/installed efficacy, private deny-list coverage, new full-suite execution or future agent compliance is established. Map/adapter/final record receipts still pending at this inspection are not inferred passed. Subsequent root-owned record closure and Git/PR delivery require their own readback; this review grants no merge or installation authority.

Only reviewer write: this report at the exact assigned scratch sink. No outside writes or source/Git mutations.

## Final closure readback

Reread the five finalized records and their local link targets. Their current 2/2/7 native-contract counts,13 root package checks, four76-pass adapters and three package maps/five XML member contracts match the available bounded receipts. Full605/545/146/146 suites remain attributed to dc25ea4, with no fresh full-suite or installation claim. PR creation readback now has an explicit2026-10-21 date. No new actionable finding; hold/authority boundaries remain intact.

Independently parsed the actual generated XML, rather than only the map verification JSON. Unique named members, source files/lines and new version text match all five recorded rows: Codex and DSH `test_actual_layout_and_adapter_contract` line89; Claude `test_real_package_binds_and_states_duty` line246, `_routing_problems` line545 and `test_routed_entries_name_carrier_and_launchers` line1363. Stale current-version literals are absent from those member contracts; the Claude session example contains both2.2.0 and3.1.0. All three Doxygen stderr files are empty; tool exit0 is root-reported (there are no separate exit-code files in this scratch sink).

Personally read all four adapter SUMMARY rows: exit0,pass76,warn0,fail0, neutral71files/447anchors/1243norms/28capabilities/7parameters,spec3.1.0. Source freeze versus later record closure is explicitly distinguished. Subsequent report import/commit/push remains root-owned and unreviewed delivery activity.

Write audit unchanged: only this exact assigned report file written, no source/Git mutations, tests, application probes or delegation.


Root imported this follow-up report into the existing review history after its final readback; source fixes and original review observations are preserved.
