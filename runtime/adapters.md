---
id: runtime.adapters
title: Adapters
status: draft
---

# Adapters

This file states the adapter contract: how one harness adopts the methodology, and what a tool checks about it. The
norms of the contract live once, in `FORMAT.md`, in the section `format.adapter` (FMT-26 to FMT-38); this file cites them
and carries no norm of its own.

<!-- anchor: runtime.adapters.purpose -->

## What an adapter is

An adapter is how one harness adopts this methodology. It is a single JSON file that lives in the harness's own
repository or its declared implementation package here (FMT-26). In it the harness accounts for every neutral file of this repository, meets every
capability, and sets every parameter. The methodology stays neutral; the adapter holds everything that is the harness's
own.

<!-- anchor: runtime.adapters.ways -->

## Four ways to adopt a file

A harness takes each neutral file in exactly one of four ways. The JSON records the first, second and fourth as a
`mode`; the third is a vendored entry that also lists overrides.

1. **By reference.** The harness keeps no copy. It points at one of its own files (`via`) that names the neutral file's
   id or path. This fits a harness whose own text already says the same thing and only needs to stay linked to it.
2. **Vendored with a hash.** The harness keeps a copy of the file and records the SHA-256 of the neutral bytes at the
   time of the copy. This fits a harness that installs the text as it is: the tool tells it when the neutral file has
   moved on.
3. **Vendored with overrides.** The harness keeps a copy that differs from the neutral file in named sections. Each
   difference is an override: an anchor, a reason, an owner, and a date or a trigger. This fits a harness that must
   word one section its own way for a stated reason and for a limited time.
4. **Not applied.** The harness does not adopt the file and says why. This fits a file about something the harness does
   not do.

<!-- anchor: runtime.adapters.fields -->

## The fields

| Field | Meaning | Norm |
|---|---|---|
| `harness` | The name of the harness that owns the adapter. | FMT-27 |
| `owner` | Who answers for the adapter. | FMT-27 |
| `spec_version` | The version of this methodology the adapter was written against; an older one is a warning. | FMT-27, FMT-37 |
| `spec_root` | Where this repository is, absolute or relative to the directory of the adapter file. | FMT-27 |
| `parameters` | Every declared parameter mapped to a non-empty value. | FMT-28 |
| `capabilities` | Every declared capability mapped to an object with a non-empty `mechanism`, a non-empty `fallback`, or both. | FMT-29 |
| `files` | The path of every neutral file mapped to one entry. | FMT-30 |
| `files.<path>.mode` | `reference`, `vendored` or `not-applied`. | FMT-30 |
| `files.<path>.via` | For `reference`: the harness file that names the neutral file's id or path; it must exist. | FMT-27, FMT-31 |
| `files.<path>.path` | For `vendored`: the harness's copy, absolute or relative to the directory of the adapter file. | FMT-27, FMT-32 |
| `files.<path>.sha256` | For `vendored`: the SHA-256 of the neutral file's bytes with line endings normalised to LF at the time of the copy, in lowercase hex. | FMT-32, FMT-38 |
| `files.<path>.overrides` | For `vendored`, optional: the sections the copy words its own way. | FMT-32, FMT-33 |
| `overrides[].anchor` | The anchor of the overridden section; it exists in the neutral file. | FMT-34 |
| `overrides[].reason` | Why the section differs. | FMT-34 |
| `overrides[].owner` | Who answers for the difference. | FMT-34 |
| `overrides[].until` | An ISO date; it must not lie in the past. | FMT-34, FMT-35 |
| `overrides[].trigger` | An event that ends the override, checked for presence only. | FMT-34 |
| `files.<path>.reason` | For `not-applied`: why the file is not adopted; non-empty. | FMT-36 |

<!-- anchor: runtime.adapters.capabilities-and-parameters -->

## Capabilities and parameters

The adapter meets the two registries of this directory. `runtime/capabilities.md` lists the adaptation points that the
neutral text may call; for each one the adapter gives a `mechanism` (what the harness does), a `fallback` (what it does
without one), or both (FMT-29). `runtime/parameters.md` lists the values the neutral text may call; the adapter gives
each a non-empty value (FMT-28). An adapter that leaves a declared name out, or adds a name that is not declared, is
reported.

The [model selection policy](../policies/models.md) uses the existing mechanical, routine and judgment parameters
without changing their definitions. Their values name concrete selections or configuration references; the model-tier
mechanism/fallback explains actual selection authority, supported effort/settings and limitations (FMT-28, FMT-29).
Classify the task by its hardest necessary step rather than a role-only default. An adapter can declare one adequate
model for several tiers or fixed configuration without dynamic selection, stating absent effort controls explicitly.
Requested selections and exposed observations stay distinct in existing run records. Structural adapter coverage does
not establish that a live harness performs these decisions or achieves savings.

<!-- anchor: runtime.adapters.check -->

## What the check reports

`conform adapter` reads the adapter, the schema and this repository, and reports one row per finding, in the table and
the summary line described in `checks/conform.md`. It refuses to run, with exit 2, when the adapter or the repository
cannot be read. It fails, with exit 1, when the adapter breaks a norm above. It warns, with exit 0, when the adapter's
`spec_version` is older than this repository's `SPEC_VERSION` (FMT-37) or when a vendored copy is stale because the
neutral file has changed since the copy was made (FMT-38); a copy whose sections differ without an override is a
failure when it is fresh and a warning when it is stale (FMT-33).

<!-- anchor: runtime.adapters.adopt -->

## How a harness adopts the methodology

1. Copy `examples/adapter.example.json` into the harness's own repository or its owned declared implementation package and set `harness`, `owner`, `spec_version`
   and `spec_root`.
2. Account for every neutral file: choose one of the four ways for each path in `files`.
3. Meet every capability: give each a `mechanism`, a `fallback`, or both.
4. Set every parameter to a non-empty value.
5. Run `conform adapter` on the file until it exits 0, and read every warning.

<!-- anchor: runtime.adapters.packages -->

## Co-located implementation profile

A declared package under `implementations/` owns its adapter, native format, complete inventory, tests and map configuration. Its files are outside neutral Markdown membership under FMT-1, but every intended public package member remains in publication/privacy traversal. Common conformance checks the unchanged neutral adapter contract; explicit independent package checks validate native assembly and behavior. Run both command families. A package's existence or structural reference token cannot prove full current rule adoption or live enforcement.

At `implementations/codex/adapter.json`, `spec_root` is `../../` resolved from that adapter's directory, and `via` paths resolve from the same directory under FMT-27. The first supported Codex profile is a complete co-located checkout with explicit candidate-source loading. Required current neutral core/role/protocol/runtime content must actually resolve and be read; missing, stale, stub or truncated required input blocks dependent action. Another caller cwd does not change the binding. Detached cached/offline installation and automatic discovery are unsupported in this profile; do not silently substitute an installed package.

The existing schema bytes/fields/modes remain unchanged; its historical own-repository description is not a new location validator. Package/source identities and actual capability mechanisms, fallbacks and semantic deviations retain their separate proof and authority. Package/source loading supplies no installation, publication, license, integration or model-effect claim.
