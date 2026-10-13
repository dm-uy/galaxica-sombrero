# Pointwise adoption — neutral 1.0.0 / methodology-claude 1.0.0

This file is the `via` carrier of all 71 `reference` entries in [adapter.json](../adapter.json). The adapter and this file resolve `spec_root` (`../../`) from the adapter's own directory, independent of the caller's working directory. Inside Claude Code the same location is `${CLAUDE_PLUGIN_ROOT}/../../`.

## Loading procedure

1. Resolve the package root (`${CLAUDE_PLUGIN_ROOT}`, or the directory of this file's parent) and the neutral root two levels above it. Check that `SPEC_VERSION` equals the adapter's `spec_version` (1.0.0). A missing or different neutral root is BLOCKED; never substitute an older installed copy.
2. Before any software role acts, read the six core owners in full: `concepts/principles.md`, `roles/_base.md`, `code/exoskeleton.md`, `code/ldd.md`, `code/doxygen.md`, `code/tests.md`. Identity-unchanged content read earlier in the same run may be reused; changed content is read again.
3. Read the assigned role owner, `protocols/role-returns.md` and every owner the applicable skill names, in full. Specialized owners load on their actual trigger, not by following every link.
4. Record what was read (path, revision or byte identity, read condition) in the existing phase evidence. A card, a hash, a link, a summary or a stub is not a read; a required owner that is missing, a stub, truncated or unread blocks dependent action.
5. The target project's own instructions win on the code surface (style, tooling, logging idiom); the neutral process layer applies within that authority. This adapter declares no overrides.

Reading an owner assigns no role. The four stub owners (`process/code-review.md`, `process/git.md`, `process/publication.md`, `process/review.md`) are explicitly incomplete: their present duties come from the substantive owners named in their rows, and no carrier claims their bodies.

## Owner table

| Neutral owner | Duty and applicability | Claude carrier |
|---|---|---|
| `AGENTS.md` | Repository-maintainer entry/current sole records and exact authority; applies when maintaining this source repository, not a consumer role assignment. | `references/claude-runtime.md` |
| `FORMAT.md` | Neutral namespace/card/anchor/norm/version and adapter contract; package native formats distinct, full public traversal retained. | `skills/document-protocol/SKILL.md` |
| `checks/conform.md` | Actual common checker outputs/exits and finite recognizer limits; run required self/adapter and retain all warnings, no semantic truth inferred. | `references/claude-runtime.md` |
| `checks/lints.md` | Actual observable check evidence/locators and limitations; stale/unavailable mechanisms remain unaccepted. | `references/claude-runtime.md` |
| `checks/orient.md` | Entry and closure assessment of actual adopted records/grants/ownership and eligible next action, readonly status without bootstrap authority. | `skills/feature-dev/SKILL.md`, `skills/pm-handoff/SKILL.md`, `hooks/session_start.py` |
| `checks/preflight.md` | Complete selected prerequisites before effects/spend; all cheap independent checks despite failure, dependent rows withheld and unverified behavior disclosed. | `skills/feature-dev/SKILL.md`, `skills/prompting-verify/SKILL.md` |
| `checks/qa-scans.md` | Eight named registry, actual preflight/runtime timing, triggers/structured findings and contrary controls; no required criterion waived by N/A. | `skills/feature-dev/SKILL.md` |
| `checks/run-audit.md` | Readonly original run reconstruction from actual records/effects/counters and source identities; chronology and missing costs retained. | `skills/analyzer/SKILL.md`, `skills/feature-dev/SKILL.md`, `skills/prompting-verify/SKILL.md`, `skills/pm-review-run/SKILL.md` |
| `code/ax-ui.md` | Applicable web control role/name/state/stable identity and actual AX/component evidence; visual claims separate. | `skills/ax-ui-contract/SKILL.md` |
| `code/data.md` | Actual schema/population, transformation/join invariants, native direct logic and owned isolated data resources. | `skills/data-transform/SKILL.md` |
| `code/doxygen.md` | Mandatory actual tool/config/build, covered source currency and full own entity paragraphs/location associations absent explicit prohibition. | `skills/semantic-exoskeleton/SKILL.md` |
| `code/exoskeleton.md` | Complete rich module/entity semantic fields, paired containment, qualified links and precise edit-local/language exceptions. | `skills/semantic-exoskeleton/SKILL.md` |
| `code/ldd.md` | Owned authored trajectory, imp/function/block/events, critical success9/failure10, safe host encoding and complete relevant-log audit. | `skills/semantic-exoskeleton/SKILL.md` |
| `code/navigation.md` | Use current actual graph/map then relevant full source; maintain contracted actual maps, read-only readers request refresh. | `skills/devplan-protocol/SKILL.md`, `skills/graph-protocol/SKILL.md` |
| `code/tests.md` | Native direct imports/isolated fixtures, outcome plus actual trace, expected-only errors, real channel/shape/discrimination, separate counters and full relevant final suite. | `skills/semantic-exoskeleton/SKILL.md` |
| `concepts/glossary.md` | Use source-backed forty-term meanings in actual context; catalog neither installs engine nor substitutes substantive core/protocol. | `skills/spec-recon/SKILL.md` |
| `concepts/principles.md` | Six-member finite full operative constitution, authentic bounded authority, complete behavior and separate actual delivery/adoption claims. | `skills/semantic-exoskeleton/SKILL.md` |
| `documents/conventions.md` | Actual adopted five logical homes/layer/metadata/format/report enclosure; no new defaults override existing target. | `skills/document-protocol/SKILL.md`, `skills/durable-layer/SKILL.md` |
| `documents/templates/AGENTS.md` | Full AGENTS reusable form and fictional illustration, only applied at actual target-selected home under conventions; no sample grant/result treated as authentic. | `references/claude-runtime.md` |
| `documents/templates/HANDOFF.md` | Full HANDOFF reusable form and fictional illustration, only applied at actual target-selected home under conventions; no sample grant/result treated as authentic. | `references/claude-runtime.md` |
| `documents/templates/INDEX.md` | Discover five full editable forms/fictional examples; templates never become consent/results. | `references/claude-runtime.md` |
| `documents/templates/ROADMAP.md` | Full ROADMAP reusable form and fictional illustration, only applied at actual target-selected home under conventions; no sample grant/result treated as authentic. | `skills/roadmap/SKILL.md` |
| `documents/templates/TASKS.md` | Full TASKS reusable form and fictional illustration, only applied at actual target-selected home under conventions; no sample grant/result treated as authentic. | `references/claude-runtime.md` |
| `documents/templates/VISION.md` | Full VISION reusable form and fictional illustration, only applied at actual target-selected home under conventions; no sample grant/result treated as authentic. | `references/claude-runtime.md` |
| `flow/delegation.md` | Self-contained exact role inputs/paths, one writer, independent native actors and pure trusted/untrusted briefings, parent acceptance/retries. | `skills/feature-dev/SKILL.md`, `skills/prompting-agent-design/SKILL.md`, `skills/prompting-decompose/SKILL.md`, `skills/pm-run-batch/SKILL.md` |
| `flow/finalize.md` | Assigned current Finalize after independent QA/Review; actual outputs/full scope/map/AC/live report, no source repair; result consent separate. | `skills/code-review/SKILL.md`, `skills/feature-dev/SKILL.md` |
| `flow/phases.md` | Approved entry and evidence predicates for native Bootstrap/Architect/Code/QA/Review/Debug/Finalize, causal repairs and explicit terminals. | `skills/feature-dev/SKILL.md`, `workflows/feature-dev.js` |
| `flow/run-state.md` | Immutable baseline/inputs and mutable candidate, single-writer atomic chronology, pre-entry cumulative Debug and separate bounded retries/resume freshness. | `skills/feature-dev/SKILL.md`, `skills/feature-dev/scripts/run_state.py` |
| `policies/autonomy.md` | Actual delegated choices and genuine ambiguity within authentic scope, constraints and human-dependent stops. | `skills/hitl-gates/SKILL.md` |
| `policies/credentials.md` | Actual credential consumer/presence authority only, no payload/stores/provider side effects; gaps not invented readiness. | `references/claude-runtime.md` |
| `policies/language.md` | Actual dialog/artifact/prompt language binding and preserved product text, no unrelated translation or model science. | `skills/prompting/SKILL.md` |
| `policies/models.md` | Hardest-step classification, adequate strength/context, actual authority/settings/requested versus observed facts; no automatic provider change or savings claim. | `references/claude-runtime.md`, `agents/*.md (model frontmatter)` |
| `process/batch.md` | Plan/approve/activate/track/assess actual batch, preserve carryover/decisions and distinct result consent. | `skills/durable-layer/SKILL.md`, `skills/pm/SKILL.md`, `skills/pm-plan-batch/SKILL.md`, `skills/pm-run-batch/SKILL.md` |
| `process/bootstrap.md` | Arrival criterion and actual project shape before granted five-record initialization; missing records alone not greenfield. | `skills/greenfield-bootstrap/SKILL.md`, `skills/pm-bootstrap/SKILL.md` |
| `process/code-review.md` | Disclosed stub; use substantive current roles/reviewer and full actual review evidence, never claim this body completed. | `skills/code-review/SKILL.md` |
| `process/decisions.md` | Real authority/evidence for open alternatives, hold/collapse/PM decision profiles and retained reopening/history. | `skills/brainstorm/SKILL.md` |
| `process/gates.md` | Authentic exact specification/run and concrete-result decisions, structured channel/default and qualified authorized fallback, no silence consent. | `skills/feature-dev/SKILL.md`, `skills/hitl-gates/SKILL.md`, `skills/pm/SKILL.md`, `skills/pm-plan-batch/SKILL.md` |
| `process/git.md` | Disclosed stub; current gates/base/PM/safety own actual preservation and parent commit boundaries, no invented Git procedure. | `references/claude-runtime.md` |
| `process/learning.md` | Contextual error notes and external candidate pointers only under scope; systematic learning/comparable measurement remains deferred. | `skills/analyzer/SKILL.md` |
| `process/lifecycle.md` | Actual meaningful tracks/checkpoints/task plan/order/replanning/backlog/snapshot, complete roles and owner-selected route. | `skills/durable-layer/SKILL.md`, `skills/pm/SKILL.md`, `skills/roadmap/SKILL.md` |
| `process/publication.md` | Disclosed stub; no publication/install claimed or authorized by local package, residual procedure/license evidence required before that future action. | `references/claude-runtime.md` |
| `process/reconnaissance.md` | Original requirements plus actual independent Code/Data/Decisions/conditional Legacy/Web, populations/citations/contradictions/unchecked limits before spec. | `skills/pm/SKILL.md`, `skills/prod-log-vacuum/SKILL.md`, `skills/spec-recon/SKILL.md` |
| `process/review.md` | Disclosed stub; existing Reviewer/run-audit provide scoped present duties; no deferred comparison engine inferred. | `skills/analyzer/SKILL.md`, `skills/pm-review-run/SKILL.md` |
| `process/safety.md` | Action-conditioned complete preservation/ownership/unknown effect, granted metadata snapshots and actual refs/objects limits, no destructive cleanup. | `skills/feature-dev/SKILL.md`, `skills/prod-log-vacuum/SKILL.md`, `hooks/guard_destructive.py` |
| `process/session.md` | Layer-aware entry/current artifacts, five records and recoverable closure/HANDOFF with actual evidence/commit authority. | `skills/durable-layer/SKILL.md`, `skills/pm/SKILL.md`, `skills/roadmap/SKILL.md`, `skills/pm-handoff/SKILL.md` |
| `process/specification.md` | Original measured intent/RECON/constraints, all AC and delivery/scope, contradiction and deficiency handling without silent narrowing. | `skills/brownfield-spec-template/SKILL.md`, `skills/greenfield-bootstrap/SKILL.md` |
| `prompting/agent-prompt-design.md` | Author agent loop/tool/state/boundary/evaluation contract; DRAFT defenses and actual separately granted target evaluation distinct. | `skills/prompting-agent-design/SKILL.md` |
| `prompting/brainstorm.md` | Open broad forks five distinct ideas and effects then reasoned scored selection; bounded choices no padding/settled reopening. | `skills/brainstorm/SKILL.md` |
| `prompting/decomposition.md` | Actual phased modes/inputs/results/effects/verification/handoff and structural-temporal agreement, bounded independent parallelism. | `skills/prompting-decompose/SKILL.md` |
| `prompting/grace.md` | Full applicable goal/role/context/constraints/output/success/examples prompt authoring and source-specific syntax, not prompt execution. | `skills/prompting/SKILL.md` |
| `prompting/prompt-markup.md` | Collision-safe paired semantic sections/data boundaries and actual message roles; delimiters are not permission/security proof. | `skills/prompting-markup/SKILL.md` |
| `prompting/solution-design.md` | Evidence-grounded actual solution alternatives, patterns and constraints with source-backed criteria and concise decision record. | `skills/prompting/SKILL.md` |
| `prompting/superposition-collapse.md` | Genuine alternatives, unresolved axes and evidence-based authorized collapse; settled decisions preserved. | `skills/brainstorm/SKILL.md` |
| `prompting/verification.md` | Evidence/CoVe/Diagnostic Trio/independent checks, finite attempts and uncertainty; same-model agreement not independent confirmation. | `skills/prompting-verify/SKILL.md` |
| `protocols/dev-plan.md` | Actual plan identity/sections1–6/full graph/flow/visual/AC/channel/commands/literal verification commitments. | `skills/devplan-protocol/SKILL.md`, `skills/prompting-decompose/SKILL.md` |
| `protocols/document.md` | Outline before detail, complete paired contracted artifacts/types/bodies/directed ID links and ordinary-meaning readiness. | `skills/document-protocol/SKILL.md`, `skills/prompting-markup/SKILL.md` |
| `protocols/graph.md` | Complete CODE/DOMAIN profiles/shared grammar/nine DOMAIN sections, actual directed source relations and brownfield evidence, syntax versus meaning. | `skills/devplan-protocol/SKILL.md`, `skills/graph-protocol/SKILL.md`, `skills/prompting-decompose/SKILL.md` |
| `protocols/role-returns.md` | Unmodified full canonical envelopes/status-dependent payloads/list scans and parent semantic acceptance before state. | `skills/feature-dev/SKILL.md`, `references/handoffs.md` |
| `protocols/spec-brownfield.md` | Full measured delta specification, protected APIs/regressions/scope/AC/Expected Architecture and real delivery risk. | `skills/brownfield-spec-template/SKILL.md` |
| `protocols/spec-greenfield.md` | Full genuinely new product goal/stack/MVP/architecture/BR/AC/real probe/risk without incidental infrastructure. | `skills/greenfield-bootstrap/SKILL.md` |
| `roles/_base.md` | Full shared preamble/core/runtime/protocol/current grant, original readonly boundaries, inner no delegation/commit and canonical actual returns. | `skills/semantic-exoskeleton/SKILL.md` |
| `roles/architect.md` | Assigned design full approved inputs/current map/alternatives/ready plan and separately assigned current Finalize. | `agents/architect.md` |
| `roles/coder.md` | Complete in-scope slice/tests/guide/current markup/log/map/external IDs/quantities/deviations with actual preSUCCESS checks. | `agents/coder.md` |
| `roles/debugger.md` | Precharged current causal diagnosis/repair/structured findings/scars/regression/postfix full tests/QA renewal and no resource reset. | `agents/debugger.md` |
| `roles/pm.md` | Full current five-record preparation/route/gates/source-led work; explicitly authorized root exception only, inner PM no dispatch. | `skills/pm/SKILL.md`, `skills/prod-log-vacuum/SKILL.md` |
| `roles/qa.md` | Independent readonly original files/Git, authorized scratch probes, full suite/eight scans/actual trace/quantities/BUG_REPORT/limits. | `agents/qa.md` |
| `roles/reviewer.md` | Independent full current delta/scope/correctness/regression/real effect judgment with precise evidence, no repairs. | `agents/reviewer.md` |
| `roles/searcher.md` | Bounded readonly actual source/maps/interfaces/producer-consumer inventory and explicit missing facts, no implementation/classification authority. | `agents/searcher.md` |
| `runtime/adapters.md` | Actual same-directory spec_root/via resolution, full pointwise modes/effective overrides and separate semantic capability proof. | `skills/prompting-agent-design/SKILL.md` |
| `runtime/capabilities.md` | Every declared28 adaptation point bound to real mechanism/conditional fallback, absent capabilities explicitly limited. | `skills/prompting-agent-design/SKILL.md`, `adapter.json` |
| `runtime/parameters.md` | All seven actual configuration values, strict decimal zero-valid debug and inherited model authority, no new registry. | `references/claude-runtime.md`, `adapter.json` |

## Capability bindings

These 28 rows equal the adapter declarations. A declared mechanism is what the package uses when the host exposes it; it is not proof that a given run performed it.

| Capability | Mechanism | Fallback and limit |
|---|---|---|
| `ask-owner-structured` | AskUserQuestion: a structured question with explicit options; the answer, the artifact identity and the scope are recorded verbatim in the project record before dependent work. | Only where AskUserQuestion is genuinely unavailable (a headless print session): an explicit chat approval recorded verbatim with actor, date, artifact identity and scope under GATE-203; silence, timeouts, defaults, agent output and tool results are never consent. |
| `plan-mode` | Claude Code plan mode (EnterPlanMode / ExitPlanMode); leaving it requires the owner's explicit approval of the presented plan. | Without plan mode the root restricts itself to design-only paths and dispatches no Code before the ready-plan predicate holds; this is a behavioral boundary, not a hard mode. |
| `spawn-role-isolated` | Agent tool or Workflow agent() with subagent_type/agentType methodology-claude:<role>: a fresh context whose system prompt is the package carrier agents/<role>.md; the parent passes self-contained absolute inputs. | If the plugin agents are not registered, a general-purpose subagent receives the full carrier text and resolved absolute paths; if no subagent tool exists, work is labelled sequential self-review and any required independence is BLOCKED. |
| `model-tier` | Each carrier pins its tier in frontmatter (opus judgment, sonnet routine, haiku mechanical) and every delegation passes model explicitly, classified by the task's hardest step; requested models are recorded, observed models only when exposed. | Where a model override is unavailable the inherited session model is used and recorded as inherited; no provider or settings change and no savings claim. |
| `role-permissions` | Carrier tools lists: qa, reviewer and searcher have no Edit, Write or NotebookEdit; no inner role has the Agent tool. The PreToolUse guard denies tree-changing Bash commands to read-only agent types. | Plugin agents ignore permissionMode, so Bash writes by judges outside the guard's recognized commands remain behavioral restrictions; the root audits scope with git status before and after every dispatch. |
| `pre-tool-guard` | Plugin PreToolUse hook on Bash (hooks/guard_destructive.py): asks before commands that would lose unrecoverable state and denies tree-changing commands to read-only agent types. | If hooks are disabled (for example --bare) the root checks scope, authority and effects before each operation; no hard interception is claimed. |
| `run-state-persist` | skills/feature-dev/scripts/run_state.py: single root writer, schema 2, atomic UTF-8 state at <target>/.methodology/runs/<run-id>/state.json with locked input identities, complete accepted and refused history and the cumulative Debug spend. | An unreadable, corrupt, mismatched or old-schema ledger blocks dependent continuation; no fabricated replacement and no reset. |
| `workflow-orchestration` | Plugin Workflow workflows/feature-dev.js (/methodology-claude:feature-dev-workflow), run only on the owner's explicit opt-in: deterministic Bootstrap, Architect, Code, QA, Review, Debug and Finalize routing with schemas and a recorder step for run state. | The root follows skills/feature-dev and dispatches each phase with the Agent tool, recording every verified return through run_state.py; no hidden daemon. |
| `structured-output` | Workflow agent() schema (StructuredOutput validation) per phase status; the interactive root extracts the final JSON object and validates shape, conditional fields and identities before run_state.py record. | Manual JSON extraction with one bounded response correction per phase attempt; a second unusable return ends BLOCKED, or ESCALATED_FINALIZE in Finalize. |
| `skill-loading` | Skill tool with plugin skills methodology-claude:<topic>; each entry names its neutral owners as ${CLAUDE_PLUGIN_ROOT}/../../<path>, read in full with Read before dependent action. | Without the Skill tool the actor reads the SKILL.md and its owners by path; a missing, stub, truncated or unread required owner blocks dependent work. |
| `rules-injection` | SessionStart hook injects the binding status and the six-core reading duty; every carrier lists the six core owners and its role owners for full reading; the target's CLAUDE.md and AGENTS.md load natively. | Plugins cannot ship CLAUDE.md: where the hook is disabled the root supplies the full core content or exact resolved paths in each assignment. |
| `session-start-hook` | Plugin SessionStart hook (startup, resume, clear, compact) runs hooks/session_start.py: verifies the in-place neutral binding and reports the target's durable records for Orient. | With hooks disabled the arriving root performs Orient manually under checks/orient.md and states that no hook ran. |
| `background-command` | Bash run_in_background with completion notifications, Monitor for streamed events; the locator, complete streams and exit status are retained. | A bounded foreground run where safe, with the absent background capacity disclosed. |
| `web-research` | WebSearch and WebFetch for external facts, primary documentation for technical identifiers. | Missing access leaves the claim unverified or BLOCKED; internal evidence is used only where it settles the claim. |
| `browser` | The built-in browser pane or Claude in Chrome: read_page accessibility tree for role, name and state; screenshots only for visual claims. | Component and controller tests within scope; a mandatory live-browser criterion stays BLOCKED, never an invented snapshot. |
| `worktree` | git worktree on an owned branch (EnterWorktree or Workflow isolation: worktree) preserving foreign changes, one writer per path. | An owned complete copy without .git; judges never create worktrees or carry .git into scratch. |
| `schedule` | Scheduled tasks or routines only on an explicit matching owner request. | No scheduling in the package or its smoke; the owner runs the action manually. |
| `memory` | Project files are the durable memory (five records, decisions, notes); Claude auto-memory and installed memory plugins are session aids outside the repository. The knowledge layer is an external OKF-format bundle maintained outside this repository. | Without a memory tool the session relies on the five records and HANDOFF; no external memory write without an explicit request. |
| `todo-list` | TodoWrite or the session task tools for the run's own checklist. | The run checklist is kept in the assignment text and the run-state history. |
| `goal` | TASKS.md current task and HANDOFF next action carry the persistent goal across turns and sessions. | Without the records the goal is restated from the approved specification at each entry. |
| `code-map-build` | doxygen Doxyfile in the target via Bash; XML output read back for entity associations. | Missing doxygen or Doxyfile is owed bootstrap work and reported, never an exemption; only an explicit written host prohibition is NOT_APPLICABLE. |
| `check-runner` | Bash runs the target's declared test, lint, map and probe commands with complete streams and exit codes retained. | An unavailable command leaves its criterion BLOCKED with the reason. |
| `run-record-access` | The run-state ledger (run_state.py show), Workflow journals, session transcripts in the user-level Claude projects directory and the target's notes, read-only. | Missing records are reported as missing; no reconstruction presented as fact. |
| `packaging-install` | claude --plugin-dir <repo>/implementations/claude for one session, CLAUDE_CODE_PLUGIN_DIRS set to that path in the user settings env for every session, or a local directory marketplace whose root contains the package, loads the package in place; claude plugin validate --strict checks it. | Copied installs (git marketplace, cache) are unsupported: the SessionStart hook reports the missing neutral binding as BLOCKED and dependent work stops. A symlinked skills-directory plugin is unsupported too: its neutral references miss although the hook reports it bound. |
| `launch-environment` | The session working directory, added directories, the owner's permission mode and environment define roots and autonomy; credentials follow policies/credentials.md. | Unknown roots or permissions are discovered and stated before effects; no settings change. |
| `capability-discovery` | The session's tool list and deferred-tool search, the registered agent types, and claude plugin details for the package inventory. | An undiscoverable capability is treated as absent and its fallback applies. |
| `context-management` | Automatic compaction, subagents for context isolation, and the SessionStart hook on compact re-orienting from the records. | HANDOFF and the run-state ledger restore the state after a lost context. |
| `tracker-integration` | An issue-tracker connector only on an explicit owner request for that project. | TASKS.md is the tracker. |

## Parameter bindings

| Parameter | Value |
|---|---|
| `dialog-language` | Russian unless controlling owner or project instructions select otherwise |
| `owner-label` | owner |
| `model-mechanical` | haiku (Claude Code alias for the current Haiku model); used for marker scans, inventories, counting and recorder steps |
| `model-routine` | sonnet (Claude Code alias for the current Sonnet model); used for reconnaissance of a named area, code from an approved plan, QA and debugging with a clear trace |
| `model-judgment` | opus (Claude Code alias for the current Opus model); used for architecture, plans, specifications, Review, Finalize and synthesis |
| `gate-cadence` | per-change exact specification; an approved batch scope where the owner expressly granted it; the result decision stays separate |
| `debug-entry-cap` | 4 |
