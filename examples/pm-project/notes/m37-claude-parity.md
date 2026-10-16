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

Consequential-open under BRAIN-104 (package/ownership boundary, shared CLI contract for consumer projects, oracles, long-term maintenance). Brief, persisted unranked HOLD and evaluation live in [m37-decision-c2-port](m37-decision-c2-port/). Pending evaluation and the owner's specification decision.
