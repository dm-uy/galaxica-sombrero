---
id: runtime.parameters
title: Parameters
status: draft
---

# Parameters

This file declares the parameters of the methodology: the values that each harness sets in its adapter.

<!-- anchor: runtime.parameters.purpose -->

## What a parameter is

A parameter is a value that each harness sets in its adapter. A neutral text calls it with a parameter call written in
a code span, for example `{{param:owner-label}}`, and never writes the value itself. The adapter maps every declared
parameter to a non-empty value (FMT-28). A call resolves only to a declaration in the list below (FMT-20).

<!-- anchor: runtime.parameters.list -->

## The parameters

- **param:dialog-language** The language the agents speak with the owner in dialog.
- **param:owner-label** The word the agents use for the person who owns the project and approves at its gates, where the neutral text says "the owner".
- **param:model-mechanical** The model for mechanical work: finding files and symbols, marker scans, counting, format checks and pulling fields whose place is known.
- **param:model-routine** The model for routine work of a known shape: reconnaissance of a named area, extraction into a fixed template, code from an approved plan, verification scans and debugging with a clear trace.
- **param:model-judgment** The model for judgment: architecture and development plans, specifications, new material, legal, privacy and security reasoning, options for the owner's decision, open investigations and synthesis across many lanes.
- **param:gate-cadence** The cadence for the first owner decision: per-change, approving each specification, or batch, approving tasks and their recorded scope in advance; the concrete result still needs the second decision.
- **param:debug-entry-cap** The adapter's cumulative maximum entries into Debug, default four; a nonnegative integral value may lower the default. Increasing allowance requires an explicit bounded owner grant under the gate contract. The phase/run-state contract defines pre-entry spend, failure preservation and separate retry units.
