---
name: pm-handoff
description: "Owner-invoked command: close a working session so the next one continues from the files without loss. Reconciles changed task states and evidence, updates HANDOFF when needed, uses the adopted orient check and reports what waits for the owner."
argument-hint: "[closing note]"
disable-model-invocation: true
---

# pm-handoff

Leave a baton that a reader with no chat can pick up: the goal, the current task, the next authorized action, the owner-only decisions and the latest evidence.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../process/session.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/batch.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/decisions.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/learning.md`
- `${CLAUDE_PLUGIN_ROOT}/../../documents/templates/HANDOFF.md`
- `${CLAUDE_PLUGIN_ROOT}/../../checks/orient.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/gates.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Compare each task's state and finish claim with the real artifacts. Keep the original packet and its results before replacing current work; keep blocked, deferred, failed and unfinished rows with their next disposition. Reconcile the route's achieved outcomes, focus and diagram together.
2. Audit this session for facts that no record carries yet (a decision made only in chat, an ignored file the next step needs, a changed configuration, a defect, a stale number, an unrecorded uncertainty) and route each to its one owning record. A binding decision goes to the decision home with its actual human source and provenance; an accepted decision body is never edited, only its status, superseded_by and amended_by change, and where the project numbers decisions a new number comes only from the parent's ordered allocation. A genuinely open alternative stays an open question. A useful failure, remedy or corrected belief becomes a dated project note as process/learning.md describes. This is fact recording, not learning ingestion.
3. Move an expired live hazard to dated history with its proof and recheck condition; drop only its warning.
4. Follow the shared session cadence on material changes, grouped progress and before planned compaction/handoff. If continuation state is already current, reuse it. Otherwise update HANDOFF from its template: the owner blockers first (name each pending decision and the action needed, or say nothing), then the present and previous state with the checked revision and what is uncommitted, the next authorized action pointing at TASKS, and the live traps.
5. Use the adopted profile's existing read-only orient check where applicable, without dispatching QA or a separate documentation judge, and fix what is in scope; keep every unexplained or unavailable result with its recovery action. Commit only the named files this session owns and only if committing was granted; report foreign changes without bundling them.
6. Read the baton as a newcomer would. The final message leads with what waits for the owner, then the concrete changes and checked result, then the confirmed findings and limits, and states whether anything was saved but not committed.

Limits:
- Do not report a merge, publication or adoption that did not happen.
- A status-only request edits nothing.
- A missing, stub or unread required owner is BLOCKED; no installation follows, and an inner role never delegates or commits.

Consumer PM profile: for an adopted `methodology-consumer-pm/1.0.0` target, read `${CLAUDE_PLUGIN_ROOT}/references/consumer-pm-profile.md` and the Codex carrier it names in full. HANDOFF keeps the headings Blocked on the owner, State, Queue and Traps exactly once and in that order, and the orient check of step 5 is `orient PROJECT --check` through the launcher `${CLAUDE_PLUGIN_ROOT}/bin/orient` (bare `orient` only when `command -v orient` resolves to that launcher). Fix only granted defects; name every other failed or unavailable row with its rule under the owner block.
