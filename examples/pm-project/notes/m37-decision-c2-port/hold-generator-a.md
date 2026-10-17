# HOLD — generator A original proposals (verbatim)

Actor: fresh Claude Code subagent (general-purpose, model opus requested), session-local id af4b7ad7c8b5f6e66, dispatched 2026-10-16 by the root with the shared brief (SHA-256 01838020ce941442ccc6660c820b578c903dd63660aa7fef3ad4fa92ef0d71c7); read-only; no peer output. Unranked. Saved by the root before any evaluator dispatch.

---

**Profile:** generator-only. Five unranked alternatives (BRAIN-101/102), with no scores, ranking or selection. I wrote nothing and ran only read-only commands. The worktree has uncommitted changes from another writer (`git status`: README.md and several files under `implementations/claude/` show M), so what I read reflects that dirty tree.

## Grounding shared by all alternatives (verified unless marked)

- **G1 Hook pins.** Three existing tests pin a single SessionStart command:
  - `implementations/claude/tests/test_session_start.py::test_hooks_json_command_runs_through_a_shell` asserts `len(entries) == 1` and `len(entries[0]["hooks"]) == 1`.
  - `test_package_contract.py::test_hooks_and_workflow` asserts `len(start) == 1`.
  - `tests/test_c1_review_and_routing.py::test_session_start_source_bridge_preserves_ast` pins the whole AST of `session_start.py`; only `PACKAGE_VERSION` normalizes.
  - So any orientation delivered by a package hook means amending existing assertions.
- **G2 Membership and count pins.** Both root oracles refuse symlinked members and any sibling outside `DECLARED_PACKAGES = {"codex", "claude"}`. Codex `run_state.py` hard-codes `== 73` members, and test_c1 normalizes exactly that selector.
- **G3 Helper portability.** The C2 helpers contain no harness identity. Each imports its sibling `consumer_files`, and `markup_migrate` finds its template at `scripts/../templates/Doxyfile`. The profile carrier, by contrast, names Codex ("source package3.0.1", "Wire methodology-codex/2.0.0").
- **G4 `orient` behaviour.**
  - C2 `orient` refuses to run without an explicit PROJECT ("explicit PROJECT or nonempty portfolio required"). It has no `--hook` and no cwd default.
  - `resolve_layout` treats "Project Conventions 1.4.0" as a read-only legacy dialect, and orient then reports "legacy-read-only-dialect; unsupported native assessment".
  - The old plugin's CONVENTIONS is `conventions_version: 1.4.0`.
  - *Assumption:* the five consumers declare 1.4.0. I did not read their files.
- **G5 What changes the neutral population.**
  - The neutral population is every `*.md` outside tests/examples/implementations: 71 files, pinned in both packages.
  - `documents/templates/` is pinned to the five forms plus INDEX (`tests/test_skeleton.py`).
  - Root Python and root `bin/` do not change the population.
  - Root `bin/conform` is a realpath launcher; its own comment says "A harness links this file into its own bin directory".
- **G6 PATH today.**
  - In this session `orient` is not on PATH. The old plugin has no `bin/orient`; bare `orient` was served by its hook.
  - `codemap` resolves from the old plugin's source `bin/`.
  - *Assumption U1:* the `bin/` of a plugin loaded in place (`--plugin-dir` / `CLAUDE_CODE_PLUGIN_DIRS`) reaches the Bash PATH. This is not verified.
  - *Assumption U2:* `CLAUDE_PLUGIN_ROOT` is absent from the Bash environment. The old launcher's comment says so; I did not verify it. Launchers therefore resolve their location through realpath.
- **Common to all alternatives.** Claude's `skills/{pm,pm-bootstrap,pm-plan-batch,pm-run-batch,pm-handoff}/SKILL.md` gain the consumer-profile route. Claude's pm-bootstrap currently seeds only the five neutral templates.

---

## A. Byte-mirror twin with a sync oracle

- **Essence:** Claude carries its own byte-identical copies of the four helpers and the 13 seeds. A root test fails on any divergence from Codex. Only the profile carrier differs: Claude identity and Claude invocation. Commands are exposed through package `bin/` launchers plus the explicit `python3 -B` forms in skills.
- **Files:**
  - Claude adds `skills/pm/scripts/*.py` (4), `skills/pm/templates/*` (13), `references/consumer-pm-profile.md`, `bin/{orient,codemap,markup-migrate}` (realpath launchers of kind `helper`, so run_state `KINDS` stays untouched) and `tests/test_consumer_pm.py` (routes, carrier CV/CHECK counts, launchers).
  - Claude updates `package-layout.json` (59 → about 81), the root `tests/test_claude_package.py` EXPECTED list, the contract counts, and `adoption.md` and `source-disposition.md`.
  - A new root `tests/test_consumer_pm_twin.py` compares SHA-256 of the 17 files.
  - Codex is unchanged; its four tests remain the behaviour oracle.
- **Dependencies:** U1. Codex is canonical by convention only.
- **Orientation and bare names:** no hook, so G1 holds. Agents run `orient PROJECT`. A no-argument `orient` fails (G4). The three CLAUDE.md lines saying "the plugin injects" become false and need per-project granted edits. Projects on 1.4.0 get the legacy refusal until they migrate.
- **Side effects:**
  - (+) No behavioural drift, and that is provable by hashes. Codex is untouched.
  - (−) Every helper fix becomes a two-place edit plus a re-hash. The precedent is poor: the `run_state` and `visual_gate` copies are already "not asserted to behave identically".
  - (−) Heavy membership and oracle churn, and no injection at session start.
- **Migration and rollback:** moderate. Rollback removes the added members and restores the 59-path oracle.
- **Third harness:** makes yet another mirror, and the sync test grows.
- **Constraints stressed:** single source holds by policy, not by structure; consumer continuity.

## B. Claude-native fork with the old plugin's ergonomics

- **Essence:** port the helpers, then adapt the Claude copy:
  - default to the current directory;
  - add `--hook session-start` (silent outside declared projects, never fails the session);
  - add a legacy 1.4.0 read assessment;
  - expose bare `orient`, `codemap` and `markup-migrate`.
  - The result is recorded as "adapted from C2" in source-disposition, with no byte sync.
- **Files:**
  - Additions as in A, without the twin test.
  - A second SessionStart command in `hooks/hooks.json`: `python3 "${CLAUDE_PLUGIN_ROOT}/skills/pm/scripts/orient.py" --hook session-start`. `session_start.py` stays untouched.
  - The single-hook assertions are amended in both Claude tests (G1).
  - New Claude tests cover the hook, cwd default and legacy behaviours.
- **Dependencies:**
  - U1.
  - *Assumption:* Claude Code runs several SessionStart commands from one plugin and concatenates their context.
  - Fits within the hook timeout.
- **Side effects:**
  - (+) Best match to what the consumers' AGENTS.md and CLAUDE.md already say; little consumer editing at first.
  - (−) A deliberate departure from the C2 contract ("no --hook/PATH"). The owner rule that "a difference is a package defect" is stressed, and the same project gets two orient semantics.
  - (−) The legacy assessment is new behaviour that needs its own specification and QA.
- **Migration and rollback:** moderate to high. Rollback removes the hook entry and the members and restores the assertions.
- **Third harness:** forks again, so behaviour fragments.
- **Constraints stressed:** single source (weakest of the five); preservation of existing assertions; Codex parity.

## C. Neutral-root shared tool behind root `bin/`

- **Essence:** helper code moves to the root as `tools/consumer_pm/`. Root `bin/orient`, `bin/codemap` and `bin/markup-migrate` follow the `conform` realpath pattern, and both packages expose thin entry points. Seeds stay owned by the packages, because root `.md` seeds would enter the neutral population (G5). Claude mirrors the seeds under a hash test, and the code takes its template root from the caller.
- **Files:**
  - Root gains `tools/consumer_pm/*.py`, the three `bin/*` launchers, and root tests moved or repointed from `implementations/codex/tests/test_{consumer_files,consumer_pm,codemap,markup_migrate}.py`.
  - Codex `skills/pm/scripts/*.py` become shims, which keeps 73 members and the documented `PACKAGE/skills/pm/scripts/<command>.py` form. The default template path in `markup_migrate` is parameterized.
  - Claude adds `bin/*` that exec `../../bin/*`, the templates, the carrier and the skill routes.
  - The root README names the new homes.
- **Dependencies:**
  - A complete checkout, which both packages already require.
  - U1 for Claude.
  - The owner may separately link root `bin/` into a personal PATH; that is the owner's own action and nothing is shipped for it.
- **Side effects:**
  - (+) One code source for every harness, and the commands work with no harness at all.
  - (−) The neutral root gains code bound to a package profile identity (`methodology-consumer-pm/1.0.0`), which blurs neutral versus package.
  - (−) Accepted C2 files change. Codex tests load modules with `spec_from_file_location` and inspect loggers, so shims risk re-export and logging differences, and Codex QA must be repeated. Seeds remain duplicated.
- **Migration and rollback:** high, because Codex is touched. Rollback is a git restore.
- **Third harness:** cheap: link root `bin/` and mirror the seeds.
- **Constraints stressed:** Codex constraint and the tie-breaker; the spirit of REPO-102 on root scope.

## D. Third typed sibling package shared by both harnesses (inverts the self-contained-package assumption)

- **Essence:** create `implementations/consumer-pm/`, a harness-neutral helper package with its own layout, inventory and tests. It holds the four helpers, the 13 seeds and the launchers. Codex's copy moves there. Both harness packages reference `../consumer-pm/` and keep only their carriers and skills.
- **Files:**
  - The new package: `references/package-layout.json`, `scripts/`, `templates/`, `bin/`, `tests/`, `README.md`, `pytest.ini`.
  - A new root oracle `tests/test_consumer_pm_package.py`, and `DECLARED_PACKAGES` changed in both existing oracles.
  - Codex loses 21 members (73 → 52), and its `run_state.py` constant 73 plus the test_c1 selector change. Its README invocation contract and profile paths are rewritten.
  - Claude gets the carrier, the routes and `bin/` launchers pointing at the sibling (about 63 members).
- **Dependencies:** whether FMT-1's "typed implementation-package namespace" admits a package that is not a harness is unclear, since FMT-26 frames packages around a harness adapter; that may need the owner's interpretation. The Codex snapshot ships the whole repository, so the sibling travels with it (verified in the Codex README packaging).
- **Side effects:**
  - (+) A structural single source and a versioned helper contract independent of either harness.
  - (−) The largest change to accepted Codex C2: membership, a pinned constant and the documented commands.
  - (−) The sibling negative controls change shape, and the packages become interdependent at load time.
- **Migration and rollback:** highest. Rollback is a multi-package revert.
- **Third harness:** best fit; it simply references the sibling.
- **Constraints stressed:** Codex constraints, the pinned `run_state` constant and the test_c1 selector, FORMAT interpretation, and the tie-breaker.

## E. No code port: Claude borrows Codex's helpers and consumers own their wiring (inverts "bare names must keep working")

- **Essence:** Claude ships no helper or seed copies. A Claude delta carrier routes the four entries to Codex's helpers and seeds inside the checkout, at `${CLAUDE_PLUGIN_ROOT}/../codex/skills/pm/…`, which the mandatory complete-checkout profile guarantees is present. Bare names retire. When the owner grants a consumer's migration through `pm-bootstrap`:
  - the project moves from 1.4.0 to `methodology-consumer-pm/1.0.0`;
  - its AGENTS.md switches to the explicit invocation;
  - optionally, its own `.claude/settings.json` SessionStart hook runs `orient "$CLAUDE_PROJECT_DIR"`.
- **Files:**
  - Claude adds `references/consumer-pm-profile.md` (a delta plus pointers) and updates the five skills, README, adoption and source-disposition (59 → 60 members).
  - A Claude contract test asserts that every cross-reference resolves and that no copy exists.
  - A root test pins the Codex paths Claude depends on.
  - Codex is unchanged.
- **Dependencies:** Codex's path layout becomes a cross-package contract. Each consumer needs a per-project grant, and the persistent-configuration change needs explicit permission. No dependence on U1.
- **Side effects:**
  - (+) The smallest Claude change, no Codex change, and perfect sync; the PATH uncertainty disappears.
  - (−) Claude depends on another harness package: a Codex refactor breaks Claude, and Claude users read Codex-worded carriers.
  - (−) The five migrations become the critical path, and the old plugins stay enabled until each project has migrated.
- **Migration and rollback:** low inside the repository, high across the consumers. Repository rollback is trivial.
- **Third harness:** borrows Codex too, so Codex becomes a de facto library.
- **Constraints stressed:** consumer continuity; package ownership boundaries; the owner rule that a difference is a package defect, since Claude's behaviour is defined by Codex files.

---

## Files actually read (fully or in excerpts)

- `<worktree>/examples/pm-project/notes/m37-decision-c2-port/brief.md` (full; SHA-256 matches 01838020…71c7)
- `<worktree>/prompting/brainstorm.md` (lines 1–60, including both requested sections)
- `<worktree>/FORMAT.md` (FMT-1, versions, adapters)
- `<worktree>/bin/conform`, `tools/conform.py` (head), `tools/conformlib/markdown.py` (excerpt)
- `<worktree>/implementations/codex/`:
  - `references/consumer-pm-profile.md` (headings, lines 13–39)
  - `skills/pm/scripts/{consumer_files,orient,codemap,markup_migrate}.py` (grep excerpts, `resolve_layout`, `orient.main`)
  - `tests/test_consumer_pm.py` (excerpts) and `tests/test_{codemap,consumer_files,markup_migrate}.py` (grep)
  - `README.md` (grep)
  - `skills/{pm,pm-bootstrap,pm-handoff}/SKILL.md` (grep)
  - `skills/feature-dev/scripts/run_state.py` (grep)
- `<worktree>/implementations/claude/`:
  - `.claude-plugin/plugin.json`, `hooks/hooks.json`, `hooks/session_start.py` (first part)
  - `references/package-layout.json` (head), `references/source-disposition.md`
  - `README.md` and `references/claude-runtime.md` (grep)
  - `skills/pm-bootstrap/SKILL.md`, `adapter.json` (grep)
  - `tests/test_package_contract.py` and `tests/test_session_start.py` (excerpts)
  - `skills/feature-dev/scripts/run_state.py` (constants)
- `<worktree>/tests/`: `test_claude_package.py`, `test_codex_package.py`, `test_c1_review_and_routing.py`, `test_skeleton.py`, `test_cli.py` (excerpts)
- `<owner-agent-skills-checkout>/plugins/product-methodology/`: `hooks/hooks.json`, `bin/codemap`, `README.md` (grep), `scripts/orient.py` (grep), `CONVENTIONS.md` (head), `.claude-plugin/plugin.json`
