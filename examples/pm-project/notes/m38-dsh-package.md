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
| Inventory | `references/package-layout.json` declares 75 members; it declared 74 before the subagent/workflow reference joined after the original review. The package map is deliberately not a member of the population it enumerates, so the complete shipped population is 76. |
| Tests | The package's own 146 tests pass, and a new root contract test `tests/test_dsh_package.py` independently checks the 75-member assembly, the profile, the bundle manifest and the neutral boundary. |

## Verified

The measurements in this section and the next were taken on the pre-rebase package at the original review. The rebase validation is under [Delivery state](#delivery-state).

- `bin/conform adapter implementations/dsh/adapter.json` exits 0: 71 adapter files, 28 capabilities, seven parameters, no failure and no warning.
- `bin/conform self --deny-list <owner list>` exits 0 on the current tree.
- `python3 -m pytest -c implementations/dsh/pytest.ini implementations/dsh/tests` — 146 passed.
- `python3 -m pytest tests/test_dsh_package.py` — 2 passed, including 17 negative assembly controls with exact byte and mode restoration.
- `python3 -m pytest tests/test_codex_package.py tests/test_claude_package.py` — 11 passed after the declared sibling set was extended to include `dsh`.
- **Real installation into a scratch profile**: `dsh plugin --profile web add <package>` linked the package and appended `@methodology/dsh` to `dsh.profile.bundles`; `dsh --profile web --dump-config` composed a real `# == @methodology/dsh` layer carrying the expected row; and the row's loader expression resolves, from the profile directory, to the package's `skills/` directory holding 27 entries. The scratch profile was restored with `dsh plugin ... remove`.

## Verified in the follow-up round

- **The package map builds.** `doxygen Doxyfile` from this package exits 0 and produces 53 XML files in its own `doxygen_output/`, covering all six helpers (`run_state`, `orient`, `codemap`, `consumer_files`, `markup_migrate`, `visual_gate_lint`) by their own source, entity and location fields. The output directory is ignored by the root `.gitignore`, so the build leaves the tree clean.
- **Every skill card is valid for the harness.** All 27 `SKILL.md` files open with a well-formed card, carry `name` equal to their directory and a non-empty `description`, use only those two keys, and each `name` matches the harness's kebab-case rule. A malformed card would make the harness drop that skill silently with a warning, so this is the check that the catalog is complete rather than merely present.
- **The installation holds on a fresh profile.** Repeated on a second, empty scratch harness home: `dsh plugin --profile web add` appended `@methodology/dsh` to `dsh.profile.bundles`, `--dump-config` composed exactly one `# == @methodology/dsh` layer with the expected row, and that row resolved to the package's `skills/` directory holding 27 entries for every baseUrl form the loader can supply (the profile directory as a path, as a file URL, and the profile's config file). Both scratch homes were then removed.
- **Conformance still holds after the document corrections.** `bin/conform self` exits 0 and `bin/conform adapter implementations/dsh/adapter.json` exits 0 with 76 passes and no warning.

Three factual corrections came out of this review, each inherited verbatim from the sibling package and wrong here: the composition line claimed 73 members (this package declares 74 and ships 75); `source-disposition.md` named neutral 1.1.0 against the current 3.0.1; and both references closed with a paragraph about the Claude package that has no bearing on this one. The package's own documents now match its measured composition.

## Not verified

This section records the state at the original review. Later installation, rebase and merge are under [Delivery state](#delivery-state).

- **No native behavioral acceptance.** No agent ran a methodology flow through this package: no Bootstrap-to-Finalize run, no checkpoint and resume, no independent QA or Review of a real target, and no session observed its skill catalog. The package tests and the installation check are structural and source-level.
- **No preset and no hooks.** The bundle adds a skill provider only. Per-role `persona`/`toolFilter` isolation is a deployment decision this package documents but does not impose, because crafting a preset replaces the profile's complete child-plugin list.
- **The live harness home profile was not modified.** Installation was proved on a scratch `DSH_HOME`; pointing the owner's profile at this worktree happened only there and was removed.
- **Root suite baseline.** `tests` carries 67 pre-existing failures on unmodified `main` (65 in `test_flow_contract.py`, one in `test_pm_role.py`, one stale helper-algorithm pin in `test_c1_review_and_routing.py`). A detached baseline checkout of `b8696a2` reproduces them. This work adds no failure to that set: the new DSH tests pass, and the two sibling package suites pass.
- **C1 helper pin.** `_algorithm_identity` normalizes the release and membership selectors and then compares the whole AST against a fixed pin. The DSH helper deviates in one structural line, so it cannot share the codex pin. Rather than weaken that frozen check or reshape the package to satisfy a stale literal, the DSH engine was left out of that loop. Adding it needs a reviewed pin and an explicit normalization branch, which is its own change with its own evidence.
- **A `.DS_Store` and an untracked research note** were left in the read-only harness checkout by a delegated reconnaissance reader; they are outside this repository and outside its grant, so they were not touched.

## Design note — why a bundle and not a preset

DSH makes the skill catalog the portable content layer, a bundle the installable transport and a preset the composition of one session's agent. A subagent joins its *parent's* preset revision and inherits that scope chain; neither the delegation tool nor a workflow can give a child its own instructions, skill catalog or preset. The only native lever for role separation is the fixed per-instance `persona`/`toolFilter`/`maxDepth` of a separately registered delegation tool.

So the package ships the portable layer globally, through a second skill provider that reaches every session regardless of the selected preset, and documents the isolation seam honestly instead of shipping a preset that would silently replace the deployment's whole agent surface.

## Delivery state

The package was built on an isolated scoped branch, one writer for every path. The owner then approved the `main` merge and the live installation: «надо смержить и поставить в профиль этот бандл». The first delivery was a local fast-forward of `af7eab7` into the canonical checkout, followed by installation into the `web` profile and then into the `desktop` profile that the DSH GUI actually runs; see [the first-run note](m38-run-01.md) and [TASKS](../TASKS.md). Both profiles keep their previous `package.json` and `cordis.patch.yml` beside them as `.bak-m38` for one-step rollback. That local fast-forward never reached `origin/main` and is superseded.

After M37 merged, the owner granted a rebase, conflict resolution and push. The full M38 history was rebased onto the M37 merge `380dd00`, with HANDOFF/TASKS/C1 conflicts resolved so that both checkpoints, the M37 records, the Claude 2.1.0 assertions and the M37 Python 3.12 helper pins were kept. The DSH package stayed byte-identical to its pre-rebase tip and no source helper changed. An independent read-only verifier confirmed ancestry, executable C1 equality with upstream, links, M37 carryover and the interpreter explanation for the pins; it reported no blocking findings and no writes outside the three resolution paths.

Rebase validation on Python 3.12, 2026-10-19:

- root `pytest -q tests`: 605 passed;
- DSH package suite: 146 passed;
- focused C1 tests: 6 passed;
- DSH adapter conformance: exit 0, 76 passes, no warnings or failures;
- `git diff --check`: passed;
- `bin/conform self`: not run, because its private deny list was not supplied.

The owner then merged the rebased branch into `origin/main` through PR10 (merge `1ff633c`, 2026-10-19); the merged tree equals the verified rebase tip. The source is public through that merge. A packaged release remains a separate decision. The live profiles were not re-probed after the merge.

### Root-suite repairs during M38

Before the rebase, M38 saw the C1 helper-algorithm pin test fail, diagnosed the two pin literals as stale after a normalizer rewrite and recalibrated them (`037ed5f`). That measurement was taken under Python 3.9. The failure is interpreter-bound: Python 3.9's AST omits empty `type_params` fields, so the same helpers hash differently, and the upstream pins pass under Python 3.12. The rebase therefore kept the upstream pins. The merged tree carries no recalibration; `tests/test_c1_review_and_routing.py` gained only contract comments: a rebase note, a LAST_CHANGE entry and a clarified `@io` guarantee.

M38's evidence that the helper algorithm did not change still holds. It was established twice, independently:

- the pinned and current helper sources normalize to byte-identical ASTs;
- the only differing string constants across the two revisions are release values;
- every injected drift control (schema version, `max_debug`, `profile_cap`, neutral version, a missing or duplicated selector) still changes the identity.

M38's further claim about the provenance of the old pin literals was also a Python 3.9 measurement and is not relied on.

The same work exposed a markup defect: `tests/test_dsh_package.py` placed its import block against the contract region, which `test_code_layer.py` refuses. It is fixed.

The C1 pin keeps three residual risks:

1. A pin cannot separate an intentional algorithm change from drift. Whoever edits the helper can re-pin it, so the control list in the test body is what refuses a wrong release value, and any re-pin must be reviewed against the source delta.
2. The pin covers the pinned function's own docstring, so a documentation-only edit inside that function forces a re-pin.
3. The DSH helper stays outside that pin loop: its membership selector has a different shape, it carries a second membership set and its contract version is its own. Joining the loop needs a reviewed normalization branch, not a weakened check.

A delegated reconnaissance reader had written its report into this repository's root. It is now owned by the package as [the DSH subagent/workflow reference](../../../implementations/dsh/references/dsh-subagent-workflow.md) and declared in the layout.
