# methodology-claude test guide

This guide maps the eight historical M22 acceptance criteria ([technical specification](../../../examples/pm-project/specs/m22-claude-package.md)) to the shipped checks. Original private acceptance/results are unavailable in this public tree and are not transformed-export evidence. Commands and criteria below are requirements; fresh public-candidate execution is NOT_RUN at the export preparation baseline, and no native session outcome is inferred.

## Commands

From the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -c implementations/claude/pytest.ini implementations/claude/tests -p no:cacheprovider -s -v --basetemp OWNED_ABSENT_DIR
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests -p no:cacheprovider -q --basetemp OWNED_ABSENT_DIR
bin/conform adapter implementations/claude/adapter.json
bin/conform self --deny-list PRIVATE_DENY_LIST
claude plugin validate --strict implementations/claude
```

From `implementations/claude/`: `doxygen Doxyfile` must finish without a message. The package `pytest.ini` puts `skills/feature-dev/scripts`, `skills/devplan-protocol/scripts` and `hooks` on the import path; tests import the real helpers, never copies. `tests/test_workflow.py` needs Node and Python 3 on `PATH` (a missing Node fails the suite rather than skipping it) and runs the real `workflows/feature-dev.js` through `tests/workflow_harness.mjs` in two modes: scripted scenarios with an emulated recorder, and real-helper scenarios in which the recorder executes the exact commands of the spine's recorder prompt against the real `run_state.py` on an owned temporary target (the test builds a framework copy at `<tmp>/implementations/claude` with the neutral files above it and passes it as `M22_REAL_FRAMEWORK`, with `M22_REAL_WORK` as the empty work root). Roles in real mode take their identities only from the commands quoted in their prompts. `M22_WORKFLOW` lets the oracle run against another copy of the spine, used to prove that the real-helper tests fail on the pre-fix spine; `M22_REAL_SCRATCH` (supplied by the fixture, a directory under the system temporary root that is removed afterwards) is the judges' scratch root, and `M22_NO_SCRATCH=1` makes the harness omit the `scratch` argument to drive a pre-Debug-2 spine.

Every test prints its owning IMP:7–10 trace lines before asserting (`code/tests.md`). Fixtures live inside each module; the package has no `conftest.py`. Tests that need a writable package or neutral tree copy the real files into `tmp_path`.

## Criterion map

| Criterion | Checks |
|---|---|
| AC-M22-1 Assembly | Root `tests/test_claude_package.py::test_complete_claude_package` and `::test_claude_package_refusals` (independent 59-path oracle; generated `__pycache__`, `.pytest_cache`, `doxygen_output` and the git-ignored macOS `.DS_Store` are not members: missing, extra, unknown sibling, unsafe, absolute, duplicate, profile, detached, linked, malformed, wrong kind, package runtime footprint, role map). Root `tests/test_codex_package.py` still refuses an unknown sibling. Package `test_package_contract.py::test_layout_matches_members`. |
| AC-M22-2 Adapter and privacy | `bin/conform adapter implementations/claude/adapter.json`; `bin/conform self` with the private deny lists; root `tests/test_claude_package.py::test_claude_publication_channels` plants every canary in agent, hook, workflow, harness, skill and adapter carriers; package `test_package_contract.py::test_manifest_and_adapter` recomputes the neutral population and registries. |
| AC-M22-3 Package behavior | `test_package_contract.py` (agents' models and tools, judges without Edit/Write, no delegating role, skill parity and invocation modes, every `${CLAUDE_PLUGIN_ROOT}` reference resolves, hooks wiring); `test_session_start.py` (real binding, BLOCKED reasons, orientation); `test_guard.py` (ask, deny, silence, read-only agent types, scope switch; judges' git ref, config and fetch changes including abbreviated long options, file-changing forms such as `chmod --ref`, `sed -Ei`, `cp -t`, branch listing forms kept silent, owned helper traces); `test_run_state.py` (identity, schema, Debug cap types and routes, eight named scans, retries, terminal and Finalize, real CLI checkpoint/resume; candidate identity over real git targets: an ignored Anti-Loop counter, an ignored map and an ignored virtual environment never change the candidate or block QA-to-Debug, unignored files and links still do, the regenerable names stay excluded without ignore entries, non-git and subdirectory targets use the declared fallback, failed ignore enumeration is refused; git runs hermetically — a repository-configured fsmonitor program never runs and a foreign GIT_DIR or index does not change the candidate; an ambient `.DS_Store` does not break the binding and a membership refusal names the offending paths); `test_visual_gate.py`; `test_workflow.py` (scripted spine scenarios, plus real-helper routes: green, Code/QA/Review-origin Debug, cumulative entries, cap 0, Debug BLOCKED, bound plan, visual PASS, Doxygen prohibition arm, and one discriminating negative per spine-to-helper rule; git targets with and without ignore rules for the Anti-Loop counter and an ignored map; judge scratch evidence imported and accepted by the real helper; the real guard run over every write location the judge prompts grant (silent) and every in-project path they name (denied); recorder transport, checksum and diagnostic-path rules; precheck refusals that copy nothing for a partial, existing-destination or link citation; case-insensitive and alias-aware import names; run-namespaced judge directories; plan commands without a fixed in-target sink). |
| AC-M22-4 Loadable plugin | `claude plugin validate --strict implementations/claude` and `claude plugin details` on the in-place package. |
| AC-M22-5 Maps | Root `doxygen Doxyfile` and package `doxygen Doxyfile` silent; the workflow script is excluded from the map because this Doxygen setup has no JavaScript parser, and carries its contract in comments. |
| AC-M22-6 Real session | Headless `claude -p --plugin-dir implementations/claude` in an owned scratch project: SessionStart binding context, a plugin skill resolved, a plugin role agent dispatched that reads a neutral owner in place. |
| AC-M22-7 Regression | Full root suite and the Codex package suite. |
| AC-M22-8 Independent judgment | Independent QA (Sonnet) and Review (Opus) of the whole delta; findings and fixes in the result note. |

## Limits

Structural tests prove assembly, reference resolution and helper behavior. They do not prove that a live session read the owners in full, that judges never write through Bash, or any model effect. The workflow harness proves the spine's routing over scripted returns, not real agent quality.
