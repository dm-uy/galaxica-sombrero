# Consumer PM profile for Claude Code — methodology-claude 2.1.1

Identity: `methodology-consumer-pm/1.0.0`, opt-in only, carried by reference. The Claude package does not copy the profile. Its complete statement — adoption and homes, operational forms and routes, the 13 seeds, the command contracts and supported input, the deliberately held capacities, the 75 source duties and the 22 checker rows — is the Codex carrier [consumer-pm-profile.md](../../codex/references/consumer-pm-profile.md) (`${CLAUDE_PLUGIN_ROOT}/../codex/references/consumer-pm-profile.md`). Read it in full whenever a target adopts or uses the profile. The scripts and seeds are the accepted Codex C2 files under `${CLAUDE_PLUGIN_ROOT}/../codex/skills/pm/`; where the Codex carrier writes `PACKAGE/skills/pm/`, the Claude package means that directory. Wire `methodology-claude/1.0.0`, run-state schema 2 and the six roles are unchanged.

This file adds no duty and weakens none. It states only the five Claude Code deltas below. Where it and the Codex carrier or a neutral owner seem to differ, the Codex carrier and the neutral owners win and the difference is a package defect. The profile needs the complete checkout: the package is loaded in place ([runtime](claude-runtime.md)), and a missing sibling Codex package is BLOCKED, never replaced by another copy.

## Claude Code deltas

### 1. Invocation

While the package is loaded in place, its `bin/` directory is on the Bash tool's PATH. Another enabled plugin may ship a command of the same name in its own `bin/` (for example `codemap` or `markup-migrate`), and the PATH order between plugins is not specified, so a bare name can start a different copy. Run a command by bare name only after `command -v <cmd>` resolves to `${CLAUDE_PLUGIN_ROOT}/bin/<cmd>`; otherwise call that launcher by its absolute launcher path. `markup-migrate --apply` writes into the consumer project, so `markup-migrate --apply` always uses the absolute launcher path. The three commands and their launchers:

| Command | Launcher file | Runs |
|---|---|---|
| `orient PROJECT [--check]`; `orient --portfolio ROOT [ROOT ...] [--roots-file FILE] [--check]` | `${CLAUDE_PLUGIN_ROOT}/bin/orient` | `python3 -B ${CLAUDE_PLUGIN_ROOT}/../codex/skills/pm/scripts/orient.py` |
| `codemap PROJECT TARGET` | `${CLAUDE_PLUGIN_ROOT}/bin/codemap` | `python3 -B ${CLAUDE_PLUGIN_ROOT}/../codex/skills/pm/scripts/codemap.py` |
| `markup-migrate PROJECT [--check \| --apply] [--file REL ...] [--python EXEC ...] [--approval-record FILE] [--receipt-dir DIR]` | `${CLAUDE_PLUGIN_ROOT}/bin/markup-migrate` | `python3 -B ${CLAUDE_PLUGIN_ROOT}/../codex/skills/pm/scripts/markup_migrate.py` |

A launcher resolves its own real path, then the package root, then the sibling script. It runs that script with the current interpreter and `-B`, passes every argument unchanged, adds no default project and no option, and leaves the script's own streams and exit status to the caller, also when the caller closed stdout or stderr. When the sibling is missing, not a regular file or outside the checkout, it prints one `methodology-claude BLOCKED:` line naming the expected path to stderr and exits 2. It never searches PATH, the working directory or an installed copy for its sibling; which launcher starts is decided before it runs, by the name or path the caller types. The explicit `python3 -B` forms are the same contract when the plugin's `bin/` is not on PATH. Launchers run only in roles that have Bash; the read-only searcher has none and navigates through the current Doxygen map or a codemap answer its parent supplies. `markup-migrate --apply` writes into the consumer project and runs only by the root or an assigned writer under the Codex carrier's apply conditions, never by a judge. `METHODOLOGY_LAUNCHER_LOG`, set to a level name, shows the launcher's own trace on stderr; `ORIENT_LOG`, `CODEMAP_LOG` and `MARKUP_MIGRATE_LOG` keep their Codex meaning.

### 2. Consent

Profile adoption, seed materialization, migration of existing records, a markup-migration apply and the optional per-project hook each need the owner's exact grant, asked with AskUserQuestion and recorded verbatim with the date, the artifact and the scope (runtime section 5). An explicit chat approval counts only where AskUserQuestion is genuinely unavailable, such as a headless print session, and is recorded verbatim. A template, a worker's message or a structured record never authenticates consent; a fictional probe's fixture-local grant authorizes only that fixture, is recorded verbatim and never stands in for a consumer's batch or result gate.

### 3. Delegation model

Every delegation the root makes under the profile passes `model` explicitly, chosen by the task's hardest step under `policies/models.md` (runtime section 3). The requested model is recorded; the observed model only when the host exposes it.

### 4. No package hook

The package adds no hook for the profile. `hooks/hooks.json` keeps exactly its SessionStart binding check and its Bash guard, and nothing in the package registers a PATH entry beyond the plugin's own `bin/`, changes a user or plugin setting, or edits a consumer project.

### 5. Optional per-project SessionStart hook

Only under an explicit per-project grant (delta 2), `pm-bootstrap` may add a machine-local SessionStart command to the consumer's `.claude/settings.local.json` that runs the absolute `orient` launcher on `$CLAUDE_PROJECT_DIR`. Merge it into the existing settings without changing other keys. Before writing, confirm that the file is ignored by the project's version control (`git check-ignore -q .claude/settings.local.json`); otherwise add an ignore rule only under its own grant. `<checkout>` stands for the absolute path of the complete methodology checkout on that machine; never write it into a tracked file. Nothing in this repository installs the hook, and deleting the entry removes it.

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume|clear|compact",
        "hooks": [
          {
            "type": "command",
            "command": "\"<checkout>/implementations/claude/bin/orient\" \"$CLAUDE_PROJECT_DIR\" 2>&1 || true",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

A SessionStart hook cannot stop a session. `|| true` keeps the exit status 0, so the orient report reaches the session context even when the project is not assessable; an unavailable result is read as such, never as PASS. `2>&1` carries a launcher `methodology-claude BLOCKED:` line, which is written to stderr, into the same context; without it a missing sibling Codex package would leave the context empty.
