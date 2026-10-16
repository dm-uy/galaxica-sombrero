# Current: M38 DSH native implementation package

## Owner decisions

The owner approved implementing the methodology for the DeepSeek Harness under `implementations/`, chose the full Codex-twin package, installation as a plugin in the `web` profile, and then explicitly approved the `main` merge and the live installation ("надо смержить и поставить в профиль этот бандл"). Both are done: checked M38 source `af7eab7` was fast-forwarded into canonical `main`, and `dsh plugin --profile web add ./implementations/dsh` installed the bundle into the live profile against the canonical checkout. Publication remains a separate decision and has not been taken. M30 native Claude remains explicitly deferred; C3 remains exhausted. The pending `claude/m37-claude-parity` work is another writer's branch and is untouched.

## Current state

Current source versions: neutral/Codex3.0.1 and Claude2.0.1. **M38 adds a third package, `implementations/dsh`, at 3.0.1 over neutral 3.0.1**, on branch `dsh/m38-harness-package` in the isolated worktree `/private/tmp/methodology-m38-dsh-harness`. It is not on `main`. [Result, evidence and limits](notes/m38-dsh-package.md); [task entry](TASKS.md).

The package carries an adapter over all 71 neutral files, 28 capabilities and seven parameters, 27 DSH skill carriers, six role carriers, the six shared Python helpers, the 13 PM templates and a DSH bundle whose single row mounts the package's own `skills/` root. `bin/conform adapter` and `bin/conform self` both exit 0; the package suite is 146 passed; the new root contract test is 2 passed; the two sibling package suites are 11 passed. A scratch-profile `dsh plugin add` composed a real bundle layer and the row resolved to a skill root holding 27 entries.

The live `web` profile now composes one `# == @methodology/dsh` layer whose row resolves to this checkout's `implementations/dsh/skills` (27 entries); the previous `package.json` and `cordis.patch.yml` are saved beside them as `.bak-m38` for one-step rollback. No native behavioral acceptance exists yet: no flow ran, no checkpoint resumed and no session observed the catalog. The run that would establish it is prepared and specified at [the first-run note](notes/m38-run-01.md); it needs a fresh session, because a session's catalog is fixed when it is created and the session that installed the bundle predates it.

## Next action

Run [M38-RUN-01](notes/m38-run-01.md) in a fresh session: load `pm` through the skill tool and record the reported base directory, run the bounded smoke, then take this repository's own next bounded task through the flow. Retain the three probe outputs verbatim. A headless probe from a shell cannot substitute: it fails with `MISSING_CREDENTIAL` because the provider key lives in the Web host's credential service, not in a child environment.

## Retained traps

The root `tests` suite carries **67 pre-existing failures** on unmodified `main` — 60 in `test_flow_contract.py`, six in `test_pm_role.py`, and the stale helper-algorithm pin in `test_c1_review_and_routing.py::test_release_bridge_keeps_wire_and_helper_algorithms`. A detached checkout of `b8696a2` reproduces them; they are not caused by M38 and must not be read as M38 regressions. The DSH helper deliberately stays out of that pin loop: it deviates structurally by one line, and joining the pin needs a reviewed normalization branch rather than a weakened check.

C3: unaccepted/unmerged, terminal ESCALATED/review, Debug4/4 exhausted; no reset/fifth repair. M30: source integrated, full checkpoint acceptance incomplete, native Claude AC4/ClaudeAC5 deferred/unfulfilled and Debug1/4 retained. Minimal-safeguard → bounded API/database trial → separately scoped C4–C6 route and later frontend/Telegram/MCP remain. Public source visibility and local installation do not satisfy these proofs. See [ROADMAP](ROADMAP.md) and the linked original result records for history.

A delegated reconnaissance reader had written its report into this repository's own root. It is now owned by the package as [the DSH subagent/workflow reference](implementations/dsh/references/dsh-subagent-workflow.md) and declared in the layout. The reader also left a `.DS_Store` in the foreign `deepseek-harness` checkout; that checkout is outside this grant, so the file was left alone.
