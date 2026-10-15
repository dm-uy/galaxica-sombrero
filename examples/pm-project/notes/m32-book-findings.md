# M32 — book-derived improvements, checked incrementally

## Owner direction and scope

On 2026-10-15 the owner selected the preceding three-part proposal and asked:

> Давай отметим все наши находки и будем двигаться по этому маршруту, поэтапно проверяя и внедряя, если что-то приживется.

This grants recording the findings and progressing through bounded investigation, candidates and checks, adopting useful results conditionally. It does not accept an unobserved benefit or authorize main merge, publication, installation, a new mandatory workflow or revival of exhausted/deferred runs. Existing chat authority is retained; do not ask again merely to record or investigate these selected candidates.

Use the accepted [lightweight direction](pm-lightweight-direction.md): documentation and small corrections receive relevant local checks. A new executable helper or substantial behavioral change needs its concrete recon/specification and applicable development method. Keep each candidate's result separate from its release/integration decision.

M32 selects a bounded improvement route. It does not activate the deferred systematic learning/comparative-evaluation program. A focused check of a selected candidate is permitted; an open-ended benchmark program is outside this packet.

## Evidence population and limits

The parent read the owner's `AI_Instructions.md`; three independent native reading lanes studied the book and compared canonical sources. Lanes covered introduction/chapters 1–7; chapters 8–11 and 14; chapters 12–13; relevant glossary, practical templates and source references. Required excerpts initially truncated by tool output were reread in smaller ranges. Scientific papers in the bibliography were not independently reviewed. No model-benefit experiment was performed during that study.

Sources were local read-only inputs supplied from the owner's book-source checkout, under `SoT`; the original request retains their machine-local locations. Source identity SHA256:

| Input | SHA256 |
|---|---|
| `AI_Instructions.md` | `cc8270891547415a6b873ccd78dfcec710f868f729fa207f2c9887bf9f33d646` |
| Book, owner-supplied Russian-title Markdown, chapters 1–14 and appendices | `ffc3e2daccbe470d6d32a0a2801a05557547484b334c964ae864c7ef3b3ad0ef` |

Canonical comparison baseline: `8d98a5859cbaab73b81bfc2f87b0b798bc0c4101`, clean main before work. This record is authored in the isolated `codex/m32-book-findings` worktree. Root owns this note and affected TASKS/ROADMAP/HANDOFF; VISION is unchanged. Readers were allowed no source or Git writes; restrictions were behavioral, not a claimed per-worker hard sandbox. Original archival checkout work is outside this change.

Evidence labels below distinguish observed text from proposed checks. Textual coverage does not establish execution or adoption. Independent source checks confirmed the carrier discrepancy and the payment-example limitation; no live Stripe behavior was checked.

## Findings and dispositions

### F1 — conflicting prompting carriers: selected first

Observed: the installed `prompting-methodology` 0.5.0 entry and the source candidate in the owner's `agent-skills` checkout have identical SHA256 `d81dcaa006af750d3382b13f9aa87352a1298d43dc04828fdf956595e551bddc` for `plugins/prompting-methodology/skills/methodology/SKILL.md`. Source checkout HEAD is `6aa66c26eb9a5790de777edc050dc71ef7b0112a`, clean when inspected. Plugin metadata also declares 0.5.0. This is a located source candidate, not proof of the marketplace's configured upstream; verify that binding before release.

The source/installed entry makes categorical claims at lines 31–36 and 49–50: first 200–500 tokens, fixed marker spacing, the middle as a dead zone, deterministic Plan/Code/Debug/QA order, arithmetic error for numbers above ten, clean context without agent system prompts, and contracts activating accuracy weights. Canonical [GRACE](../../../prompting/grace.md#prompting.grace.profiles), [markup](../../../prompting/prompt-markup.md#prompting.prompt-markup.profiles) and [agent design](../../../prompting/agent-prompt-design.md) already qualify such heuristics, permit suitable collision-safe markup and preserve actual authority, software ordering and spent attempts.

Additional first-stage observation: the source checkout's `.claude-plugin/marketplace.json` declares the source marketplace and points this plugin to `./plugins/prompting-methodology`, but declares version 0.4.0 while the plugin's own manifest declares 0.5.0. Include that source metadata discrepancy in reconciliation. The source inventory comprises the plugin manifest, two agents, five commands and two skill directories with templates/ontology/framework references; this is file discovery, not full semantic review of every carrier. The actual configured installed marketplace's upstream remains unverified.

Candidate: reconcile the maintained prompting entry, templates, commands and agents against those qualifications. Fix the real upstream source, not a transient cache. Keep the already useful tool delegation and contract structure. Inspect the agent-skills checkout's own instructions and source/marketplace ownership before editing it.

Finish: a concrete source delta resolves the identified contradictions, all affected derived instruction carriers agree, examples preserve real system authority and current software phases, and relevant static/readback checks pass. Report any remaining conflicting carrier. Behavioral benefit is not inferred from editorial consistency. Release and user-level activation remain separately decided.

### F2 — verified extraction from long document sources: selected second

Observed: `AI_Instructions.md` section 2 gives TOC → semantic anchor → bounded content reading. Current [reconnaissance](../../../process/reconnaissance.md), [markup](../../../prompting/prompt-markup.md) and [native runtime](../../../implementations/codex/references/codex-runtime.md) require scoped current evidence and complete required bodies, but the inspected document-reading procedures do not provide an equally concrete delivery-coverage recipe.

Candidate: add a short optional recipe to the existing owning procedure. Identify the actual source, inspect its index, select relevant sections, resolve current boundaries, read manageable chunks, distinguish selected/delivered/unread content and reread truncated or changed ranges. Return question → section → evidence with exclusions. Required normative bodies still require full reading; selection is for the research corpus and optional detail. The recipe proves delivery coverage, never mental adoption.

Checks: valid source; missing/duplicate anchor; broken nesting; TOC/body disagreement; truncated output; source change between locating and reading. A check either establishes the complete claimed range or explicitly withholds its dependent conclusion. Support headings/ranges when a source has no tags. No new registry, compulsory markup conversion or executable helper by default.

Finish: use the recipe on a bounded real source, record observed failure handling and remaining friction, then retain/revise/drop it. The normative change and any helper are not pre-approved merely by this research finding.

### F3 — fresh-reader usefulness: selected third

Observed: book section 13.3 defines Zero-Context Survival. [Exoskeleton](../../../code/exoskeleton.md) already requires rich contracts; [SESSION-105](../../../process/session.md#process.session.baton) already recommends checking a fresh reader's reconstruction. The gap is unmeasured usefulness in the selected case, not absence of a rule.

Candidate: a fresh reader receives existing project entry/current records and relevant source, without author chat history. Ask it to recover goal, current task, constraints, next authorized action, owner-only decisions, latest result and deferred work. For a changed module, recover inputs/outputs/effects/errors/invariants and identify dependencies it cannot resolve. Compare against actual source and authoritative decisions; detect an intentionally contradictory contract in an isolated fixture.

Finish: retain actual inputs/outputs/bindings, omissions and unsupported inferences; correct the specific deficient record/contract and check again only when needed. Decide retain/revise/drop based on usefulness versus added work, without claiming broad efficacy from one sample. This concretizes existing session checks, not a new compulsory QA stage. Any full API/database trial retains the existing accepted-minimal-safeguard prerequisite; a read-only document check does not close C3 or C5/C6.

### Already covered — retain, do not duplicate

| Book material | Existing owner |
|---|---|
| Goal/constraints/format/criteria/examples and ordering qualifications | [GRACE](../../../prompting/grace.md) |
| Paired boundaries, collisions, context map and outline/body agreement | [Markup](../../../prompting/prompt-markup.md), [document protocol](../../../protocols/document.md) |
| Alternatives, HOLD, independent generation/evaluation and authorized choice | [Brainstorm](../../../prompting/brainstorm.md), [superposition/collapse](../../../prompting/superposition-collapse.md) |
| Static/dynamic projections, decomposition and phase I/O | [Development plan](../../../protocols/dev-plan.md), [decomposition](../../../prompting/decomposition.md) |
| Compact recoverable state, real tools and preserved budgets | [Session](../../../process/session.md), [agent design](../../../prompting/agent-prompt-design.md) |
| CoVe, Diagnostic Trio, Anti-Loop, independent review and real delivery | [Verification](../../../prompting/verification.md), [code review](../../../process/code-review.md), [QA scans](../../../checks/qa-scans.md) |
| Semantic contracts, bug rationale, logs, traces and discriminating regressions | [Exoskeleton](../../../code/exoskeleton.md), [LDD](../../../code/ldd.md), [tests](../../../code/tests.md) |

### Source cautions — preserve as qualifications

Observed source claims are not independently verified universal facts: fixed token windows/ceilings, Russian-language cost/accuracy percentages, global attention from a literal summary tag, accuracy-weight activation, immunity from comments and the instruction file's 95-percent savings claim. Canonical GRACE-105 already requires qualification. Do not promote them into new MUST rules.

The source glossary also uses Collapse for degradation while chapter 8 uses it for selecting alternatives; preserve our operational terminology rather than importing contradictory labels. Agreement between model answers, a generic numeric tolerance or a persuasive explanation cannot establish factual truth; current verification already addresses this.

The section 13.3 payment example states at line 3189 that failure deducts no money, but lines 3225–3249 show the payment call followed by database/commit/email operations and a generic rethrow, without demonstrating compensation for a subsequent error. Static conclusion: the example does not demonstrate its stated guarantee. No claim about actual provider behavior follows. Source examples require normal contract/code/effect checks before reuse.

### Conditional observations — not selected new work

The reliability lane suggested checking whether interleaved concurrent LDD events remain attributable to individual operations, and whether BUG_FIX_CONTEXT remains accurate after later edits. These are hypotheses without an observed current defect. Existing trace, contract-update and regression duties apply. Reopen only on a concrete ambiguous trace or stale explanation in the actual task; do not add universal log fields, a scar-maintenance system or concurrent feature work from this note.

## Route and acceptance policy

The single current [ROADMAP](../ROADMAP.md) owns ordering; [TASKS](../TASKS.md) owns runnable work. Order: F1 carrier reconciliation → F2 delivery recipe → F3 fresh-reader usefulness. A later stage is a selected direction, not a claim that the earlier candidate has succeeded.

For each stage record: question and source identity; smallest candidate; concrete check and observed result; benefit/friction/limits; disposition retain, revise, drop or hold; next action. Keep negative results and reasons. Accept a practice only within its demonstrated scope. Do not accumulate obligatory skills, ledgers or gates merely because the book names a technique. New consequential design forks follow the current decision procedure; routine editorial choices do not reopen settled direction.

## Current result

The reading findings, qualifications and route are retained here. First-stage source location, entry-byte equivalence, source marketplace declaration and carrier file inventory are checked. Actual configured upstream and complete semantic review of dependent carriers remain the next research step. No prompting source edits, package release, installation, model-benefit run or full consumer trial has been performed by this packet.

Record checks: an independent read-only verifier recovered goal/current task/next authority from the files, checked pivotal source claims and resolved all local links/explicit anchors. This one record-readback observation is not a completed F3 comparison or efficacy result. Diff whitespace checks pass. The original transfer deny-list self check passes. Primary deny-list checks found new source-checkout and marketplace labels here; both were removed without changing the evidence hashes or source findings. Its remaining two hits are unchanged pre-existing M31 receipt text in TASKS and the lightweight-direction note; full primary-list cleanliness is not claimed. No deny list or scanner was changed.

Delivery limitation: the installed GitHub CLI could not resolve the canonical private repository through its current API access; no draft PR was created and no remote write was attempted. Keep this local review branch and resume remote delivery when access is available. This does not block source read-only preparation or confer merge authority.
