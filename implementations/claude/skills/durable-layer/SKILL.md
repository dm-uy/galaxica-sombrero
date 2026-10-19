---
name: durable-layer
description: "Старт, продолжение или передача контрольной точки проекта: «где мы остановились», «продолжим с прошлой сессии», «обнови HANDOFF», «зафиксируй состояние проекта». Use when starting, resuming or handing off a meaningful project checkpoint: read the five project records in their declared homes, keep files (not chat) as the durable authority, and keep a recoverable current HANDOFF."
---

# durable-layer

Keep state for the next agent/session, using the shared `process/session.md` cadence: synchronize affected records after material changes, periodically across routine steps and before planned compaction/handoff. Save current task/status, next action and relevant decisions/blockers; retain VISION unless intent changes. Reuse an already-current baton. This is ordinary record maintenance, with no QA role, extra approval or new workflow. Unexpected host compaction is recovered by re-reading durable files, not by claiming an unavailable interception hook.

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
5. Close through the applicable lightweight handoff: reconcile changed state, update HANDOFF only when needed and commit only named, authorized files through the root. The pm-handoff entry preserves this cadence; an unchanged current baton is reused.

Limits:
- A goal or a standing task is created only on an explicit owner request.
- Claude auto-memory and memory plugins are session aids, not project records.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.

Consumer PM profile: for an explicitly adopted `methodology-consumer-pm/1.0.0` target, read `${CLAUDE_PLUGIN_ROOT}/references/consumer-pm-profile.md` and the Codex carrier it names, the actual declared homes, packet and baton, and orient at entry with `orient PROJECT` through the launcher `${CLAUDE_PLUGIN_ROOT}/bin/orient`. pm-handoff owns granted closure. Never impose the profile on maintainer records.
