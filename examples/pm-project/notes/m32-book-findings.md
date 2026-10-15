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

Continuation grant: after the owner was told that preparation/checks could proceed and integration/installation would wait for a concrete result, the owner replied on 2026-10-15: “Вперед, значит.” M32-T1 now prepares the source candidate in isolated branch `codex/m32-prompting-carriers` from source HEAD `6aa66c26eb9a5790de777edc050dc71ef7b0112a`. Root alone may edit `plugins/prompting-methodology/` and only that plugin's entry in `.claude-plugin/marketplace.json`, plus M32 findings/current records in the separate methodology branch. Other plugins, source default branch, installed copies, book and global settings remain unchanged. Candidate metadata may advance consistently for review; no release or installation is inferred. The previous read-only source restriction described T0 recordkeeping, not this separately started T1 continuation.

M32-T1 source result: local candidate commit `53b62f0` on `codex/m32-prompting-carriers` updates the prompting entry, templates, commands, two agents, ontology, agent-prompt skill and framework/adversarial references. The own manifest and only the matching marketplace entry agree at candidate 0.6.0. Other plugins, source default checkout and installed copies are unchanged. The source README identifies this checkout as its canon; the local Claude marketplace registry points at it. Codex installed-entry bytes match that source baseline; its independently configured upstream remains unproven until activation checking.

Independent document review found omitted categorical claims in five ontology nodes plus the agent-suitability checklist and then two adjacent nodes. Those omissions were corrected and rechecked; final scoped review found no remaining actionable issue. Static checks preserve all 116 annotation-bearing concept IDs and 85 Link records with resolving targets, other marketplace entries and agent model pins. Both skill-creator validators and diff whitespace check pass. These are static properties, not measured model gains.

A fresh native author actually used the updated agent-prompt skill to produce a complete no-tool notice-classifier prompt, rationale/reproducibility contract and 11 separate eval inputs. Independent review checked authority, schema/unknown handling, distinct injection probes, supplied synthetic secret, normal controls and honest DRAFT. The system text in prompt and eval matches. No target response was generated: all target cases remain NOT_RUN. Full authored artifacts and static receipts are retained in the session-owned local `m32-t1-evidence` scratch; do not mistake them for target-run receipts.

Disposition: retain the T1 source candidate for concrete review; no merge/release/install. The source repository's existing no-push-without-explicit-command direction is preserved. M32-T2 can now investigate an optional document-reading recipe within the already selected route; no compulsory new helper or skill is inferred.

Record-check history: an independent read-only verifier recovered goal/current task/next authority from the initial files, checked pivotal source claims and resolved local links/explicit anchors. Whitespace and original transfer-list self checks passed. Primary checks initially found new source-checkout/marketplace labels and two inherited private plugin-label hits in M31 receipts. New labels were removed; later T3 readback exposed stale M31 status wording in those current records. The narrow cleanup clearly marks the historical pre-release wording and describes the superseded plugin generically, preserving disabled/retained state, the original release receipt and Git history. No deny list or scanner was changed. Final current checks are recorded after this cleanup.

Delivery limitation: the installed GitHub CLI could not resolve the canonical private repository through its current API access; no draft PR was created and no remote write was attempted. Keep this local review branch and resume remote delivery when access is available. This does not block source read-only preparation or confer merge authority.

## T2 and T3 — bounded reading checks

T2 disposition: retain the [optional reading recipe](m32-context-reading-recipe.md), with no new compulsory procedure or helper. A fresh reader applied it to seven small synthetic sources: valid tags, missing end, duplicate anchor, crossed nesting, TOC/title disagreement, headings without tags and changed content after a supplied locator. Separate simulated transport output included a readable prefix, truncation marker and closing tag. The reader recovered the missing range from actual source, distinguished literal statements from valid-section claims, flagged source defects and replaced the stale capacity assertion with the current one. All source identities were rechecked before synthesis. These are bounded source/fixture observations, not a real concurrent change, transport failure or efficacy comparison.

Root additionally extracted actual book sections 10.3 and 13.3 by unique boundaries after the existing TOC read, checked their TOC membership/nesting and retained content identities. This verifies those concrete ranges, not the whole book's truth, all possible markup or model comprehension. The trial did not justify a persistent parser or universal tag requirement.

T3 disposition: retain the existing fresh-reader check for relevant future cases, without adding a mandatory phase. A fresh reader using only current files recovered purpose, T1 candidate state, next authorized T2 action, integration limits and C3/M30/C4–C6 holds. It correctly refused to infer T2 completion from its later-step dispatch: the supplied records still showed T2 active. T3 read-only preparation ran while T2 results were returning; it crossed no integration or adoption gate, and this final synchronization records T2 before T3 disposition. Treat that observation as a real state-freshness limitation, not a completed transition proved by the worker.

The same reader inspected an explicitly synthetic module without execution or author history. It identified the contradiction between a failure-atomicity promise and append-before-callback code, and gave a distinguishing callback-that-raises input. Its source/effect reasoning was checked against the fixture. It also found historical M31 unreleased wording adjacent to completion receipts; those stale current-status formulations were marked as superseded. This sample supports local usefulness of fresh reading and directly motivated the correction; no broad measured model benefit, actual fixture execution or full consumer trial is claimed.

Full pilot inputs and unedited readbacks remain in session-owned local scratch `m32-t2-evidence` and `m32-t3-evidence`; the parent conversation retains the original worker returns. These are diagnostic reading fixtures, not deployed services or new framework runtime components.

Final record checks after the narrow M31 cleanup: both unchanged original deny-list self checks exit0, and diff whitespace check passes. Earlier failures remain recorded above; neither the scanner nor its populations/lists were weakened. Original canonical and prompting source checkouts remain clean. Independent final record/claim review completed without substantive findings; source identities, pilot results, current route, local links and private archive integrity were verified within the stated limits.

Durable private evidence: original authored artifacts, fixtures, raw readbacks and receipts are copied byte-for-byte under the canonical common Git directory at `methodology-evidence/M32-20261015/`; `manifest.json` binds their paths, sizes and SHA256 values. The temporary scratch names above remain their original provenance. The private archive is outside the tracked publication set and is not a software run-state ledger.

## Owner integration decision — 2026-10-15

After the concrete local package (source candidate53b62f0 and records14191a0), checks and remaining GitHub-access limitation were presented, the owner answered “Разрешаю.” to the request to proceed with merging the prepared branches. This settles the integration decision for those results; do not ask it again. Execute local main integration in both repositories, preserving history and existing work. Installation remains a separate action, as stated in the question and acknowledged to the owner.

Access observation at this decision: ordinary configured Git transport can read the canonical remote main, while GitHub CLI cannot resolve the private repository even without process token overrides. The built-in browser has no authenticated GitHub session. Do not extract credentials, change accounts, bypass controls or claim a PR. The owner approved merging after disclosure of this limitation; local merges are the available bounded action. Canonical PR delivery remains owed/unfulfilled; source no-push-without-explicit-command remains in force.

### Actual local integration

The authorized fast-forward merges completed without conflicts: source main moved from `6aa66c26eb9a5790de777edc050dc71ef7b0112a` to checked candidate `53b62f0fc9332e53daa3abf432f80b3ed3a17a33`; canonical main moved from `8d98a5859cbaab73b81bfc2f87b0b798bc0c4101` to accepted records packet `14191a078dd1719c8ea862d1dd5e5c39af0e61e2`. Both worktrees were clean after those merges, and their trees matched the respective reviewed branch tips. This later receipt is prepared on the existing records branch and fast-forwarded into canonical main as a separate closure commit; it changes only current state and evidence pointers.

Source main's changed-file digests match the retained T1 static receipt. The installed Codex entry still has its original baseline digest and resolves outside the source checkout. The Claude installed entry also resolves to its independent cached path; its installed registry still reports0.4.0, while the Codex prompting cache remains0.5.0. Source0.6.0 has not been installed. No source push, remote main update, PR creation, release or global configuration change occurred. Canonical remote PR delivery remains unfulfilled under its repository procedure, despite completed local integration; do not silently call this a remote merge.

M32's local integration decision is settled and implemented; do not ask for it again. Remote delivery and installation are separate next actions with their existing scope/access requirements. The authored classifier still has no target-run proof, and C3/M30/C4–C6 limitations remain unchanged.

Integration-receipt checks: both unchanged original deny-list self checks returned exit0 again; diff whitespace check passed. Their raw JSON outputs are retained with the private integration receipt.
