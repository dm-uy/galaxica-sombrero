# Independent draft-specification verification

Actor: `/root/continuation_completeness`. Profile: read-only nonsoftware document/source verification, not Architect, implementation QA, proposal generation or evaluation. Root remains the sole writer. Exact permitted write paths: **NONE**, including scratch/Git.

Target/source: `WORKTREE_ROOT`, unchanged implementation baseline `388c94495d86a771da6fa5e8514249976dc8c8a1`.

## Verdict

**One material coupled-consumer scope omission requires reconciliation before marking the specification ready for owner review.** It is a bounded release-metadata correction, not a new architecture question or reason to reopen the authorized comparison.

Otherwise, the draft faithfully represents proposed A, keeps human specification approval pending, preserves the Codex-only implementation scope and exposes the external compatibility hold without pretending the isolated candidate can complete overall QA/Finalize or shared integration.

## Finding — missing neutral release-coupled consumer scope

**Severity:** readiness-blocking scope deficiency under SB-302/SP-203/SP-205.

The draft permits local `SPEC_VERSION`4.1, but its MAY EDIT population omits existing unconditional neutral release consumers:

| Actual consumer | Verified coupling |
|---|---|
| `tests/test_skeleton.py:409`, `test_spec_version_is_0_19_0` | Requires exact `SPEC_VERSION` bytes4.0.0. |
| `tests/test_first_layer.py:287`, `test_release_and_example_adapter_are_current` | Requires both neutral4.0.0 and example adapter4.0.0. |
| `tests/test_ldd_testing_protocols.py:1737–1741`, `_allocation_failures`, plus its matching mutation fixture | Rejects any other actual neutral/example-adapter version. |
| `tests/test_code_core_protocols.py:1273`, `test_core_promotions_and_remaining_homes` | Requires current README version4.0.0. |
| `examples/adapter.example.json:4` | Declares neutral4.0.0. |
| `README.md` | Current neutral version declaration couples to the preceding guard. |

These neutral-owned consumers are not all explained by deferred sibling implementation. Also account explicitly for shared-root `tests/test_claude_package.py:131` and `tests/test_dsh_package.py:153`: both inspect actual shared `SPEC_VERSION`. Their final package/compatibility expectations must be bound to accepted external contributions; this does not authorize local sibling source changes.

**Precise fix:** add purpose-bound identity-only release maintenance to MAY EDIT and the source correspondence, preserving unrelated assertions, historical text, norm meanings, mutation discrimination, Claude algorithm/default/wire protections and original guard strength. Separate:

1. Local neutral/Codex release identity consumers.
2. Shared-root sibling compatibility selectors updated only against the accepted external compatibility receipt.
3. Full combined execution still held until the compatible source exists.

Do not use blanket version replacement, broad AST normalization or an opaque new hash. Historical LAST_CHANGE/provenance strings are not automatically current-version obligations.

The existing AC-CONT-10/12 partition is sound once this owning scope is explicit; it already prevents claiming combined green or overall Finalize while external compatibility remains unresolved.

## Verified substantive correspondence

- Original A+B is one bounded change; В–Д stay with existing preflight/plan/test/lifecycle owners.
- Codex-only executable work and separate Claude/DSH explanatory instructions are retained.
- Proposed schema3/package5.0 is clearly a draft design requiring owner review. Persistent schema3, neutral4.1, native5.0 and unchanged role wire2.0 are distinct.
- Historical3.2/native0 plus parent4 reconciliation, current4.0 terminals and own closed schema3 artifacts are explicit admitted populations. Broader sidecars/schema1/active-run migration remain excluded.
- Frozen imported/closed terminal artifacts are distinguished from the mutable authority checkpoint; diagnostic-refusal and interrupted-publication risks are covered.
- Enrollment, supported-domain exclusivity, causal Code precharge, conditional seven-terminal reentry, no-repair QA, remaining allowance, bounded extensions, unknown-completion refusal and four scoped retry units appear in both requirements and acceptance.
- Real-shape artifact proof, actual shipped CLI and separate native-parent dispatch evidence are required. Script/mock evidence cannot substitute for native-parent proof.
- New IDs `PREFLIGHT-204`, `PLAN-405`, `TST-1003`, `LIFE-108` are unoccupied in current owning source. The draft proposes additive duties under FMT-24 and explicitly refuses silently changing existing meanings.
- The exact Codex whole-AST exception is disclosed, with meaningful boundary/mutation controls instead of a blanket repin.
- BR-1–10 and AC-CONT-1–12 are unique and source-mapped in both directions.
- All reviewed local file links resolve. No absolute home paths or email addresses were found in the16 publication-visible task documents/evidence entries checked.

No further material unresolved architectural fork was identified in this bounded population.

## Evidence and custody checks

Checked draft specification identity:

`7c0f7686a52a9a27dc64cc4a718d00aeb7454388fa2b1de2c6e095e9ca5f4b0a`

Checked original A/B/HOLD identities match their saved custody declarations:

- A: `b5677ccfb5b11df1cbedb97f26f1b19f037ee261ffe1dcc53fe48f26ab95484e`
- B: `204e1fcbb2eb5e96da51a859530f2e833536d3b5eca81e18d6b8509c384954a1`
- HOLD: `22006eef1f51ec94c1985ec104b1655fdebea5c9aa329b1f30069a5a72437fbf`

Evaluation arithmetic independently agrees: A7.00/B6.80 under the predeclared formula. Scores remain attributed judgments, not empirical superiority or approval.

Raw original brief hash `29844a0195dfc88551d2413964b3237b96b42a55d5d05445dcd8033ec15c940d` and original completeness report hash `2570fc9402cb015590de517bca0f4d0e9c5749d645afb9ccbe445779ac348a1e` are preserved in ignored task evidence. Tracked projections preserve the original body with the declared local-path substitution and separate projection note. All manifest source hashes match current bytes.

I verified saved originals and custody bindings; I do not independently certify hidden historical dispatch timing or every evaluator turn. The authentic launch reply is supplied in the assigning parent’s inherited authority/context and retained brief. It is not treated as implementation approval.

## Limits and write audit

Read complete draft/specification receipt, both proposals, HOLD, brief/addendum, evaluation, drafting decision and transfer instructions; relevant original owners/source/guards and current privacy/custody projections. Large initial combined outputs truncated; claim-bearing windows were reread separately. This is not exhaustive software correctness or whole-repository privacy certification.

No tests, builds, helper/probe execution, network calls, delegation, configuration changes, Git mutation or writes were performed.

After the exact scope/correspondence correction, a small read-only delta check is sufficient; no new proposal round or repeated launch permission is needed.
