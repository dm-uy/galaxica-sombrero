# CONT-BOUND Claude ordinary compatibility — checked locally

Status: Claude 3.1.0 candidate on branch `claude/cont-bound-compat`, based on the Codex candidate `a3ecb5c`. Source commits `5e68c96`, `de6b91b`, `eba2905` and `e5d292d`; recover the closing record commit from the branch. Owner result is pending. Main, installed plugins and every sibling package are unchanged. This is the return the [transfer briefs](bounded-continuation-transfer-briefs.md) require from the Claude agent's first bounded packet.

## Authority and scope

Owner, 2026-11-04: «надо доработать наш плагин с методологией», pointing at the transfer briefs, then, asked to choose the scope: «Сначала совместимость». This covers ordinary compatibility of the Claude package with neutral 4.1.0. Porting continuation stays a separate later decision. Merge, push and installation are not granted. The work followed a lighter procedure as an additive release with one independent reviewer, not a feature-dev run, so no run ledger or role envelopes exist for it.

The owner was told before starting that the base defect in `tests/test_recon_decision_checkpoint.py` would be fixed here unless they objected. That file is outside the Codex specification's MAY EDIT list, which governed that task. Only its module contract changed. The Claude selectors in `tests/test_claude_package.py` and `tests/test_c1_review_and_routing.py` are conditional in that specification on an accepted receipt for the exact source, so they can reach main only with the owner's acceptance.

## Identities

| Domain | Value |
|---|---|
| Neutral | 4.1.0, unchanged by this work |
| Claude package | 3.0.0 → 3.1.0: MINOR, as FMT-24 and the precedent of 3.1.0/2.2.0 and 3.2.0/2.3.0 give for additive neutral releases |
| Run-state contract and schema | `methodology-claude/1.0.0`, schema 2, unchanged |
| Default Debug cap | 4, zero valid, unchanged |
| Codex and DSH | Codex 5.0.0 and DSH 4.0.0, zero bytes changed |

## Touched paths

- Release constants: `implementations/claude/.claude-plugin/plugin.json`, `adapter.json`, `references/package-layout.json`, `hooks/session_start.py`, `skills/feature-dev/scripts/run_state.py`.
- Version stamps in text: `implementations/claude/README.md`, `references/consumer-pm-profile.md`, `references/source-disposition.md`, `references/handoffs.md`, `skills/semantic-exoskeleton/SKILL.md`.
- The four duties and the helper's limits: `skills/pm/SKILL.md`, `skills/devplan-protocol/SKILL.md`, `skills/feature-dev/SKILL.md`, `references/claude-runtime.md`, `references/adoption.md`.
- Package tests: `tests/test_package_contract.py` gains two tests and corrected module facts; `test_session_start.py`, `test_run_state.py` and `test_consumer_profile.py` change identity selectors only; `tests/test_guide.md` gains a section.
- Shared root: `tests/test_claude_package.py` and `tests/test_c1_review_and_routing.py` change Claude selectors only; `tests/test_recon_decision_checkpoint.py` gets a complete module contract; `tests/test_guide.md`, `README.md` and `CHANGELOG.md` report the release.

## What did not change

Between `a3ecb5c` and `e5d292d` there is no delta in `implementations/claude/workflows`, `agents`, `hooks/guard_destructive.py`, `hooks/hooks.json`, `implementations/codex`, `implementations/dsh`, the neutral `checks`, `protocols`, `code`, `process`, `flow`, `roles` or `SPEC_VERSION`. The executable lines changed in the helper are exactly its three release constants, and in the hook its one. The frozen Claude helper and hook AST pins in `tests/test_c1_review_and_routing.py` pass with their values unchanged.

`workflows/feature-dev.js` needs no change for ordinary operation: it holds no package or neutral release literal, and its harness scenarios, which drive the real helper with scripted agents, pass.

## Evidence on `e5d292d`

The table is from a Git-free `git archive` of that commit with Python 3.12, exposed streams, no skips. The helper CLI probe, boundary refusals, hook runs and live session below ran on `eba2905`; the only source difference since is one runtime paragraph and one test.

| Check | Result |
|---|---|
| Claude package suite | 547 passed |
| Root suite | 616 passed |
| Codex package suite | 200 passed |
| DSH package suite | 83 failed, 63 passed; held, see below |
| `bin/conform adapter` | Claude and Codex pass 76, fail 0; DSH pass 75, warn 1 (adapter targets 4.0.0), fail 0 |
| `doxygen Doxyfile`, root and Claude | exit 0, empty stdout and stderr |

**Why replacing the version alone was not enough.** On a scratch copy of `a3ecb5c`, replacing `4.0.0` with `4.1.0` throughout the Claude package, including its tests and stamps, took the package suite from 167 failed to 545 passed and bound the hook, with none of the four duties carried. The suite could not see them. `test_additive_duties_reach_their_carriers` now catches removal of each listed statement or a change inside it, across 43 controls. It is a finite recognizer, not a prose solver. The root AST guard, already red at the adapter version, then refused at `wrong release comparison`, which is why its selectors moved and its pins did not.

**Real helper CLI.** An owned inert probe drove the full ordinary route through the shipped CLI under Python 3.15.0, 3.12.13 and 3.9.6: Bootstrap → Architect → Code → QA → Review → Finalize, then SUCCESS at spend 0 of cap 4, bound to neutral 4.1.0, schema 2. A malformed record exits 2 with progress and counters unchanged. Records are structural fixtures, not role acceptance.

**Real boundary refusals.** `capabilities`, `continue`, `reserve`, `released`, `recover` and `episode` exit 2 with empty stdout. `--max-debug 5` exits 2. A real Codex 5.0 schema 3 ledger is refused unchanged. A real Codex 4.0 schema 2 ledger is refused, but a refused `record` appends its diagnostic to that file, as for any shape-valid schema 2 ledger.

**Live native session.** A fresh Claude Code 2.1.285 session started with `--setting-sources project,local`, `--plugin-dir` on the candidate and Sonnet as root; the exact command is retained in the evidence home. Its init event lists the candidate path and all six `methodology-claude:` roles. The SessionStart hook exits 0 with `methodology-claude 3.1.0 bound in place to neutral methodology 4.1.0`. The session loaded the `feature-dev` skill from the candidate, ran `init` and `show` through the default `python3` with neutral 4.1.0 bound, and dispatched `methodology-claude:searcher` on Haiku, which returned its inventory line. This shows loading and dispatch, not model obedience or efficacy.

**Base defect.** `tests/test_code_layer.py::test_every_python_module_has_the_exoskeleton_before_imports` fails on `main` at `388c944` too, with seven diagnostics in that one file: main's root suite is red today, independently of this work. It passes here with no test logic changed.

**Retained run mistake.** The first parallel root, Codex, DSH and conform run lost its working directory and copied `main` instead of the candidate. Its `spec-version=4.0.0` and 146 Codex tests exposed this; it was discarded as candidate evidence and kept as the `main` baseline: root 613 passed and 1 failed, Codex 146, DSH 146. `main` itself was only read. The first version of this record also failed the publication scan through a home-relative path, 40 root failures on `scan.home-relative` and its dependents; the check was right and the text was corrected.

## Independent review

Reviewer: `methodology-claude:reviewer` on Opus 5.5, read-only with one scratch write root; no write outside it in any round. Both rounds found no blocker and independently confirmed the functional compatibility and all protections, including a structural AST diff, identical pin digests and file mutations that fail the pins. The originals are in the private evidence home.

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
| N6 Stale Codex stamps | Outside this scope; see below |

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

## Known failures and unsupported routes

- **DSH blocks shared integration.** Its package suite fails 83 tests, each on `neutral version mismatch`. Its own agent owns this. The root suite stays green regardless and says nothing about DSH.
- **No continuation here.** The helper has no continuation operation, historical import, Debug extension above 4 or dispatch reservation record. An owner-approved successor is a fresh `init` from Bootstrap, and its accounting is unenforced: the helper holds only the cap, the root's count lives outside the ledger, and no suite or native run exercises this route, only the reviewer's fixtures. This matters only if a Claude successor is relied on.
- **Runs do not cross an upgrade.** A run bound to an earlier package refuses after any in-place update. A read-only scan of the owner's development directory found 20 RUNNING Claude ledgers, and all 20 already refuse under the current main helper, so 3.1.0 strands none of them newly. This is the established effect of each earlier in-place release, not a new one.
- **Not run:** a native Workflow run or a whole feature-dev flow under 3.1.0, `bin/conform self` for lack of the private deny list, and the suites under Python 3.9 or 3.15, where only the CLI probe and hook ran. PM-INVOKE's live probe stays open.

## Findings for other owners

- **Codex owner, before integration.** `implementations/codex/skills/semantic-exoskeleton/SKILL.md:8-9` still stamps 4.0.0 and `methodology-codex4.0.0`. `implementations/codex/references/consumer-pm-profile.md:3` still says package 4.0.0 over neutral 4.0.0, is pinned by `tests/test_claude_consumer_bridge.py:70`, and is where the Claude carrier sends readers. Not changed here because one writer owns each path and the owner assigned Codex separately.
- **Codex owner, wording.** The Codex carriers narrow the same norms that were corrected here: PLAN-405 to missing authority, TST-1003 without timeout and partial or mismatched results, and PM's PREFLIGHT-204 trigger.
- **Neutral, later release.** The transfer note says: "Do not port a Codex historical ledger into another engine without its own measured approved bridge". No neutral owner carries this. As a process rule it belongs in `flow/run-state.md` so DSH is bound too. It was left out of the Claude carriers, which state only what the helper accepts.
- **Neutral, later release.** STATE-301 and STATE-303 do not list a repair made by a successor's Code in the counted Debug unit. This package counts it as its conservative reading of STATE-702 and STATE-305, following the Codex specification. `flow/run-state.md` should decide this for every package.
- **Neutral, later release.** Every in-place release strands in-flight runs by design. Whether that is intended for the supported profile is an open question for the owner, not a defect fixed here.

## Remaining decisions

1. Owner's concrete-result decision on this candidate and on the Codex candidate beneath it: merging this branch also merges Codex 5.0.
2. A separately assigned DSH agent for its first bounded packet.
3. The Codex stamps above, then exact combined common/sibling/native validation.
4. Only after those: main merge, push and installed updates, each by its own grant. Because the plugin loads in place from main, Claude 3.1.0 must enter main together with neutral 4.1.0, never apart from it.
5. Whether to port continuation to Claude at all. The motivating Jeni ledger is Codex's, so this port would not serve it.

Private evidence is under ignored `.methodology/continuations/cont-bound-claude-compat/evidence/` in this worktree: suite logs, conform and Doxygen streams, probe scripts and reports, the native stream, the `main` baseline run and the reviewer's original transcript. Preserve it before archiving the worktree. It is not tracked or a release artifact.
