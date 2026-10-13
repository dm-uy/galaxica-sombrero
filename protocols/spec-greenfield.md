---
id: protocols.spec-greenfield
title: Greenfield specification
status: draft
---

# Greenfield specification

A first specification fixes a useful first outcome and the boundary of the agreed MVP before implementation. It starts from actual inputs, including an existing brief, rather than treating a missing roadmap as an empty product.

<!-- anchor: protocols.spec-greenfield.context -->

## Classification and first value

- **SG-101** MUST: Use this profile for genuinely new work with no existing implementation to preserve. Inspect source, tests, instructions, README, briefs and durable records; existing code makes the affected work brownfield or mixed even when PM documents are absent. Route mixed work by its actual preservation obligations through [specification](../process/specification.md).
- **SG-102** MUST: Read the complete brief and settled decisions before choosing direction. Use read-only Input RECON covering existing decisions, any legacy surface and load-bearing external facts; record evidence and unknowns. Brainstorm only actual open choices, not decisions already approved.
- **SG-103** MUST: State product, audience, first value (one falsifiable user-visible outcome), non-negotiables, agreed stack, MVP boundary and probe route before Code. Use [bootstrap](../process/bootstrap.md) and the project's current record conventions for durable state; this form does not authorize seeding or resetting an existing project.

<!-- anchor: protocols.spec-greenfield.profile -->

## Architecture authority profiles

- **SG-201** MUST: Declare the architecture profile selected by actual project/owner context and its provenance. In **target-projection**, provide the already selected or required target component graph and connections/seams, distinguishing fixed decisions from designable details. In **constraint-led**, state fixed outcomes, stack and boundary seams while leaving the implementation graph, file layout and classes to Architect; do not invent them for form completion.
- **SG-202** MUST: Preserve Architect ownership of technical design in both profiles. A new target graph is not a brownfield invariant subgraph. Compare real simultaneously binding requirements; if they demand incompatible architecture authority, use the existing SPEC_BLOCKED path rather than silently choosing a donor or adding a gate.

The PM harness/native PM adaptation first-spec family provides target projections after direction selection. The standalone development distribution example deliberately supplies constraints without an implementation graph. These are contextual profiles, not a blanket ranking of source strength or recency.

<!-- anchor: protocols.spec-greenfield.content -->

## Complete first specification

- **SG-301** MUST: Follow the [document contract](document.md), stable metadata/path and shared sweeps in [specification](../process/specification.md). Include the top **Done when** and **Stop and ask when** lists and all fields of the full form below. The lists summarize the finish line and escalation edges; they replace neither acceptance criteria nor established gates.
- **SG-302** MUST: Describe What we build observably: commands/endpoints or interactions, output/data shape, defaults, validation/errors, persistence and relevant lifecycle behavior. Describe Stack by language, framework, storage, transport and dependencies, giving a reason and the required verified identifiers/version constraints for each. Explicitly state inapplicable categories and forbidden additions; do not introduce speculative dependencies.
- **SG-303** MUST: Make BR-1 the falsifiable MVP success rule. Declare subsequent business requirements independently, then meaningful behavior/test/scope/delivery ACs with unique IDs, exact operations, evidence and pass conditions. Do not manufacture a regression population or arbitrary test quota for nonexistent code.
- **SG-304** MUST: Fill Always do / Ask first / Never do from actual task rules and granted authority. Define included MVP work, explicit exclusions, deferred work with return conditions and dependency limits. Where actual existing instructions or artifacts need protection, identify them and the intended plan/test/doc homes; greenfield does not imply unrestricted file edits.
- **SG-305** MUST: If adding or modifying an LLM call, include prompt-injection requirements from the actual target catalog or inline defenses when none is defined: adversarial input is data, separate instructions from data, constrain decision outputs and sanitize file content when applicable; an LLM output alone cannot relax a safety decision. Include a discriminating adversarial AC that cannot change the protected verdict/flag. An inapplicable call is stated as such.
- **SG-306** MUST: Define an authorized Live Probe with runnable command, target environment, actual destination/sink, prerequisite, scenario and observable pass/fail conditions. Identify delivery mechanism/configuration where output crosses a boundary; capture fixtures alone prove invocation. Keep missing access visible, and never infer permission for messages, money or external writes from a probe proposal. Pure local logic uses its actual local outcome without inventing a remote service.
- **SG-307** MUST: Record real risks and limits, including applicable secrets, cost/rate limits, state format and missing probe access. A deferred check names exact command/prerequisite/reason/criterion and covers no criterion until executed. Preserve every deficiency and interpretation through the shared process to Code.

<!-- anchor: protocols.spec-greenfield.form -->

## Full form

This is a complete reusable content form; project metadata is supplied using its declared convention, separate from this repository's neutral card. Fill every field, choose one architecture profile and state justified N/A conditions.

```markdown
# First specification: [Product and MVP]
[Stable record metadata: status, Input RECON, approval reference in project convention]
$START_SPECIFICATION
PURPOSE: [Audience and first outcome]
SCOPE: [Agreed MVP]
KEYWORDS: [Product domain, capability]
$START_DOCUMENT_PLAN
$DOCUMENT_PLAN
GOAL [First useful outcome and complete MVP contract] => GOAL_MVP
$END_DOCUMENT_PLAN
$START_SECTION_MVP
$START_ARTIFACT_GOAL_MVP
TYPE: GOAL
KEYWORDS: [Audience, first value, MVP]
$START_CONTRACT
$CONTRACT
PURPOSE: [Value to the audience]
DESCRIPTION: [Observable complete outcome]
RATIONALE: [Why this is the first slice]
ACCEPTANCE_CRITERIA: [AC identifiers below and how they close this artifact]
$END_CONTRACT
$START_BODY
**Done when:**
- [Falsifiable delivered outcome, tests/probe and scope checks]
**Stop and ask when:**
- [Task-specific unresolved authority/intent or boundary decision]
## Context
[Actual classification, complete brief/decision references, Input RECON evidence/limits,
audience, first value and non-negotiables]
## What we build
[Interactions, inputs/outputs/data shape, defaults, validation/errors, persistence/lifecycle]
## Stack
[Language/framework/storage/transport/dependencies: identifiers and required versions,
justification, verification evidence or required unavailable lookup; N/A where genuine]
## Architecture
[Profile: target-projection or constraint-led; selecting authority/evidence]
[Target-projection: chosen components/graph/seams/provenance and fixed/designable choices]
[Constraint-led: fixed outcomes/stack/seams; Architect owns graph/layout/classes]
## Business Requirements
BR-1: [Falsifiable MVP success]
BR-2: [Other declarative outcome]
[LLM conditional: catalog/path or complete inline defenses; otherwise N/A reason]
## Boundaries
Always do: [Actual unconditional task rules]
Ask first: [Actual actions requiring owner authority, accounting for existing grants]
Never do: [Actual prohibited actions]
## MVP boundary
Included: [Complete agreed slice and intended implementation/test/doc/plan homes]
Excluded: [Explicit non-MVP capabilities and forbidden dependencies]
Deferred: [Work and concrete return condition]
Protected existing records/instructions: [Actual constraints or justified none]
## Acceptance Criteria
AC-MVP-1: [Behavior check, method, observable threshold/result]
AC-MVP-2: [Meaningful positive/error tests and exact command]
AC-MVP-3: [MVP/scope/dependency/secret verification]
AC-MVP-4: [Real delivery/probe command and pass conditions]
[Conditional discriminating PI AC; otherwise N/A]
[Deferred check: exact command, prerequisite, reason and criterion; fulfills none yet]
## Live Probe
[Environment, authorized destination, mechanism/configuration, exact runnable command,
prerequisite, scenario, pass/fail conditions, access limits and evidence receipt location]
## Risk Notes
[Actual cost/rate/secret/state/environment risks and mitigation/limits]
## Deficiencies / interpretations
[Exact blocks and chosen interpretation for Code; explicit none if none]
$END_BODY
$START_LINKS
IMPLEMENTS: (none)
IMPACTS: (none)
REQUIRES: (none)
$END_LINKS
$END_ARTIFACT_GOAL_MVP
$END_SECTION_MVP
$END_SPECIFICATION
```

<!-- anchor: protocols.spec-greenfield.example -->

## Complete worked example: local checklist

All domain decisions, paths and measurements in this example are fictional illustrative inputs. The command is a proposed deliverable for that example; no product implementation or probe execution is claimed. The context selects constraint-led architecture; a target-projection context would instead supply its selected graph and authority as required above.

```markdown
# First specification: a local checklist
Record: specs/first-checklist.md; status: approved in this fictional example.
Input RECON: notes/checklist-input.md. Approval: owner selected the local CLI MVP and
constraint-led profile in the illustrative brief; result acceptance remains separate.
$START_CHECKLIST_SPEC
PURPOSE: Let one person persist a short checklist and inspect it after restarting.
SCOPE: Local add/list operations on a user-selected JSON file.
KEYWORDS: checklist, CLI, local persistence
$START_DOCUMENT_PLAN
$DOCUMENT_PLAN
GOAL Deliver a persistent local checklist => GOAL_CHECKLIST
USE_CASE Add a task and inspect it after restart => CASE_RESTART
$END_DOCUMENT_PLAN
$START_SECTION_MVP
$START_ARTIFACT_GOAL_CHECKLIST
TYPE: GOAL
KEYWORDS: first value, checklist, persistence
$START_CONTRACT
$CONTRACT
PURPOSE: Replace temporary notes with an inspectable local checklist.
DESCRIPTION: A person adds one task and sees it in a fresh process reading the same file.
RATIONALE: Persistence is the minimum value; accounts and a GUI are unnecessary for this slice.
ACCEPTANCE_CRITERIA: AC-CL-1 through AC-CL-5 below cover behavior, tests, scope and live delivery.
$END_CONTRACT
$START_BODY
**Done when:**
- A fresh process lists the task created by the first process; rejection cases leave bytes intact.
- Declared tests and local probe pass, with only the agreed MVP implemented.
**Stop and ask when:**
- A requirement needs multi-user writes, network access or a dependency beyond the selected stack.
- Missing evidence or incompatible owner intent prevents safe validation; use existing refusal semantics.
## Context
Input RECON reads the illustrative brief and empty implementation/test inventory. The directory
contains only that brief and current project records; no running code needs preservation.
Audience: one local user. First value: add "Buy tea", restart, list it once. The brief fixes local
storage, no accounts and no network. Its inventory is illustrative, not a current runtime receipt.
## What we build
`python3 -m checklist --store PATH add TEXT` trims outer whitespace, appends a nonempty task,
prints `added` plus newline and exits 0. Whitespace-only text exits 2, prints `task required`
to stderr and changes no file. `list` prints task text one line each in insertion order; an absent
store prints `No tasks` and exits 0 without creating it. Duplicates are allowed.
Store shape: UTF-8 JSON object `{"tasks": ["Buy tea"]}`; every task is a nonempty string.
Malformed JSON or an incompatible shape exits 2 with `invalid store`, preserving existing bytes.
Writes replace the file atomically after validation. Concurrent writers are outside the MVP.
## Stack
Language: Python 3.12.10, fixed by the illustrative brief for a repeatable local runtime; use only
its standard library to avoid package/network setup. Before delegation, inspect the actual selected
interpreter with `python3 --version` and compare it to this requirement; an unavailable/mismatched
required runtime is BLOCKED. This fictional version selection is not a current installed-version receipt.
Framework: none, the standard argument parser is sufficient. Storage: UTF-8 JSON in a local file,
readable by the user. Transport: process stdout/stderr and that file. Dependencies: none beyond
that interpreter; no package/API/image lookup is required. Additional packages are excluded.
## Architecture
Profile: constraint-led, selected by the illustrative brief. Fixed seams: CLI command input,
validated JSON storage, stdout/stderr and process exit. Architect owns the component graph,
file layout and classes in the technical plan. The spec does not prescribe them.
## Business Requirements
BR-1: Adding Buy tea to an absent store then listing in a fresh process displays Buy tea once.
BR-2: Valid additions preserve insertion order and duplicates across process restarts.
BR-3: Invalid task/store inputs exit 2 and preserve the prior store bytes.
BR-4: The missing-store list is empty and read-only; storage changes occur only on valid add.
LLM calls: N/A, no model is used, so PI-specific behavior is inapplicable.
## Boundaries
Always do: validate before write, keep process output/exit behavior explicit, run meaningful tests
and the real CLI/file probe before reporting completion, respect existing project records.
Ask first: adding any network service, dependency or concurrent-write requirement, or accepting the
finished result for integration when that separate decision has not been given.
Never do: write outside the user-selected store/probe-owned temporary directory, erase malformed
user data, commit secrets or rewrite existing current records without the task purpose.
## MVP boundary
Included: add/list, validation, atomic file replacement, command help, tests and runnable probe.
Implementation home: checklist/; tests: tests/; probe: scripts/probe_checklist.py; usage: README.md;
plan: plans/checklist.md. Existing brief, specs/first-checklist.md and current records are protected.
Excluded: accounts, GUI, sync, task completion/edit/delete, threads, brokers and third-party packages.
Deferred: edit/delete after add/list is accepted and the owner chooses those semantics; multi-user
storage after an authorized concurrency requirement. No dependency may be added for those future tasks.
## Acceptance Criteria
AC-CL-1: Add Buy tea, restart, list: stdout is `Buy tea` plus newline and exit is 0.
AC-CL-2: `python3 -m unittest discover -s tests` passes positive/order/duplicate/missing-store and
invalid-text/malformed-shape cases; error cases assert bytes unchanged and stderr/exit 2.
AC-CL-3: Scope review shows only the named MVP homes changed, no third-party dependencies,
network calls or secrets; current brief/spec/records are preserved.
AC-CL-4: `python3 scripts/probe_checklist.py` invokes the real `python3 -m checklist` entrypoint
in a probe-owned temporary directory and asserts both process streams/exits and persisted bytes.
AC-CL-5: A repository fixture `tests/fixtures/valid-checklist.json` of the declared JSON shape
is read by a behavior test; malformed shape rejection is independently exercised.
PI, remote health and database checks: N/A for this local program. Deferred checks: none.
## Live Probe
Environment: selected local interpreter, no remote service or credentials. Destination: only the
probe's temporary JSON store, stdout/stderr. Mechanism: the real CLI reads/writes the declared file.
Command: `python3 scripts/probe_checklist.py`. Prerequisite: the package and probe exist in the
agreed checkout and that temporary directory is writable. Scenario: missing list → add Buy tea →
fresh-process list → invalid empty add → unchanged list/file. Pass: every expected stream/exit/file
assertion succeeds, probe prints GREEN and exits 0. Any failure exits nonzero. Capture process and
file receipts in notes/checklist-result.md; no current receipt exists in this illustrative document.
## Risk Notes
A process crash must not truncate existing JSON; atomic replacement and rejection byte checks
address that boundary. Concurrent writers remain unsupported. Store task text may be personal;
probe uses only fictional data and temporary files. No model cost, token or remote rate limit exists.
## Deficiencies / interpretations
(none). Code must report Deviations explicitly, including any later reinterpretation.
$END_BODY
$START_LINKS
IMPLEMENTS: (none)
IMPACTS: CASE_RESTART
REQUIRES: (none)
$END_LINKS
$END_ARTIFACT_GOAL_CHECKLIST
$END_SECTION_MVP
$START_SECTION_USE_CASES
$START_ARTIFACT_CASE_RESTART
TYPE: USE_CASE
KEYWORDS: local user, restart, list task
$START_CONTRACT
$CONTRACT
PURPOSE: Demonstrate the first useful persistent outcome.
DESCRIPTION: Local user → add Buy tea and restart the process → inspect the same task.
RATIONALE: A single-process in-memory test cannot demonstrate restart persistence.
ACCEPTANCE_CRITERIA: AC-CL-1 and AC-CL-4 establish the visible result and real file boundary.
$END_CONTRACT
$START_BODY
Begin with a missing store. Add Buy tea, terminate that process, then invoke list in another
process using the same path. Observe one Buy tea line. Attempt an empty add and list again;
observe rejection and the same persisted title. No network destination participates.
$END_BODY
$START_LINKS
IMPLEMENTS: GOAL_CHECKLIST
IMPACTS: (none)
REQUIRES: GOAL_CHECKLIST
$END_LINKS
$END_ARTIFACT_CASE_RESTART
$END_SECTION_USE_CASES
$END_CHECKLIST_SPEC
```

<!-- anchor: protocols.spec-greenfield.limits -->

## Coverage limits

- **SG-401** MUST: Judge the entire selected-profile form and example against actual requirements, not a donor excerpt or token presence. Record missing required evidence as BLOCKED and human-dependent contradictory intent as SPEC_BLOCKED through existing roles/returns. Completing this form does not prove integration, runtime adoption or whole-source transfer.

Source synthesis retains first-value and full-form duties from the PM harness, native PM adaptation and standalone development distribution, composed with the shared development families. General decision lifecycle, full graph grammar and detailed prompting remain separate work.
