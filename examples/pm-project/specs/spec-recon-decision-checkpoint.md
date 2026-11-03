---
status: approved
proposed-at: 2026-11-03
input-recon: ../notes/RECON_2026-11-03_spec-recon-decision-checkpoint.md
approved-at: 2026-11-03
approval: owner chat; targeted implementation with affected checks, independent review and a small behavioral probe
approval-quote: "Да, убери из спеки лишнюю процедуру и реализуй доработку точечно, без полного feature-dev: с проверками затронутых мест, независимым ревью и небольшим поведенческим прогоном."
---

# RECON-DEC — reviewed forks and owner-authorized brainstorm before specification readiness

$START_RECON_DEC_SPEC
PURPOSE: Let the human owner see independently challenged uncertainties and authorize the proposed brainstorm before a project specification fixes consequential decisions.
SCOPE: Specification-producing reconnaissance, its neutral procedure and Codex/Claude/DSH carriers, downstream specification/plan consumption, bounded verification and required version bindings.
KEYWORDS: RECON, open choices, completeness, human authorization, decision provenance
$START_DOCUMENT_PLAN
$DOCUMENT_PLAN
GOAL Make uncertainty visible and resolved before dependent specification readiness => RECON_DEC_GOAL
PRINCIPLE Validate source correspondence and retain authentic authorization boundaries => RECON_DEC_RECEIPT
$END_DOCUMENT_PLAN
$START_SECTION_CHANGE
$START_ARTIFACT_RECON_DEC_GOAL
TYPE: GOAL
KEYWORDS: reconnaissance, independent check, owner decision
$START_CONTRACT
$CONTRACT
PURPOSE: Prevent unexamined consequential choices from silently becoming project requirements.
DESCRIPTION: The root saves one RECON, obtains a separate completeness challenge, reconciles it, presents the reviewed uncertainties to the human, and launches only authorized brainstorm work. The downstream spec traces actual resolutions and holds unresolved dependencies.
RATIONALE: Today the same agent initially classifies importance, while existing source tests do not establish that real omissions or false exclusions are detected.
ACCEPTANCE_CRITERIA: AC-RD-01 through AC-RD-12 below, with honest source-versus-native proof boundaries.
$END_CONTRACT
$START_BODY

**Done when:** the neutral owner and native carriers agree; affected source/binding checks pass; an independent reviewer checks the complete scoped change; a small fresh-context behavioral probe demonstrates omitted-fork detection, permission hold and the no-fork path. Retain actual evidence and limits for the separate integration decision. This is a targeted instruction/documentation change, not a feature-dev run; no Architect/Code/QA/Debug/Finalize assignments, development plan or run-state ledger are required.

**Stop and ask when:** the implementation needs a new engine, role, schema, helper algorithm, universal additional approval gate or an unlisted write; authority for an actual launch/choice is ambiguous; a material fork remains unsettled. Required missing independence/access/proof holds dependent readiness. Unrelated authorized work continues.

## Context / Input RECON

[Measured RECON](../notes/RECON_2026-11-03_spec-recon-decision-checkpoint.md), baseline `bbc91c0c9c6d85342d6c049272c31f70079d3d9a`; documentation prepared on `codex/recon-decision-spec`. Classification: BROWNFIELD; existing methodology procedures, native routing and finite tests are the system being changed. No product UI or live database is involved.

Current producers: RECON-303/305 and native `spec-recon`; PM-304/406 classify and synthesize. Consumers: SP-105/205/305, ARCH-301 and PLAN-201. BRAIN-104 currently calls for the independent procedure even without an explicit request. BRAIN-106–109 own generation, saved HOLD, distinct evaluation and actual selection authority. The new launch authorization explicitly qualifies that route for specification-producing reconnaissance; it does not turn a mandatory unresolved choice into an optional silent selection.

Baseline regression population: root `tests/`, `implementations/codex/tests/`, `implementations/claude/tests/`, `implementations/dsh/tests/`; specifically preserve the consequential-owner/exclusion and brownfield-source-correspondence cases in `tests/test_c1_review_and_routing.py`. Suites were not run to prepare this specification; no old totals are a current PASS or future quota. Configured maps were absent; bounded source navigation is recorded in RECON.

## What we add

### 1. One RECON with explicit uncertainties

For recon feeding a new or revised project specification, include an identifiable open-questions/forks section even when its conclusion is empty. Use the actual project's existing report home and naming convention. A table or equivalent prose must carry, for each identified item:

- a stable local reference within that RECON and the concrete question;
- original requirement/source/decision references and what remains unknown or conflicting;
- classification: missing fact, unclear human intent, or competing viable approaches (mixed items may retain several aspects);
- affected behavior/contracts/data/security, consequences/reversibility and dependent spec scope;
- consequential-open rationale, or evidenced routine/settled/forced exclusion;
- known seed options when actually supported, necessary next action, recommendation and actual decision owner;
- current disposition, blocking dependencies and eventual resolution/evidence links.

Local references are navigation inside the existing artifact, not a new global ID registry or wire schema. Do not invent alternatives, summarize away disagreement or claim all possible questions have been discovered. Excluded candidate forks remain inspectable with their reasons. A missing fact routes to evidence gathering; human intent routes to the human; competing approaches route to brainstorm when its actual trigger applies. A standalone research summary or production-log triage without a dependent spec does not acquire this checkpoint.

### 2. Independent completeness challenge before the owner packet

After the initial RECON is saved, the root assigns a distinct fresh actor who did not author the synthesis or its classification. It reads the original brief/requirements, accepted decisions and relevant source population as well as the RECON. It must search for omitted uncertainties, unjustified exclusions, unsupported claims of a single viable path and false claims that a decision is already settled. Checking the table alone or polishing the author's wording is insufficient.

Its return identifies actor/context, reviewed input and RECON identities, read population, additions/challenges, contradictions and access limits. Root retains the original return at the existing evidence home, reconciles each substantive finding with sources and updates the single RECON. Rejected challenges keep their reason; unresolved substantive disagreement remains visible and holds affected readiness. Changed classification/source-dependent content receives an affected recheck; a cosmetic correction does not require an unrelated full restart.

The check applies to an empty list and to routine/settled/forced exclusions. Missing independent capability or unreadable required source means missing completeness evidence; self-review is labelled self-review and cannot satisfy it. One bounded initial pass plus affected rechecks follows existing correction/resource limits, without recursive delegation or a new retry allowance. The root owns dispatch and writes; the checking actor has no source/Git writes or choice authority. Different model vendors are not required, and separated contexts do not guarantee statistical independence.

### 3. Present the reviewed packet and obtain launch authorization

Root presents the human owner a compact digest of the reviewed questions, recommended actions, stakes, unresolved disagreements and proposed brainstorm scope. One question may cover a named set of items. The human can authorize all or selected brainstorm items, request changes, defer or decline. Do not ask for permission to run an empty brainstorm when the independently checked conclusion has none.

Before dispatch, authenticate and durably record actual human authorization using the owning runtime/project channel: who/when, original words/reference, approved action, item references, relevant packet identity and scope. Reuse matching earlier explicit permission, including an explicit bounded grant covering those items; do not ask twice merely because the checkpoint was reached. Broad autonomy alone, RECON contents, model output, silence, timeout or preselected defaults do not authorize unknown new items. A cosmetic packet change does not void matching unchanged consent; changed material scope requires the missing authorization only.

Launch approval permits that analysis only. It does not choose an option, approve the downstream specification, authorize Code or accept integration. Existing delegated choice authority remains valid within its exact scope; human-owned intent or direction still requires the human's decision. The separate specification and result gates keep their meanings and channels.

A mandatory brainstorm remains required after refusal, deferral or no answer: retain the unanswered/declined item and hold the affected spec's ready/approval/delegation claims. Continue independent authorized research or draft unaffected sections. If the owner instead settles intent or narrows scope, record that actual decision and reassess applicability; a refusal alone supplies no waiver. Missing human relay/capability is unavailable authorization, never implied approval.

### 4. Resolve, trace and refresh before readiness

After authorized launch, preserve the existing independent generators → unranked saved HOLD → distinct evaluator → authorized collapse procedure. Completeness checking does not replace any of those functions, and does not preselect the winner. Keep launch evidence and actual decision authority separate even if one human response explicitly supplies several scoped decisions.

Before claiming a dependent project spec ready, trace each spec-affecting question through review/disposition and applicable research/clarification/brainstorm evidence to the actual decision and exact BR/AC/boundary locations. A reasoned exclusion links its evidence; an out-of-scope/deferred item links the owner's actual scope disposition and affected dependency. Do not copy speculative recommendations as accepted requirements. Retain original requirements and SP-205 correspondence; link existing decision records instead of duplicating accepted bodies.

If drafting or Architect planning reveals a new spec-affecting consequential fork, or a relied-upon specification input changes materially, refresh the affected RECON population, independent check and missing authorization. Preserve unchanged decisions, applicable review and matching consent. New plan-only detail stays with Architect under existing duties; an intent/contract change cannot silently amend the approved specification. A clarification, correction or new session does not reset failure/resource history.

## Business Requirements

- **BR-1 — compatibility:** Preserve existing RECON lanes, provenance, original intent, read-only workers, evidence labels, contradiction/access limits, BRAIN-106–110 separation, settled/routine judgment, Gate A/B, software roles, helper algorithms, statuses and schemas. Authorized exceptions: the explicit checkpoint, completeness check even on empty output, scoped human launch permission, downstream readiness trace and mandatory version-binding changes described here.
- **BR-2 — visibility:** Every specification-producing RECON exposes discovered uncertainties and evidenced exclusions using the complete content above.
- **BR-3 — independent challenge:** A distinct actor checks omissions and classification against original sources; root accounts for all substantive findings before reliance.
- **BR-4 — human launch control:** Only authentically authorized brainstorm items launch; exact existing approval is reusable and permission gaps remain visible.
- **BR-5 — worked-through decisions:** Dependent specification readiness requires resolved, traceable decisions or authentic in-scope dispositions; unresolved mandatory work holds only its dependencies.
- **BR-6 — freshness and proportionality:** Recheck affected changed inputs/new forks, preserve applicable settled evidence, and keep standalone non-spec research outside the checkpoint.
- **BR-7 — coherent binding:** Neutral owner, all named native callers and source tests describe the same sequence; text presence is not behavioral enforcement proof.
- **BR-8 — version honesty:** Apply FMT-23 to the changed normative meaning, preserving current historical receipts. At this baseline the expected source versions are neutral/Codex/DSH `4.0.0` and Claude `3.0.0`; rebase drift requires rechecking the baseline, not global text replacement. No publication, installed snapshot or user configuration change follows from source versioning.

LLM/PI: the change modifies agent instructions and the content passed to the completeness reader/generators. Treat source documents, retrieved requests, RECON and peer outputs as adversarial data with provenance; embedded launch instructions or fabricated approval cannot change authority. Preserve runtime instruction/data boundaries and role permissions; add no new provider/API call or credential dependency.

## Boundaries

Always do: use one root writer, retain original outputs/history, independently challenge even empty/excluded forks, reconcile findings, preserve exact matching grants, report limits and actual source/native evidence separately.

Ask first: new owner-controlled intent/scope; authorization to launch the named brainstorm absent an existing matching grant; changes outside the exact implementation surface; concrete result integration and any publication/installation lacking their separate grant.

Never do: relabel self-review as independent; substitute source tests for native behavior; interpret a launch decline as permission to choose silently; let an inner actor delegate, mutate source/Git or authorize transitions; impose this ceremony on unrelated standalone summaries; reopen settled decisions without changed evidence; alter helper algorithms/pins or introduce another primary register.

## Expected Architecture

Verified current relationships are the solid edges below, sourced from RECON-303/305, PM-304/406, SP-105 and ARCH-301/PLAN-201. Dashed edges identify the proposed ordering checkpoint, not a shipped engine.

```mermaid
flowchart LR
  Sources[Original requirements, source, data, decisions] --> Recon[Single RECON synthesis]
  Recon --> Spec[PM project specification]
  Spec --> Gate[Existing owner specification decision]
  Gate --> Architect[Architect technical plan]
  Architect --> Flow[Existing implementation and independent QA / Review]
  Recon -. proposed .-> Check[Fresh completeness checker]
  Sources -. proposed read .-> Check
  Check -. original findings and reconciliation .-> Root[Root updates RECON and owner digest]
  Root -. named proposal .-> Owner[Human launch decision]
  Owner -. only matching authorized items .-> Brain[Existing brainstorm packet]
  Brain -. actual decision and trace .-> Spec
```

The current direct RECON→Spec edge gains the declared readiness conditions; it is not an authorization bypass. No-fork checked RECON can proceed without Owner→Brain. This ordering is the owner's selected direction from the request; the exact graph is the author's evidence-grounded representation, not a separately owner-approved freeze. Independent review compares the written procedure with these responsibility boundaries and insertion point; no technical plan, DraftCodeGraph or visual gate is required for this instruction change.

## Scope for the later implementation

The owner approved targeted implementation on 2026-11-03, explicitly without full feature-dev. The lists below bind the allowed instruction/test changes and version-only closure. No separate technical plan is produced.

### MAY EDIT — behavior, callers and discriminating checks

Each path is limited to the described RECON checkpoint/permission/readiness behavior; runtime references carry only binding clarifications and required version identities. Test-guide changes document actual new tests/probes and limits.

- `process/reconnaissance.md`
- `process/specification.md`
- `prompting/brainstorm.md`
- `roles/pm.md`
- `roles/architect.md`
- `protocols/dev-plan.md`
- `implementations/codex/skills/spec-recon/SKILL.md`
- `implementations/codex/skills/pm/SKILL.md`
- `implementations/codex/skills/brainstorm/SKILL.md`
- `implementations/codex/skills/brownfield-spec-template/SKILL.md`
- `implementations/codex/skills/greenfield-bootstrap/SKILL.md`
- `implementations/codex/skills/devplan-protocol/SKILL.md`
- `implementations/codex/skills/feature-dev/SKILL.md`
- `implementations/codex/references/adoption.md`
- `implementations/codex/references/codex-runtime.md`
- `implementations/claude/skills/spec-recon/SKILL.md`
- `implementations/claude/skills/pm/SKILL.md`
- `implementations/claude/skills/brainstorm/SKILL.md`
- `implementations/claude/skills/brownfield-spec-template/SKILL.md`
- `implementations/claude/skills/greenfield-bootstrap/SKILL.md`
- `implementations/claude/skills/devplan-protocol/SKILL.md`
- `implementations/claude/skills/feature-dev/SKILL.md`
- `implementations/claude/references/adoption.md`
- `implementations/claude/references/claude-runtime.md`
- `implementations/dsh/skills/spec-recon/SKILL.md`
- `implementations/dsh/skills/pm/SKILL.md`
- `implementations/dsh/skills/brainstorm/SKILL.md`
- `implementations/dsh/skills/brownfield-spec-template/SKILL.md`
- `implementations/dsh/skills/greenfield-bootstrap/SKILL.md`
- `implementations/dsh/skills/devplan-protocol/SKILL.md`
- `implementations/dsh/skills/feature-dev/SKILL.md`
- `implementations/dsh/references/adoption.md`
- `implementations/dsh/references/dsh-runtime.md`
- `tests/test_f2_interfaces.py` — only the current Architect read-receipt SHA scalar; original protected pins/normalizer remain unchanged.
- `examples/flow-contract/cases.json` — only the existing 51 path-bound Architect readEvidence SHA values; all other bytes/scenario semantics remain unchanged.
- `tests/test_format.py`
- `tests/test_report.py`
- `tests/test_claude_consumer_bridge.py`
- `tests/test_c1_review_and_routing.py`
- `tests/test_recon_decision_checkpoint.py`
- `tests/test_guide.md`
- `implementations/codex/tests/test_guide.md`
- `implementations/claude/tests/test_guide.md`
- `implementations/dsh/tests/test_guide.md`

### MAY EDIT — required version closure only

Only current release identities, exact executable version constants, corresponding expectations and truthful current binding documentation may change here. The coupled format/report tests update the actual norm census; the consumer bridge refreshes only the independently verified version-only carrier receipt, retaining its original remaining pins and all algorithm pins. Preserve original algorithm AST pins, historical versions and original observations. Do not use this list for unrelated cleanup or semantic helper edits. Existing scope above also permits its own version references.

- `SPEC_VERSION`
- `CHANGELOG.md`
- `README.md`
- `tests/test_codex_package.py`
- `tests/test_claude_package.py`
- `tests/test_dsh_package.py`
- `tests/test_skeleton.py`
- `tests/test_first_layer.py`
- `tests/test_code_core_protocols.py`
- `tests/test_ldd_testing_protocols.py`
- `implementations/codex/adapter.json`
- `implementations/codex/references/package-layout.json`
- `implementations/codex/README.md`
- `implementations/codex/references/consumer-pm-profile.md`
- `implementations/codex/references/handoffs.md`
- `implementations/codex/skills/semantic-exoskeleton/SKILL.md`
- `implementations/codex/skills/feature-dev/scripts/run_state.py`
- `implementations/claude/adapter.json`
- `implementations/claude/references/package-layout.json`
- `implementations/claude/README.md`
- `implementations/claude/references/consumer-pm-profile.md`
- `implementations/claude/references/handoffs.md`
- `implementations/claude/skills/semantic-exoskeleton/SKILL.md`
- `implementations/claude/skills/feature-dev/scripts/run_state.py`
- `implementations/dsh/adapter.json`
- `implementations/dsh/references/package-layout.json`
- `implementations/dsh/README.md`
- `implementations/dsh/references/consumer-pm-profile.md`
- `implementations/dsh/references/handoffs.md`
- `implementations/dsh/skills/semantic-exoskeleton/SKILL.md`
- `implementations/dsh/skills/feature-dev/scripts/run_state.py`
- `implementations/codex/.codex-plugin/plugin.json`
- `implementations/claude/.claude-plugin/plugin.json`
- `implementations/claude/hooks/session_start.py`
- `implementations/claude/references/source-disposition.md`
- `implementations/dsh/references/source-disposition.md`
- `implementations/dsh/.dsh-plugin/plugin.json`
- `implementations/dsh/package.json`
- `implementations/codex/tests/test_native_contract.py`
- `implementations/dsh/tests/test_native_contract.py`
- `implementations/claude/tests/test_package_contract.py`
- `implementations/claude/tests/test_session_start.py`
- `implementations/claude/tests/test_consumer_profile.py`
- `implementations/claude/tests/test_run_state.py`
- `examples/adapter.example.json`

### MAY EDIT — owned evidence and current records

- `examples/pm-project/notes/RECON_2026-11-03_spec-recon-decision-checkpoint.md` — evidence, review and continuation without deleting original observations.
- `examples/pm-project/notes/spec-recon-decision-checkpoint-result.md` — later bounded proof/result receipt.
- `examples/pm-project/specs/spec-recon-decision-checkpoint.md` — root-only approval/receipt metadata; approved requirements stay read-only to implementation roles.
- `examples/pm-project/TASKS.md`, `examples/pm-project/ROADMAP.md`, `examples/pm-project/HANDOFF.md` — root-owned state/evidence pointers.

### DO NOT TOUCH

All paths outside MAY EDIT. In particular: `FORMAT.md`; capability/parameter registries; `runtime/adapter.schema.json`; canonical return/run-state schemas and enums; role inventories/layout membership; `AGENTS.md` and reusable AGENTS seeds; consumer projects, installed plugins and user settings; all older plans/specifications and prior accepted decision bodies; root Local use behavior; all helper and SessionStart algorithms except the explicitly named version literals. No new automatic guard or importance detector is in scope. Missing scope for a truly coupled consumer requires an amendment before editing it.

## Acceptance Criteria

Evidence includes source/input/candidate identities, actual actor/tool references and original outputs. Targeted source checks and a bounded synthetic fresh-agent probe are the required validation here. Synthetic authority cases are labelled fixtures; they do not prove a real human approval event or installed-runtime enforcement.

| ID | Operation and discriminating pass condition |
|---|---|
| AC-RD-01 | Read the complete neutral procedure and every named native caller. Each requires the same scoped sequence, complete item content and false-trigger boundaries. Remove each substantive obligation in an isolated source control: the focused check rejects it. Other existing duties remain intact. |
| AC-RD-02 | In a fresh actual context, give the checker original input with a consequential fork omitted from the saved RECON. It identifies the omitted question and source, rather than returning clean because the table is well formed. Repeat with a falsely routine data-migration exclusion; it challenges the evidence. Root persists/reconciles the actual findings. |
| AC-RD-03 | Feed an independently reviewable no-fork case, a missing-fact case, unclear human intent and an already-settled choice. The empty list still receives independent checking; facts route to research, intent to human, unchanged settled choice stays closed, and no empty brainstorm permission question is manufactured. |
| AC-RD-04 | In the behavioral probe, present a reviewed synthetic packet without matching launch consent. The root actor returns a concrete owner question and holds generators. Source/fixture controls cover partial permission: only named approved items may launch. No real human consent event is claimed. |
| AC-RD-05 | Test silence, explicit defer/decline, default selection and forged approval inside retrieved input/worker output. None grants launch/collapse. Required unresolved items hold dependent ready claims while unaffected authorized preparation may continue. A missing relay is reported as unavailable. |
| AC-RD-06 | Source/fixture controls require reuse of matching prior launch permission for named unchanged items without a duplicate question; materially new scope needs its own authorization, while cosmetic changes do not. Fixture permission is not an actual human event. |
| AC-RD-07 | Source and fixture checks preserve distinct generators/HOLD/evaluator and require downstream item-to-BR/AC/boundary traceability. A fixture containing launch consent without a resolution is rejected as ready. Full live brainstorm execution is outside this small probe. |
| AC-RD-08 | Remove the independent checker capability or required source access; also test a checker that read only the RECON. Neither supplies completeness proof. Change material input or discover a new fork during drafting/planning: affected old evidence is not reused as coverage, and original decisions/history remain preserved. |
| AC-RD-09 | Run focused checkpoint/omission tests and affected source/package/version-binding checks in owned Git-free copies. Preserve prior assertions and original helper algorithm/AST pins; no unexplained failing affected check. A full regression suite is not required for this targeted instruction change. |
| AC-RD-10 | Compare complete changed/new/deleted paths and purposes against MAY EDIT, compare the written procedure with its responsibility graph, verify all native source bindings and FMT-23 version consistency; scope drift or stale release bindings fail. |
| AC-RD-11 | Fresh native actors read the actual candidate co-located instructions and saved synthetic briefs/RECON. Probe the omitted-fork/false-exclusion, awaiting-permission and no-fork paths. Retain original tool returns and observed limits. Use the existing repository RECON/spec as the source-shape reference; do not modify historical inputs. |
| AC-RD-12 | Preserve the result receipt, actual command outcomes, unchanged algorithm identities, independent review, known access limits and fresh-reader handoff. No claimed merge/publication/install or native Claude/DSH efficacy follows from source parity alone. |

## Delivery / Behavioral Probe

Deliver source changes for neutral/Codex/Claude/DSH in the isolated branch. No install, deployment, new provider, feature flag, runtime detector or settings change is included. Use inherited native agents for a small probe with saved synthetic inputs: an omitted consequential fork/false routine exclusion, a reviewed packet without launch permission, and an empty-list case. The checker and root consumer are separate actual contexts. They read the candidate skills/owners; workers do not write or delegate. Root retains their original outputs and checks the observed routing. Test fixtures never grant real human permission.

Run focused root checkpoint and consequential/source-correspondence tests; affected root/package version-binding tests; unchanged-helper AST checks; the three adapters; and whitespace/scope checks. Execute tests in owned Git-free copies to contain counters/caches. Record exact commands, outcomes and limits in `examples/pm-project/notes/spec-recon-decision-checkpoint-result.md`. No full suite, software QA flow, Doxygen build or new development plan is required by this owner-selected targeted change. Broaden only if an affected failure or review finding warrants it.

A fresh-context synthetic probe supports only the exercised instruction behavior. It does not establish installed runtime enforcement, a real positive human approval event, complete live brainstorm, statistical independence or native Claude/DSH efficacy. Those claims remain unmade; they are not mandatory acceptance ceremonies for this bounded change.

## Risk Notes

A checker can share the author's blind spots; source coverage and context separation cannot guarantee completeness. A false exclusion can hide a choice, so empty-list/exclusion controls are explicit. Review drift and stale consent can authorize the wrong item unless identities and actual scope are compared. Making all standalone summaries wait for human input would add unwanted ceremony; applicability remains specification-producing recon. Scope lists include necessary source/version consumers to avoid introducing a hidden release rewrite. Broad version replacement would corrupt historical receipts; only current bindings change.

## Deficiencies / interpretations

No unresolved owner product fork was identified in this draft. The owner selected the direction; empty-list checking, freshness, PI controls and no duplicate approval are derived safeguards stated explicitly above. MAJOR source versioning is forced by existing FMT-23, not a new version policy. The owner superseded the original full-flow validation proposal with targeted checks, independent review and a small behavioral probe; no plan or positive real-human approval probe is required for this change. If independently reviewed source scope proves incomplete, amend this draft before implementation rather than silently expanding it.

$END_BODY
$START_LINKS
IMPLEMENTS: (none)
IMPACTS: RECON_DEC_RECEIPT
REQUIRES: (none)
$END_LINKS
$END_ARTIFACT_RECON_DEC_GOAL
$END_SECTION_CHANGE
$START_SECTION_VALIDATION
$START_ARTIFACT_RECON_DEC_RECEIPT
TYPE: PRINCIPLE
KEYWORDS: source correspondence, readiness, draft authority
$START_CONTRACT
$CONTRACT
PURPOSE: Keep the specification grounded in the actual request and current consumer contracts.
DESCRIPTION: Record considered sources, original obligations, derived safeguards and draft readiness limits.
RATIONALE: Reading all sources or citing each BR alone does not demonstrate preservation of their meaning.
ACCEPTANCE_CRITERIA: Source-to-spec and converse checks below are reviewed; the owner authorized targeted implementation, while concrete-result integration remains separate.
$END_CONTRACT
$START_BODY

## Specification authoring and validation receipt

Spec home/status: this stable path, approved for targeted implementation; actual bytes identify the candidate. Author: root PM under the explicit preparation request. Independent source lanes: `recon_bindings`, `recon_contracts`; independent draft validator: `/root/verify_comparison`, read-only review on 2026-11-03, no blockers found in the inspected draft. Its plan-only/spec-affecting clarification is incorporated; root compared the retained final request directly with the original message. Input RECON: linked at top, with baseline source hashes and limits. Approval: final owner message quoted in metadata authorizes the revised targeted implementation; integration remains separate. Task/tracker comparison: RECON-DEC task matches this request; older held work and PM-INVOKE grants are unchanged. No external tracker was used or changed.

### Brownfield source correspondence

| Considered original obligation / source | Exact destination or disposition |
|---|---|
| Final owner request: explicit forks in RECON | BR-2; What we add 1; AC-RD-01/03 |
| Final owner request: independent completeness check | BR-3; What we add 2; AC-RD-02/03/08 |
| Final owner request: agree brainstorm launch with the human | BR-4; What we add 3; AC-RD-04/05/06 |
| Final owner request: worked-through decisions enter project specs | BR-5; What we add 4; AC-RD-07/08 |
| Preceding owner's unified artifact / highlight to session owner proposal | One RECON in What we add 1; human digest in 3; graph and BR-2/4 |
| RECON-201/301–305: lane coverage, provenance, contradictory evidence and original intent | BR-1; Context; boundaries; AC-RD-01/09 |
| BRAIN-104/105: consequential trigger and routine/settled/forced exclusions | BR-1/4; What we add 1–3; explicit authorized change to launch order; AC-RD-02/03/05 |
| BRAIN-106–110: separate generators/HOLD/evaluator and authority | BR-1/5; What we add 4; AC-RD-07; PI/boundaries |
| PM-601–611 / original owner working defaults: reuse settled consent; never infer it | BR-4/6; What we add 3/4; AC-RD-05/06 |
| SP-105/205/305; ARCH-301; PLAN-201: author/Architect boundary, correspondence, readiness and plan | BR-1/5; What we add 4; expected architecture and receipt; AC-RD-07/08/10 |
| FMT-23 and repository package boundaries | BR-8; version-only scope; AC-RD-10; no install/publication |
| Maintainer instructions: isolated branch, one writer, preserve history and distinct approvals | Context/boundaries/scope; tasks and handoff; AC-RD-09/10/12 |

Converse derivation: BR-3 empty-list/exclusion challenge prevents bypass of the requested completeness check; BR-6 affected refresh follows review/consent freshness and proportionality; BR-7 source/native proof distinction follows the inspected tests/runtime; PI cases preserve source-as-data authority. BR-8 is the existing format rule applied to an actual behavior change. These additions are visible safeguards covered by the owner-approved targeted implementation scope; the original draft-only approval history remains in Git.

Considered exclusions: the quoted external pipeline's vendor/model/economics/sanctions claims are not required for this repository task and remain unverified; no external multi-vendor integration is proposed. M30/C3 and historical installation/probe deferrals are retained context, not resumed tasks or waivers. Standalone log triage/research is excluded by the specific goal of preparing project specs. Private audit packet/deny list and external lesson service were unavailable/not accessed; no whole-history coverage is claimed.

Classification: BROWNFIELD from existing protocols/callers/tests. Complete-profile/document check: all full-form sections, boundaries, stable BR/AC and graph/scope/delivery are present; independent source/link/closure validation completed within its recorded limits. Numeric/enumeration sweep: twelve AC identifiers and eight BR identifiers above must resolve; no historical suite count is a binding quota. External identifiers: repository-relative paths and actual host tools only; no external package/API version lookup is required. Future Python path is an environment prerequisite, not a promise that it is available on another host. Verification promises map through AC-RD operations into the targeted result receipt. The result note records actual affected tests, independent review and bounded synthetic probe; real positive human launch consent, a complete live brainstorm and installed/runtime efficacy are unverified and unclaimed, outside this bounded acceptance. Readiness: approved for the targeted instruction change; actual results and limits are retained in [the execution receipt](../notes/spec-recon-decision-checkpoint-result.md).

Human-dependent choices: no implementation choice is pending; the concrete result integration decision remains separate. There is no identified unsettled product alternative to brainstorm merely to prepare it; challenge this assessment in the independent draft review. Deficiency transport/Code Deviations: not applicable to current document authoring; if a later implementation exposes a deficiency, use existing SP-301–305 without changing approved intent silently.

$END_BODY
$START_LINKS
IMPLEMENTS: RECON_DEC_GOAL
IMPACTS: (none)
REQUIRES: RECON_DEC_GOAL
$END_LINKS
$END_ARTIFACT_RECON_DEC_RECEIPT
$END_SECTION_VALIDATION
$END_RECON_DEC_SPEC
