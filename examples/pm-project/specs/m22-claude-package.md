# M22 first native Claude Code package specification

Status: HISTORICAL TECHNICAL SPECIFICATION. Retained at its original code-metadata target. Historical scope and requirements below describe the Claude package's technical contract; private request, reconnaissance and M23 approval records are unavailable here. They create no current implementation, integration, installation or publication grant.

## 1. Purpose and context

Give Claude Code one maintained native plugin package under `implementations/claude/` that binds the neutral methodology 1.0.0 the way `implementations/codex/` binds it for Codex. S1–S8 in the [package disposition](../../../implementations/claude/references/source-disposition.md) are neutral technical duty labels. The neutral files stay the single statement of every rule; the package supplies Claude-native carriers, mechanisms and checks.

Historical reconciliation addressed differing QA-scan profiles (5 vs 6 vs 8), debug caps (4 vs 2) and stale installed profiles. After: one package with an adapter that accounts for all 71 neutral files, 28 capabilities and 7 parameters, real Claude mechanisms (subagents, hooks, Workflow, structured questions), its own tests and map, and a real load check.

## 2. Decisions

- **Profile `colocated-in-place`.** The package is loaded in place: `claude --plugin-dir <repo>/implementations/claude` or a local directory marketplace. Bodies reference neutral owners as `${CLAUDE_PLUGIN_ROOT}/../../<path>`. A copied install (git marketplace, cache) is unsupported; the SessionStart hook reports a missing neutral binding as BLOCKED and never falls back to an older installed copy.
- **Identity.** Plugin name `methodology-claude` (the `claude-` prefix is reserved), package version 1.0.0, run-state contract `methodology-claude/1.0.0`. Neutral version stays 1.0.0: no neutral file changes.
- **Topics.** The 23 Codex topic names for cross-runtime parity, plus five user-invoked PM lifecycle commands (`pm-bootstrap`, `pm-plan-batch`, `pm-run-batch`, `pm-handoff`, `pm-review-run`) with model invocation disabled, so automatic triggering stays with the parity topics. The learning-ledger command is omitted: systematic learning is owner-deferred (M13).
- **Roles.** Six Claude subagents (`architect`, `coder`, `debugger`, `qa`, `reviewer`, `searcher`) with model tiers from the model policy (judgment `opus`, routine `sonnet`, mechanical `haiku`) and tool lists: judges (`qa`, `reviewer`, `searcher`) have no Edit, Write or NotebookEdit; no inner role has the Agent tool.
- **Mechanics.** SessionStart hook (binding check and orientation context), PreToolUse Bash guard (adapted from S2, asks before unrecoverable commands, denies tree-changing commands to read-only agent types), run-state helper (adapted from the Codex helper, same schema-2 contract, own identity), visual-gate lint (Codex helper), Workflow spine `feature-dev` aligned to the current flow.
- **No neutral, Codex or global change.** Only the root sibling-package assertion and root records/tests/README change outside the package.

## 3. Requirements

- BR-1: Preserve all neutral files, registries, schema, the Codex package and every existing check except the one declared sibling-set assertion.
- BR-2: The package is complete and self-describing: declared layout equals actual members; adapter accounts 71/28/7 with Claude mechanisms and honest fallbacks.
- BR-3: Every carrier, skill and hook resolves the neutral owners in place and refuses (BLOCKED) when the binding is missing, stale or detached.
- BR-4: The flow mechanics follow the current neutral contracts: eight named QA scans, Review phase, separately assigned Architect Finalize, cumulative Debug cap default 4 with 0 valid, one response correction per phase attempt, canonical terminal vocabulary.
- BR-5: Public package content is English, carries no home paths, private names or e-mail addresses, and passes the publication scan with the private deny lists.
- BR-6: Delivery is a locally committed branch with independent QA and Review evidence; merge is the owner's M23 decision.

## 4. Exact package members

`implementations/claude/` holds exactly these 59 regular files (generated `__pycache__`, `.pytest_cache`, `doxygen_output` excluded):

```text
.claude-plugin/plugin.json            plugin-manifest
Doxyfile                              config
README.md                             documentation
adapter.json                          adapter
agents/{architect,coder,debugger,qa,reviewer,searcher}.md   role
examples/smoke-spec.md                example
hooks/guard_destructive.py            helper
hooks/hooks.json                      hook-config
hooks/session_start.py                helper
pytest.ini                            config
references/adoption.md                documentation
references/claude-runtime.md          documentation
references/handoffs.md                documentation
references/package-layout.json        layout
references/source-disposition.md      documentation
skills/<28 topics>/SKILL.md           skill
skills/devplan-protocol/scripts/visual_gate_lint.py   helper
skills/feature-dev/scripts/run_state.py               helper
tests/test_guard.py                   test
tests/test_guide.md                   test-guide
tests/test_package_contract.py        test
tests/test_run_state.py               test
tests/test_session_start.py           test
tests/test_visual_gate.py             test
tests/test_workflow.py                test
tests/workflow_harness.mjs            test
workflows/feature-dev.js              workflow
```

The 28 topics: analyzer, ax-ui-contract, brainstorm, brownfield-spec-template, code-review, data-transform, devplan-protocol, document-protocol, durable-layer, feature-dev, graph-protocol, greenfield-bootstrap, hitl-gates, pm, pm-bootstrap, pm-handoff, pm-plan-batch, pm-review-run, pm-run-batch, prod-log-vacuum, prompting, prompting-agent-design, prompting-decompose, prompting-markup, prompting-verify, roadmap, semantic-exoskeleton, spec-recon.

## 5. Scope

MAY EDIT: `implementations/claude/**` (the members above only); `tests/test_codex_package.py` (sibling set `{codex}` → `{codex, claude}`, unknown sibling still refused); new `tests/test_claude_package.py` (independent assembly oracle); `tests/test_guide.md` (rows for both); root `README.md` (package section, layout row, commands); `examples/pm-project/{VISION,ROADMAP,TASKS,HANDOFF}.md` (M22/M23 pointers); new `examples/pm-project/{specs,plans}/m22-claude-package.md`, `notes/RECON_2026-10-10_claude-package.md`, `notes/m22-claude-package-result.md`.

DO NOT TOUCH: every neutral file, `runtime/` registries and schema, `tools/`, `bin/`, root `Doxyfile`, `pytest.ini`, `tests/conftest.py`, `implementations/codex/**`, `examples/adapter.example.json`, all existing notes/specs/plans, the main checkout's uncommitted foreign changes, the source families S1–S8 and the user-level Claude configuration.

## 6. Acceptance criteria

| Id | Criterion and check |
|---|---|
| AC-M22-1 | Root oracle `tests/test_claude_package.py` confirms exactly the 59 declared members and kinds, the profile and roles map, refuses missing/extra/unknown-sibling/unsafe/linked members; `tests/test_codex_package.py` still refuses an unknown sibling; neutral membership stays 71/67 drafts/4 stubs. |
| AC-M22-2 | `bin/conform adapter implementations/claude/adapter.json` exits 0 with no warning; `bin/conform self` exits 0 with both private deny lists. |
| AC-M22-3 | Package suite passes: layout/adapter/agents/skills/hooks contract, session-start binding and refusal cases, guard decisions, run-state contract and refusals, visual gate, Workflow spine scenarios under Node (green route, Code/QA/Review defect to counted Debug, cap 0 and exhaustion, spec blocked, visual gate fail, null response corrected once then BLOCKED, Finalize escalation). |
| AC-M22-4 | `claude plugin validate --strict implementations/claude` exits 0; `claude plugin details` lists 6 agents, 28 skills, hooks and the workflow. |
| AC-M22-5 | Root and package `doxygen Doxyfile` builds are silent; every package Python module and test carries the exoskeleton and owned LDD trace. |
| AC-M22-6 | A real headless session loaded with `--plugin-dir` shows the SessionStart binding context, resolves a plugin skill and dispatches at least one plugin role agent that reads a neutral owner through `${CLAUDE_PLUGIN_ROOT}/../../`. |
| AC-M22-7 | Full root suite passes (583 plus the new root tests) and the Codex package suite still passes 88. |
| AC-M22-8 | Independent QA (Sonnet) and independent Review (Opus) of the whole delta report no unresolved defect; findings and fixes are recorded in the result note. |

## 7. Risks and limits

- In-place loading only; detached installation, automatic discovery, publication and the global switch-over are not delivered.
- Judges' Bash writes are restrained behaviorally and by the guard hook, not by a sandbox.
- The Workflow spine validates structure in-script; semantic acceptance and human authority remain the parent's judgment; durable state needs the recorder step or the interactive root.
- Doxygen has no JavaScript parser in this setup: the Workflow script carries its markup in comments and is excluded from the map with this stated reason.
- The adapted run-state helper duplicates the Codex helper; a shared extraction is a separate future decision because it changes the Codex package.
- A real full Bootstrap→Finalize smoke run of a target task is not required for M22 acceptance; it is recorded as the next verification step if the owner wants it before switch-over.
