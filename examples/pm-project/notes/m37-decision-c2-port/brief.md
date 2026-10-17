# M37 decision brief — how the Claude package gains the consumer PM profile

Status: consequential-open choice under prompting/brainstorm.md#prompting.brainstorm.consequential (BRAIN-104). Stakes: package and ownership boundaries between the two native packages and the neutral root, a shared on-disk/CLI contract used by five consumer projects, test/membership oracles, and maintenance cost of two harness adaptations over time. Costly to reverse once consumer projects call the commands.

Decision authority: the owner (Danis Valitov) approved on 2026-10-16 the scope "small fixes now + port of the C2 consumer PM profile to the Claude package through specification → owner approval → feature-dev". This brief asks generators for architecture alternatives only; selection happens after a separate evaluation and the owner's specification approval.

## Goal

The Claude Code package `implementations/claude/` (plugin `methodology-claude`, version 2.0.2, loaded in place from a complete checkout) must give a Claude Code user the same consumer PM capability the Codex package received in C2: the opt-in consumer profile, 13 seed templates, the four lifecycle entries routed to them, and the commands `orient` / `orient --check` / portfolio, `codemap`, `markup_migrate` with a shared resolver `consumer_files`. When done, the owner disables the old in-house plugins `product-methodology` and `prompting-methodology` without losing capability in five real consumer projects.

## Facts (verified in this repository on 2026-10-16)

- Repository root holds the harness-neutral methodology (roles/, process/, flow/, protocols/, checks/, code/, documents/, prompting/, policies/, runtime/), each file a typed card under FORMAT.md. Root AGENTS.md REPO-102: no arbitrary root formatting exemptions; the typed implementation-package boundary is defined only by FORMAT.
- Codex package `implementations/codex/` (3.0.1, 73 members, 27 skills, 6 helpers, 6 roles) ships: `references/consumer-pm-profile.md` (147 lines: profile methodology-consumer-pm/1.0.0, CONVENTIONS homes, read budgets, 13 seeds, four triggers, command contracts, 75 CV duties and 22 checklist rows accounting), `skills/pm/templates/` (AGENTS, CLAUDE, CONVENTIONS, VISION, ROADMAP, HANDOFF, TASKS, DEC, SPEC, RECON, OPEN_QUESTIONS, Doxyfile, gitignore), `skills/pm/scripts/{consumer_files,orient,codemap,markup_migrate}.py` (≈2450 lines of standard-library Python with full exoskeleton/LDD markup), and tests `implementations/codex/tests/test_{consumer_files,consumer_pm,codemap,markup_migrate}.py`. Its README documents invocation as `python3 -B PACKAGE/skills/pm/scripts/<command>.py PROJECT ...`. Codex is installed for the owner as a complete repository snapshot (the whole repo, with a generated root transport manifest), so the Codex install also contains `implementations/claude/`.
- Claude package `implementations/claude/` (2.0.2, 59 members, 28 skills, 4 helpers, 6 role agents) is loaded only in place (`CLAUDE_CODE_PLUGIN_DIRS` or `--plugin-dir`); any marketplace install copies the package alone into the plugin cache and its SessionStart hook then reports BLOCKED (probed on Claude Code 2.1.299). Skills reference neutral owners as `${CLAUDE_PLUGIN_ROOT}/../../<owner>`. It ships hooks (SessionStart binding check that only reports which of VISION/ROADMAP/TASKS/HANDOFF exist next to AGENTS.md; PreToolUse Bash guard), a Workflow script, `run_state.py` and `visual_gate_lint.py`. Its pm-bootstrap seeds only the five neutral templates under `documents/templates/`. `references/source-disposition.md` marks code-map, markup-migration and run-review scripts as "outside — candidates for a later package increment".
- Membership is pinned: `references/package-layout.json` lists every member; `run_state.py` binds package identity and the declared layout; root `tests/test_claude_package.py` is an independent oracle of the 59 paths from the approved M22 specification; root `tests/test_c1_review_and_routing.py` pins whole-AST identities of both run_state helpers (only named version/census selectors normalize). Codex C2 BR-4 froze run_state algorithm changes to binding constants.
- The old product-methodology plugin ships `bin/codemap` and `bin/markup-migrate`; in this Claude Code session the Bash PATH contains that plugin's `bin/` directory (its marketplace source path; no shell-profile entry adds it), so a plugin `bin/` reaching PATH is observed here, not yet verified against documentation. It has no `orient` executable: its SessionStart hook runs `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/orient.py --hook session-start` and prints the generated orientation in declared projects; agents run its `scripts/orient.py` for `--check`.
- Five consumer projects (consumer-A, consumer-B, consumer-C, consumer-D, consumer-E) instruct agents in AGENTS.md to run bare `orient` at session start and `orient --check` at the end; consumer-D calls bare `codemap <project> <file or symbol>`; three CLAUDE.md files say the plugin injects the orientation. Their documents follow the old in-house conventions dialect (CONVENTIONS front matter, Doxyfile ALIASES block, DEC files).
- Owner defaults: time over money; fix root causes; project records stay as Markdown in git; one writer per path; neutral owner wins over a package carrier and a difference is a package defect.

## Hard constraints

- Do not change neutral owner bodies, FORMAT, registries, schema or the six software roles; do not add root formatting exemptions.
- Preserve run_state algorithms (only binding constants may move), the wire/schema, all existing tests' assertions and negative controls; membership changes must update the layout, the independent oracle and the package contract tests together.
- In-place loading stays the only supported Claude profile; no fallback to an older installed copy; a missing dependency is BLOCKED.
- No automatic adoption of consumer projects, no Git/build/install effects from checkers; `markup_migrate --apply` keeps its parent-authenticated scope and proofs.
- Codex package behavior and its installed snapshot must keep working; Codex changes, if any, need their own justification.

## What to propose

Distinct architecture alternatives for WHERE the helpers, seeds and profile live and HOW the Claude package exposes them (skills, `bin/` commands, hooks, references), including how the five consumer projects' bare `orient`/`codemap` calls are served, how tests and membership oracles change, and how the two packages stay in sync. For each alternative give: essence/mechanism, the files/directories it adds or moves, dependency assumptions, at least two side effects (one negative), migration/rollback cost, and what it implies for future harness packages.

## Predeclared evaluation criteria (for the separate evaluator; generators may read them)

| Criterion | Weight | Direction |
|---|---|---|
| Single source of truth for helper code and seeds (no drift between packages) | 0.25 | higher better |
| Compatibility: in-place loading, neutral FORMAT/REPO-102, pinned algorithms and oracles, Codex snapshot keeps working | 0.25 | higher better |
| Consumer continuity: five projects' bare `orient`/`codemap` and session-start orientation keep working after the old plugins are disabled | 0.20 | higher better |
| Implementation and verification cost (files touched, tests, oracles, QA effort) | 0.15 | lower cost scores higher |
| Reversibility and future-harness extensibility | 0.15 | higher better |

Tie-breaker: lower implementation risk to the existing accepted Codex C2 package. Scores 1–10 for feasibility, impact and risk per alternative, with reasons and uncertainty.
