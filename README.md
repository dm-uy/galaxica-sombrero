# agent-methodology

A harness-neutral methodology for agent-driven software development, written as plain Markdown files that no single
harness owns, and adopted by each harness point by point through an adapter file that a tool can check.

Version: `1.1.0` (see `SPEC_VERSION` and `CHANGELOG.md`).

License: [MIT](LICENSE), covering the project's code and associated documentation.

## What it is

Agent-driven development needs the same handful of things whatever runs the agents: roles with clear contracts, a flow
from specification to release, gates where the owner decides, rules for code markup and logging, and checks that a run
was honest. This repository states them once, in words that name no product, so that any harness can adopt them.

The repository holds three kinds of thing:

- The neutral files: Markdown, one topic each, opening with a card (`id`, `title`, `status`) and cut into sections by
  anchors. Their format is in `FORMAT.md`, as numbered norms (`FMT-1` to `FMT-39`).
- Two registries that mark where a harness must adapt the text: the capabilities (what a harness can do) and the
  parameters (values a harness sets). Neutral text calls them by name and never writes a value.
- The `conform` tool, which checks the repository itself and checks a harness's adapter against it.

The status of a file is `stub`, `draft` or `stable`. Version `1.1.0` has 69 drafts and 2 stubs among 71 neutral files.
The format, registries, adapter contract and conform tool are complete. Gates, shared role rules, QA/scans and the five
development-flow subjects and model selection policy have substantive draft bodies. Architect, reconnaissance, the development
plan, planned CODE and full generic graph, Coder, Debugger, Searcher, Reviewer and PM are also substantive drafts. Minimum Bootstrap preparation is a substantive draft. Exoskeleton, navigation, Doxygen, LDD, tests, AX, data and lints are substantive draft bodies. Document and greenfield/brownfield specification protocols and shared specification validation are substantive F4 drafts; general decision lifecycle (DEC01) and full graph are current F4 bodies; eight prompting and three remaining policy bodies are current bounded drafts; confirmed conventions/lifecycle/batch/session procedures and five project forms are current bounded F4 drafts; principles/glossary/Orient/preflight/run-audit/conditional safety contracts are current bounded drafts; wider uninspected F4 duties and learning F8 remain later. Debugger covers evidenced diagnosis, scoped repair, regression and renewed independent QA; Searcher supplies bounded actual inventory, complete marker/contract reads and ranked evidence under read-only authority; Reviewer judges the complete current result with independent read-only authority, current evidence and parent-owned continuation; PM prepares measured suitable specifications, preserves separate owner decisions and coordinates through declared root authority while inner PM returns scoped evidence; the remaining subjects retain their cards and later homes.
The current source contains 1234 norms, 444 anchors and 138 live calls. The registry declares 28 capabilities and seven parameters. Adapters account for the text; this release does not assert
that a particular harness already enforces it.

## Native Codex source package

[methodology-codex](implementations/codex/README.md) is the first co-located native source package at version2.2.0, with candidate state schema2. Historical neutral version1.0.0 recorded exactly the FMT-1/FMT-26/REPO-102 boundary changes under unchanged MAJOR policy; current1.1.0 retains all71 neutral paths/69drafts/2stubs and28capabilities/sevenparameters remain. Package native documents use their own declared format and independently checked73-member inventory. Every intended public member, including package Markdown/JSON/Python/extensionless/nested files, remains in the unchanged publication/privacy traversal. Ordinary Markdown outside the declared exceptions is still neutral.

Supported profile: complete co-located checkout and explicit loading of the current candidate entry/roles/protocols/runtime/adapter and full neutral core. The [package adapter](implementations/codex/adapter.json) resolves `../../` from its own directory. Missing/stale/incomplete required binding blocks dependent work; another caller cwd does not alter it. Detached cached/offline installation and automatic discovery are unsupported. Source packaging grants no installed-plugin replacement, activation, publication or integration claim. Actual native smoke and source checks have their own current evidence and limits.

Run both common and package checks; the common checker does not validate native package semantics. The root map covers tools/bin/tests; the package has its own map configuration and output. From the complete canonical public source root:

```sh
python3 -m pytest tests -s -v
bin/conform self --deny-list PRIVATE_DENY_LIST
bin/conform adapter examples/adapter.example.json
bin/conform adapter implementations/codex/adapter.json
python3 -m pytest -c implementations/codex/pytest.ini implementations/codex/tests -s -v
doxygen Doxyfile
```

Run the package map separately with `doxygen Doxyfile` from `implementations/codex/`. Read all real findings and current source/config/XML associations. These are commands, not executed results; the [test guide](tests/test_guide.md) separates actual measurements, pending native execution and preserved historical evidence.

Codex2.2 additionally supplies an explicit opt-in consumer PM profile,13 seeds/four PM entries and three commands over one shared reader. C3 automatic safeguards, C4 SDK/import/ledger, C5 autonomous proof and C6 loader handover remain held; no installation follows.

## Native Claude Code package

[methodology-claude](implementations/claude/README.md) 1.0.0 is the co-located Claude Code plugin for neutral 1.1.0. It consolidates the project's Claude Code practices into one maintained home: 28 skills (the 23 Codex-parity topics and five owner-invoked PM lifecycle commands), six role subagents with pinned model tiers and tool limits (the judges have no edit tools; no role can delegate), a SessionStart binding check, a PreToolUse guard for unrecoverable commands, a `feature-dev` Workflow spine aligned to the current flow, the run-state and visual-gate helpers, and an adapter accounting all 71 neutral files, 28 capabilities and seven parameters. No neutral file changes with it.

Supported profile: loaded in place with `claude --plugin-dir implementations/claude` for one session, `CLAUDE_CODE_PLUGIN_DIRS` for every session (see [Local use](#local-use)), or a local directory marketplace, so `${CLAUDE_PLUGIN_ROOT}/../../` reaches the neutral owners. Copied installs are unsupported and report the binding as BLOCKED. Check it with:

```sh
bin/conform adapter implementations/claude/adapter.json
python3 -m pytest -c implementations/claude/pytest.ini implementations/claude/tests -s -v
```

and `doxygen Doxyfile` from `implementations/claude/`.

## Local use

The packages load in place: a harness session reads the neutral owners and package files from disk while it works, not from a commit. Whatever lies in the checkout a harness is pointed at is therefore what every session on that machine follows. The rules below keep that checkout equal to accepted `main` for every agent that works in this repository.

1. Point each harness at its package in the main checkout of this repository. Claude Code: set `CLAUDE_CODE_PLUGIN_DIRS` to `<checkout>/implementations/claude` in the `env` of the user settings (Claude Code 2.1.280 or later; it also applies to desktop sessions, which take no command-line flags). Other harnesses use the in-place loading their package documents.
2. Keep the main checkout on `main`. Do not check out another branch there and do not leave uncommitted edits to neutral or package files in it; develop on a branch in a separate worktree and merge into `main`. Accepted changes reach new sessions as soon as `main` holds them; `git pull` or a merge is the update.
3. Try unmerged package changes in one session only, with `claude --plugin-dir <worktree>/implementations/claude`.
4. Do not link a package into a discovered skills directory: a symlinked plugin keeps the link path in `${CLAUDE_PLUGIN_ROOT}`, so `../../` resolves outside the repository and every neutral reference misses.
5. Before switching a user-level configuration to a package, save the previous configuration and the links it replaces, so the switch can be undone in one step.

## Responsibilities and feedback

The methodology allocates five concerns through existing subject contracts; this overview locates their responsibilities and supplies no competing norms.

- **Intelligence** — Intelligence selects appropriate models and reasoning through the current model policy and assigned role contracts. Inference and model execution engines are supplied by runtimes outside this repository. Interfaces: [model policy](policies/models.md) and [role contracts](roles/_base.md).
- **Memory/Context** — Memory/Context supplies relevant instructions, durable state and verified knowledge pointers to planning, execution and evaluation. Storage, retrieval and curation engines remain external; detailed memory and learning bodies remain deferred. Interfaces: [PM](roles/pm.md), [reconnaissance](process/reconnaissance.md) and [external knowledge pointers](runtime/capabilities.md).
- **Process/Orchestration** — Process/Orchestration assigns scoped work, preserves evidence and coordinates the existing owner decisions. Current role, phase, delegation, state, finalization and gate subjects provide the process interfaces. Interfaces: [phases](flow/phases.md), [delegation](flow/delegation.md), [run state](flow/run-state.md), [finalization](flow/finalize.md) and [gates](process/gates.md).
- **Goal/Specification/Vision** — Goal/Specification/Vision carries original human intent into measured specifications, planning and result judgment. Current PM, reconnaissance and plan interfaces use dictated durable carriers; detailed specification and document bodies are current F4 drafts. Interfaces: [PM](roles/pm.md), [Bootstrap](process/bootstrap.md), [reconnaissance](process/reconnaissance.md) and [development plan](protocols/dev-plan.md).
- **Feedback/Evaluation** — Feedback/Evaluation checks the actual result and feeds evidenced causes into improvement. Current QA, Reviewer, scan and conform interfaces provide independent evidenced checking; learning bodies remain deferred. Interfaces: [QA](roles/qa.md), [Reviewer](roles/reviewer.md), [scans](checks/qa-scans.md) and [conform](checks/conform.md).

The deferred bodies in these overview interfaces are the remaining detailed memory and learning-transfer responsibilities. General PM document management, confirmed residual lifecycle/batch/session procedures and five project forms are drafted in this release; contextual experience retains its existing contract. Runtime engines and broader original-source completion remain unproven.

The delivery loop connects original intent, measured preparation, approved specification, assigned design and work, independent evaluation and the resulting evidence. The delivery loop retains a separate owner decision for the concrete result before integration.

The methodology-learning loop connects observed failures and outcomes, causal analysis, source-backed candidates, independent verification and an owning decision. Unverified hypotheses and candidates never become policy or curated verified guidance automatically. External knowledge transfer follows its separately authorized source and curation contract.

Current F2 interfaces define bounded responsibilities without implementing their runtime engines. The exoskeleton, navigation, Doxygen, LDD, tests, AX, data and lints bodies are current F3 bodies; document and greenfield/brownfield specification protocols plus shared specification validation are current F4 bodies; general decision lifecycle (DEC01) and full graph are current F4 bodies; confirmed conventions, lifecycle, batch and session procedures and five project forms are current bounded F4 drafts; eight prompting F5 and three autonomy/credentials/language policy bodies are current bounded drafts; six neutral readiness contracts for principles, glossary, Orient, preflight, run audit and conditional safety/recovery are current bounded drafts; wider F4 duties, learning F8, source completeness, operational adoption and publication remain explicit later or unresolved homes. A stub or link never proves its detailed body completed.

One or multiple agents preserve existing authority, isolation and independent judgment. Existing safety and observability constraints apply to either topology. Existing time, economy and human-control constraints remain in force.

Runtime adoption and propagated enforcement remain unproven. Comparable real runs, measured savings and reduced owner coordination effort remain unproven. Operational F6–F9 work and publication remain pending their own evidence and authorization.

Current F2 interface bodies include role contracts, measured reconnaissance and planning, minimum preparation, flow/state/returns and owner decisions. Current F3 bodies are [exoskeleton](code/exoskeleton.md), [navigation](code/navigation.md), [documentation](code/doxygen.md), [LDD](code/ldd.md), [tests](code/tests.md), [AX](code/ax-ui.md), [data](code/data.md) and [lints](checks/lints.md). Current F4 bodies are [document](protocols/document.md), [greenfield specification](protocols/spec-greenfield.md), [brownfield specification](protocols/spec-brownfield.md) and [shared specification validation](process/specification.md). General decision lifecycle (DEC01) at [decisions](process/decisions.md) and [full graph](protocols/graph.md) are current F4 bodies; [specification](process/specification.md) retains its validation contract. Confirmed [document conventions](documents/conventions.md), [lifecycle](process/lifecycle.md), [batches](process/batch.md) and [session](process/session.md) procedures and [five project forms](documents/templates/INDEX.md) are current bounded F4 drafts, with full editable forms and fictional filled examples. Current bounded F5 prompting bodies are [agent design](prompting/agent-prompt-design.md), [GRACE](prompting/grace.md), [brainstorm](prompting/brainstorm.md), [decomposition](prompting/decomposition.md), [prompt markup](prompting/prompt-markup.md), [solution design](prompting/solution-design.md), [superposition and collapse](prompting/superposition-collapse.md) and [verification](prompting/verification.md). Current remaining policy bodies are [autonomy](policies/autonomy.md), [credentials](policies/credentials.md) and [language](policies/language.md); [model policy](policies/models.md) retains all eighteen current norms. Current bounded readiness contracts are [principles](concepts/principles.md), [glossary](concepts/glossary.md), [Orient](checks/orient.md), [preflight](checks/preflight.md), [particular-run audit](checks/run-audit.md) and [conditional safety/recovery](process/safety.md), with complete reusable forms and fictional cases. These bounded drafts do not complete all F5 or wider F4, source completeness, learning/evaluation, adoption or publication duties. Detailed F8 learning homes are [improvement](process/learning.md) and [knowledge](process/learning.md). The remaining subjects have deferred bodies; an interface or link invokes a subject without proving its body complete, including the eight completed F3 bodies. The remaining subjects that are still marked stub retain their earlier interface status. This combined release preserves accepted PM/M14 and the six inspected readiness contracts; C1 additionally completes the run-review and code-review owners and the native Codex one-shot/loop external-agent route. It does not complete all F5 or source duties of the wider document/learning system. Two stubs remain at process/git.md and process/publication.md; wider uninspected F4 duties remain. Adapter mechanisms supply runtime operation under actual scope and existing permission contracts.

The owner currently retains lightweight error recording in existing notes; systematic learning, improvement experiments and comparative measurement are deferred. Completed bounded document duties do not change that scope.

## Layout

| Directory or file | Holds |
|---|---|
| `FORMAT.md` | The format of the neutral files: cards, anchors, norms, calls, versions, adapters. |
| `concepts/` | The vocabulary and the principles. |
| `roles/` | The roles of the flow and what they share. |
| `flow/` | The phases, delegation, run state and finalization. |
| `process/` | Batches, gates, specification, reconnaissance, review, decisions, publication, safety and the rest of the working process. |
| `protocols/` | The shapes of the documents that pass between roles. |
| `policies/` | Autonomy, credentials, language and model choice. |
| `prompting/` | How to design and verify the prompts of agents. |
| `code/` | The code layer: markup, logging, tests, navigation, documentation build. |
| `checks/` | What each check verifies; `checks/conform.md` describes the tool. |
| `documents/` | Conventions for project documents and their templates. |
| `runtime/` | The adapter contract, its JSON Schema, the capability registry and the parameter registry. |
| `implementations/` | Typed implementation packages with their own declared formats, complete inventories, adapters, tests and maps; every intended public member remains in publication/privacy coverage. |
| `implementations/codex/` | The native Codex source package, own format/inventory/adapter/tests/map; separate from neutral membership, included in public privacy coverage. |
| `implementations/claude/` | The native Claude Code plugin package, own layout/adapter/tests/map; loaded in place; separate from neutral membership, included in public privacy coverage. |
| `examples/` | A working example adapter and the small harness it describes. |
| `bin/`, `tools/` | The `conform` command: a launcher and the Python package behind it. |
| `tests/` | The tests of the tool and of the repository, and their map in `tests/test_guide.md`. |
| `SPEC_VERSION`, `CHANGELOG.md` | The version of the methodology and its history. |

Local untracked execution state and evidence metadata are separate from the complete tracked publication set. Publication verification includes every tracked public member with its full bytes and modes; native-bearing working-tree scans report their different population and any failures separately. This local metadata is not a deployed harness or evidence of runtime adoption.

## How a harness adopts it

A harness keeps one JSON file, the adapter, in its own repository or its declared owned implementation package here. In it the harness accounts for every neutral file,
meets every capability and sets every parameter. `runtime/adapters.md` states the contract and
`runtime/adapter.schema.json` is its JSON Schema.

Each neutral file is taken in one of four ways:

1. By reference: the harness keeps no copy and points at one of its own files that names the neutral file's id or path.
2. Vendored with a hash: the harness keeps a copy and records the SHA-256 of the neutral bytes; the tool reports the copy
   stale when the neutral file moves on.
3. Vendored with overrides: the copy differs in named sections, and each difference carries an anchor, a reason, an owner
   and a date or a trigger.
4. Not applied: the harness does not adopt the file and gives a reason.

Capabilities (`runtime/capabilities.md`) are the adaptation points the neutral text may call. For each one the adapter
gives a `mechanism`, a `fallback`, or both. Parameters (`runtime/parameters.md`) are the values the neutral text may
call; the adapter gives each a non-empty value.

The steps:

1. Copy `examples/adapter.example.json` into the harness's repository or owned declared package and set `harness`, `owner`, `spec_version` and
   `spec_root`. Paths in the file are absolute or relative to the directory of the adapter file.
2. Choose one of the four ways for every neutral file listed in `files`.
3. Give every capability a mechanism, a fallback, or both.
4. Give every parameter a value.
5. Run `bin/conform adapter ADAPTER.json` until it exits 0, and read every warning.

The example adapter and its small harness sit in `examples/`; they are fixtures for the tests and belong to no real
harness. [Flow-contract cases](examples/flow-contract/README.md) demonstrate a bounded consumer of selected actual
normative clauses, with independent expected decisions and scratch omission/contradiction controls. The consumer
verifies this example's interpretation and process delivery; it does not execute a live harness or prove every norm
enforced by an adapter. Its documented subset and limits accompany its invocation.
[Model-economy cases](examples/model-economy/README.md) provide eleven finite decisions and five prose mutation
controls for independent review of the selection policy. They define no executable dispatcher and demonstrate no
live adoption or measured savings.

[Design-contract fixtures](examples/design-contract/README.md) contain two generic plans, actual XML and map/source
identity files, distinct negative examples, a semantic case matrix and six prose controls. These fixtures cover the minimum
planned CODE contract; the current full graph body adds profiles and grammar beyond this finite fixture population, while the detailed document contract is a draft. These fixtures claim no live
product or harness adoption.

## Running conform

Python 3 with the standard library is all it needs.

```
bin/conform self --deny-list FILE [--root DIR] [--json] [--log-level LEVEL]
bin/conform adapter ADAPTER.json [--json] [--log-level LEVEL]
```

- `self` checks this repository: the format of every neutral file, the registries, the calls, the version, and a
  publication scan for private content. The scan needs a deny list, a file of private words one per line that lives
  outside the repository; without it the mode refuses to run.
- `adapter` checks an adapter against the spec it names: the schema, the spec version, the parameters, the capabilities,
  the coverage of the neutral files, and each file's way of adoption.
- `--json` prints the report as one JSON object instead of a table. `--log-level` sends the tool's own trace to standard
  error; without it nothing goes there.

Exit codes:

| Exit | Meaning |
|---|---|
| 0 | No failure. There may be warnings and notes. |
| 1 | At least one finding failed. |
| 2 | The check could not run (an input is missing or unreadable). The report is a single `NOT RUN` row. |

`checks/conform.md` describes the table, the summary line, the JSON object and every rule.

## Versions

The methodology is versioned as one unit in `SPEC_VERSION` as `MAJOR.MINOR.PATCH`, and every version has an entry in
`CHANGELOG.md`. Removing a norm or changing its meaning raises MAJOR; adding a norm or a file raises MINOR; a wording
change that keeps every meaning raises PATCH. An adapter names the version it was written against, and the tool warns
when that is older than the repository's.

## Development

```
python3 -m pytest tests -s -v
doxygen Doxyfile
```

The tests cover the tool, the format and the example adapter, and print a trajectory line before each check; the map
from requirements to tests is `tests/test_guide.md`. The Doxygen build must finish without a message. The code carries
its own markup (module contracts, region tags, one-line structure diagrams and log lines with an importance level) so
that a reader who sees only one file can still work with it.

## Project management and maintainer sessions

The general PM layer is now applied in [document conventions](documents/conventions.md), [five forms](documents/templates/INDEX.md), [lifecycle](process/lifecycle.md), [current task/batch](process/batch.md), [session](process/session.md), [decisions](process/decisions.md) and [experience](process/learning.md). It serves different work types; existing software-development roles remain their applicable specialization. Detailed technical document/specification protocols are now substantive drafts; general decision lifecycle (DEC01) and full graph are now substantive drafts; eight prompting and three remaining policy bodies are current bounded drafts with scoped skill packaging. Confirmed conventions/lifecycle/batch/session procedures and five project forms now carry full editable forms and fictional filled cases; six readiness contracts now carry bounded draft bodies/forms/cases; four stubs, wider uninspected F4, learning/evaluation/source responsibilities, operational adoption and publication remain later or unresolved.

Start a maintainer session from [AGENTS](AGENTS.md), which points to the sole current state under examples/pm-project. The root entry is repository-specific and the example adapter explicitly does not apply it to consuming harness behavior. The retained [fictional PM example](examples/pm-integration/README.md) supplies no actual grant or operational effectiveness evidence. This complete repository is the maintained source for the neutral methodology and both implementation packages; earlier export-preparation records are historical, not a second active source. Read [VISION](examples/pm-project/VISION.md), [ROADMAP](examples/pm-project/ROADMAP.md), [TASKS](examples/pm-project/TASKS.md) and [HANDOFF](examples/pm-project/HANDOFF.md) before choosing work. Broader original-source transfer remains unproven. Result acceptance, public visibility, installation and any new native consumer exercise retain their separate decisions.

### Working with another agent

Open a complete checkout of this repository as the project folder in the chosen coding harness. Start at AGENTS.md and the four current records; use relevant owners and the chosen co-located implementation only when the task requires them. Configure an authentic owner-approved Git identity locally before the first commit. Preserve a clean main checkout for package loading, create an isolated worktree for changes, verify the affected contracts and deliver a PR. Future clones obtain the instructions through Git; local identity and credential configuration are machine-local and must be set separately.

For shared rules run conform self with an external private deny list and the example adapter. For package changes run the affected package's tests and adapter as well as root assembly checks. Code changes use the project's documented trace/runtime/map checks and independent judgment where applicable. Documentation-only edits still verify source links and preserved interfaces; do not claim a full native consumer run from a tooling check. The initial source release and all later results retain their own evidence populations.
