---
type: Spec
id: SPEC-<T-NNN>
title: "<M task> — specification"
checkpoint: "<T-NNN of batch B-NNN; roadmap step P-id>"
input: "docs/recon/RECON_<YYYY-MM-DD>_<topic>.md"
cites: [<DEC ids>]
batch: B-<NNN>
generated: { by: "<actor>", at: "<UTC timestamp from the clock>" }
status: draft
---

# <M task> — specification

**Done when:** <the finish line: observable outcomes; nothing beyond it is built>

**Stop and ask when:** <this task's stop conditions, in addition to those of AGENTS.md>

## Context

<What exists (from the Doxygen map and the reconnaissance), what is decided (DEC links), what is required (docs/requirements links).>

## Boundaries

- **May edit:** <paths>
- **Do not touch:** <paths>

## Acceptance criteria

<Measurable, each mapped to a test in tests/test_guide.md.>

## Plan

The plan is `specs/<T-NNN>-DevelopmentPlan.md`, written by the architect role of the feature-dev cycle.

## Business requirements

<Original source-backed BR identifiers and verbatim requirements, with provenance.>

## Expected Architecture

<Measured existing boundaries, proposed responsibilities, data flow, alternatives and selected rationale.>

## Regression contract

<Protected APIs, behaviors, full source scope and meaningful discriminating controls.>

## Actual delivery and live probes

<Exact inputs/commands/owned resources/real endpoint readback, thresholds, verification owner and unavailable limits.>

The development plan composes the full existing greenfield/brownfield, document and graph protocols; this reusable form never narrows their duties or supplies consent.
