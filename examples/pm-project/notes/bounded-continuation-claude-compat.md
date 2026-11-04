# CONT-BOUND Claude ordinary compatibility — checked locally

Status: Claude 3.1.0 candidate on branch `claude/cont-bound-compat`, based on the Codex candidate `a3ecb5c`. Source commits `5e68c96` and `de6b91b`; recover the closing record commit from the branch. Owner result is pending. Main, installed plugins and every sibling package are unchanged. This is the return the [transfer briefs](bounded-continuation-transfer-briefs.md) require from the Claude agent's first bounded packet.

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

Between `a3ecb5c` and `de6b91b` there is no delta in `implementations/claude/workflows`, `agents`, `hooks/guard_destructive.py`, `hooks/hooks.json`, `implementations/codex`, `implementations/dsh`, the neutral `checks`, `protocols`, `code`, `process`, `flow`, `roles` or `SPEC_VERSION`. The executable lines changed in the helper are exactly its three release constants, and in the hook its one. The frozen Claude helper and hook AST pins in `tests/test_c1_review_and_routing.py` pass with their values unchanged.

`workflows/feature-dev.js` needs no change for ordinary operation: it holds no version literal, and its real-helper harness scenarios pass.

## Evidence on `de6b91b`

All from a Git-free `git archive` of that commit with Python 3.12, exposed streams, no skips.

| Check | Result |
|---|---|
| Claude package suite | 547 passed |
| Root suite | 616 passed |
| Codex package suite | 200 passed |
| DSH package suite | 83 failed, 63 passed; held, see below |
| `bin/conform adapter` | Claude and Codex pass 76, fail 0; DSH pass 75, warn 1 (adapter targets 4.0.0), fail 0 |
| `doxygen Doxyfile`, root and Claude | exit 0, empty stdout and stderr |

**Why replacing the version alone was not enough.** On a scratch copy, swapping only the neutral literal took the Claude suite from 167 failed back to 545 passed and bound the hook, with none of the four duties carried. The suite could not see them. `test_additive_duties_reach_their_carriers` now catches removal or inversion of each listed statement, across 35 controls. It is a finite recognizer, not a prose solver. That swap also broke the root AST guard, which is why only its selectors moved and its pins did not.

**Real helper CLI.** An owned inert probe drove the full ordinary route through the shipped CLI under Python 3.15.0, 3.12.13 and 3.9.6: Bootstrap → Architect → Code → QA → Review → Finalize, then SUCCESS at spend 0 of cap 4, bound to neutral 4.1.0, schema 2. A malformed record exits 2 with progress and counters unchanged. Records are structural fixtures, not role acceptance.

**Real boundary refusals.** `capabilities`, `continue`, `reserve`, `released`, `recover` and `episode` exit 2 with empty stdout. `--max-debug 5` exits 2. A real Codex 5.0 schema 3 ledger is refused unchanged. A real Codex 4.0 schema 2 ledger is refused, but a refused `record` appends its diagnostic to that file, as for any shape-valid schema 2 ledger.

**Live native session.** A fresh Claude Code 2.1.285 session with user settings excluded, `--plugin-dir` on the candidate and Sonnet as root. Its init event lists the candidate path and all six `methodology-claude:` roles. The SessionStart hook exits 0 with `methodology-claude 3.1.0 bound in place to neutral methodology 4.1.0`. The session loaded the `feature-dev` skill from the candidate, ran `init` and `show` through the default `python3` with neutral 4.1.0 bound, and dispatched `methodology-claude:searcher` on Haiku, which returned its inventory line. This shows loading and dispatch, not model obedience or efficacy.

**Base defect.** `tests/test_code_layer.py::test_every_python_module_has_the_exoskeleton_before_imports` fails on `main` at `388c944` too, with seven diagnostics in that one file: main's root suite is red today, independently of this work. It passes here with no test logic changed.

**Retained run mistake.** The first parallel root, Codex, DSH and conform run lost its working directory and copied `main` instead of the candidate. Its `spec-version=4.0.0` and 146 Codex tests exposed this; it was discarded as candidate evidence and kept as the `main` baseline: root 613 passed and 1 failed, Codex 146, DSH 146. `main` itself was only read. The first version of this record also failed the publication scan through a home-relative path, 40 root failures on `scan.home-relative` and its dependents; the check was right and the text was corrected.

## Independent review

Reviewer: `methodology-claude:reviewer` on Opus 5.5, read-only with one scratch write root; no write outside it. Verdict on `5e68c96`: CHANGES REQUESTED, with no blocker. It independently confirmed the functional compatibility and all protections, including a structural AST diff, identical pin digests and file mutations that fail the pins.

| Finding | Disposition in `de6b91b` |
|---|---|
| S1 Wrong refusal reason for a run bound to an earlier package | Confirmed by a separate reproduction; guide and runtime corrected |
| S2 Carriers denied continuation while the package and STATE-702 offer an owner-approved one | Fixed: the runtime states what the helper lacks and what a successor can be |
| S3 No result note, stale records, no measured values | This note, the guide and the current records |
| S4 Workflow check did not discriminate | Exact usage line, ceiling and argument list |
| S5 Carrier test checked presence only | Inversion controls added, recognizer limit stated |
| S6 Inaccurate facts in the completed contract | `@links` and `@usecases` corrected |
| N1–N5 Module facts, harness wording, narrowed norms, restated norm, carrier column | Fixed in this package |
| N6 Stale Codex stamps | Outside this scope; see below |

The original report and its transcript are in the private evidence home. Return of the corrections to the same reviewer is pending at this checkpoint.

## Known failures and unsupported routes

- **DSH blocks shared integration.** Its package suite fails 83 tests, each on `neutral version mismatch`. Its own agent owns this. The root suite stays green regardless and says nothing about DSH.
- **No continuation here.** The helper has no continuation operation, historical import, Debug extension above 4 or dispatch reservation record. An owner-approved successor is a fresh `init` from Bootstrap, and the root must lower the cap and count a repair made by its Code.
- **Runs do not cross an upgrade.** A run bound to an earlier package refuses after any in-place update. A read-only scan of the owner's development directory found 20 RUNNING Claude ledgers, and all 20 already refuse under the current main helper, so 3.1.0 strands none of them newly. This is the established effect of each earlier in-place release, not a new one.
- **Not run:** a native Workflow run or a whole feature-dev flow under 3.1.0, `bin/conform self` for lack of the private deny list, and the suites under Python 3.9 or 3.15, where only the CLI probe and hook ran. PM-INVOKE's live probe stays open.

## Findings for other owners

- **Codex owner, before integration.** `implementations/codex/skills/semantic-exoskeleton/SKILL.md:8-9` still stamps 4.0.0 and `methodology-codex4.0.0`. `implementations/codex/references/consumer-pm-profile.md:3` still says package 4.0.0 over neutral 4.0.0, is pinned by `tests/test_claude_consumer_bridge.py:70`, and is where the Claude carrier sends readers. Not changed here because one writer owns each path and the owner assigned Codex separately.
- **Codex owner, wording.** The Codex carriers narrow the same norms that were corrected here: PLAN-405 to missing authority, TST-1003 without timeout and partial or mismatched results, and PM's PREFLIGHT-204 trigger.
- **Neutral, later release.** "No ledger crosses between engines" exists only in the transfer note and the Codex carriers. As a process rule it belongs in `flow/run-state.md` so DSH is bound too. It was left out of the Claude carriers, which state only the fact that the helper reads its own schema 2 ledgers.
- **Neutral, later release.** Every in-place release strands in-flight runs by design. Whether that is intended for the supported profile is an open question for the owner, not a defect fixed here.

## Remaining decisions

1. Owner's concrete-result decision on this candidate and on the Codex candidate beneath it.
2. A separately assigned DSH agent for its first bounded packet.
3. The Codex stamps above, then exact combined common/sibling/native validation.
4. Only after those: main merge, push and installed updates, each by its own grant. Because the plugin loads in place from main, Claude 3.1.0 must enter main together with neutral 4.1.0, never apart from it.
5. Whether to port continuation to Claude at all. Jeni does not need it, because a Codex ledger does not cross engines.

Private evidence is under ignored `.methodology/continuations/cont-bound-claude-compat/evidence/` in this worktree: suite logs, conform and Doxygen streams, probe scripts and reports, the native stream, the `main` baseline run and the reviewer's original transcript. Preserve it before archiving the worktree. It is not tracked or a release artifact.
