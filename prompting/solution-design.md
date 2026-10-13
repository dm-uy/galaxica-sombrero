---
id: prompting.solution-design
title: Solution design
status: draft
skill-name: solution-design
skill-when: Author requirements, structural and temporal projections, and measurable acceptance checks.
---

# Solution design

<!-- anchor: prompting.solution-design.requirements -->

## Describe the same solution from independent angles

A graph describes what exists and how components relate. A data flow describes what happens over time. Acceptance criteria describe observable success. Requiring their agreement exposes absent components, invented actions and uncheckable promises. Their agreement proves internal consistency of the declared design, not factual truth, actual execution or readiness of an external system.

- **SOLVE-101** MUST: Establish functional requirements, relevant nonfunctional requirements, hard boundaries, sources and actual unknowns before completing the design. Resolve material unknown intent rather than silently choosing it.
- **SOLVE-102** MUST: Reconcile the declared static component population, primary/error/edge flows and measurable criteria; every flow step uses an established component, every scenario-relevant component has an accounted role, and every criterion can be observed on the proposed design.

Clarify scope, audience, effects, existing components, input/output contracts and constraints first. Numerical targets belong to the actual task; do not invent latency/load/reliability thresholds to make a table look technical. Label supplied targets, estimates and measured observations separately. A component used only in an error scenario need not run in the primary scenario. Whole declared-population accounting includes optional/reference/metadata components with their stated applicability; it is not a demand that every node appear in every path.

<!-- anchor: prompting.solution-design.projections -->

## Procedure and complete form

1. Extract requirements and boundaries, preserving accepted decisions and real authority. Record source/data qualifications.
2. Produce the static graph: component IDs, purpose, input, output and relations. Software serialization uses the current [graph protocol](../protocols/graph.md), including its owned DOMAIN prompt; this general procedure does not redefine that grammar.
3. Produce the temporal projection for the primary path, relevant failure paths and boundary cases. Identify transformations, ownership, effects and missing-tool/source routes.
4. Define criteria by output, event, count or applicable measured target, with a specific check/evidence route. Cover correctness and any required performance/reliability/testability aspects. If performance is irrelevant, say so rather than inventing a target.
5. Cross-check the three projections. Repair contradictions in their owning artifact and repeat the consistency check. Unsupported environmental facts remain uncertain.
6. Hand off a bounded next-step decomposition and the actual readiness limit. Existing software [development plans](../protocols/dev-plan.md), roles and gates remain authoritative; a research/operations design does not automatically activate them.

The older source template puts TASK before REQUIREMENTS/OUTPUT. Preserve that as a contextual task-first form when the task is already bounded. For reusable mixed prompts prefer native authority and goal framing early, then context and the concrete invocation task. Neither order grants effects.

Placeholder design prompt:

```text
$START_DESIGN
$START_GOAL
[Observable result, audience and actual authority]
$END_GOAL
$START_REQUIREMENTS
[Functional; relevant nonfunctional; constraints; accepted decisions; source identities; unknowns]
$END_REQUIREMENTS
$START_STATIC_PROJECTION
[Each component ID/purpose/input/output plus actual relations; declared population and applicability]
$END_STATIC_PROJECTION
$START_DYNAMIC_PROJECTION
[Primary flow, error flow and relevant edge flows with known components and owned state/effects]
$END_DYNAMIC_PROJECTION
$START_ACCEPTANCE
[Each criterion: observable outcome, check method, evidence and applicable threshold]
$END_ACCEPTANCE
$START_CONSISTENCY
[Whole population accounted; flow uses existing nodes; criteria checkable; discrepancies/revisions]
$END_CONSISTENCY
$START_NEXT
[Bounded next artifact, dependencies, unknowns and readiness limit]
$END_NEXT
$END_DESIGN
```

<!-- anchor: prompting.solution-design.example -->

## Filled illustrative design

Fictional need: prepare a two-item workshop schedule from supplied records for a coordinator. Functional requirement: emit each valid title, room and time. Reliability requirement: report incomplete records and do not fabricate fields. Boundary: draft only, no room booking/publication. Performance has no supplied target and is not material to this small illustration.

The following complete XML is an illustrative component representation, not the software graph grammar or a new primary template:

```xml
<SYSTEM name="ScheduleDraft">
  <COMPONENT name="ReadRecords" type="input">
    <PURPOSE>Accept the explicitly supplied record population.</PURPOSE>
    <INPUTS>Invocation records</INPUTS><OUTPUTS>Record list</OUTPUTS>
  </COMPONENT>
  <COMPONENT name="CheckFields" type="validation">
    <PURPOSE>Require title, room and time on every record.</PURPOSE>
    <INPUTS>ReadRecords record list</INPUTS><OUTPUTS>Valid records or missing-field report</OUTPUTS>
  </COMPONENT>
  <COMPONENT name="DraftSchedule" type="authoring">
    <PURPOSE>Render every valid record with a draft limitation.</PURPOSE>
    <INPUTS>CheckFields valid records</INPUTS><OUTPUTS>Draft text</OUTPUTS>
  </COMPONENT>
  <COMPONENT name="ReportMissing" type="error-output">
    <PURPOSE>Expose incomplete input without invented values.</PURPOSE>
    <INPUTS>CheckFields missing-field report</INPUTS><OUTPUTS>Held result</OUTPUTS>
  </COMPONENT>
  <RELATION from="ReadRecords" to="CheckFields"/>
  <RELATION from="CheckFields" to="DraftSchedule" when="valid"/>
  <RELATION from="CheckFields" to="ReportMissing" when="incomplete"/>
</SYSTEM>
```

Primary flow: invocation supplies Reading/A/09:00 and Discussion/B/10:00 → ReadRecords retains two entries → CheckFields finds all required fields → DraftSchedule emits two rows and “Draft; date not supplied.” Error flow: invocation supplies Reading/A with no time → ReadRecords retains the incomplete entry → CheckFields identifies missing time → ReportMissing returns HELD with that missing field and no schedule claiming completion. Edge flow: empty population → ReadRecords supplies an empty list → CheckFields accepts its structural shape → DraftSchedule states “No entries supplied; draft only,” without inventing a session.

| Criterion | Check/evidence | Expected result |
|---|---|---|
| Every valid record appears exactly once | Compare source records and rendered rows | Two supplied entries produce two matching rows |
| Incomplete data is visible | Supply the no-time error case | HELD names time; no invented time or completion claim |
| Draft boundary is preserved | Inspect every output branch | Draft/held limitation present; no booking/publication claim |
| Empty population is truthful | Supply an empty list | No invented session; explicit no-entry result |

Consistency record: all four components appear across the declared scenarios; ReportMissing is error-only. Every flow step names one of those nodes; criteria1/3/4 observe DraftSchedule and criterion2 observes ReportMissing. No external service or API is assumed. Next artifact is the [decomposed authoring contract](decomposition.md); no implementation or live check is claimed. If a real consumer needs machine routing, [agent design](agent-prompt-design.md) adds an actually bound schema/control contract.
