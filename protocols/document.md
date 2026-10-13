---
id: protocols.document
title: Document protocol
status: draft
---

# Document protocol

Structured technical documents expose intent, an outline and complete artifact contracts so a reader can inspect one section without losing its relationships. This authoring protocol supports requirements, specifications and technical plans. It does not assign a software role or replace the project's declared homes for its current records.

<!-- anchor: protocols.document.application -->

## Application and authority

- **DP-101** MUST: Apply this protocol when generating structured technical project documents, including requirements and specifications. Read the actual brief, instructions and applicable document conventions before authoring; preserve settled decisions and existing authorization.
- **DP-102** MUST: Keep a repository's neutral card/anchors/norms governed by [FORMAT](../FORMAT.md), and actual project metadata/homes governed by [document conventions](../documents/conventions.md). The paired content markers below do not replace FORMAT anchors. Existing PM forms need no automatic marker retrofit.
- **DP-103** MUST: State document PURPOSE, SCOPE and KEYWORDS at the beginning of the content. PURPOSE names the intended outcome; SCOPE bounds coverage; KEYWORDS name the actual domain and concepts. Keep measured evidence separate from intended behavior.

<!-- anchor: protocols.document.outline -->

## Outline before detail

- **DP-201** MUST: Generate the entire `$DOCUMENT_PLAN` skeleton before expanding its sections. Enclose it with `$START_DOCUMENT_PLAN` and `$END_DOCUMENT_PLAN`; enumerate planned artifacts as `TYPE [Description] => [Artifact_ID]`, grouped by sections such as goals and use cases. Choose stable artifact IDs and use those same IDs in bodies and links.
- **DP-202** MUST: Wrap the document, each section, each artifact, its contract, substantive body and links in matched `$START_NAME` / `$END_NAME` boundaries, nested in that order. Close an inner boundary before its containing boundary. Names identify semantic context; a heading alone does not provide its closure.
- **DP-203** MUST: Reconcile the outline with the completed body: every planned artifact has a complete body; every authored artifact is in the outline; marker names and IDs agree. An outline of promised content or a read receipt is not a ready document.

The skeleton makes omissions visible before prose expansion. Paired boundaries provide local context for reading and editing. They are navigation conventions, not a claim that every consumer mechanically validates ordinary-language completeness.

<!-- anchor: protocols.document.artifacts -->

## Artifacts and contracts

- **DP-301** MUST: Give every artifact explicit TYPE and KEYWORDS. TYPE is one of GOAL, KEY_RESULT, USE_CASE, PRINCIPLE, DECISION, TOOL, DATA_FORMAT or NFR; choose its meaning from the actual subject rather than using a decorative label.
- **DP-302** MUST: Include a `$START_CONTRACT` / `$END_CONTRACT` block with PURPOSE (what outcome this artifact serves), DESCRIPTION (its detailed meaning), RATIONALE (why it is needed or chosen) and ACCEPTANCE_CRITERIA (how correctness can be verified). A USE_CASE description states Actor–Action–Goal.
- **DP-303** MUST: Include the artifact's actual detail in a `$START_BODY` / `$END_BODY` block. Contracts and outlines do not substitute for required rules, data shape, scenarios, decisions or verification conditions.
- **DP-304** MUST: Include a `$START_LINKS` / `$END_LINKS` block. IMPLEMENTS points from the artifact to the goal or rule it realizes; IMPACTS points to an artifact whose behavior or outcome it affects; REQUIRES points to a prerequisite. Use real declared artifact IDs, local or through an explicit document reference. For a relation with no applicable target, state `(none)` rather than inventing an ID.
- **DP-305** MUST: Check each link's target and direction against its actual meaning. Conceptual artifact links do not mandate an XML graph, a new ID registry or an expanded decision lifecycle. [Graph](graph.md) and [development plan](dev-plan.md) retain their separate contracts.

| Type | Content the artifact identifies |
|---|---|
| GOAL | Intended outcome |
| KEY_RESULT | Observable success measure |
| USE_CASE | Actor's action toward a goal |
| PRINCIPLE | Constraint or guiding rule |
| DECISION | Chosen option and its rationale |
| TOOL | Means used to perform work |
| DATA_FORMAT | Data structure and interpretation |
| NFR | Nonfunctional quality requirement |

<!-- anchor: protocols.document.form -->

## Full form

The form below is illustrative syntax. Replace its bracketed fields with substantive content and repeat complete section/artifact blocks for the entire agreed outline. Both example artifacts are declared, contracted and closed; other types use the same structure.

```markdown
$START_DOCUMENT
PURPOSE: [Outcome and intended reader]
SCOPE: [Included subjects and limits]
KEYWORDS: [Domain, concepts]
$START_DOCUMENT_PLAN
$DOCUMENT_PLAN
SECTION_GOALS:
GOAL [Intended outcome] => GOAL_MAIN
SECTION_USE_CASES:
USE_CASE [Actor action toward outcome] => CASE_MAIN
$END_DOCUMENT_PLAN
$START_SECTION_GOALS
$START_ARTIFACT_GOAL_MAIN
TYPE: GOAL
KEYWORDS: [Outcome domain]
$START_CONTRACT
$CONTRACT
PURPOSE: [What this goal enables]
DESCRIPTION: [Detailed outcome]
RATIONALE: [Why it matters]
ACCEPTANCE_CRITERIA: [Observable check and pass condition]
$END_CONTRACT
$START_BODY
[Complete goal rules, bounds and evidence distinction]
$END_BODY
$START_LINKS
IMPLEMENTS: (none)
IMPACTS: CASE_MAIN
REQUIRES: (none)
$END_LINKS
$END_ARTIFACT_GOAL_MAIN
$END_SECTION_GOALS
$START_SECTION_USE_CASES
$START_ARTIFACT_CASE_MAIN
TYPE: USE_CASE
KEYWORDS: [Actor, action, subject]
$START_CONTRACT
$CONTRACT
PURPOSE: [Value delivered by the scenario]
DESCRIPTION: [Actor] → [Action] → [Goal]
RATIONALE: [Why this scenario is required]
ACCEPTANCE_CRITERIA: [Inputs, observed outputs and failure condition]
$END_CONTRACT
$START_BODY
[Complete normal path, defaults and relevant error paths]
$END_BODY
$START_LINKS
IMPLEMENTS: GOAL_MAIN
IMPACTS: (none)
REQUIRES: GOAL_MAIN
$END_LINKS
$END_ARTIFACT_CASE_MAIN
$END_SECTION_USE_CASES
$END_DOCUMENT
```

<!-- anchor: protocols.document.example -->

## Complete worked example

This fictional local reading-list contract demonstrates ready content and typed relationships. It is an illustration, not measured product evidence or authority to build the product.

```markdown
$START_READING_LIST
PURPOSE: Let a reader keep and inspect a small local list of book titles.
SCOPE: Add and list titles in one local session; no accounts or network.
KEYWORDS: books, local list, validation
$START_DOCUMENT_PLAN
$DOCUMENT_PLAN
SECTION_GOALS:
GOAL Keep a usable reading list => GOAL_LIST
SECTION_FORMATS:
DATA_FORMAT Represent ordered titles => FORMAT_TITLES
SECTION_USE_CASES:
USE_CASE Add a title and inspect it => CASE_ADD
$END_DOCUMENT_PLAN
$START_SECTION_GOALS
$START_ARTIFACT_GOAL_LIST
TYPE: GOAL
KEYWORDS: reading, first value
$START_CONTRACT
$CONTRACT
PURPOSE: Preserve the reader's chosen titles during one session.
DESCRIPTION: A reader adds a title and later sees that title in insertion order.
RATIONALE: The first useful outcome is a visible list, without account setup.
ACCEPTANCE_CRITERIA: After adding Dune then Solaris, listing returns those two titles in that order.
$END_CONTRACT
$START_BODY
The session begins empty. Titles are added only after validation. Listing is read-only.
Ending the session discards the list; persistence is deliberately outside this contract.
$END_BODY
$START_LINKS
IMPLEMENTS: (none)
IMPACTS: CASE_ADD
REQUIRES: FORMAT_TITLES
$END_LINKS
$END_ARTIFACT_GOAL_LIST
$END_SECTION_GOALS
$START_SECTION_FORMATS
$START_ARTIFACT_FORMAT_TITLES
TYPE: DATA_FORMAT
KEYWORDS: ordered titles, whitespace, validation
$START_CONTRACT
$CONTRACT
PURPOSE: Give additions and listings an unambiguous common representation.
DESCRIPTION: The session holds an ordered sequence of nonempty text titles.
RATIONALE: A single representation avoids different rules in writing and reading.
ACCEPTANCE_CRITERIA: Leading/trailing spaces are removed; an empty trimmed title changes nothing.
$END_CONTRACT
$START_BODY
Each element is a string. Trim outer whitespace before appending; preserve internal spaces.
Duplicates are allowed and stay in insertion order. A rejected title returns the message
"title required" and leaves the sequence unchanged. The empty list displays "No books".
$END_BODY
$START_LINKS
IMPLEMENTS: GOAL_LIST
IMPACTS: CASE_ADD
REQUIRES: (none)
$END_LINKS
$END_ARTIFACT_FORMAT_TITLES
$END_SECTION_FORMATS
$START_SECTION_USE_CASES
$START_ARTIFACT_CASE_ADD
TYPE: USE_CASE
KEYWORDS: reader, add title, list titles
$START_CONTRACT
$CONTRACT
PURPOSE: Turn the reader's selection into an inspectable entry.
DESCRIPTION: Reader → add a title and request the list → see the selected title.
RATIONALE: This is the smallest scenario that demonstrates the goal end to end.
ACCEPTANCE_CRITERIA: Adding " Dune " then listing displays "Dune"; adding spaces returns "title required" with the previous list intact.
$END_CONTRACT
$START_BODY
Start a fresh session and list: observe "No books". Add " Dune ": observe success.
List again: observe the single title "Dune". Add spaces: observe "title required".
List once more: observe the same single title. Add Solaris: list Dune then Solaris.
$END_BODY
$START_LINKS
IMPLEMENTS: GOAL_LIST
IMPACTS: FORMAT_TITLES
REQUIRES: FORMAT_TITLES
$END_LINKS
$END_ARTIFACT_CASE_ADD
$END_SECTION_USE_CASES
$END_READING_LIST
```

<!-- anchor: protocols.document.verification -->

## Readiness and limits

- **DP-401** MUST: Before treating an authored document as ready, inspect its actual complete outline, paired closures, every type/keyword/contract/body and all ID relationships. Verify that its observable checks cover the agreed content. Syntax conformance alone does not prove its meaning or fulfillment.
- **DP-402** MUST: Record omissions, unavailable evidence and interpretations through the applicable [specification process](../process/specification.md) and role contracts. Do not silently narrow requirements to make a form appear complete.

The modern and legacy document families in lesson2, lesson3 and the shared development plugin agree on the outline/contract mechanism; the PM harness and native PM adaptation preserve it. Prompting methodology also uses semantic boundaries, but its prompt-specific quotas and model claims are outside this document contract. General decision lifecycle and full generic graph detail remain separate residual subjects; this body completes technical document authoring only.
