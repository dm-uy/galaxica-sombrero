# HOLD — generator B original proposals (verbatim)

Actor: fresh Claude Code subagent (general-purpose, model opus requested), session-local id ac1829da6ff30a14c, dispatched 2026-10-16 by the root in parallel with generator A, same brief (SHA-256 01838020ce941442ccc6660c820b578c903dd63660aa7fef3ad4fa92ef0d71c7); read-only; no peer output. Unranked. Saved by the root before any evaluator dispatch.

---

## Generator-only HOLD set: 6 alternatives, unranked

**Profile:** BRAIN-101 generator-only. These are not scored, ranked, selected or implemented.
**Source:** I checked that the brief's SHA-256 matches `01838020…71c7`. Worktree `claude/m37-claude-parity` is at b8696a2 plus 25 uncommitted small-fix files that someone else owns (2.0.1→2.0.2). I wrote nothing.

### Cross-cutting facts (verified in files) that every alternative inherits

- **F1. Hooks are pinned.**
  - The tests require SessionStart to have exactly one entry with one hook, and hook keys to be exactly {PreToolUse, SessionStart} (`implementations/claude/tests/test_session_start.py:587-591`, `test_guard.py:1611-1617`).
  - The whole AST of `session_start.py` is pinned except `PACKAGE_VERSION` (`tests/test_c1_review_and_routing.py:414-440`).
  - So any orientation injected automatically from inside the package changes existing assertions.
- **F2. C2 `orient` cannot read any of the five consumer projects today.**
  - None of them declares `profile: methodology-consumer-pm/1.0.0`.
  - consumer-B says "Project Conventions `1.4.0`", so `orient` treats it as legacy, read-only (`consumer_files.py:393`, `orient.py:200`).
  - The other four hit `undeclared-or-unsupported-profile` (`consumer_files.py:395`), and orient then exits 2 "unavailable" (`orient.py:510-511`).
  - `codemap` never calls `resolve_layout`.
  - So under every alternative, bare `orient` only works again after the owner grants an adoption migration per project.
- **F3. Package oracles refuse links and new siblings.** Both refuse symlinked members, members that resolve outside the package, and any sibling outside {codex, claude} (`tests/test_claude_package.py:128,156-167`; `tests/test_codex_package.py:45,105-115`).
- **F4. The code is harness-neutral in content.**
  - The helpers and seeds contain no "codex" string.
  - The Codex consumer tests find the scripts through `Path(__file__).resolve().parents[1]`.
  - `test_consumer_pm.py:387-391` also requires the profile to hold 75 CV rows and 22 CHECK rows, and the four lifecycle SKILL.md files to contain "Full owners:" and "consumer-pm-profile.md".
- **F5. The existing copy precedent has already drifted.** `visual_gate_lint.py` differs in bytes between the packages (its contract header was adapted).
- **F6. PATH behaviour is only partly known.**
  - `CLAUDE_PLUGIN_ROOT` is unset in the Bash tool environment (checked here).
  - methodology-claude is loaded through `CLAUDE_CODE_PLUGIN_DIRS`.
  - ASSUMPTION, not verified: that an in-place plugin's `bin/` joins PATH. Only the old plugin's marketplace-source `bin/` was observed on PATH.
- **F7. Bare `orient` was never a command.** The old plugin has no `orient` executable; the hook injection served it. consumer-A `CLAUDE.md:42` calls the old plugin's `orient.py` by absolute path.
- **F8. Seeds cannot move to the neutral root.**
  - `documents/templates` is pinned to five templates plus INDEX (`tests/test_skeleton.py:298-301`).
  - Markdown at the root outside tests/examples/implementations falls under FMT-1 (`tools/conformlib/markdown.py:55-56`).
  - So moving seeds to the neutral root would need an exemption, which is forbidden.

---

### ALT-1 — Claude-owned adapted port (independent copy)

- **Essence:**
  - Claude gets its own copies of the 4 helpers and 13 seeds under `skills/pm/{scripts,templates}/`, with contract headers adapted to Claude (the F5 precedent).
  - It also gets a Claude carrier `references/consumer-pm-profile.md` (invocation through `${CLAUDE_PLUGIN_ROOT}`), 4 ported tests, and routing in `pm` plus the four lifecycle skills.
  - Bare names come from `bin/orient`, `bin/codemap`, `bin/markup-migrate`: regular files of kind `helper` that resolve their own real path (as `bin/conform` does).
  - No hook change. The root runs `orient` as each consumer's AGENTS.md says.
  - Sync is a policy only: "behaviour intended identical, not asserted", as with `run_state`.
- **Files:**
  - About 24 new members (59→83).
  - Edits: layout, the `test_claude_package` expected paths, the `test_package_contract` count, and the `PACKAGE_VERSION` constants in `run_state.py`, `session_start.py` and the C1 test selectors.
  - Also README, claude-runtime, adoption, handoffs, source-disposition (code-map/migration move from "outside" to "adapted"), test_guide, and 5 SKILL.md files.
- **Dependencies:** standard-library Python 3.9+; the F6 PATH assumption.
- **Side effects:**
  - Positive: Codex is untouched (zero risk to C2), and Claude stays self-describing.
  - Negative: about 2450 lines are duplicated with no drift check, and F5 shows drift happens; every Codex fix has to be re-ported by hand.
  - Negative: session-start injection is lost, so three consumer CLAUDE.md files make false claims until they are edited.
- **Migration / rollback:** about 40 files in one PR; rollback is a revert.
- **Third harness:** a third copy; drift grows with each package.
- **Stresses:** single source of truth; one writer per path across copies.

### ALT-2 — Byte-locked mirror with a parity oracle (Codex canonical)

- **Essence:**
  - Claude carries byte-identical copies of the 4 helpers, the 13 seeds and the 4 Codex test modules. Because the tests are `__file__`-relative (F4), the identical tests exercise Claude's copies.
  - A new root `tests/test_consumer_pm_mirror.py` asserts SHA-256 equality of the 21 files across the two packages.
  - Because of F4, Claude's carrier must also hold the 75 CV / 22 CHECK rows, and its lifecycle SKILL.md files must contain "Full owners:".
  - Exposure is the same `bin/` set as ALT-1.
- **Files:** about 24 Claude members plus the root test, with the same layout, oracle and constant edits as ALT-1.
- **Dependencies:** Codex stays the only writer of the canonical bytes; the F6 assumption.
- **Side effects:**
  - Positive: drift cannot merge unnoticed, and the accepted C2 tests are reused as Claude QA.
  - Negative: every Codex helper edit forces a Claude edit in the same PR, so releases are coupled.
  - Negative: Claude copies cannot carry Claude-specific contract headers (this breaks the F5 convention), and fixtures saying `codex:test` live inside the Claude package.
- **Migration / rollback:** moderate; rollback is a revert. Converting later to ALT-4 is mechanical.
- **Third harness:** another mirror plus a longer parity list; still one oracle.
- **Stresses:** one writer per path (two paths per file); the cost of maintaining the oracle.

### ALT-3 — Inversion: no code port; Claude references the Codex members in place

- **Essence:**
  - In the same way skills already reach neutral owners through `${CLAUDE_PLUGIN_ROOT}/../../`, Claude reads `${CLAUDE_PLUGIN_ROOT}/../codex/skills/pm/{scripts,templates}` and the Codex profile's duty accounting.
  - Claude adds only:
    - a thin native carrier with Claude invocation, the hook/PATH limits, and a pointer to the Codex accounting;
    - routing in the skills;
    - `bin/` launchers that run the real Codex file and return 2 BLOCKED if it is missing;
    - one test that pins SHA-256 of the 17 Codex files Claude depends on (an upstream-change tripwire) and drives the launchers across the process boundary.
  - Precedent: `test_package_contract.py:249` already reads `implementations/codex/skills`.
- **Files:** +5 members (59→64) plus documentation and constant edits.
- **Dependencies:**
  - A complete checkout, which is already required.
  - A stable Codex layout.
  - `markup_migrate.py:445` finds its templates relative to `__file__`. That works because Claude runs the real file, not a symlink, which F3 forbids anyway.
- **Side effects:**
  - Positive: a single source, the smallest diff, and no Codex change.
  - Negative: the Claude package is no longer self-contained; a Codex bump changes Claude's behaviour unless the tripwire fails.
  - Negative: this creates the first cross-package dependency (today the neutral root is the only declared one). The binding check cannot verify the sibling, because `session_start.py` is pinned (F1).
  - Negative: the Codex profile names Codex wire and package versions.
- **Migration / rollback:** smallest of the six.
- **Third harness:** Codex becomes the de facto shared library, an asymmetric ownership.
- **Stresses:** in-place / BLOCKED semantics for a sibling dependency; the "neutral owner wins over carrier" model (a package becomes an owner).

### ALT-4 — Extract a shared typed member `implementations/consumer-pm/`

- **Essence:**
  - Move the helpers, seeds, the harness-neutral CV/CHECK accounting and the 4 tests out of Codex into a third typed directory with its own layout, Doxyfile, pytest.ini and an independent root oracle.
  - Codex and Claude keep thin carriers and routing that point to `../consumer-pm/`.
  - Claude's `bin/` points there.
- **Files:**
  - About 24 files in the new directory.
  - Codex goes from 73 to about 52 members, with edits to its layout, `EXPECTED_PATHS`, README invocation, profile, SKILLs and its `run_state` membership selector.
  - `DECLARED_PACKAGES` changes in both oracles (F3).
- **Dependencies:**
  - ASSUMPTION: that FMT-1/FMT-26 admit a non-harness tooling member under `implementations/`.
  - The Codex install is a full-repository snapshot, so relative references still resolve.
  - The `scripts/` + `templates/` sibling shape must be kept (`markup_migrate.py:445`).
- **Side effects:**
  - Positive: a true single source; a future harness adds only a carrier.
  - Negative: it changes the accepted C2 Codex package (the tie-breaker risk), and Codex's documented `PACKAGE/skills/pm/scripts/…` path breaks unless shims stay.
  - Negative: the sibling-set assertion changes in two oracles.
- **Migration / rollback:** highest; a two-package release that needs a Codex-change justification. Rollback is a multi-package revert.
- **Third harness:** best.
- **Stresses:** Codex-change justification; REPO-102/FMT interpretation; oracle negative controls.

### ALT-5 — Inversion: tooling vendored into consumer projects, with project-level hooks

- **Essence:**
  - The packages supply only the seeds, the carrier and the vendoring source (content as in ALT-2 or ALT-3).
  - Under an exact owner migration grant, pm-bootstrap writes pinned copies into each consumer: `tools/methodology/{consumer_files,orient,codemap,markup_migrate}.py` plus a version/SHA file.
  - Under a separate explicit grant, it adds a project `.claude/settings.json` SessionStart hook that runs `python3 -B tools/methodology/orient.py .`.
  - The vendored `orient --check` flags a copy that is stale against the package hash.
- **Files:** a few Claude carrier/skill edits; each consumer gets about 6 files plus its settings file.
- **Dependencies:** an owner grant per project (required anyway by F2); the consumer accepts framework code in its repository.
- **Side effects:**
  - Positive: brings back automatic session-start orientation without touching F1's pins; independent of F6; Codex sessions in the same project get identical commands.
  - Negative: five copies to refresh each release.
  - Negative: vendored code falls under the consumer's Doxyfile coverage, markup and CHECK-15 map freshness.
  - Negative: C2 says "No hook, PATH registration … follows from a form", so each hook needs its own grant.
- **Migration / rollback:** done per project; reversible per project.
- **Third harness:** almost no package work; only the hook syntax differs per harness.
- **Stresses:** no automatic adoption; single source (copies on the consumer side); consumer ownership.

### ALT-6 — Inversion: an external compatibility bridge plugin; the methodology packages expose no commands

- **Essence:**
  - The Claude package gets the carrier, routing and seeds by referencing Codex (as in ALT-3), but no `bin/` and no hook.
  - Exposure moves to a small owner-side plugin, for example one replacing product-methodology in agent-skills.
  - That plugin holds only `bin/orient|codemap|markup-migrate` and a SessionStart hook. Both run the checkout's helpers through an explicitly configured root (for example `METHODOLOGY_ROOT`), and report BLOCKED when it is unset or missing. It holds no code copy.
- **Files:** about 3–5 in this repository; about 5 in the bridge.
- **Dependencies:** the owner keeps a user-level environment setting (a configuration change that needs their decision); the bridge's `bin/` reaches PATH (observed only for marketplace-loaded plugins).
- **Side effects:**
  - Positive: no pinned assertion in this repository changes; injection and bare names come back exactly where the old plugin provided them.
  - Negative: the capability is split across two repositories, and the bridge sits outside this repository's QA and oracles.
  - Negative: it could be read as the forbidden "fallback to an installed copy".
- **Migration / rollback:** low in this repository, moderate on the owner side. Rollback is re-enabling the old plugin.
- **Third harness:** a bridge per harness.
- **Stresses:** in-place-only / no-fallback interpretation; the repository as the single complete source.

**Comparison:** deliberately left out (generator-only profile). No favourite is handed off.

### Files actually read

- `/private/tmp/methodology-m37-claude-parity/examples/pm-project/notes/m37-decision-c2-port/brief.md`
- `/private/tmp/methodology-m37-claude-parity/prompting/brainstorm.md` (lines 1-82)
- `/private/tmp/methodology-m37-claude-parity/FORMAT.md` (sections)
- `/private/tmp/methodology-m37-claude-parity/implementations/codex/references/consumer-pm-profile.md`
- `/private/tmp/methodology-m37-claude-parity/implementations/codex/README.md` (part)
- `/private/tmp/methodology-m37-claude-parity/implementations/codex/skills/pm/SKILL.md`
- `/private/tmp/methodology-m37-claude-parity/implementations/codex/skills/pm-bootstrap/SKILL.md` (grep)
- `/private/tmp/methodology-m37-claude-parity/implementations/codex/skills/pm/scripts/{orient,codemap,consumer_files,markup_migrate}.py` (headers and greps)
- `/private/tmp/methodology-m37-claude-parity/implementations/codex/skills/pm/templates/{CLAUDE,AGENTS,HANDOFF}.md`
- `/private/tmp/methodology-m37-claude-parity/implementations/codex/tests/test_{consumer_pm,consumer_files,codemap,markup_migrate}.py` (greps)
- `/private/tmp/methodology-m37-claude-parity/implementations/claude/.claude-plugin/plugin.json`
- `/private/tmp/methodology-m37-claude-parity/implementations/claude/hooks/hooks.json`
- `/private/tmp/methodology-m37-claude-parity/implementations/claude/references/{package-layout.json,source-disposition.md,claude-runtime.md}`
- `/private/tmp/methodology-m37-claude-parity/implementations/claude/skills/pm-bootstrap/SKILL.md`
- `/private/tmp/methodology-m37-claude-parity/implementations/claude/skills/feature-dev/scripts/run_state.py` (binding section)
- `/private/tmp/methodology-m37-claude-parity/implementations/claude/tests/{test_package_contract,test_session_start,test_guard}.py` (parts)
- `/private/tmp/methodology-m37-claude-parity/implementations/{codex,claude}/skills/devplan-protocol/scripts/visual_gate_lint.py` (diff)
- `/private/tmp/methodology-m37-claude-parity/tests/{test_claude_package,test_codex_package,test_c1_review_and_routing,test_skeleton}.py` (parts)
- `/private/tmp/methodology-m37-claude-parity/tools/conformlib/markdown.py` (grep)
- `/private/tmp/methodology-m37-claude-parity/bin/conform` (header)
- `/private/tmp/methodology-m37-claude-parity/documents/templates/HANDOFF.md`
- `<owner-agent-skills-checkout>/plugins/product-methodology/{.claude-plugin/plugin.json,hooks/hooks.json,bin/codemap,bin/markup-migrate}`
- AGENTS.md / CLAUDE.md / CONVENTIONS.md greps in `<five-consumer-projects>`
- `<home>/.claude/settings.json` (grep for `CLAUDE_CODE_PLUGIN_DIRS`)
