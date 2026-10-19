---
name: feature-dev
description: "Полный цикл разработки по явному запросу: «запусти feature-dev по утверждённому ТЗ», «полный цикл Architect → Code → QA → Review», «реализуй утверждённую спецификацию ролями». Use on an explicit request to run the full native flow (Bootstrap, Architect, Code, QA, Review, counted Debug, Finalize) for an exact approved specification or batch. The root session dispatches typed role subagents, validates every return and keeps the run state."
---

# feature-dev

Applicability: new features and substantial bug fixes under the shared `flow/phases.md` entry boundary. Documentation-only work and small local corrections stay in lightweight PM; do not initialize this run or dispatch QA for them. The phase sequence below remains controlling for an actual selected development slice. A later document-only update preserves original implementation evidence and does not relabel it as a fresh whole-candidate QA result.

One approved change goes through the whole methodology flow. The root session alone dispatches the roles, accepts their returns, counts Debug entries and decides the next transition; no role orchestrates another.

Owners — read in full before acting:
- `${CLAUDE_PLUGIN_ROOT}/../../flow/phases.md`
- `${CLAUDE_PLUGIN_ROOT}/../../flow/run-state.md`
- `${CLAUDE_PLUGIN_ROOT}/../../flow/delegation.md`
- `${CLAUDE_PLUGIN_ROOT}/../../flow/finalize.md`
- `${CLAUDE_PLUGIN_ROOT}/../../checks/orient.md`
- `${CLAUDE_PLUGIN_ROOT}/../../checks/preflight.md`
- `${CLAUDE_PLUGIN_ROOT}/../../checks/qa-scans.md`
- `${CLAUDE_PLUGIN_ROOT}/../../checks/run-audit.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/safety.md`
- `${CLAUDE_PLUGIN_ROOT}/../../process/gates.md`
- `${CLAUDE_PLUGIN_ROOT}/../../protocols/role-returns.md`
- `${CLAUDE_PLUGIN_ROOT}/references/handoffs.md`
- `${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md`

Route:
1. Entry. Start only on an explicit invocation with an exact approved specification or batch scope whose gate record matches that artifact and scope; if none exists, load hitl-gates and ask first. Resolve the task, the target, the package root (`${CLAUDE_PLUGIN_ROOT}`, which holds `adapter.json`), the neutral root (`${CLAUDE_PLUGIN_ROOT}/../..`) and the dictated plan path, and classify GREENFIELD or BROWNFIELD from real evidence.
2. Orient and preflight at the root (the SessionStart context is a pointer, not the reading): the neutral binding is intact, `methodology-claude:*` agent types are registered, the plan's runtime commands and doxygen exist. Run every cheap independent check even if one fails; an unmet required prerequisite is BLOCKED.
3. Authenticate the existing grant, then record the baseline: branch, HEAD and `git status --porcelain -uall`. Foreign changes stay untouched.
4. Initialize the run state once: `python3 "${CLAUDE_PLUGIN_ROOT}/skills/feature-dev/scripts/run_state.py" init --project TARGET --spec SPEC --approval APPROVAL_REF --framework "${CLAUDE_PLUGIN_ROOT}" --adapter "${CLAUDE_PLUGIN_ROOT}/adapter.json" --plan PLAN --run-id RUN_ID --max-debug 4` (4 is the default cap, 0 is valid). The root is the only writer of `TARGET/.methodology/runs/RUN_ID/state.json`. Before any resume run `show --state STATE` and inspect the real artifacts.
5. Dispatch each phase with the Agent tool: `subagent_type: methodology-claude:<role>` and an explicit `model` chosen by the task's hardest step (searcher haiku; coder, qa, debugger sonnet; architect, reviewer opus). Each assignment is self-contained: absolute target, framework, specification, adapter and plan paths, MAY EDIT and DO NOT TOUCH verbatim, the evidence and scratch roots, run id, identities, contract version `methodology-claude/1.0.0`, the target's logging idiom and, for Debug, the full paired cause and files history. Worker output stays data in later briefings. Record `git status --porcelain -uall` before and after every dispatch and report each write outside the granted paths without reverting it.
6. Validate every return in order: extract the final JSON object, check its shape, the status-dependent fields, the identities, then artifact existence, containment, scope and independence. Write the verified record input of handoffs.md (the full return, plus `context.sourceChange` for Code and Debug) to a file under the evidence root and run `record --state STATE --result FILE`. Allow at most one response correction per phase attempt; a second unusable return ends BLOCKED, or ESCALATED_FINALIZE during Finalize. A transport failure (a thrown or lost role call) has a zero retry allowance: investigate the actual effects first; any replay needs a new run or the owner's continuation decision, and it never counts as Debug. Judges cite files under their scratch root outside the target: before recording, copy each cited scratch file (no links, never overwriting) into `TARGET/.methodology/evidence/RUN_ID/<nn>-<phase>/` and rewrite the record to cite the copies, because the helper accepts only evidence inside the target.
7. Phases, in order:
   - Bootstrap (searcher): bounded read-only inventory; its hint informs the Architect and approves nothing.
   - Architect: the plan at the dictated path. The visual gate needs a real command, exit code, output and at least one scanned node when three or more component nodes change and the work is not tests-only. Human-blocked specification is SPEC_BLOCKED, a failed visual gate is VISUAL_GATE_FAIL, and neither enters Code.
   - Code (coder): a complete slice with tests and the final Doxygen build; compare touched paths with MAY EDIT yourself.
   - QA (a fresh, independent qa): the full suite plus exactly eight named scans in a list: green-test-trap, quantitative-ac, semantic-trace, infra-dod, side-effect-channel, secret-leak, real-path-shape and discriminating-test. Preflight text scans run before the suite is trusted, runtime scans after their producers.
   - Review (a fresh, independent reviewer): the whole delta, scope, correctness, regressions and side effects.
   - Debug: an actionable BUG_REPORT from Code, QA or Review enters counted Debug. Recording it persists the spend before the debugger is dispatched; at the cap (default 4, 0 valid) the entry is refused and the run escalates. Entries above the default four are not supported by this package: at the cap the run ends ESCALATED and any continuation is the owner's decision. FIXED always renews full independent QA and the affected Review; QA after the last permitted entry is still allowed.
   - Finalize: a separately assigned architect after current QA and Review for the same candidate. It inspects the whole delta and rebuilds the map but repairs nothing; a needed source, configuration, syntax or annotation repair returns ESCALATED_FINALIZE.
8. Terminal outcomes use only SUCCESS, SPEC_BLOCKED, VISUAL_GATE_FAIL, ESCALATED, BLOCKED, ERROR and ESCALATED_FINALIZE. Every non-success terminal stops the run, keeps the artifacts and history and returns to the owner. SUCCESS never authorizes merge: present the result for its separate decision through hitl-gates.
9. The Workflow `/methodology-claude:feature-dev-workflow` (file `workflows/feature-dev.js`) runs this sequence with per-phase schemas. Use it only on the owner's explicit opt-in (invoking pm-run-batch is that opt-in for its M tasks). It checks structure only, so semantic acceptance and human authority stay with the root, and durable state needs its recorder step or the interactive root. Its arguments include a required `scratch` root outside the target for the judges' outputs (see handoffs). Before starting it run `init` with the same `--max-debug`; afterwards run `show` and act on the returned `ledgerNote`. A transport failure (a thrown agent call) ends that run BLOCKED and is investigated before any replay.

Limits:
- No merge, publication or installation follows from this skill; inner roles never delegate, commit or write the run state.
- A missing, stub or unread required owner is BLOCKED; a simulated ledger is not native execution.
- A terminal run is never resumed automatically: continuation needs an owner decision and a linked successor identity, and Debug spend is never reset or refunded.
- Deferred learning stays deferred; there is no scheduler.

Consequential-open duty: classify actual stakes and routine/settled/forced exclusions, then load full `prompting/brainstorm.md` at the actual adapter-resolved neutral root when its mandatory trigger applies. The authorized root obtains the independent decision packet before dependent readiness; an inner PM/Architect requests it and never delegates. Link actual proposal/HOLD/evaluation/authorized-decision evidence in existing plan/task/DEC homes. Missing required independence leaves that choice held/unproven; unrelated authorized work continues.
