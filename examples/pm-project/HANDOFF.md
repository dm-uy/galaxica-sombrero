# Current: M38 DSH native implementation package

## Owner decisions

The owner approved implementing the methodology for the DeepSeek Harness under `implementations/`, chose the full Codex-twin package, and chose installation as a plugin in the `web` profile. That authorization covers preparing the package and proving the installation mechanism. It does not yet cover a `main` merge, installation into the owner's live harness home, or publication; those remain separate matching decisions and none has been taken. M30 native Claude remains explicitly deferred; C3 remains exhausted. The pending `claude/m37-claude-parity` work is another writer's branch and is untouched.

## Current state

Current source versions: neutral/Codex3.0.1 and Claude2.0.1. **M38 adds a third package, `implementations/dsh`, at 3.0.1 over neutral 3.0.1**, on branch `dsh/m38-harness-package` in the isolated worktree `/private/tmp/methodology-m38-dsh-harness`. It is not on `main`. [Result, evidence and limits](notes/m38-dsh-package.md); [task entry](TASKS.md).

The package carries an adapter over all 71 neutral files, 28 capabilities and seven parameters, 27 DSH skill carriers, six role carriers, the six shared Python helpers, the 13 PM templates and a DSH bundle whose single row mounts the package's own `skills/` root. `bin/conform adapter` and `bin/conform self` both exit 0; the package suite is 146 passed; the new root contract test is 2 passed; the two sibling package suites are 11 passed. A scratch-profile `dsh plugin add` composed a real bundle layer and the row resolved to a skill root holding 27 entries.

No native behavioral acceptance of this package exists: no flow ran, no checkpoint resumed and no session observed the catalog. The package is a source and installation artifact, and it is reported as one.

## Next action

The owner's next decisions, in order: (1) whether to merge `dsh/m38-harness-package` into `main`; (2) whether to install the bundle into the live profile, which the package README describes and which is proved only on a scratch profile so far; (3) whether a real methodology run should be performed to begin behavioral acceptance. Absent a matching decision, do not merge, do not touch the live harness home, and do not present the package as accepted.

## Retained traps

The root `tests` suite carries **67 pre-existing failures** on unmodified `main` — 60 in `test_flow_contract.py`, six in `test_pm_role.py`, and the stale helper-algorithm pin in `test_c1_review_and_routing.py::test_release_bridge_keeps_wire_and_helper_algorithms`. A detached checkout of `b8696a2` reproduces them; they are not caused by M38 and must not be read as M38 regressions. The DSH helper deliberately stays out of that pin loop: it deviates structurally by one line, and joining the pin needs a reviewed normalization branch rather than a weakened check.

C3: unaccepted/unmerged, terminal ESCALATED/review, Debug4/4 exhausted; no reset/fifth repair. M30: source integrated, full checkpoint acceptance incomplete, native Claude AC4/ClaudeAC5 deferred/unfulfilled and Debug1/4 retained. Minimal-safeguard → bounded API/database trial → separately scoped C4–C6 route and later frontend/Telegram/MCP remain. Public source visibility and local installation do not satisfy these proofs. See [ROADMAP](ROADMAP.md) and the linked original result records for history.

One delegated reconnaissance reader left a `.DS_Store` and an untracked `dsh-subagent-workflow-reference.md` in the read-only harness checkout under the home directory. That checkout is foreign to this repository and outside this grant, so neither file was removed; a later owner decision can clean them.
