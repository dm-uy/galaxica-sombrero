---
name: pm-bootstrap
description: "Owner-invoked command: bring a project onto the methodology's document conventions (five records, Doxyfile, code map) and pass the owner's gate on the result. Use to start a new project or to restructure an existing one."
argument-hint: "[project path]"
disable-model-invocation: true
---

# pm-bootstrap

Prepare a project so the next role has its records, its code map and its settled inputs, without writing anything the owner did not grant.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../process/bootstrap.md`
- `${CLAUDE_PLUGIN_ROOT}/../../documents/conventions.md`
- `${CLAUDE_PLUGIN_ROOT}/../../documents/templates/INDEX.md`
- `${CLAUDE_PLUGIN_ROOT}/../../roles/pm.md`
- `${CLAUDE_PLUGIN_ROOT}/../../code/doxygen.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Resolve the project from the argument or the working directory. Orient read-only first (the SessionStart context, then the entry and existing records), record the baseline with `git status --porcelain -uall`, and classify from real source: existing executable code is never greenfield.
2. Preparation writes need a matching bounded grant. The owner's bootstrap request is the trigger; ask with AskUserQuestion for the exact files to be created or moved, including whether a short CLAUDE.md that imports AGENTS.md is wanted.
3. Inventory the existing documents and give each its one home under the conventions. Never overwrite and never delete truth: if a move would lose content, stop and return that gap.
4. Seed only the missing records (AGENTS, VISION, ROADMAP, HANDOFF, TASKS) from the five templates listed in the templates index, at the homes the target selects, preserving existing Git and ignore rules. The vision stays a draft; a decision becomes a record only when the owner has confirmed it.
5. Make sure the Doxyfile covers the source and tests, create the output directories, run `doxygen Doxyfile` with Bash and read the exit code and the XML back. A missing doxygen or Doxyfile is owed work, reported, never an exemption.
6. Run the project's available checker and keep every remaining failure with its owner in HANDOFF under the blockers.
7. Gate: ask once with AskUserQuestion to approve, rework or cancel, recording the answer verbatim. Report in this order: what waits for the owner, what changed, what was found.

Limits:
- No `git init`, commit or merge without a matching grant; foreign changes are preserved.
- Preparation authors no architecture or code, and it grants no result decision.
- A missing, stub or unread required owner is BLOCKED; no publication or installation follows, and an inner role never delegates or commits.
