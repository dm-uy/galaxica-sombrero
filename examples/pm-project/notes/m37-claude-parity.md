# M37 — Claude package actualization

## Authority and scope

On 2026-10-16 the owner asked (Claude Code desktop session, Russian): study the project, check how current the Claude implementation under `implementations/claude` is compared with the current Codex package and the neutral core, and bring it up to date where something is missing or diverges, so that the owner's Claude Code work can run on this framework instead of the in-house plugins.

After a read-only reconciliation the root asked one structured question (AskUserQuestion, 2026-10-16). The owner's selected answers, verbatim:

- Scope: «Правки + порт C2 (Recommended)» — fix the package defects now as a patch; port the Codex C2 consumer PM profile to Claude through reconnaissance → specification → owner approval → feature-dev.
- Plugin name: «Оставить имя (Recommended)» — keep `methodology-claude`; document the host's name warning and validate without `--strict`.
- M30 native Claude proof: «Снять в этой задаче (Recommended)» — the earlier deferral of M30 AC4/Claude AC5 is lifted; run the live proof in this task.
- Old in-house plugins: «После порта orient (Recommended)» — keep `product-methodology` and `prompting-methodology` enabled until the Claude package ships orient/codemap and the consumer projects are repointed; disabling them is the owner's own settings change on a later command.

A second structured answer, «Залогинился, запускай», confirmed that the owner signed in the standalone CLI for the live probe.

This grants the 2.0.2 patch, the C2 port reconnaissance/decision packet/specification and the live M30 Claude probe. It does not grant C2 Code (that follows the specification approval), main merge, push, release, installation changes, user-settings changes or edits in consumer projects. Work is isolated in worktree branch `claude/m37-claude-parity` from clean main `b8696a2` (= origin/main).

## Reconciliation findings

Two read-only lanes (Sonnet) compared the Claude package with the Codex package and with the in-house plugins; the root re-checked every finding it reports below against the files.

- Structural binding was current: both adapters passed 76/76, Claude package 526 and Codex package 146 tests passed on Python 3.9.
- The Claude package lacked the whole C2 consumer PM profile that Codex received in `bbd2696` (profile carrier, 13 seeds, `consumer_files`/`orient`/`codemap`/`markup_migrate`, routed lifecycle entries). `references/source-disposition.md` had declared these "outside — a later package increment", so this is a recorded deferral, not drift.
- Package defects (fixed in 2.0.2, below): stale `2.0.0` identity in `skills/semantic-exoskeleton/SKILL.md` and `references/handoffs.md`; `prompting`/`prompting-agent-design` still in the initial-release form without the one-shot/loop three-artifact route Codex received in `78d4190` (root test C1-AC3 read only Codex); analyzer and pm-review-run lacked the unsent continuation message of RUNREV-301; the four lifecycle entries read narrower neutral owner sets than Codex (DECISION-502/503 reservation and accepted-body immutability, LEARN-101, SP-103/104, SAFE-101 and the code-review owner were not triggered).
- Install claims were wrong for the current host: Claude Code 2.1.299 copies a plugin from a local directory marketplace into its plugin cache (isolated probe with a scratch `CLAUDE_CONFIG_DIR`; `installPath` under `cache/`; the binding hook then reports BLOCKED: SPEC_VERSION and the six core owners missing). `claude plugin validate --strict` fails on 2.1.299 only because of the advisory that the name reads as one of Anthropic's own; plain `validate` passes with that warning.
- The in-house plugins remain enabled beside `methodology-claude` (`CLAUDE_CODE_PLUGIN_DIRS` loads the package in place): duplicate skill names, two SessionStart hooks and two Bash guards are active. Five consumer projects (consumer-A, consumer-B, consumer-C, consumer-D, consumer-E) depend on the old plugin's orient/codemap; `pm-ingest-candidates` and `run_review.py` stay deferred by the earlier decision and are outside this scope.
- Root regression on main: since `6580d05` (owner-approved M31 change to `flow/phases.md` and `roles/pm.md`) the root suite failed 66 tests: all 351 `flow/phases.md` read receipts in `examples/flow-contract/cases.json` kept the pre-M31 hash and `tests/test_pm_role.py` pinned the pre-M31 PM-103/PM-812 clauses. M31–M36 ran bounded document checks only. Bisect: `aaaa784` 176/176 pass, `6580d05` 66 fail.
- Interpreter limit: `tests/test_c1_review_and_routing.py::test_release_bridge_keeps_wire_and_helper_algorithms` passes on the declared test interpreter `/opt/homebrew/bin/python3.12` and fails on the system `/usr/bin/python3` 3.9.6 because its whole-AST pins were serialized under 3.12. The pins are protected (C2 BR-4); this is recorded, not changed.

## Patch 2.0.2

Claude package 2.0.1 → 2.0.2 over unchanged neutral 3.0.1; membership 59, six roles, wire and schema unchanged. Changes:

- Version identity in the plugin manifest, layout, README, hook and run-state constants, adoption/runtime titles, devplan-protocol, semantic-exoskeleton and handoffs, with the matching package and root test expectations.
- `prompting` routes another agent's system prompt, one-shot or loop, to the full prompting-agent-design entry; `prompting-agent-design` delivers the three AGENTPROMPT-103 artifacts in both modes, applies loop mechanics only to loops and keeps adversarial inputs and a synthetic-secret probe separate and DRAFT/NOT_RUN (AGENTPROMPT-105). The root route test now also checks the Claude carriers.
- analyzer and pm-review-run return an unsent owner-ready continuation message.
- pm-handoff (+batch, decisions, learning), pm-plan-batch (+decisions, specification), pm-run-batch (+code-review, safety) and pm-bootstrap (+session, safety, gates) read the same neutral owner sets as Codex, with short duty sentences for decision provenance/immutability/reservation, lightweight error notes, M-task specification paths, held tasks, consequential archive/cleanup/commit effects and mapped moves.
- README, runtime, adoption, adapter `packaging-install` and the test guide: in-place loading only; any marketplace install (git or local directory) copies the plugin and is unsupported; validate without `--strict`, where the name warning is expected.
- Root oracle repairs for the M31 regression: 351 phases receipt hashes refreshed to the current owner; PM-103/PM-812 required clauses updated to the current text; `tests/test_f2_interfaces.py` generalizes the M30 Architect receipt normalization to a `RECEIPT_REFRESH` table (Architect 51, phases 351) under the unchanged original whole-fixture pin, with wrong/missing/duplicate/case-byte controls still refused.

## Checks on the patch

Final run on the complete branch candidate (records included), `PYTHONDONTWRITEBYTECODE=1`, owned basetemps, after the independent review findings were addressed:

- Root suite 600 passed, Claude package 526 passed, Codex package 146 passed, all on `/opt/homebrew/bin/python3.12`. On the system Python 3.9.6 the root suite gives 599 passed and 1 failed (the interpreter-bound AST pin above), as on main before M37.
- `bin/conform adapter` for Claude and Codex: 76 pass each. `bin/conform self` with a task-local public-hygiene deny list (9 tokens covering owner-local paths, organization and consumer project names; not the original private lists): 24 pass, after redacting home-relative paths it first caught in two public decision copies.
- `claude plugin validate implementations/claude` (Claude Code 2.1.299): passed with only the expected name warning. Package `doxygen Doxyfile` silent. `git diff --check` clean. `implementations/codex/` byte-identical to `b8696a2`.
- Independent read-only review (Sonnet, separate actor): 0 HIGH, 2 MED, 11 LOW/INFO. Both MED fixed (pm-run-batch cleanup now states BATCH-108 instead of an unsupported `git branch -d` rule; adoption `via` row for agent-prompt-design updated); LOW items fixed except F13 (oracle pins the first sentence of each PM norm, accepted as sufficient).

## M30 native Claude proof (AC4 / Claude AC5)

The owner lifted the M30 deferral for this task. The standalone `/opt/homebrew/bin/claude` (Claude Code 2.1.285) first returned `Failed to authenticate: OAuth session expired`; passing the desktop host's session environment was not attempted. After the owner signed in (`claude auth status`: logged in, claude.ai), three fresh headless sessions ran in parallel on 2026-10-16 against a complete Git-free copy of this 2.0.2 candidate (tree identity `ac97fcbb…741f`, unchanged after the runs), each in its own fictional Lumen Notes project with AGENTS/VISION/ROADMAP/TASKS/HANDOFF and an owner grant that delegates in-checkpoint choices to the PM root.

Command (from the M30 specification, cwd = the case, prompt on stdin, `env -i` with only HOME/USER/PATH/LANG): `claude --print --restricted --strict-mcp-config --setting-sources '' --no-session-persistence --permission-mode dontAsk --tools Read,Glob,Grep,Agent,Skill,Write,Edit --allowedTools Read Glob Grep Agent Skill 'Write(./**)' 'Edit(./**)' --plugin-dir FRAMEWORK/implementations/claude --add-dir FRAMEWORK --output-format stream-json --verbose`. Declared deviation from the specified tool list: `Write`/`Edit` confined to the case directory and `Skill` were added, because BRAIN-107 requires the root to persist the HOLD and the package entries are skills. The init event of every run reported `methodology-claude` 2.0.2 `@inline` from the candidate copy, model `claude-opus-5-5`, no other non-builtin plugin.

| Case | Prompt (no brainstorm instruction) | Observed | Turns / cost / time |
|---|---|---|---|
| Important (AC4) | Start M2 offline editing and sync: decide how clients store notes offline and reconcile conflicts, record the choice, create M2 tasks; no code. | Root read the runtime, orient, core owners, `methodology-claude:pm`, PM/lifecycle/batch/session/gates owners, `prompting/brainstorm.md` and `process/decisions.md`; dispatched two `general-purpose` opus generators in parallel with the same brief and predeclared criteria (byte-identical except the label prefix A/B, no peer output); wrote both originals, the brief and `hold.md` to `notes/m2-sync/`; only then dispatched a distinct opus evaluator that read the four saved files; wrote `evaluation.md`, an accepted DEC with `decided` naming the actual delegation channel and links to the packet, M2 tasks in TASKS, ROADMAP and HANDOFF. | 11 / $2.57 / 273 s |
| Trivial (Claude AC5) | Fix the typo «sychronization» in VISION.md. | Grep, Read, one Edit; no Agent or Skill. | 4 / $0.13 / 12 s |
| Settled (Claude AC5) | Add a `conflicts` field to the `POST /sync` response in the M2 spec. | Read the spec, entry, records and accepted DEC-001; no Agent or Skill; DEC-001 unchanged; only `specs/m2-sync.md` changed. It disclosed that under DEC-001 the literal field would always be empty, added the minimal request fields `device_id`/`base_ts` and offered a no-new-field alternative. | 9 / $0.26 / 57 s |

Assessment: AC4 and the Claude half of AC5 are supported as bounded observations on fictional data — one fresh run per case, all actors from one model family, no statistical independence or hard isolation claimed. Observations: the root used a no-op Haiku agent ("placeholder wait") to wait for its background generators (small, harmless cost); the settled control's added request fields stay a disclosed draft change for its owner. Raw streams, prompts, case trees before/after and their SHA-256 (`run-important.jsonl` `a8a638f4…77f5`, `run-trivial.jsonl` `7545bb58…5315`, `run-settled.jsonl` `dd431f53…7c3c`) are kept in the owner's private evidence directory, because they contain owner-local paths. M30 full checkpoint acceptance still needs the renewed independent QA, whole Review and assigned Finalize that ROADMAP names; this note does not claim them.

## C2 port decision packet

Consequential-open under BRAIN-104 (package/ownership boundary, shared CLI contract for consumer projects, oracles, long-term maintenance). Brief, persisted unranked HOLD and evaluation live in [m37-decision-c2-port](m37-decision-c2-port/). Two fresh generators proposed 11 alternatives; a distinct evaluator recommended H (reference the Codex C2 helpers in place, launchers, tripwire) with M1 (byte mirror) as runner-up. The owner approved the [C2-port specification](../specs/m37-claude-consumer-profile.md) on 2026-10-16 («Да, утверждаем H.»), which collapsed the packet to H.

## C2 port — feature-dev run m37-c2-20261016

Interactive root (this Claude Code session) with methodology-claude role agents, framework = an immutable snapshot of main `b8696a2`, run state schema 2 in the untracked local evidence home. Models: searcher haiku; architect, reviewer and finalizer opus; coder, QA and debugger sonnet.

- Bootstrap (one response correction: unknown `map` field) and Architect (one response correction: `mayEdit` not exact paths, stale candidate identity; the helper refused to record that architect-phase control event because the written plan had already changed the candidate — a helper limitation, retained in the evidence). Plan: [m37-claude-consumer-profile](../plans/m37-claude-consumer-profile.md), visual gate PASS (61 nodes).
- Code SUCCESS after one transport failure (API unreachable); the owner answered «Try again», the root verified the effects (all inside scope, Codex untouched, nothing recorded) and resumed the same coder.
- Root AC5 live probes (headless Claude Code 2.1.285, `--restricted`, Bash limited to the launchers): pre-Debug run 1 failed N7/E4 because a generic dontAsk denial of a chained command ended Bash use; the rerun with an appended environment note passed. After Debug, attempt 1 failed N7/E4 because the probe allowed only bare launcher names while the fixed carrier calls the absolute path; attempt 2 (absolute-path rules for the same launchers) passed N1, N2, N4–N9 and E1–E5; N3 is only indirectly evidenced (stream-json does not echo the prompt).
- QA SUCCESS (8 scans), then Review BUG_REPORT with three defects: bare launcher names can be shadowed by another enabled plugin's `bin/` (MEDIUM); launchers crashed with exit 1 on a closed stdout/stderr (LOW); the carrier said a fixture grant never authenticates consent, contradicting the Codex probe route (LOW). Debug 1 of 4 fixed all three with discriminating regression tests; renewed QA and renewed Review were SUCCESS.
- Finalize (separately assigned Architect) verified everything green and returned BLOCKED on one owner decision: AC5's literal "bare `orient --check`" versus the absolute-path launcher call that the Debug 1 rule requires. Run terminal: BLOCKED, Debug spent 1/4.

Final candidate `9cb1e6e3e8d8465d1e3c3a32733b6d88ea8c4028fd8c61894c2c205a16e62092`: Claude 2.1.0, 64 members; `bin/orient`, `bin/codemap`, `bin/markup-migrate` launchers that execute the Codex C2 scripts of the same checkout with `-B`, unchanged arguments, streams and exit status, or answer one BLOCKED line with exit 2; the by-reference carrier `implementations/claude/references/consumer-pm-profile.md`; routing in nine skills and the searcher; the root tripwire pinning 18 Codex files. Measured on Python 3.12: root 603, Claude 545, Codex 146 passed; launcher tests 19/19 on 3.9 and 3.12; three adapters, `conform self`, `plugin validate` and silent Doxygen maps pass; `implementations/codex` byte-identical to `b8696a2`.

### Owner result decisions (AskUserQuestion, 2026-10-16, verbatim)

- AC5: «Принять (Recommended)» — the absolute-path launcher call counts as meeting AC5; the probe deviations are accepted as recorded; the result is accepted with the named limits below.
- Integration: «Push + PR, слияние после вас (Recommended)» — push the branch and open a PR to main; the owner merges after review.
- Ignore rule: «Да (Recommended)» — add `.methodology/` to `.gitignore` in the same PR.

### Post-run documentation corrections (not part of the judged candidate)

After the run the root made documentation-only corrections: the stale package counts in `implementations/claude/examples/smoke-spec.md`; historical "Current" wording and the oracle path count in root `tests/test_guide.md`; the AC5 and validate pointers in the package test guide; `.methodology/` in `.gitignore`; public copies of the plan and decision packet with the run's worktree and probe paths replaced by placeholders (originals kept privately with their hashes); the current maintainer records.

### Limits and follow-ups

- While the in-house `product-methodology` plugin stays enabled, bare `codemap` and `markup-migrate` in consumer projects may resolve to either plugin's `bin/` (the old plugin ran `orient` from its `scripts/` and its SessionStart hook, not from `bin/`); PATH order between plugins was never measured. Address this in the per-project migrations or by disabling the in-house plugin.
- C2 `orient` accepts only `methodology-consumer-pm/1.0.0`; the five consumer projects need their own owner-granted migrations before the in-house plugins are disabled.
- Non-blocking Review observations: a BLOCKED refusal exits 120 instead of 2 when stderr is a broken pipe; `_emit`'s open-stream path writes no own trace event; the launchers' `@purpose` still says "by bare name".
- The run-state helper cannot record an architect-phase response correction after the plan was written, and has no continuation mechanism for a terminal run; both are retained as package observations.
- Raw evidence (run state, role returns, live-probe streams, about 1 GB) is kept in the owner's private evidence directory, not in this public repository.
- Test-environment trap found at the final check: `test_package_contract.py::test_manifest_and_adapter`, several root tests and `bin/conform adapter`/`self` (whose skip list omits `.methodology`) count every `*.md` in the working tree as neutral population, including the ignored local `.methodology/` evidence home once it holds a Markdown report; with such a file present they fail although the candidate is unchanged. Run the suites on a clean export (as QA and Finalize did) until the walk honours the ignore rule.

## In-house plugin retirement (2026-10-19)

After the M37 and M38 merges the owner asked, in Russian: «Давай придушим вот эти вот старые плагины, потому что, по идее, в новом все уже есть, и надо работать в рамках него.» The owner then asked for this record: "Record the disabling of the in-house plugins in HANDOFF, TASKS and the M37 record, open a PR and merge it."

What changed:

- `product-methodology` and `prompting-methodology` are disabled at user scope with `claude plugin disable --scope user`. Their `enabledPlugins` entries are now false; no other user setting changed, and `CLAUDE_CODE_PLUGIN_DIRS` still loads methodology-claude in place.
- Both plugins stay installed in the plugin cache. Rollback is `claude plugin enable --scope user <plugin>@<owner marketplace>`.
- A scan of project settings in the owner's projects folder (four levels deep) found none that re-enable either plugin.
- This happened before the consumer migrations, which the owner chose to accept. For new sessions it supersedes the first limit above, by inference, and the ordering condition of the second; C2 `orient` still accepts only `methodology-consumer-pm/1.0.0`.

Verification: a fresh headless session (Claude Code 2.1.285, `-p` with stream-json output) started in the canonical checkout. Its init event listed:

- methodology-claude, loaded in place, and three built-in plugins;
- the six methodology-claude roles, and no agent from either old plugin;
- 29 methodology-claude skill and command entries, and none from the old plugins;
- one SessionStart hook response, reporting methodology-claude 2.1.0 bound to neutral 3.0.1.

The model call in that session failed on the headless CLI's expired login. That failure does not affect the init listing. Sessions started before the disable keep the old plugins until they restart; whether a plugin reload also applies the change was not measured.

What has no direct replacement:

- `pm-ingest-candidates` (skill) and `run_review.py` (script) are absent from methodology-claude. Both stayed deferred by the earlier decision. Owner-level instructions that cite `run_review.py` now name a disabled tool.
- The old prompting commands (`agent-prompt`, `brainstorm`, `contract`, `design`, `verify-fact`), the `agent-prompt` and `methodology` skills, and the `architect-agent`/`brainstorm-agent` agents map onto methodology-claude's `brainstorm`, `prompting`, `prompting-agent-design`, `prompting-decompose`, `prompting-markup` and `prompting-verify` skills and its roles. The names differ, and no one-to-one parity was measured.
- The old plugin's hooks are gone. Its PreToolUse `guard_destructive.py` has an adapted twin in methodology-claude. Its SessionStart `orient.py` injection, which ran in every project, has no equivalent for unmigrated consumers. methodology-claude's own SessionStart hook reports the package binding and which project records exist, and leaves orientation to the `orient` check.
- The old `bin/` held `codemap` and `markup-migrate`. New sessions now get those names, plus `orient`, only from methodology-claude. This is inferred from the init listing; no Bash call measured it.

Consumer impact until each consumer migrates:

- The five consumer projects keep their pre-C2 profile and their CLAUDE.md lines that claim plugin injection.
- C2 `orient` accepts only `methodology-consumer-pm/1.0.0`, so expect it to refuse their current profile. This was not measured in those projects.
- Each migration (M37-T7) still needs its own grant.
