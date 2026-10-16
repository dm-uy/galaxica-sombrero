# M38 — DSH native implementation package

Owner request: study this repository, implement the methodology for the DeepSeek Harness (DSH) under `implementations/`, reconcile it against the current source, and connect it as a DSH plugin. The owner selected the full Codex-twin package and installation as a plugin in the `web` profile.

## What was built

`implementations/dsh/` is a third typed implementation package beside `codex` and `claude`, at package version 3.0.1 over neutral 3.0.1.

| Area | Delivered |
|---|---|
| Adapter | `adapter.json` accounts for all 71 neutral files in reference mode through `references/adoption.md`, all 28 declared capabilities and all seven parameters, each bound to an actual DSH mechanism with its honest fallback. |
| Runtime | `references/dsh-runtime.md` is written against the harness's real surface and states where that surface cannot meet a neutral duty. |
| Skills | 27 DSH skill carriers, frontmatter `name`/`description`, each naming its neutral owners in full; bodies are re-read on every load by the harness, so there is no cache to invalidate. |
| Roles | Six role carriers under `roles/`, unchanged in contract from the sibling packages. |
| Helpers | The six Python helpers (`run_state.py`, `orient.py`, `codemap.py`, `consumer_files.py`, `markup_migrate.py`, `visual_gate_lint.py`) and the 13 PM templates. |
| Bundle | `package.json` with `dsh.bundle`, `cordis.patch.yml`, `.dsh-plugin/plugin.json`. The bundle adds exactly one host-plane row: a second local skill provider whose only root is this package's `skills/`. |
| Inventory | `references/package-layout.json` declares 74 members; the package map is deliberately not a member of the population it enumerates, so the complete shipped population is 75. |
| Tests | The package's own 146 tests pass, and a new root contract test `tests/test_dsh_package.py` independently checks the 75-member assembly, the profile, the bundle manifest and the neutral boundary. |

## Verified

- `bin/conform adapter implementations/dsh/adapter.json` exits 0: 71 adapter files, 28 capabilities, seven parameters, no failure and no warning.
- `bin/conform self --deny-list <owner list>` exits 0 on the current tree.
- `python3 -m pytest -c implementations/dsh/pytest.ini implementations/dsh/tests` — 146 passed.
- `python3 -m pytest tests/test_dsh_package.py` — 2 passed, including 17 negative assembly controls with exact byte and mode restoration.
- `python3 -m pytest tests/test_codex_package.py tests/test_claude_package.py` — 11 passed after the declared sibling set was extended to include `dsh`.
- **Real installation into a scratch profile**: `dsh plugin --profile web add <package>` linked the package and appended `@methodology/dsh` to `dsh.profile.bundles`; `dsh --profile web --dump-config` composed a real `# == @methodology/dsh` layer carrying the expected row; and the row's loader expression resolves, from the profile directory, to the package's `skills/` directory holding 27 entries. The scratch profile was restored with `dsh plugin ... remove`.

## Not verified

- **No native behavioral acceptance.** No agent ran a methodology flow through this package: no Bootstrap-to-Finalize run, no checkpoint and resume, no independent QA or Review of a real target, and no session observed its skill catalog. The package tests and the installation check are structural and source-level.
- **No preset and no hooks.** The bundle adds a skill provider only. Per-role `persona`/`toolFilter` isolation is a deployment decision this package documents but does not impose, because crafting a preset replaces the profile's complete child-plugin list.
- **The live harness home profile was not modified.** Installation was proved on a scratch `DSH_HOME`; pointing the owner's profile at this worktree happened only there and was removed.
- **Root suite baseline.** `tests` carries 67 pre-existing failures on unmodified `main` (60 in `test_flow_contract.py`, six in `test_pm_role.py`, one stale helper-algorithm pin in `test_c1_review_and_routing.py`). A detached baseline checkout of `b8696a2` reproduces them. This work adds no failure to that set: the new DSH tests pass, and the two sibling package suites pass.
- **C1 helper pin.** `_algorithm_identity` normalizes the release and membership selectors and then compares the whole AST against a fixed pin. The DSH helper deviates in one structural line, so it cannot share the codex pin. Rather than weaken that frozen check or reshape the package to satisfy a stale literal, the DSH engine was left out of that loop. Adding it needs a reviewed pin and an explicit normalization branch, which is its own change with its own evidence.
- **A `.DS_Store` and an untracked research note** were left in the read-only harness checkout by a delegated reconnaissance reader; they are outside this repository and outside its grant, so they were not touched.

## Design note — why a bundle and not a preset

DSH makes the skill catalog the portable content layer, a bundle the installable transport and a preset the composition of one session's agent. A subagent joins its *parent's* preset revision and inherits that scope chain; neither the delegation tool nor a workflow can give a child its own instructions, skill catalog or preset. The only native lever for role separation is the fixed per-instance `persona`/`toolFilter`/`maxDepth` of a separately registered delegation tool.

So the package ships the portable layer globally, through a second skill provider that reaches every session regardless of the selected preset, and documents the isolation seam honestly instead of shipping a preset that would silently replace the deployment's whole agent surface.

## Delivery state

Source changes are on branch `dsh/m38-harness-package` in the isolated worktree `/private/tmp/methodology-m38-dsh-harness`, one writer for every path. No merge into `main`, no installation into the owner's live profile and no publication has been performed or implied.
