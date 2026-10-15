---
id: documents.conventions
title: Project document conventions
status: draft
---

# Project document conventions

<!-- anchor: documents.conventions.canon -->

## Canon and document homes

The primary reader is an agent entering or resuming a session. Optimize the canonical records for an unambiguous current goal/task/next action, stable paths and linked decisions/evidence. A readable human presentation is produced on request from this same state, without a second editable documentation set. Synchronization follows [session](../process/session.md#process.session.baton): material changes, periodic grouped progress and before planned compaction/handoff. Only affected records change; no full QA workflow or mandatory independent documentation judge accompanies ordinary record maintenance.

- **DOC-101** MUST: Declare one editable home per project-document role and existing binding instructions. AGENTS owns the entry/path map and a short project profile; VISION owns intended outcome; ROADMAP owns outcome route; TASKS owns authorized current work; HANDOFF owns the present baton. References point to evidence rather than duplicating its body.
- **DOC-102** SHOULD: Use those five current documents as the default. Decisions and notes/results are event-driven records without mandatory separate forms. Small open choices may stay with TASKS. Add a separate profile, index or question register only for real complexity or retained binding project conventions.
- **DOC-103** MUST: Preserve actual grants, accepted decisions, foreign state and original task/result history when mapping an existing project. A filled form or proposed queue item creates no authority; package revisions are not automatic adoption.
- **DOC-104** MUST: Keep project-document metadata and vocabulary distinct from the neutral specification format. FORMAT governs this repository's neutral cards/anchors/norms; a project's declared conventions govern its actual records.
- **DOC-105** MUST: Keep design as intent and evidence as established observation. A registry only indexes records. Sensitive evidence uses authorized pointers and disclosed access limits, not copied payloads.

<!-- anchor: documents.conventions.profile -->

## Declaring the project profile

The purpose of a profile is to make the existing project legible to its next reader. Its input is the owner's task, binding entry instructions, actual documents and their ownership, the adopted conventions and existing storage rules. Its output is the entry's compact map of those facts. The custodian writes that map within the task grant; changes to binding conventions or direction belong to their declared human authority. A package update supplies a proposed profile, not a newly adopted rule.

- **DOC-106** MUST: Resolve the adopted conventions revision, document layer and actual paths from project instructions before creating or migrating records; record any conflict and its controlling authority in the current baton.
- **DOC-107** MUST: Give each declared document role its reader, writer, update event and applicable retention or size policy; retain existing backlog and snapshot roles with reciprocal navigation rather than absorbing them into the route.
- **DOC-108** MUST: Classify new, existing, migration and resume work from actual intent and artifacts; absence of a preferred file alone is not evidence of a new project or permission to replace existing records.

Use a single layer when one custodian owns the current records. A layered project declares each layer's path and write boundary: for example, a direction owner keeps VISION and binding decisions, while a delivery custodian keeps a scoped ROADMAP, TASKS, HANDOFF and notes. The delivery layer reads the authoritative direction; a short local vision, if retained, links to it and is explicitly a condensation. A discrepancy becomes a request to the direction owner, recorded in the delivery handoff; neither custodian silently rewrites the other's layer. These are declared profiles, not required directory names. In an established project, resolve its actual mode and path instead of assuming that a runtime's working directory is the durable root.

The default role map below states responsibilities, not universal filenames. AGENTS declares the actual locations, permitted writers and reading order. When a project already uses another name, keep that home and link to it. A role absent because it is unnecessary is explicitly marked as such; it does not justify a new register.

| Role | Reader | Writer and authority | Update event | Retention |
|---|---|---|---|---|
| Entry/profile (AGENTS) | Every arriving contributor | Entry custodian under the applicable instruction-change grant | Adopted profile, path, ownership or work-method change | Current compact map; prior binding revisions remain recoverable |
| Direction (VISION) | Owner and task planners | Direction owner, or custodian recording an authentic owner decision | Outcome, user, constraint or non-goal changes | Current intent with links to its decision provenance |
| Outcome route (ROADMAP) | Planners and arriving contributors | Route custodian within approved direction | Approved start, verified close, dependency change or replan | Stable IDs, current focus and deferred outcomes; detail points to retained evidence |
| Current packet (TASKS) | Work assignees, reviewer and owner | Packet custodian; individual task writers within assigned scope | Plan, matching approval, activation, task state/result or carryover | One current packet; original packet and results retained before replacement |
| Present baton (HANDOFF) | Next session and owner | Session custodian for its layer | Activation, material blocker or session closure | Current and relevant previous state; historical narrative moves to notes |
| Binding decision | Future contributors affected by the choice | Declared decision authority; recorder preserves provenance | Actual binding choice, amendment or supersession | Accepted body retained under project decision policy |
| Notes/result | Task author, reviewer and later linked readers | Assigned writer within the task | Observation, local choice, error or result | Evidence and context retained; only linked portions read at resume |
| Existing backlog | Planner selecting future work | Existing backlog custodian | Idea, priority or selection changes | Idea pool; a selected item points to the route ID without losing its origin |
| Existing snapshot/status record | Reader inspecting observed state | Existing snapshot custodian | New observation with its identity/time | Observed state, not a competing plan; route points to the relevant observation |
| Generated evidence/index | Readers navigating actual outputs | Configured generator or evidence custodian | Its source inputs change or a relevant check runs | Actual output identity and access limits; an index holds pointers |

An adopted profile can prescribe common metadata such as type, stable ID, title, provenance time, status and source links. Follow that project's key set and status vocabulary: a project task's `active` or a vision's `accepted` is not this repository's neutral `draft` card. If a profile uses generated timestamps, obtain them from the clock; name the actual actor and approval channel. Do not infer approval from a status word. Keep filenames stable when status changes, using the declared field or body line for state. Existing valid metadata is retained during an additive edit; an incompatible parser or naming migration needs its own grant.

A project may declare read budgets, handoff line caps, short route rows or a maximum route size. Record the applicable value and the overflow home in its entry/profile. Such values control that project only. Shorten current navigation by linking to retained results; never erase evidence, pending authority or failed work to meet a cap. Long normative references may use structured sections; frequently rewritten current records can stay plain Markdown under their declared format. Existing generated code maps describe current code only when that software method provides them; architecture describes intent. General document work needs neither a code map nor a new generator.

<!-- anchor: documents.conventions.adoption -->

## Establishing or recovering the homes

1. **Inspect before choosing.** Read the entry and actual current records, their links, relevant accepted decisions and the working-state ownership. Establish what initiative exists, which work is authorized and which records already answer each role. Produce a role-to-path map and list missing inputs; a filename search alone does not settle the classification.
2. **Genuine new project.** An owner starts an initiative without existing product/work records to recover. Capture purpose, users, arrival criterion, constraints and non-goals in VISION; derive an outcome route where the initiative needs multiple phases. Propose the five current homes from the [forms index](templates/INDEX.md), adapted to the actual project. Initial drafting does not authorize implementation or a reserved release.
3. **Existing project.** Existing documents, deliverables or decisions establish prior work even when the preferred five files are absent. Map and link those records first. Fill only genuine gaps within the grant, retaining accepted direction, IDs, pending approvals and original outcomes. Existing backlog and observed snapshots keep their distinct roles. Date factual corrections and cite the observation that replaces a stale claim.
4. **Conventions migration.** A matching owner decision authorizes changed homes or profile rules. Record the old-to-new role/path map, adopted revision, writer boundaries and affected readers. Preserve original content and history before moving it; update inbound links and check that the declared readers reach the new home. Keep a reference at an old location only when needed for navigation, clearly identifying the new editable home. A profile proposal with no migration grant remains proposed.
5. **Resume.** Resolve the same declared homes and active packet. Reconcile the handoff with actual artifacts and the last checked revision; retain failures, counters, held work and unknown effects. Follow [session recovery](../process/session.md). Resume is not adoption of a fresh template or restart of an old task.
6. **Read back the change.** Inspect each changed home and its links as an arriving reader. Verify writer authority, actual paths, intended update events, metadata compatibility and retention. Follow project storage/commit policy; report saved but uncommitted owned files when a commit is ungranted or blocked by foreign state. A syntax check establishes syntax only.

The output is a usable entry/profile and the necessary current records, with authentic adoption provenance and retained source pointers. Stop dependent work when ownership conflicts, missing authoritative inputs or an ungranted profile migration prevents it; continue other already authorized work. A status-only request reads this map and changes nothing.

<!-- anchor: documents.conventions.entry -->

## Entry duties and additive reconciliation

The entry's early continuity block is a compact navigation/behavior contract under DOC-101, LIFE-103 and SESSION-101–105. Use the [AGENTS form](templates/AGENTS.md#documents.templates.agents.form) for new entries. It makes five existing duties visible: recover actual goal/current task/grant/next action; connect task to route and intended value; distinguish planned/executed/verified/accepted; synchronize affected owning records at the session cadence; leave a usable continuation without chat. Current facts remain in their owning documents, detailed procedures at their adopted homes. Respect project metadata and any mandatory preamble before placing this block; its position implies no model-attention guarantee.

During authorized bootstrap/onboarding or an explicitly requested entry update, inspect the complete existing entry and applicable linked rules before editing. Compare the five duties by meaning, not exact headings, wording, filenames or markers. Record covered, missing and conflicting duties with existing source pointers in the current task/result; no new permanent checklist or registry is required. A matching bootstrap/entry-update grant covers scoped additions; reuse it rather than asking again. Read-only status or ordinary resume does not authorize instruction edits or adoption of a newer profile.

For a new entry, fill the compact block and actual document-home map from measured inputs. For an existing entry, keep covered clauses, original rules, metadata, ordering constraints, document names/paths and links intact; insert only missing nonconflicting duties at the earliest permitted location. Do not replace the entry with the seed, normalize unrelated prose, duplicate an equivalent rule or create shadow documents. If a project requires its entry to remain unchanged, or a proposed duty conflicts with its rules or writer scope, preserve it, record the exact conflict and route only the missing decision. Continue independent granted work. Missing purpose, records or approval stays an explicit gap, not an invented answer or consent.

Read back the actual result and diff: original content is preserved, additions are scoped, actual links resolve, and the arriving reader can recover goal/current/next/authority/result/holds from the declared homes. Repeating the same comparison on that result should propose no further additions unless inputs changed. Report unresolved duties and checks separately. An available structural checker such as an orientation marker check cannot certify this semantic comparison; no automatic entry installer or repair is implied.

<!-- anchor: documents.conventions.cases -->

## Worked profile cases

The following cases are fictional. “Meadow document review” and every grant, path and observation in these cases are invented to demonstrate the procedure; they are not project evidence or permission.

**New initiative.** An imagined owner asks a custodian to review a supplied policy packet for consistent definitions. No earlier Meadow initiative exists. The proposed single-layer profile declares AGENTS at the root, VISION/ROADMAP/TASKS/HANDOFF under `records/`, local observations under `records/notes/`, and source documents as read-only. The goal is a review packet whose claims are checked against the supplied text; publication is a non-goal. The imagined drafting grant permits these records and a review draft. The custodian records that grant's exact scope, keeps external sharing pending, and chooses a document comparison method. No software workflow is required.

**Existing records and later migration.** Meadow already has `review-charter.md`, `review-route.md`, `current-work.md` and `baton.md`, plus `ideas.md` and `source-observations.md`. There is no VISION filename. The custodian classifies the project as existing: the charter owns intent, the route owns outcomes, current-work owns the approved packet and baton owns present state. Ideas remains the backlog; source-observations remains the dated snapshot. Without a migration grant, the custodian adds only authorized links and missing profile facts. If the imagined owner later authorizes moving these four homes to `records/`, the custodian retains their originals, writes a path mapping and updates references; the existing outcome IDs and failed task record survive the move. A cold reader can follow the entry to the sole editable homes.

**Resume and refusal.** The next Meadow session finds a review draft and a handoff saying “approval pending.” A filled template in a reference folder says “approved,” but it is labeled fictional. The session checks the actual gate record and earlier owner response; if neither grants the next action, it records the blocker and does not activate that action. If the real prior grant covers continued local comparison, that work resumes without another approval request. A read-only request for status reports the observed draft, pending sharing decision and next permitted comparison; it neither migrates records nor marks readiness. Missing source observations remain a missing-input limit, even when every form field is filled.
