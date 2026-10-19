---
name: ax-ui-contract
description: "Контракт доступности веб-интерфейса: «спроектируй веб-экран или форму», «новый веб-интерфейс на React», «доступность контролов: роль, имя, состояние». Use before designing any slice that creates or changes web UI (React, Next.js, HTML, web components): fixes role, accessible name, state and stable identity for every control and how they are verified. Absent for pure backend or CLI work."
---

# ax-ui-contract

Make web UI testable by agents through the accessibility tree: every control has a role, a name, states and a stable identity, and the tests assert them.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../code/ax-ui.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Load this before the plan is written. Confirm from the specification and the real source that the slice creates or changes web UI; otherwise record NOT_APPLICABLE with that fact and stop.
2. For each interactive control record its semantic role, accessible name, dynamic states (loading, error, selected, disabled) and a stable test identity. Prefer native HTML elements and correct keyboard behavior; expose errors and status in accessible live regions.
3. In the plan name, for every UI-facing acceptance criterion, the accessibility-observable state its test asserts. Plan component tests over typed fixtures and documented end-to-end operations; never start a server inside a unit test.
4. For live verification use the built-in browser pane or Claude in Chrome and read the accessibility tree (`read_page`) for role, name and state. Use screenshots only for visual claims, which are judged separately.
5. If no browser is available, run the component and controller tests that remain in scope and report the gap: a mandatory live-browser criterion stays BLOCKED and no snapshot is ever invented.

Limits:
- Pure backend, CLI and document slices get no UI mapping invented for them.
- A screenshot or a console message is not accessibility evidence.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.
