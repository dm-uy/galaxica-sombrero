---
id: protocols.dev-plan
title: Development plan
status: draft
---

# Development plan

This contract makes the design consumable by Code and independent QA. It retains plan-local document structure and readiness duties alongside the detailed [document](document.md) contract.

<!-- anchor: protocols.dev-plan.authority -->

## Identity, authority and artifact readiness

- **PLAN-101** MUST: Preserve the original approved requirements and decisions beside required RECON evidence. Cite their actual identities, scope and constraints; the synthesis never becomes the sole authority or erases original quantifiers. Write at the actual dictated plan path: explicit invocation override first, then the project's declared artifact convention/layer, then its documented legacy default. Record actual path and rule; basename similarity is insufficient.
- **PLAN-102** MUST: State METHODOLOGY_VERSION copied from the actually loaded constitution, purpose, scope, classification, rules and source identity. Create the section outline before detail. State purpose, rationale and verification contract for the plan and every independently produced artifact/slice, mapping to exact approved criteria. A missing purpose, rationale or verification contract is a readiness defect.
- **PLAN-103** MUST: Preserve ordered sections 1 Draft Code Graph, 2 Step-by-step Data Flow, 3 Visual Verification, 4 Acceptance Criteria, 5 Delivery Contract and 6 Runtime Commands. Rationale may precede section 1; verification commitments may follow section 6. Preserve mandatory content rather than copying a donor numbering variant.
- **PLAN-104** MUST: When the target format uses START/END markers, use matching explicit boundaries with correct nesting and a closed outline. A heading alone does not terminate a marked block. Do not emit unclosed boundaries, omitted-code placeholders or illustrative empty content as a ready plan. Assigned subject reads still apply; reading a stub supplies no substantive contract, and reading the completed [document](document.md) subject alone does not establish actual plan readiness.

<!-- anchor: protocols.dev-plan.design -->

## Design and process projection

- **PLAN-201** MUST: Record approved MAY EDIT/DO NOT TOUCH, cardinal target rules, regression/API invariants, deficiencies/deviations and independently implementable slices with tests and actual applicability of all four Architect patterns. Before details, compare two or three viable alternatives against sourced criteria and record collapse/rejections under ARCH-301–304. Human-dependent unresolved intent refuses readiness; autonomous routine selection adds no gate. At the consequential-open trigger load the complete [brainstorm owner](../prompting/brainstorm.md#prompting.brainstorm.consequential); link the parent-prepared proposal/HOLD/evaluation/authorized-decision packet before dependent readiness. Record routine/settled/forced exclusions with their reason; missing mandatory independence leaves that choice held.
- **PLAN-202** MUST: Place one well-formed DraftCodeGraph under [graph](graph.md) in section 1. Its definitions describe the new/modified design; unchanged brownfield dependencies use evidence-backed typed references. Keep approved requirement membership and definition/reference/metadata distinctions explicit.
- **PLAN-203** MUST: In section 2 describe key algorithms in ordered steps from inputs through transformations, integration and output/error behavior; mentally simulate primary and critical failure paths. Align process projection with actual graph entities/relationships. The structural and temporal projections are complementary; neither excuses a contradiction in the other.

<!-- anchor: protocols.dev-plan.visual -->

## Visual verification and readiness evidence

- **PLAN-301** MUST: Activate the mechanical visual gate for at least three new or modified component definitions unless the task is tests-only. Project metadata, unchanged references and links are excluded from changed-component counts. Below three or for tests-only, record actual counts/exception and SKIPPED/NOT_APPLICABLE reason; per-file structure diagrams still serve their separate purpose.
- **PLAN-302** MUST: When active, use {{cap:check-runner}} to run the adapter-declared actual visual check against the actual plan and approved specification. Preserve command, cwd, complete output, exit status, candidate identity and scanned-definition count. Mechanical PASS requires exit 0 and at least one recognized definition. Exit 1 is FAIL and stops Code; exit 2 or a missing/empty scan refuses readiness. An orchestrator independently confirms evidence under PHASE-403/405 and RETURN-403; do not manufacture success by renaming unsupported entities.
- **PLAN-303** MUST: Check every new/modified definition for missing, empty or non-BR satisfaction (SCOPE_CREEP), every named BR against approved membership (UNKNOWN_BR), and every approved BR for satisfying definitions (UNCOVERED_REQUIREMENT). Treat these as distinct errors and stop on each. Run all three checks for GREENFIELD too; GREENFIELD_WEAK labels only the unavailable prior-architecture comparison, never skipped unknown/coverage checks. References and metadata cannot supply coverage.
- **PLAN-304** MUST: Disclose the actual recognizer's supported syntax and unrecognized definitions. XML parsing, regex recognition/coverage and human semantic fidelity are separate evidence. Zero recognized definitions cannot be PASS. Unsupported or mixed syntax requires a recorded manual review permitted by the applicable protocol, with extent/limits and authoritative consumer decision; it cannot waive a genuine recognized-node defect or claim unsupported nodes were mechanically checked.
- **PLAN-305** MUST: In an active visual section render traceability deterministically from actual satisfies values: every approved BR appears, every changed component appears and each edge is component to requirement. A Mermaid requirement name uses an XML-safe normalized alias such as BR_1 with id BR-1; use valid id/text/risk/verifymethod fields. Verify orphan/unknown/uncovered meaning independently of a decorative diagram.
- **PLAN-306** MUST: Provide a structural flowchart or block projection from the XML and compare every node/edge with that source. An absent or contradictory diagram edge is RENDER_HALLUCINATION and a design defect. Until a deterministic transform is actually supplied, this projection requires semantic judgment; a coverage lint does not establish fidelity.
- **PLAN-307** MUST: When at least two components exchange data, provide a primary-scenario sequenceDiagram derived from section 2. When an entity has at least three distinct states/statuses, provide stateDiagram-v2. For database schema changes provide erDiagram; use classDiagram where introduced hierarchy or central inheritance/polymorphism is not adequately visible in the graph. Record actual reasons for inapplicable projections, without broadening the task.
- **PLAN-308** MUST: In explicitly interactive work obtain the required owner projection/collapse decision, comparing supplied Expected Architecture; authorized autonomous work uses actual mechanical evidence and independent structural judgment without an extra plan gate. Preserve known manual exceptions and their limitations rather than calling them mechanical PASS.

<!-- anchor: protocols.dev-plan.verification -->

## Acceptance, delivery and actual operation

- **PLAN-401** MUST: In section 4 preserve every approved AC, including conditions and quantitative thresholds; state the measurement command/query, population, expected result and evidence. Use clear checkable outcomes, actual code reading or operations and independent meaning judgment where needed. Do not synthesize tighter acceptance as a substitute for original approval.
- **PLAN-402** MUST: In section 5, for every AC/invariant naming an observable side-effect channel, state the actual sink, delivery mechanism and real success evidence. A log deliverable, event, metric or audit record with no delivery path is DELIVERY_CONTRACT_MISSING and refuses readiness. Pure in-process return values do not trigger an invented external channel. Capture/mock evidence proves an API call; an applicable deliverable or process/container boundary also needs real-endpoint runtime proof under QA's channel/infra scans.
- **PLAN-403** MUST: List every relied-upon verification mechanism as a literal test token -> real production symbol or operation -> claimed outcome. The token is an actual intended test/fixture/module identifier, not a technique name; after Code its exact occurrence and actual exercised operation must be verified. Fake-to-fake proxies, mere symbol/file existence and the document declaring a forbidden observable do not prove operation. If no tests are produced, state that explicitly with reason and the actual verification alternatives. Report dropped/replaced commitments as deviations.
- **PLAN-404** MUST: A rationale's verifiability promise reappears in verification commitments with its concrete mechanism; counts follow the actual design. Select differentiating tests that expose meaningful failure classes and real input/output shape. Keep production success evidence, fixture-only conclusions and unverified external premises distinct.

<!-- anchor: protocols.dev-plan.commands -->

## Runtime command table

- **PLAN-501** MUST: In section 6 resolve commands from actual target instructions/manifests/tool constraints during archaeology and supply test, dependency verification, run, health/readiness and lint/typecheck rows with cwd, applicable prerequisites and reasons for N/A. Code, QA and Debug use the documented commands verbatim through {{cap:check-runner}}; long operations use {{cap:background-command}} where required.
- **PLAN-502** MUST: Include a row set for each applicable stack side. A target-forbidden command never appears even as a fallback. Only when no tooling is documented use compatible defaults for actual required operations, such as python -m pytest for Python tests and python -m pip index versions for read-only package verification; do not install a new environment merely to fill the table.
- **PLAN-503** MUST: Derive runtime/health probes from this table and the actual DoD; container steps apply only when the deliverable names containers. Record real commands/stdout/stderr/exits and failures; a command proposal is NOT RUN until exercised. Applicable product code-map obligations persist, with no new service, provider or adoption claim implied by this contract.
