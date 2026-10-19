---
name: hitl-gates
description: "Гейты согласования с владельцем: «согласуй со мной ТЗ перед реализацией», «спроси меня перед мержем или деплоем», «утверждение результата». Use before implementation starts (the specification or batch decision) and before the concrete result is merged, published or deployed (the result decision). Passes each gate through a structured owner question and records the answer."
---

# hitl-gates

The owner decides what will be built and whether the concrete result is accepted. The agent executes and never answers for the owner.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../process/gates.md`
- `${CLAUDE_PLUGIN_ROOT}/../../policies/autonomy.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Look for an existing authorization before asking: the specification's gate record, the batch record, decision records, the HANDOFF owner block and earlier answers in this session. Reuse a record only if it matches the exact artifact and scope.
2. If a decision is missing, prepare the concrete artifact first, then ask one question with AskUserQuestion. Specification gate: approve and launch, rebuild with the requested changes, or cancel. Result gate: merge, rework with a concrete Bug Report, or reject. Put the digest (goal, scope, measurable criteria, delivery contract, deficiencies, risks) or the result evidence (tests, blast radius, live probe, Finalize report, review) in the question; recommend merge only when the probe and evidence are green.
3. Record the answer verbatim at once, with the owner, the date, the mechanism, the artifact identity or hash and the scope, in the specification front matter or batch record and the notes, before any launch, commit or merge. The run-state ledger binds only the approval reference given at `init`; it records no later decision.
4. Wait. Independent, reversible work inside the approved scope may continue. For a large specification you may submit the complete plan with ExitPlanMode; an agreement in chat while plan mode is active is not approval.
5. Re-ask a malformed answer through a fresh question and block after three. Only where AskUserQuestion is genuinely unavailable (a headless print session) accept an explicit chat approval, recorded verbatim with actor, date, artifact identity and scope; ask again on ambiguous wording.

Limits:
- Specification consent and result consent are separate, and neither is granted in advance.
- Silence, a timeout, a default option, another agent or a tool result is never consent; rejection grants no destructive rollback.
- No merge, publication or installation follows from this skill, and an inner role never delegates or commits.
- A missing, stub or unread required owner is BLOCKED.
