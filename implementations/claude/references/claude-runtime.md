# Claude Code runtime — methodology-claude 1.0.0

This is the runtime procedure of the native Claude Code package for neutral methodology 1.1.0. It says how Claude Code carries the neutral rules; it restates none of them. Where this file and a neutral owner seem to differ, the neutral owner wins and the difference is a package defect.

## 1. Profile and binding

Profile `colocated-in-place`. The package lives at `implementations/claude/` of a complete methodology checkout and is loaded in place:

```sh
claude --plugin-dir <checkout>/implementations/claude
```

for one session, through `CLAUDE_CODE_PLUGIN_DIRS` set to the same path in the `env` of the user settings for every session (Claude Code 2.1.280 or later; source `methodology-claude@inline`), or through a local directory marketplace whose root contains this directory (a plugin source must start with `./` and may not contain `..`). All three load it in place. A symlink to this directory under a discovered skills directory is unsupported: `${CLAUDE_PLUGIN_ROOT}` keeps the link path and every `../../` reference misses, although the SessionStart hook, which resolves real paths, reports the binding bound. Inside Claude Code the package root is `${CLAUDE_PLUGIN_ROOT}` and the neutral root is `${CLAUDE_PLUGIN_ROOT}/../../`. `adapter.json` resolves `spec_root` (`../../`) from its own directory, so the caller's working directory never changes the binding.

The SessionStart hook checks the binding at every start, resume, clear and compaction: adapter, `SPEC_VERSION` equal to the adapter's `spec_version`, the package layout identity and the six core owners present as drafts. A failed check is reported as BLOCKED in the session context. A copied install (git marketplace, plugin cache) has no neutral root above it and is unsupported: dependent methodology work stops; never fall back to an older installed copy of these practices.

## 2. Entry and orientation

At entry or resume the root (the main session acting for the owner) reads in full `checks/orient.md`, `checks/preflight.md`, `checks/run-audit.md` and `process/safety.md` before the assessments they govern, then the target's entry instructions (`AGENTS.md`, `CLAUDE.md`) and its five durable records (purpose, route, tasks, handoff, instructions) where the project keeps them. Orient and preflight are performed with real reads and permitted commands; the hook output is a pointer, not the assessment. Run all cheap independent checks even after one fails, and withhold only the dependent effects. Read-only work needs no clean tree.

Required reading follows [adoption](adoption.md): the six core owners before any software role acts, the assigned role owner and `protocols/role-returns.md`, and the owners named by the applicable skill. A link, card, hash or summary is not a read. A required owner that is missing, a stub, truncated or unread blocks dependent action.

## 3. Roles, models and permissions

The package ships six role carriers as Claude subagents under `agents/`. The root dispatches them as `methodology-claude:<role>`:

| Role | Phase | Model tier | Tools |
|---|---|---|---|
| `searcher` | Bootstrap, bounded reconnaissance | `haiku` (mechanical) | Read, Glob, Grep |
| `architect` | Architect; separately assigned Finalize | `opus` (judgment) | Read, Glob, Grep, Write, Edit, Bash, TodoWrite, Skill, WebSearch, WebFetch |
| `coder` | Code | `sonnet` (routine from an approved plan) | Read, Glob, Grep, Write, Edit, Bash, TodoWrite, Skill, WebSearch, WebFetch |
| `qa` | independent QA | `sonnet` (verification) | Read, Glob, Grep, Bash, TodoWrite, Skill |
| `reviewer` | independent Review | `opus` (whole-result judgment) | Read, Glob, Grep, Bash, Skill |
| `debugger` | Debug | `sonnet` (diagnosis with a trace) | Read, Glob, Grep, Write, Edit, Bash, TodoWrite, Skill, WebSearch, WebFetch |

The root (PM, or the feature-dev parent) is the only orchestrator: no carrier has the Agent tool, so inner roles cannot delegate. Every delegation also passes `model` explicitly, chosen by the task's hardest step under `policies/models.md`; a task with one judgment step and much routine work is split. The requested model is recorded; the observed model only when the host exposes it.

Hard limits: the judges `qa`, `reviewer` and `searcher` have no Edit, Write or NotebookEdit. The PreToolUse guard denies tree-changing Bash commands to the read-only agent types and asks before commands that would lose unrecoverable state. Behavioral limits: Claude Code ignores `permissionMode` in plugin agents, so other Bash writes by a judge are restrained by its carrier, not by a sandbox. The guard is a tripwire, not a sandbox, and the root's before/after `git status` audit is the backstop. For judges it denies the recognized forms inside the project — redirects, `tee`, `cp`, `mv`, `rm`, `touch`, `sed -i` (GNU spellings), `chmod`, `chown`, `truncate`, `ln`, `install`, `dd of=`, `perl -i`, and the git verbs listed in the guard's contract (branch and config writes, fetch, update-ref, worktree changes, commit-, merge-, reset- and checkout-family verbs) — matching long options of `git branch`, `git config` and the GNU file commands by unique prefix. It does not intercept, among others, `mkdir`, `rsync`, `tar -x`, `curl -o`, `python -c`, `eval`, `xargs sh -c`, `bash -lc`, `patch`, BSD `sed -I`, the `>|` redirect, or git verbs such as `bisect`, `update-index`, `checkout-index`, `read-tree`, `symbolic-ref`, `gc` and `remote add`. For every agent the ask path covers the exact destructive spellings the guard lists (for example `git reset --hard`, `git clean -f`, `git push --force`, `git branch -D`); abbreviated long options and separately written `-d -f` are not recognized there. It watches only the session project and its git worktrees. The root records `git status` before each dispatch and reports every write outside the granted paths afterwards; it never reverts another writer's change itself.

Reading a carrier or an owner confers no role. A carrier acts only on an explicit parent assignment.

## 4. Delegation

Each assignment is self-contained (`flow/delegation.md`): absolute target, specification, plan and package roots; the neutral root; exact MAY EDIT and DO NOT TOUCH paths; evidence and scratch roots; classifiers with their evidence; the logging idiom; the output contract. One writer per path. Independent QA and Review inspect a stable candidate and write their own outputs only under a scratch root the assignment grants outside the target (`roles/qa.md` QA-206); the root imports what they cite into the run's evidence home. Use `isolation: worktree` or an owned branch worktree only where parallel writers would otherwise collide.

Two root embodiments exist:

- **Interactive root** — the main session follows `skills/feature-dev` and dispatches each phase with the Agent tool, validating each return and recording it with the run-state helper. This is the default.
- **Workflow spine** — `workflows/feature-dev.js` (`/methodology-claude:feature-dev-workflow`) sequences the phases deterministically with per-phase schemas. It runs only on the owner's explicit opt-in (invoking `pm-run-batch` is that opt-in for its M tasks). Workflow scripts have no filesystem access, so the spine persists state through a recorder step that runs the helper; the root initializes the run before starting the spine and reads the returned `ledgerNote` for any outcome the ledger cannot represent. Its required `scratch` argument names a root outside the target where the judges write; the recorder imports the judges' cited files into the run's evidence home. A thrown role agent ends the run BLOCKED as a transport failure and is never replayed automatically; a lost recorder also ends it BLOCKED because the ledger outcome is unknown ([handoffs](handoffs.md)).

## 5. Gates and consent

Owner decisions use AskUserQuestion (`process/gates.md`): the specification or batch decision before implementation, and the concrete-result decision before any merge, publication or deployment. Record the owner's words, date, the exact artifact identity, the action and the scope. Reuse an existing matching approval instead of asking again. An explicit chat approval counts only where AskUserQuestion is genuinely unavailable (a headless print session), recorded verbatim. Silence, a timeout, a default option, a worker's message or a tool result is never consent. A rejection authorizes no destructive rollback. Plan mode, when the owner selects it, is left only through its explicit approval.

## 6. Run state and repair

The root is the single state writer. It initializes the run once with the exact framework, adapter, specification, plan and approval reference, and records only verified phase returns ([handoffs](handoffs.md)):

```text
python3 ${CLAUDE_PLUGIN_ROOT}/skills/feature-dev/scripts/run_state.py init --project TARGET --spec SPEC --approval APPROVAL_REFERENCE --framework ${CLAUDE_PLUGIN_ROOT} --adapter ${CLAUDE_PLUGIN_ROOT}/adapter.json --plan PLAN --run-id RUN_ID --max-debug 4
python3 ${CLAUDE_PLUGIN_ROOT}/skills/feature-dev/scripts/run_state.py show --state STATE
python3 ${CLAUDE_PLUGIN_ROOT}/skills/feature-dev/scripts/run_state.py record --state STATE --result VERIFIED_RECORD_JSON_FILE
```

State lives at `<target>/.methodology/runs/<run-id>/state.json` (schema 2, atomic UTF-8). The ordinary route is Bootstrap → Architect → Code → QA → Review → separately assigned Architect Finalize → SUCCESS. Code, QA and Review defects share one cumulative Debug allowance: default 4, lowered to any nonnegative integer (0 valid); an extension above 4 is BLOCKED because the package has no supported bounded grant mechanism yet. The spend is recorded before each entry and never refunded. Debug FIXED renews full independent QA and the affected Review. Each phase attempt gets at most one response correction; a second unusable return ends BLOCKED, or ESCALATED_FINALIZE in Finalize. An unknown side-effect outcome is investigated before any replay. Terminal statuses are SUCCESS, SPEC_BLOCKED, VISUAL_GATE_FAIL, ESCALATED, BLOCKED, ERROR and ESCALATED_FINALIZE; a terminal run never resumes automatically. Before resuming, run `show`, inspect the real artifacts and keep every counter and history entry. The helper checks structure and order; it proves neither the truth of a return, nor independence, nor consent.

## 7. QA scans and delivery evidence

QA accounts all eight named scans of `checks/qa-scans.md` at their real timing: text scans before trusting the suite, runtime trace, delivery and stream checks after the producing operations. Green tests, captured logs and mocks prove neither a real sink nor overall success: a declared deliverable or a process boundary needs an actual endpoint, CLI, file or channel proof. A false-trigger N/A never waives a required criterion. Review separately judges the whole diff, scope, correctness, regressions and side effects. Finalize, by a separately assigned Architect after current QA and Review, verifies the whole delta and repairs nothing; a needed source repair returns ESCALATED_FINALIZE. Overall SUCCESS still awaits the owner's concrete-result decision.

## 8. Code layer

Product code follows the six core owners: semantic exoskeleton on authored code, owned LDD trajectories, meaningful tests with real channel probes, and a Doxygen code map. The map is mandatory unless the target's own instructions explicitly forbid Doxygen; a missing Doxyfile is owed bootstrap work, not an exemption.

## 9. Hooks

| Event | Script | Effect |
|---|---|---|
| SessionStart (startup, resume, clear, compact) | `hooks/session_start.py` | Verifies the in-place binding and adds a short context: the bound neutral root or the BLOCKED reasons, the reading duty, and, when the target has an `AGENTS.md`, which of its durable records exist. Never writes, never fails the session. |
| PreToolUse (Bash) | `hooks/guard_destructive.py` | Asks before commands that would lose unrecoverable state; denies tree-changing commands to read-only agent types; silent otherwise. `METHODOLOGY_GUARD_SCOPE=off` disables it. |

With hooks disabled (for example `--bare`) the root performs Orient manually and checks scope and effects itself before each operation.

## 10. Language, continuity and limits

Dialog with the owner is Russian unless the project's or owner's instructions select otherwise; project artifacts are English unless the target's conventions say otherwise. The target's files govern continuity: the five records and notes support compaction and resume. Schedules, monitors, external memory or tracker writes need an explicit matching request. Deferred learning and comparative measurement are not activated by this package.

Not supplied: detached or cached installation, automatic discovery, publication, global configuration changes, a hard sandbox for judges' Bash, and any claim about model effectiveness. Package SUCCESS on a run never authorizes merge, install or publication.
