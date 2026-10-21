---
id: process.decisions
title: Decisions and unresolved choices
status: draft
---

# Decisions and unresolved choices

<!-- anchor: process.decisions.authority -->

## Decision history

The [verification sequence](../prompting/verification.md#prompting.verification.cove) explains how to challenge and revise a consequential recommendation before using it to collapse a choice. Reuse its actual applicable reflection evidence in the decision record. This supports the existing brainstorm evaluation and decision authority; it neither reopens settled choices nor creates another phase or approval.

- **DECISION-101** MUST: Retain consequential choices with question/context, meaningful alternatives, criteria/reasons, chosen option, actual owner/consent provenance, date and affected scope/documents. Unresolved choices retain stakes, reversibility, options, evidence/dependencies and decision owner. At the consequential-open trigger load the full [brainstorm owner](../prompting/brainstorm.md#prompting.brainstorm.consequential) and link actual independent proposals, persisted HOLD and separate evaluation to the authorized decision; this record cannot substitute for those events.
- **DECISION-102** MUST: Preserve accepted decision text. A changed choice is an explicit amendment or supersession with links; new evidence does not silently rewrite authority.
- **DECISION-103** MUST: Reuse applicable prior consent, avoid reopening settled choices and distinguish grant from separately reserved result/release decisions. Involve the owner for real ungranted choices, not ordinary in-scope work.
- **DECISION-104** MAY: Keep a small unresolved choice with its task; follow an existing required question register when declared. Record the eventual resolution as a binding decision when it constrains later work.

<!-- anchor: process.decisions.profiles -->

## Applicable record profiles

A durable record makes a consequential collapse discoverable after its originating run. It records what the choice defeated and why, so a later reader does not repeat the fork from memory. The detailed profile below and the PM profile are distinct encodings of that purpose. Their document metadata belongs to a consumer project's declared convention; it is not extra metadata on this neutral file's card. Their forms are embedded here and introduce no additional primary repository template.

- **DECISION-201** MUST: When the detailed profile applies, record a collapse that fixes a plane or ownership boundary, a contract shared across artifacts (port, wire/on-disk format or schema), process/tooling/gate/launcher topology, or verification strategy. Reuse the record owning that axis; do not create a competing current verdict. Purely local variable/loop/helper choices with no cross-artifact consequences remain local.
- **DECISION-202** MUST: When the PM profile applies, put a binding direction/scope/architecture/contract/convention/tool/owner-override choice in the project's decision collection; keep a checkpoint-local choice inside its checkpoint notes. The test is whether a future session needs to find the choice without knowing which checkpoint produced it.
- **DECISION-203** MUST: Apply the actual project's record convention and authority. The detailed profile permits refreshing factual paths/names while preserving the verdict; a changed verdict creates a successor linked both ways. The PM accepted-body profile below permits only its specified metadata updates. Neither facts refresh nor a status label grants permission, proves consent or releases a separately reserved result decision.

<!-- anchor: process.decisions.detailed-record -->

## Detailed record structure and status

- **DECISION-301** MUST: In the detailed profile, use level-one body sections in this order: Status → Context → Decision → Alternatives → Consequences. Context stands without the verdict and explains the actual fork; Decision states collapsed reality in the present tense, not a promised unshipped plan; Consequences states both costs and benefits. Extra Rationale or technical sections may appear between required sections without changing their order.
- **DECISION-302** MUST: In the detailed profile, put the status on the first nonempty line of Status and use the closed vocabulary and its obligations: `Fixed (YYYY-MM-DD).` is dated and binding; `Open.` names an observation trigger; `Superseded by [successor](successor.md).` links the real successor; `Rejected — reason.` gives the reason on the status line. The rejected rationale remains useful while it prevents a plausible mistake; removal when that utility ends requires applicable project retention/authorization and never licenses deletion of protected history.
- **DECISION-303** MUST: In the detailed profile, record each genuine alternative with its concrete losing reason, as a bold-led paragraph or contested `## Why not <option>?` subsection. If there was exactly one viable path, say so and explain why as the single entry; do not pad the record with options nobody held. Only genuinely unrecoverable pre-protocol alternatives may replace the Alternatives section with the exact comment `<!-- dec-format: alternatives-not-recorded (pre-protocol decision) -->`. This is visible historical debt, not a general omission option or permission to invent remembered alternatives.
- **DECISION-304** MUST: Where the detailed concept-bundle convention applies, use its lowercase `docs/decisions/dec-NNN-topic-slug.md` path and concept metadata (`type: Decision`, `title`, `description`, `tags`, `timestamp`) in the record. Validate those fields and general link health under that bundle's applicable checks separately from body presence. Do not add these keys to the neutral FORMAT card.

Complete detailed-profile authoring form; all slots are filled from actual evidence before binding use. This fence is form data, not an accepted decision:

```markdown
---
type: Decision
title: <actual choice in one line>
description: <the consequential axis and affected scope>
tags: [<applicable concepts>]
timestamp: <actual recording timestamp in the bundle convention>
---
# Status
<Fixed (actual date). | Open. Trigger: actual observation. | Superseded by [actual successor](actual-successor.md). | Rejected — actual reason.>

# Context
<Actual situation, constraints, evidence links, affected scope and criterion that make the fork understandable without the verdict. Actual owner/consent provenance belongs here or in the project's declared metadata; missing approval remains missing.>

# Decision
<Current collapsed choice in present tense, with the owning axis and its boundary. An Open record instead states what remains uncollapsed and links its owning register item. A superseded record retains its original verdict and status successor link.>

# Alternatives
**<Genuine option>** — <concrete reason it lost against the stated criterion>.
**<Another genuine option>** — <concrete reason it lost>.
<For a genuinely forced collapse, replace these entries with one bold-led statement explaining the single viable path. For unrecoverable pre-protocol history only, replace this section with the exact historical comment.>

# Consequences
Costs: <what the choice costs, constrains or risks, and affected documents>.
Benefits: <what it buys against the criterion, and affected documents>.
```

<!-- anchor: process.decisions.held-axes -->

## Held axes and PM open questions

- **DECISION-401** MUST: Where the detailed held-axis profile applies, keep deliberately uncollapsed axes in one owning numbered register, conventionally `docs/decisions/dec-open-*.md`. Each item names its axis, why held and the observation trigger ending the hold. A corresponding Open record links that collection/item rather than becoming another scattered owner. The register ends with a level-one Rule section stating what work is forbidden while held, normally code artifacts on that axis; specification and roadmap scoping may continue. Independently authorized work on other axes continues. A date or a feeling alone is not an observation trigger.
- **DECISION-402** MUST: Where the PM open-question profile applies, retain question, stakes/reversibility, options, evidence, dependencies and decider in `OPEN_QUESTIONS.md`, and link the eventual binding decision at resolution. Do not silently impose the detailed register's trigger/no-code fields on this separate profile or turn all unresolved questions into a project-wide stop.

Complete held-axis form, shown as form data:

```markdown
# Open axes

1. **<axis>**
   Why held: <specific unresolved evidence or material fork>.
   Trigger: <observable result that permits reconsideration, with where it will be checked>.
   Options: <actual candidates and criteria>.
   Owner/scope: <actual decision owner and affected work>.
   Related record: [<Open record if one exists>](<record.md>#status).

# Rule
While item 1 remains open, <prohibited work on its axis, normally including code artifacts> is forbidden. Specification and roadmap scoping on that axis are permitted within the grant; independent authorized work on other axes continues. Observe the named trigger and obtain any required authority before collapsing; calendar passage alone does not release the hold.
```

Complete PM-compatible open-question form, shown as form data:

```markdown
---
type: OpenQuestions
title: <project> — open questions
generated: { by: <actual actor>, at: <actual UTC recording timestamp> }
status: active
---
# Open questions
A question leaves the open population when a decision answers it; its retained entry points to that record.

## Q<n>. <actual question>
- Stakes and reversibility: <why it matters and cost of changing later>.
- Options: <genuine seed options>.
- Evidence: <actual source links; explicit unknowns>.
- Decider: <actual owner>. Depends on: <actual questions/dependencies or none>.
- Resolution: <unresolved, or link to actual binding DEC after it exists>.
```

<!-- anchor: process.decisions.pm-record -->

## PM accepted records, amendments and numbers

- **DECISION-501** MUST: In the PM decision profile, retain `type: Decision`, `id: DEC-NNN`, `status: accepted | superseded`, `generated`, and `decided: { by, at, via }` with the actual actor/date/channel. Record question, held options and consequences, choice, options not taken with reasons, and affected files/rules/route. A non-obvious superposition records genuinely different options scored against stated criteria and collapses with the applicable owner's consent; those scores are judgments, not measured probabilities. A conversational decision retains the actual words and date. Confirm genuinely ambiguous consent through the available supported channel; reuse already clear matching consent.
- **DECISION-502** MUST: In the PM accepted-body profile, never edit the body after acceptance; only `status`, `superseded_by` and `amended_by` may change. A whole replacement creates a new decision with `supersedes`, marks the old `superseded` with `superseded_by`, and resolves both directions. A partial change creates a new amendment; the old stays `accepted`, its unchanged body retains the original scope, and `amended_by` names the later record/effect as one string or a list of `DEC-NNN: effect` strings. The amendment identifies the old record and exact changed part; it does not silently replace the whole verdict.
- **DECISION-503** MUST: Where the PM numbering/reservation convention applies, the parent session running the batch allocates numbers in order from the highest recorded or reserved number; tasks do not independently take numbers on their branches. A task needing a decision records `**Reserves:** DEC-NNN` in its task entry when it starts. No number is recorded twice; decision references in the always-read set and open-question register resolve to a record or that declared task reservation. A reservation is not a decision or consent.

Complete PM-compatible form, shown as form data:

```markdown
---
type: Decision
id: DEC-<NNN>
title: <actual decision>
generated: { by: <actual actor>, at: <actual UTC timestamp> }
status: accepted
decided: { by: <actual decider>, at: <actual decision date>, via: <actual channel/reference or quoted words with date> }
---
# DEC-<NNN> — <actual decision>

**Question.** <What must be decided and why it matters.>
**Options held.** <Genuine candidates and consequences; scoring table when superposition is used.>

| Option | <criterion> | <criterion> | Judgment/reason |
|---|---|---|---|
| <actual option> | <score> | <score> | <why> |
| <actual alternative> | <score> | <score> | <why> |

**Decision.** <Actual choice; exact owner quote/date when given in conversation.>
**Options not taken, and why.** <Each losing candidate and specific loss.>
**What it changes.** <Affected files, rules and roadmap steps; costs and benefits.>
```

Lifecycle metadata form data (each line is used only on the named record after the corresponding real decision):

```yaml
# Whole replacement: old record
status: superseded
superseded_by: DEC-<new>
# Whole replacement: new record (its complete independent body explains the new choice)
supersedes: DEC-<old>
# Partial amendment: old record keeps status accepted and its entire body unchanged
amended_by: "DEC-<amendment>: <specific partial effect>"
# Multiple partial amendments, when present
amended_by:
  - "DEC-<first>: <first effect>"
  - "DEC-<second>: <second effect>"
```

<!-- anchor: process.decisions.index-and-roles -->

## Discoverability and existing software duties

- **DECISION-601** MUST: Where the detailed bundle index applies, reconcile it in both directions: every actual record/register is listed, and every listed record/register exists at the named target. Check general paths/anchors separately; basename agreement alone is not link health or actual succession proof.
- **DECISION-602** MUST: Inside an already authorized software flow using the detailed profile, Architect records a consequential collapse before handing the plan to Code, and the plan links the owning record; chat-only collapse is not a durable record. Debug invalidating a recorded verdict creates a linked successor or held register axis with observation trigger. A local `BUG_FIX_CONTEXT` does not replace the systemic record. QA never treats decision text as test evidence or a substitute for a required runtime probe. These are duties within existing roles, not role assignments to document/research/product/operations authors or a new execution gate.

The [specification process](specification.md), [Architect](../roles/architect.md), [Debug](../roles/debugger.md) and [QA](../roles/qa.md) retain their governing contracts. Applicable autonomous design records cite sourced or synthesized criteria, substantial distinct hypotheses, collapse reasons and promised verification identifiers under the existing plan convention; interactive material owner forks use actual owner authority. The per-run rationale and durable record serve different lifetimes. Broader prompting policy stays in its own subject.

<!-- anchor: process.decisions.worked-examples -->

## Complete fictional illustrations

The following collection is authored fictional data about a training workshop's attendance-export contract. Its paths, people, dates, criteria, observations, grants and outcomes are invented illustration, never actual project consent, implementation or runtime evidence. Each named fence is a separate fictional file; links inside the fences describe that fictional collection, not repository files. This collection illustrates the detailed profile, not the PM lexical schema.

Fictional `docs/decisions/dec-001-export-format.md` (original body retained, current status links its replacement):

```markdown
---
type: Decision
title: Delimited attendance export
description: Original attendance-exchange contract
tags: [attendance, export]
timestamp: 2026-01-10T12:00:00Z
---
# Status
Superseded by [DEC-002](dec-002-structured-export.md).

# Context
The fictional workshop hands one attendance list to one spreadsheet operator. The declared criterion is direct opening in that operator's spreadsheet with no setup. The fictional owner Mira says “Use the delimited file for this workshop” on 2026-01-10; this sentence is illustrative consent, not a real authorization.

# Decision
The attendance exchange uses a delimited UTF-8 file with one row per attendee.

# Alternatives
**Structured object export** — the operator must install an importer before opening the first list, which fails the zero-setup criterion for this workshop.
**Manual retyping** — a second transcription of the same list creates a mismatch point at every attendee name and does not meet the single-source criterion.

# Consequences
Costs: consumers must preserve the chosen delimiter/quoting convention; nested sessions require flattening, and export instructions document that limitation.
Benefits: the operator opens the list directly, and a single exchange contract replaces ad hoc transcription. The current replacement is linked in Status; this original verdict is preserved as history.
```

Fictional `docs/decisions/dec-002-structured-export.md`:

```markdown
---
type: Decision
title: Structured attendance export
description: Replacement exchange contract for nested workshop sessions
tags: [attendance, export, sessions]
timestamp: 2026-02-03T12:00:00Z
---
# Status
Fixed (2026-02-03).

# Context
In this fictional scenario, sessions now have multiple attendance events per person and the recipient already has an object importer. The declared criterion is preserving each event's session identity without duplicate person fields. The fictional owner Mira says “Use the structured contract for the session exchange” on 2026-02-03. It replaces [DEC-001](dec-001-export-format.md), whose status points back here; no real deployment is asserted.

# Decision
The session exchange uses structured objects containing a person and that person's session events. This record owns the exchange-format axis and supersedes DEC-001 in whole.

# Alternatives
**Keep the flat delimited contract** — repeating person data on each event row creates multiple potentially disagreeing person copies, contrary to the declared identity criterion.
**Separate person and event files** — the recipient must coordinate two file deliveries and handle an event file whose person file has not arrived, introducing a second delivery failure mode.

# Consequences
Costs: the importer is now a contract dependency; spreadsheet-only recipients need an explicit adapter, documented in exchange instructions.
Benefits: session identity and person identity remain distinct without repeated person fields. The contract documentation points to this current record and retains DEC-001's reciprocal history link.
```

Fictional `docs/decisions/dec-003-delivery-mode.md`:

```markdown
---
type: Decision
title: Delivery mode remains held
description: Open scheduled-versus-on-demand delivery axis
tags: [attendance, delivery]
timestamp: 2026-02-04T12:00:00Z
---
# Status
Open. Trigger: the first representative replay that records recipient availability and produces comparable missed-delivery results for both modes.

# Context
The fictional recipient's availability is unknown. Scheduled delivery and requested delivery both fit the structured format, but choosing now would assume an availability pattern. The owning collection is [open axis 1](dec-open-workshop.md#open-axes); this record does not own a second independent hold.

# Decision
The delivery-mode axis remains uncollapsed pending the register's observation and applicable owner decision. The already fixed exchange format is unaffected.

# Alternatives
**Collapse to scheduled delivery now** — it assumes the recipient can receive at the chosen schedule without a representative observation.
**Collapse to on-demand delivery now** — it assumes request latency is tolerable before the replay compares it with missed scheduled delivery.

# Consequences
Costs: delivery implementation on this axis is held, so the next delivery milestone cannot claim completion.
Benefits: the replay can compare the two real candidates before commitment; independent authorized contract documentation continues.
```

Fictional `docs/decisions/dec-004-dual-export.md`:

```markdown
---
type: Decision
title: Reject permanent dual export
description: Rejected duplicate exchange-contract proposal
tags: [attendance, export]
timestamp: 2026-02-04T13:00:00Z
---
# Status
Rejected — permanent dual export creates two contracts that recipients can update inconsistently.

# Context
The fictional workshop considers keeping both old and new exports indefinitely to reduce migration work. The criterion is one authoritative attendance-exchange contract. [DEC-002](dec-002-structured-export.md) owns that accepted format axis; this rejected proposal is rationale against a tempting duplicate, not a competing current verdict.

# Decision
The workshop declines permanent dual export; the structured contract remains authoritative in this fictional scenario.

# Alternatives
**Permanent flat and structured exports** — recipients may apply changes to one representation while continuing to distribute the other, violating the single-contract criterion.
**Retain the flat contract alone** — nested session events still require duplicated person data, the concrete loss already recorded in DEC-002.

# Consequences
Costs: migration instructions must explain the structured importer, rather than preserving every old consumer unchanged.
Benefits: one authoritative contract removes the two-output disagreement mode. This rejected rationale is retained while that proposal remains plausible; protected project history cannot be deleted merely by citing this illustration.
```

Fictional `docs/decisions/dec-open-workshop.md`:

```markdown
# Open axes

1. **Delivery mode: scheduled versus on demand**
   Why held: recipient availability is unknown, so neither mode can be chosen against the missed-delivery/latency criteria yet.
   Trigger: the first representative replay recording recipient availability and comparable missed-delivery results for both modes, reviewed with request latency. Calendar arrival alone is insufficient.
   Options: scheduled delivery, or recipient-requested delivery.
   Owner/scope: fictional owner Mira; delivery-mode implementation only.
   Related record: [DEC-003](dec-003-delivery-mode.md).

# Rule
While axis 1 is open, delivery-mode implementation, normally including code artifacts choosing either mode, is forbidden. Specification and roadmap scoping for the comparison are permitted. Independent authorized work on the fixed exchange contract continues. The observed replay does not itself supply owner consent; any required collapse decision is recorded before releasing dependent work.
```

Fictional `docs/decisions/index.md`:

```markdown
# Workshop decisions
- [DEC-001: original delimited exchange, superseded](dec-001-export-format.md)
- [DEC-002: current structured exchange, fixed](dec-002-structured-export.md)
- [DEC-003: delivery mode, open](dec-003-delivery-mode.md)
- [DEC-004: permanent dual export, rejected](dec-004-dual-export.md)
- [Owning open-axis register](dec-open-workshop.md)

Each of the five record/register targets listed above exists in this fictional collection, and all five actual illustrated files are listed. DEC-001 and DEC-002 link in both succession directions. The index statement describes illustrative consistency only, not an executed check.
```

A fictional PM partial amendment would leave the accepted DEC-011 body untouched, keep `status: accepted`, and add only `amended_by: "DEC-012: delivery window changes to recipient local time"`. The complete new DEC-012 records its actual question/options/reasons/owner provenance and explicitly identifies that part of DEC-011; all other DEC-011 duties remain binding. A later whole replacement DEC-013 instead places `supersedes: DEC-011` on itself and `status: superseded` plus `superseded_by: DEC-013` on DEC-011. These metadata examples are not real records or consent and cannot be used as proof of a project change.

<!-- anchor: process.decisions.verification-limits -->

## Verification, limits and negative judgments

- **DECISION-701** MUST: Verify applicable record/register/index structure and actual authority/meaning separately. Presence checks do not prove genuine options or losing reasons, a dated binding choice, an observed trigger, a real successor, applicable historical escape, one owning register, prohibited work, or receipt of consent. Review those against actual source/evidence and the chosen project profile; QA's required delivery evidence remains independent.
- **DECISION-702** MUST: Report the actual limits of a declared decision checker. The detailed source checker recognizes lowercase decision/register filenames, required heading/order, status prefixes, a trigger word, any Markdown successor link, a minimal reason, a named alternative or exact historical escape, Rule heading, per-numbered-item trigger and basename index consistency. It does not enforce the date's truth, observation quality, successor existence, alternative honesty/loss reasons, historical applicability, singleton/nonempty register, final Rule position, no-code meaning or general frontmatter/link health. The PM source checker checks accepted/superseded status, decided presence and superseded target resolution, but its implementation does not validate `amended_by` resolution despite that duty in its prose checklist. Do not claim that omitted check passed or transplant either checker as a new engine.

Useful negative judgments are profile-specific: “trigger: next Friday” alone fails the detailed observation duty even if a checker sees the word trigger; “superseded” with an unrelated Markdown link fails real succession; a fictitious option with a bold heading fails truthful Alternatives; the historical escape on a new decision fails applicability; two held collections or a Rule that permits choosing code on the held axis fail the detailed register contract. A PM open question with no observation field is not thereby invalid. Editing accepted PM body text to refresh a path fails that profile even where the detailed facts-refresh convention allows the same refresh. An index listing an absent file or omitting a present register fails its respective direction. A resolved amendment still needs actual authority and an unchanged old body.

[Decision lint boundaries](../checks/lints.md) describe the checking home. Structural parsing, manual source/authority review and any required runtime probe have different evidence populations; none substitutes for another. These complete forms and fictional examples certify no runtime adoption, executable gate, historical source transfer or whole-methodology completion.
