# Methodology Claude

Native Claude Code package 2.2.1 for the neutral methodology 3.1.1 of this repository. It is a Claude Code plugin named `methodology-claude` that binds the neutral rules in place: its skills and role agents point at the neutral owners two levels up, its hooks check that binding, and its adapter accounts for every neutral file, capability and parameter.

## Load it

The package must stay inside a complete checkout of this repository. Load it in place:

```sh
claude --plugin-dir <checkout>/implementations/claude
```

That loads it for one session. For every session, desktop sessions included, set `CLAUDE_CODE_PLUGIN_DIRS` to the same path in the `env` of the user settings (Claude Code 2.1.280 or later); the plugin then loads in place as `methodology-claude@inline`. Keep that checkout on `main` as the repository README's Local use section describes. Any marketplace install copies the plugin elsewhere and is unsupported: Claude Code 2.1.299 copies a plugin from a git or even a local directory marketplace into its plugin cache without the neutral files above it, and the SessionStart hook then reports the binding as BLOCKED. A symlink to this directory under a discovered skills directory is unsupported as well: the plugin loads and the hook, which resolves real paths, reports it bound, but `${CLAUDE_PLUGIN_ROOT}` keeps the link path, so every `../../` reference of the skills and agents misses.

Check the plugin and see what it contains:

```sh
claude plugin validate <checkout>/implementations/claude
claude plugin details methodology-claude
```

Read the validation output. Claude Code 2.1.299 warns that the name `methodology-claude` reads as one of Anthropic's own; the name is kept because it is the namespace of the role agents (`methodology-claude:<role>`), so `--strict`, which turns that warning into an error, fails. The manifest is valid when that name warning is the only warning.

## What it contains

| Part | Content |
|---|---|
| `skills/` | 23 topics with the same names as the Codex package (for example `pm`, `feature-dev`, `semantic-exoskeleton`, `devplan-protocol`, `brainstorm`) and 5 owner-invoked lifecycle commands: `pm-bootstrap`, `pm-plan-batch`, `pm-run-batch`, `pm-handoff`, `pm-review-run`. Invoke as `/methodology-claude:<name>`. |
| `agents/` | Six role subagents — `architect` and `reviewer` on opus, `coder`, `qa` and `debugger` on sonnet, `searcher` on haiku. The judges `qa`, `reviewer` and `searcher` have no Edit or Write tools; no role can delegate. |
| `hooks/` | SessionStart: verifies the in-place binding and orients on the target's records. PreToolUse on Bash: asks before unrecoverable commands and denies tree-changing commands to the judges. |
| `bin/` | `orient`, `codemap`, `markup-migrate`: launchers of the opt-in consumer PM profile. They run the sibling Codex C2 helpers in place and report BLOCKED when the sibling is missing. |
| `workflows/feature-dev.js` | Workflow `/methodology-claude:feature-dev-workflow`: deterministic spine Bootstrap → Architect → Code → QA → Review → Finalize with counted Debug, run only on the owner's explicit opt-in. |
| `skills/feature-dev/scripts/run_state.py` | Durable run state (schema 2) with locked inputs, cumulative Debug spend and refusals. |
| `skills/devplan-protocol/scripts/visual_gate_lint.py` | Mechanical visual-gate check for development plans. |
| `adapter.json`, `references/` | Adapter (71 files, 28 capabilities, 7 parameters), [runtime](references/claude-runtime.md), [handoffs](references/handoffs.md), [adoption](references/adoption.md), [source disposition](references/source-disposition.md), [layout](references/package-layout.json), [consumer PM profile](references/consumer-pm-profile.md). |

Each of the 23 model-invoked skill descriptions opens with a Russian use-case label and Russian trigger phrases, followed by the unchanged English description, because the adapter binds `dialog-language` to Russian. In live probes on 2026-10-19, Russian phrases placed after the English text did not fire `prompting-verify` (0 of 3), while the same phrases placed first did (3 of 3). The five lifecycle commands keep `disable-model-invocation: true`: Claude Code keeps their descriptions out of the model's context, so only their slash commands invoke them.

Read the [runtime](references/claude-runtime.md) before using `pm` or `feature-dev`. Typical entry points: `/methodology-claude:pm` to resume a project checkpoint, `/methodology-claude:pm-plan-batch` and `/methodology-claude:pm-run-batch` for a batch, `/methodology-claude:feature-dev` with an approved specification, `/methodology-claude:pm-handoff` at the end of a session.

## Consumer PM profile

A project that explicitly adopts `methodology-consumer-pm/1.0.0` uses the same profile as the Codex package, by reference: the [carrier](references/consumer-pm-profile.md) states the Claude deltas and points at the Codex carrier, seeds and helpers. While the package is loaded in place, its `bin/` directory is on the Bash tool's PATH, but another enabled plugin can ship a command of the same name and PATH order between plugins is not specified. Run `orient`, `codemap` or `markup-migrate` by bare name only when `command -v <cmd>` resolves to this package's `bin/<cmd>`; otherwise call the launcher by its absolute path, and always do so for `markup-migrate --apply`. Adoption is an owner-granted `pm-bootstrap` step; nothing in this package changes a consumer project, a user setting or the global PATH.

## Checks

From the repository root:

```sh
bin/conform adapter implementations/claude/adapter.json
python3 -m pytest -c implementations/claude/pytest.ini implementations/claude/tests -p no:cacheprovider -s -v
python3 -m pytest tests -p no:cacheprovider -q
python3 -m pytest -c implementations/claude/pytest.ini implementations/claude/tests/test_consumer_profile.py -p no:cacheprovider -s -v
python3 -m pytest tests/test_claude_consumer_bridge.py -p no:cacheprovider -q
```

Run the launcher tests under both the system Python 3.9 and Python 3.12.

From `implementations/claude/`: `doxygen Doxyfile` builds the package's own code map silently. The common checker validates the adapter contract, not the package's native semantics; the package suite and the root assembly test (`tests/test_claude_package.py`) cover those. The [test guide](tests/test_guide.md) maps each acceptance criterion to its checks.

## Limits

In-place loading only. No detached install, automatic discovery, publication or change to the user's global Claude configuration is supplied. Judges' Bash commands are restrained by their carriers and the guard hook, not by a sandbox. A SUCCESS of a run never authorizes merge, installation or publication; those stay the owner's decisions.

The consumer PM profile needs the sibling Codex package of the same checkout; a missing sibling is BLOCKED. Claude Code documentation states that claude.ai and Cowork do not install a plugin with a top-level `bin/` directory; this package is a Claude Code in-place package only.
