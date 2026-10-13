---
name: durable-layer
description: "Use when starting, resuming or handing off a meaningful project checkpoint: read the five project records in their declared homes, keep files (not chat) as the durable authority, and close with a recoverable HANDOFF."
---

# durable-layer

Files are the durable memory of a project. Chat, compaction and Claude's own memory only point at them.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../process/session.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/lifecycle.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/batch.md`
- `${CLAUDE_PLUGIN_ROOT}/../../documents/conventions.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Entry. Read the binding entry (the project's AGENTS.md and CLAUDE.md load natively), then VISION, the scoped ROADMAP, HANDOFF and TASKS in their declared homes and order, then only the linked notes, decisions and artifacts that matter. The SessionStart hook output is a pointer to this reading, not a substitute for it. A missing preferred filename triggers recovery, never a greenfield assumption.
2. Establish the goal, the active task, the live grant, the source revision and the foreign or uncommitted state (`git status --porcelain -uall`). One writer owns each artifact; foreign changes are preserved.
3. While working, record each material fact where it belongs when you find it: intent in VISION, a local result in TASKS or its notes, a binding choice in the decision home, a live hazard in HANDOFF. Preserve route ids, decisions, failures, pending gates and spent resources.
4. After compaction or a restart, re-orient from the records (the hook runs again on compaction) and from the run-state ledger (`run_state.py show`); a compaction never resets a run or its budgets.
5. Close through the pm-handoff command: reconcile evidence, rewrite HANDOFF, and commit only named, authorized files through the root.

Limits:
- A goal or a standing task is created only on an explicit owner request.
- Claude auto-memory and memory plugins are session aids, not project records.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.
