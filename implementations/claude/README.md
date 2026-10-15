# Methodology Claude

Native Claude Code package 2.0.1 for the neutral methodology 3.0.1 of this repository. It is a Claude Code plugin named `methodology-claude` that binds the neutral rules in place: its skills and role agents point at the neutral owners two levels up, its hooks check that binding, and its adapter accounts for every neutral file, capability and parameter.

## Load it

The package must stay inside a complete checkout of this repository. Load it in place:

```sh
claude --plugin-dir <checkout>/implementations/claude
```

That loads it for one session. For every session, desktop sessions included, set `CLAUDE_CODE_PLUGIN_DIRS` to the same path in the `env` of the user settings (Claude Code 2.1.280 or later); the plugin then loads in place as `methodology-claude@inline`. Keep that checkout on `main` as the repository README's Local use section describes. A local directory marketplace also loads it in place, but only when the marketplace root contains this directory: a plugin source must start with `./` and may not contain `..`. Any install that copies the plugin elsewhere (a git marketplace, the plugin cache) loses the neutral files above it and is unsupported; the SessionStart hook then reports the binding as BLOCKED. A symlink to this directory under a discovered skills directory is unsupported as well: the plugin loads and the hook, which resolves real paths, reports it bound, but `${CLAUDE_PLUGIN_ROOT}` keeps the link path, so every `../../` reference of the skills and agents misses.

Check the plugin and see what it contains:

```sh
claude plugin validate --strict <checkout>/implementations/claude
claude plugin details methodology-claude
```

## What it contains

| Part | Content |
|---|---|
| `skills/` | 23 topics with the same names as the Codex package (for example `pm`, `feature-dev`, `semantic-exoskeleton`, `devplan-protocol`, `brainstorm`) and 5 owner-invoked lifecycle commands: `pm-bootstrap`, `pm-plan-batch`, `pm-run-batch`, `pm-handoff`, `pm-review-run`. Invoke as `/methodology-claude:<name>`. |
| `agents/` | Six role subagents — `architect` and `reviewer` on opus, `coder`, `qa` and `debugger` on sonnet, `searcher` on haiku. The judges `qa`, `reviewer` and `searcher` have no Edit or Write tools; no role can delegate. |
| `hooks/` | SessionStart: verifies the in-place binding and orients on the target's records. PreToolUse on Bash: asks before unrecoverable commands and denies tree-changing commands to the judges. |
| `workflows/feature-dev.js` | Workflow `/methodology-claude:feature-dev-workflow`: deterministic spine Bootstrap → Architect → Code → QA → Review → Finalize with counted Debug, run only on the owner's explicit opt-in. |
| `skills/feature-dev/scripts/run_state.py` | Durable run state (schema 2) with locked inputs, cumulative Debug spend and refusals. |
| `skills/devplan-protocol/scripts/visual_gate_lint.py` | Mechanical visual-gate check for development plans. |
| `adapter.json`, `references/` | Adapter (71 files, 28 capabilities, 7 parameters), [runtime](references/claude-runtime.md), [handoffs](references/handoffs.md), [adoption](references/adoption.md), [source disposition](references/source-disposition.md), [layout](references/package-layout.json). |

Read the [runtime](references/claude-runtime.md) before using `pm` or `feature-dev`. Typical entry points: `/methodology-claude:pm` to resume a project checkpoint, `/methodology-claude:pm-plan-batch` and `/methodology-claude:pm-run-batch` for a batch, `/methodology-claude:feature-dev` with an approved specification, `/methodology-claude:pm-handoff` at the end of a session.

## Checks

From the repository root:

```sh
bin/conform adapter implementations/claude/adapter.json
python3 -m pytest -c implementations/claude/pytest.ini implementations/claude/tests -p no:cacheprovider -s -v
python3 -m pytest tests -p no:cacheprovider -q
```

From `implementations/claude/`: `doxygen Doxyfile` builds the package's own code map silently. The common checker validates the adapter contract, not the package's native semantics; the package suite and the root assembly test (`tests/test_claude_package.py`) cover those. The [test guide](tests/test_guide.md) maps each acceptance criterion to its checks.

## Limits

In-place loading only. No detached install, automatic discovery, publication or change to the user's global Claude configuration is supplied. Judges' Bash commands are restrained by their carriers and the guard hook, not by a sandbox. A SUCCESS of a run never authorizes merge, installation or publication; those stay the owner's decisions.
