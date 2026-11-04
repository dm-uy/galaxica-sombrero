# CONT-BOUND Claude ordinary compatibility — checked locally

Status: Claude 3.1.0 candidate on branch `claude/cont-bound-compat`, based on the Codex candidate `a3ecb5c`. Source commits `5e68c96`, `de6b91b`, `eba2905`, `e5d292d`, `fbf0fd0`, `3a5ae50` and `985795b`; recover the closing record commit from the branch. Proposed to main through a pull request at the owner's word; owner result and merge are pending. Main, installed plugins and the DSH package are unchanged by this branch; the Codex package changes on this branch only as stated under [stale Codex stamps](#stale-codex-stamps). This is the return the [transfer briefs](bounded-continuation-transfer-briefs.md) require from the Claude agent's first bounded packet.

## Authority and scope

Owner, 2026-11-04: «надо доработать наш плагин с методологией», pointing at the transfer briefs, then, asked to choose the scope: «Сначала совместимость». This covers ordinary compatibility of the Claude package with neutral 4.1.0. Porting continuation stays a separate later decision. Merge, push and installation are not granted. The work followed a lighter procedure as an additive release with one independent reviewer, not a feature-dev run, so no run ledger or role envelopes exist for it.

The owner was told before starting that the base defect in `tests/test_recon_decision_checkpoint.py` would be fixed here unless they objected. That file is outside the Codex specification's MAY EDIT list, which governed that task. Only its module contract changed. The Claude selectors in `tests/test_claude_package.py` and `tests/test_c1_review_and_routing.py` are conditional in that specification on an accepted receipt for the exact source, so they can reach main only with the owner's acceptance.

Owner, 2026-11-04, asked whether to correct the stale Codex version stamps on this branch or leave them to a Codex agent: «Да, поправь здесь». This covers stale release, schema, member-count and path statements in the Codex package and the guard against their return. Codex carrier wording stays with its owner. No shipped Codex helper or script changes; one Codex test gains the guard.

Owner, 2026-11-04: «А сделай pull request в main». This grants pushing this branch and opening the pull request, not its merge or any installation.

## Identities

| Domain | Value |
|---|---|
| Neutral | 4.1.0, unchanged by this work |
| Claude package | 3.0.0 → 3.1.0: MINOR, as FMT-24 and the precedent of 3.1.0/2.2.0 and 3.2.0/2.3.0 give for additive neutral releases |
| Run-state contract and schema | `methodology-claude/1.0.0`, schema 2, unchanged |
| Default Debug cap | 4, zero valid, unchanged |
| Codex and DSH | Codex stays 5.0.0: stale statements and one test, no shipped helper or script change; DSH 4.0.0, zero bytes changed |

## Touched paths

- Release constants: `implementations/claude/.claude-plugin/plugin.json`, `adapter.json`, `references/package-layout.json`, `hooks/session_start.py`, `skills/feature-dev/scripts/run_state.py`.
- Version stamps in text: `implementations/claude/README.md`, `references/consumer-pm-profile.md`, `references/source-disposition.md`, `references/handoffs.md`, `skills/semantic-exoskeleton/SKILL.md`.
- The four duties and the helper's limits: `skills/pm/SKILL.md`, `skills/devplan-protocol/SKILL.md`, `skills/feature-dev/SKILL.md`, `references/claude-runtime.md`, `references/adoption.md`.
- Package tests: `tests/test_package_contract.py` gains two tests and corrected module facts; `test_session_start.py`, `test_run_state.py` and `test_consumer_profile.py` change identity selectors only; `tests/test_guide.md` gains a section.
- Shared root: `tests/test_claude_package.py` and `tests/test_c1_review_and_routing.py` change Claude selectors only; `tests/test_recon_decision_checkpoint.py` gets a complete module contract; `tests/test_guide.md`, `README.md` and `CHANGELOG.md` report the release.
- Stale stamps, Codex: `adapter.json`, `README.md`, `examples/smoke-spec.md`, `references/consumer-pm-profile.md`, `references/source-disposition.md`, `skills/semantic-exoskeleton/SKILL.md`, two comments in `skills/feature-dev/scripts/run_state.py`, `tests/test_native_contract.py`, `tests/test_guide.md`.
- Stale stamps, shared and Claude: the carrier's pin in root `tests/test_claude_consumer_bridge.py`; comments in the Claude `run_state.py` and `session_start.py`.

## What did not change

Between `a3ecb5c` and `985795b` there is no delta in `implementations/claude/workflows`, `agents`, `hooks/guard_destructive.py`, `hooks/hooks.json`, `implementations/dsh`, the neutral `checks`, `protocols`, `code`, `process`, `flow`, `roles` or `SPEC_VERSION`. The Codex package differs only in the paths listed above, and its `run_state.py` has the same AST as at `a3ecb5c`. The executable lines changed in the Claude helper are exactly its three release constants, and in the hook its one. The frozen Claude helper and hook AST pins in `tests/test_c1_review_and_routing.py` pass with their values unchanged.

`workflows/feature-dev.js` needs no change for ordinary operation: it holds no package or neutral release literal, and its harness scenarios, which drive the real helper with scripted agents, pass.

## Evidence on `985795b`

The table is from a Git-free `git archive` of that commit with Python 3.12, exposed streams, no skips. The helper CLI probe, boundary refusals, hook runs and live session below ran on `eba2905`. Since then the Claude source differs by one runtime paragraph, tests and comments: the Claude helper and hook have the same AST as at `eba2905`.

| Check | Result |
|---|---|
| Claude package suite | 548 passed |
| Root suite | 616 passed |
| Codex package suite | 201 passed |
| DSH package suite | 83 failed, 63 passed; held, see below |
| `bin/conform adapter` | Claude and Codex pass 76, fail 0; DSH, on `eba2905` with no DSH or neutral delta since, pass 75, warn 1 (adapter targets 4.0.0), fail 0 |
| `doxygen Doxyfile`, root, Claude and Codex | exit 0, empty stdout and stderr |

**Why replacing the version alone was not enough.** On a scratch copy of `a3ecb5c`, replacing `4.0.0` with `4.1.0` throughout the Claude package, including its tests and stamps, took the package suite from 167 failed to 545 passed and bound the hook, with none of the four duties carried. The suite could not see them. `test_additive_duties_reach_their_carriers` now catches removal of each listed statement or a change inside it, across 43 controls. It is a finite recognizer, not a prose solver. The root AST guard, already red at the adapter version, then refused at `wrong release comparison`, which is why its selectors moved and its pins did not.

**Real helper CLI.** An owned inert probe drove the full ordinary route through the shipped CLI under Python 3.15.0, 3.12.13 and 3.9.6: Bootstrap → Architect → Code → QA → Review → Finalize, then SUCCESS at spend 0 of cap 4, bound to neutral 4.1.0, schema 2. A malformed record exits 2 with progress and counters unchanged. Records are structural fixtures, not role acceptance.

**Real boundary refusals.** `capabilities`, `continue`, `reserve`, `released`, `recover` and `episode` exit 2 with empty stdout. `--max-debug 5` exits 2. A real Codex 5.0 schema 3 ledger is refused unchanged. A real Codex 4.0 schema 2 ledger is refused, but a refused `record` appends its diagnostic to that file, as for any shape-valid schema 2 ledger.

**Live native session.** A fresh Claude Code 2.1.285 session started with `--setting-sources project,local`, `--plugin-dir` on the candidate and Sonnet as root; the exact command is retained in the evidence home. Its init event lists the candidate path and all six `methodology-claude:` roles. The SessionStart hook exits 0 with `methodology-claude 3.1.0 bound in place to neutral methodology 4.1.0`. The session loaded the `feature-dev` skill from the candidate, ran `init` and `show` through the default `python3` with neutral 4.1.0 bound, and dispatched `methodology-claude:searcher` on Haiku, which returned its inventory line. This shows loading and dispatch, not model obedience or efficacy.

### Stale Codex stamps

The Codex 5.0 candidate raised its constants and left free-text identity behind: the exoskeleton stamp and consumer profile named package 4.0.0, neutral 4.0.0 and schema 2, and the adapter's `run-state-persist` row named schema 2 under `.methodology/runs`. No test read them, so every suite stayed green. The source disposition, README and smoke specification held older member counts, paths and labels. All now state the actual identity, measured from the layout, adapter and `continuation.capabilities`: package 5.0.0, neutral 4.1.0, schema 3, wire `methodology-codex/2.0.0`, 75 members, 27 skills, seven helpers, six roles.

Replacing the number alone would have been wrong: "Wire methodology-codex/2.0.0/schema2 remains unchanged" became "Wire methodology-codex/2.0.0 remains unchanged; persistence is schema3", because at Codex 4.0 the wire was the same and the schema was 2. The bridge pin moved to `fd0e0dde…` with a dated reason, as its module requires.

The cause is free-text identity outside any check: in Codex no test read these stamps, and in Claude a consumer-profile test read only three version stamps, not the neutral tokens or five other carriers. So each package suite gains `test_release_stamps_match_package_identity`: 19 statements in eight Codex carriers plus the adapter row with 38 controls, and eight Claude statements with 12 controls. The Codex guard failed on the old bytes, naming five statements, before the correction. Blinding either predicate fails its test. Both are finite recognizers: they detect a lost statement, not a contrary sentence added beside it, and cannot prove other text current. The Claude stamps were already correct; two helper comments and one hook comment there were not, and they are fixed.

### Other evidence

**Base defect.** `tests/test_code_layer.py::test_every_python_module_has_the_exoskeleton_before_imports` fails on `main` at `388c944` too, with seven diagnostics in that one file: main's root suite is red today, independently of this work. It passes here with no test logic changed.

**Retained run mistake.** The first parallel root, Codex, DSH and conform run lost its working directory and copied `main` instead of the candidate. Its `spec-version=4.0.0` and 146 Codex tests exposed this; it was discarded as candidate evidence and kept as the `main` baseline: root 613 passed and 1 failed, Codex 146, DSH 146. `main` itself was only read. The first version of this record also failed the publication scan through a home-relative path, 40 root failures on `scan.home-relative` and its dependents; the check was right and the text was corrected.

## Independent review

Compatibility reviewer: `methodology-claude:reviewer` on Opus 5.5, read-only with one scratch write root; no write outside it in any round. All three rounds found no blocker and independently confirmed the functional compatibility and all protections, including a structural AST diff, identical pin digests and file mutations that fail the pins. The originals are in the private evidence home.

Round 1 on `5e68c96`, CHANGES REQUESTED, dispositioned in `de6b91b`:

| Finding | Disposition |
|---|---|
| S1 Wrong refusal reason for a run bound to an earlier package | Confirmed by a separate reproduction; guide and runtime corrected |
| S2 Carriers denied continuation while the package and STATE-702 offer an owner-approved one | The runtime states what the helper lacks and what a successor can be |
| S3 No result note, stale records, no measured values | This note, the guide and the current records |
| S4 Workflow check did not discriminate | Exact usage line, ceiling and argument list |
| S5 Carrier test checked presence only | Inversion controls added, recognizer limit stated |
| S6 Inaccurate facts in the completed contract | `@links` and `@usecases` corrected |
| N1–N5 Module facts, harness wording, narrowed norms, restated norm, carrier column | Fixed in this package |
| N6 Stale Codex stamps | Outside the first scope; corrected later at the owner's word, see the stamp review below |

Round 2 on `a071849`, CHANGES REQUESTED, dispositioned in `eba2905` and `4e078c8`:

| Finding | Disposition |
|---|---|
| D1 The successor wording allowed 5 of 4 cumulative repairs, reproduced with the real helper | The root counts that repair before dispatching it and passes `init` the cap that keeps cumulative spend within the allowance |
| D2 Counting a successor's Code repair is a process rule neutral does not state | Marked as this package's conservative reading; raised below |
| D3 Factual errors: another package's ledger, the ledger rule's home, hook interpreters, Workflow literal, the AST guard | Corrected; the hook now ran under all three interpreters with retained output |
| D4 Clauses inside the statements were unguarded | Pinned; ten further mutations from that review each detected by a separate check |
| R1–R3 Module facts, unsourced consumer claim, evidence outside its home | Fixed |

Round 3 on `4e078c8`, CHANGES REQUESTED, narrow check. It confirmed D2, D3, R1, R2 and R3 closed and the changed record claims true. It ran the formula against the real helper across prior spend 2, 3 and 4 with and without a counted repair: cumulative spend stayed at or below 4 of 4, and a result below zero exits 2 at `init`.

| Finding | Disposition in `e5d292d` |
|---|---|
| F1 The sentence gave no formula and placed the count after `init`, so a root could silently reach 5 of 4 | Count decided before `init`, formula stated, a later repair has no supported route |
| F2 Words deciding that sentence's meaning sat outside the pinned strings | Sentences pinned whole; ten mutations from this round each detected by a separate check |

These last two corrections were not returned to the reviewer. They apply the reviewer's own formula and fix direction to one paragraph and one test, and no further round was run. Whether a real root follows the sentence is a behavioral question no check here answers.

Stamp reviewer: a fresh `methodology-claude:reviewer` on Sonnet 5.5, because this is a routine check of facts, not a judgment of design. It wrote only under its scratch root apart from one stray temporary file outside it, which it removed and reported. It ran the helpers, mutations and targeted suites, not the full suites.

Round 1 on `fbf0fd0`, CHANGES REQUESTED, dispositioned in `3a5ae50`:

| Finding | Disposition |
|---|---|
| B1 Blocker: the Claude guard's control never reached the predicate, so a blinded predicate passed | Both guards mutate one field of one statement and require the same predicate to name it |
| S1 The same stale facts still stated as current in Codex disposition, README and two `@io` comments | Corrected |
| S2 Stale counts in the Claude guide | Corrected from the suite logs |
| S3 Claude helper comments claimed a ledger shape shared with Codex | Reworded; the reviewer then ran each helper against the other's ledger and both refuse |
| N2 Guards covered three carriers, and a stale runtime heading stayed green | Eight carriers per package; wire read from the helper; limit stated in the guides |
| N3, N4, N5 Comment, contract details, smoke-spec path and count | Corrected |

Round 2 on `3a5ae50`, APPROVED with two low findings, F1 a stale manifest label and F2 stale smoke-spec counts, applied in `985795b` with the note N-d. The pin reason's two checks were still pending when `fbf0fd0` was committed; this review and the 548 passed on the later commits make both true. Two notes are left: N-a, controls read only literal `{field}` placeholders and no stamp uses a conversion; and N-c, listed under findings for the Codex owner.

Round 3 on `a47bf6a`, a narrow check of these corrections and of this record's figures, line references and links against their logs. It confirmed the suite, adapter, map, scope, AST and count claims and that the guard names the F1 label. Its five low wording remarks are applied in the closing record commit without a further round.

## Known failures and unsupported routes

- **DSH on this branch alone.** Its package suite fails 83 tests, each on `neutral version mismatch`, and this branch does not change it. Draft PR 21 on branch `dsh/continuation`, by a separate agent from the same base `a3ecb5c`, carries DSH 5.0.0 and changes no path this branch changes. Earlier versions of this record said no DSH agent had started, because the remote had not been read. The root suite on this branch says nothing about DSH.
- **No continuation here.** The helper has no continuation operation, historical import, Debug extension above 4 or dispatch reservation record. An owner-approved successor is a fresh `init` from Bootstrap, and its accounting is unenforced: the helper holds only the cap, the root's count lives outside the ledger, and no suite or native run exercises this route, only the reviewer's fixtures. This matters only if a Claude successor is relied on.
- **Runs do not cross an upgrade.** A run bound to an earlier package refuses after any in-place update. A read-only scan of the owner's development directory found 20 RUNNING Claude ledgers, and all 20 already refuse under the current main helper, so 3.1.0 strands none of them newly. This is the established effect of each earlier in-place release, not a new one.
- **Not run:** a native Workflow run or a whole feature-dev flow under 3.1.0, `bin/conform self` for lack of the private deny list, and the suites under Python 3.9 or 3.15, where only the CLI probe and hook ran. PM-INVOKE's live probe stays open.

## Findings for other owners

- **DSH owner.** The cause of the stale Codex stamps, free-text identity outside any check, was present in both packages checked here, in Claude only partly. DSH's stamps were not inspected for this; they should be measured and given the same guard.
- **Codex owner.** `references/source-disposition.md` counts seven helpers but has no row for `continuation.py`, a gap from the Codex candidate. `examples/smoke-spec.md` lists the lineages path among its generated effects but not `.methodology/admissions/<digest>.json`, which `init` also writes under the same excluded `.methodology` tree.
- **Codex owner, wording.** The Codex carriers narrow the same norms that were corrected here: PLAN-405 to missing authority, TST-1003 without timeout and partial or mismatched results, and PM's PREFLIGHT-204 trigger.
- **Neutral, later release.** The transfer note says: "Do not port a Codex historical ledger into another engine without its own measured approved bridge". No neutral owner carries this. As a process rule it belongs in `flow/run-state.md` so DSH is bound too. It was left out of the Claude carriers, which state only what the helper accepts.
- **Neutral, later release.** STATE-301 and STATE-303 do not list a repair made by a successor's Code in the counted Debug unit. This package counts it as its conservative reading of STATE-702 and STATE-305, following the Codex specification. `flow/run-state.md` should decide this for every package.
- **Neutral, later release.** Every in-place release strands in-flight runs by design. Whether that is intended for the supported profile is an open question for the owner, not a defect fixed here.

## Remaining decisions

1. Owner's concrete-result decision on this candidate and on the Codex candidate beneath it: merging this branch also merges Codex 5.0.
2. Merge order with PR 21: this branch first, because PR 21 alone raises the neutral release under Claude 3.0.0 and blocks every Claude session. The root `README.md` line naming DSH 4.0.0 then needs its DSH 5.0.0 value, because neither branch can state the combined result alone.
3. Exact combined common/sibling/native validation.
4. Only after those: main merge, push and installed updates, each by its own grant. Because the plugin loads in place from main, Claude 3.1.0 must enter main together with neutral 4.1.0, never apart from it.
5. Whether to port continuation to Claude at all. The motivating Jeni ledger is Codex's, so this port would not serve it.

Private evidence is under ignored `.methodology/continuations/cont-bound-claude-compat/evidence/` in this worktree: suite logs, conform and Doxygen streams, probe scripts and reports, the native stream, the `main` baseline run, the reviewers' original transcripts and, under `stamps/`, the failing guard run and the closing runs of the stamp correction. Preserve it before archiving the worktree. It is not tracked or a release artifact.
