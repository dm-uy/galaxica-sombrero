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
- `${CLAUDE_PLUGIN_ROOT}/../../process/session.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/safety.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/gates.md`
- `${CLAUDE_PLUGIN_ROOT}/../../documents/conventions.md`
- `${CLAUDE_PLUGIN_ROOT}/../../documents/templates/INDEX.md`
- `${CLAUDE_PLUGIN_ROOT}/../../roles/pm.md`
- `${CLAUDE_PLUGIN_ROOT}/../../code/doxygen.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Resolve the project from the argument or the working directory. Orient read-only first (the SessionStart context, then the entry and existing records), record the baseline with `git status --porcelain -uall`, and classify from real source: existing executable code is never greenfield.
2. Preparation writes need a matching bounded grant. Authenticate the owner's existing bootstrap/entry-update request against the actual files and actions; reuse clear matching consent. Ask with AskUserQuestion only for missing or ambiguous scope, including an optional CLAUDE.md import or a move not already granted.
3. Inventory the existing documents and give each its one home under the conventions. Never overwrite and never delete truth: map the proposed homes first, treat every move as a consequential effect that needs a matching grant (a clear existing grant counts), and if a move would lose content, stop and return that gap.
4. Seed only the missing records (AGENTS, VISION, ROADMAP, HANDOFF, TASKS) from the five templates listed in the templates index, at the homes the target selects, preserving existing Git and ignore rules. The vision stays a draft; a decision becomes a record only when the owner has confirmed it. Apply documents/conventions.md#documents.conventions.entry: put the compact continuity duties and actual home map early in new entries; compare existing entries by meaning, retaining equivalent clauses and adding only missing nonconflicting duties within the grant. Preserve original rules/bytes, metadata, mandatory preamble, links and alternate names; never replace an existing entry with the form. Report conflicts without overriding them.
5. Make sure the Doxyfile covers the source and tests, create the output directories, run `doxygen Doxyfile` with Bash and read the exit code and the XML back. A missing doxygen or Doxyfile is owed work, reported, never an exemption.
6. Read back the actual entry/current homes for recoverable goal/current/next/grants/result/holds, original-rule preservation and no duplicate additions on repeat inspection. Return covered/missing/conflicting duties in the existing result. Run the project's available checker and keep every remaining failure with its owner in HANDOFF under the blockers; structural markers do not certify semantic duty coverage.
7. Gate: ask once with AskUserQuestion to approve, rework or cancel, recording the answer verbatim. Report in this order: what waits for the owner, what changed, what was found.

Limits:
- No `git init`, commit or merge without a matching grant; foreign changes are preserved.
- Preparation authors no architecture or code, and it grants no result decision.
- A missing, stub or unread required owner is BLOCKED; no publication or installation follows, and an inner role never delegates or commits.
