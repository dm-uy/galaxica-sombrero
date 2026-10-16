---
status: approved
proposed-at: 2026-10-16
approved-at: 2026-10-16
approval-mechanism: owner chat reply to the structured next-step question "Утверждаете спецификацию порта C2 с вариантом H?"
approval-quote: "Да, утверждаем H."
decision-packet: ../notes/m37-decision-c2-port/README.md
record: ../notes/m37-claude-parity.md
---

$START_DOC_M37_C2
# M37-C2 — consumer PM profile for the Claude package

**PURPOSE:** Give Claude Code users the C2 consumer PM capability (profile, seeds, orient, codemap, safe markup migration) from `methodology-claude`, so the owner can retire the in-house plugins project by project.
**SCOPE:** Claude package source, its tests and one root tripwire; Codex and neutral owners unchanged. Code starts only after the owner approves this specification.
**KEYWORDS:** consumer PM profile, in-place reference, launchers, tripwire, brownfield

$START_DOCUMENT_PLAN
**SECTION_SPEC:**
- GOAL Claude consumer PM parity without a second copy of the C2 code => M37C2_GOAL
- PRINCIPLE Mechanism H, exact scope, protected interfaces and measurable proof => M37C2_SPEC
$END_DOCUMENT_PLAN
$START_SECTION_SPEC
$START_ARTIFACT_M37C2_GOAL
**TYPE:** GOAL
**KEYWORDS:** parity, single source, consumer continuity
$START_CONTRACT
**PURPOSE:** A Claude Code session can adopt, orient, check, navigate and safely migrate a consumer project with the same C2 contracts Codex already ships.
**DESCRIPTION:** The Claude package references the accepted Codex C2 helpers and seeds in place inside the complete checkout and exposes them through Claude-native skills and `bin/` launchers.
**RATIONALE:** The C2 code is harness-neutral in content; one copy avoids drift (the two existing copied helpers already differ in their contract headers). The owner chose in-place loading, which guarantees the sibling Codex package is present.
**ACCEPTANCE_CRITERIA:** AC1–AC7 below on one current candidate.
$END_CONTRACT
$START_BODY
**Done when:** AC1–AC7 pass on one candidate after independent QA, whole Review and assigned Finalize, and the result is ready for the owner's integration decision.
**Stop and ask when:** a change outside MAY EDIT is needed; any Codex byte, neutral owner, FORMAT, registry, schema, role, run-state or SessionStart algorithm, `hooks.json` or the Workflow would change; a consumer project or user setting would be edited; the C2 helpers prove to need a Claude-specific code change; or required proof is unavailable.
$END_BODY
$START_LINKS
**IMPLEMENTS:** (none)
**IMPACTS:** M37C2_SPEC
**REQUIRES:** decision packet in [m37-decision-c2-port](../notes/m37-decision-c2-port/README.md)
$END_LINKS
$END_ARTIFACT_M37C2_GOAL
$START_ARTIFACT_M37C2_SPEC
**TYPE:** PRINCIPLE
**KEYWORDS:** BROWNFIELD, UI=false, in-place reference, BLOCKED launchers, tripwire
$START_CONTRACT
**PURPOSE:** Fix the mechanism, scope, protected interfaces and proofs of the port.
**DESCRIPTION:** Mechanism H of the decision packet: thin Claude carrier, skill routing, three launchers, a root tripwire, and an optional per-project SessionStart hook applied only under its own grant.
**RATIONALE:** Highest evaluated total (7.25 ± 0.5) with Codex untouched and the lowest file/QA cost; U1 (in-place `bin/` on PATH) was verified after evaluation. Runner-up M1 (byte-locked mirror) remains the fallback if the owner rejects a runtime dependency on the sibling package.
**ACCEPTANCE_CRITERIA:** AC1–AC7.
$END_CONTRACT
$START_BODY

## Context

Input: [M37 record](../notes/m37-claude-parity.md), [decision packet](../notes/m37-decision-c2-port/README.md), accepted [C2 specification](m28-c2-consumer-profile.md) and the Codex carrier `implementations/codex/references/consumer-pm-profile.md`. Baseline: branch `claude/m37-claude-parity` with Claude 2.0.2 (59 members, 28 skills, 4 helpers, 6 roles), Codex 3.0.1 (73 members) and neutral 3.0.1. BROWNFIELD: existing package behavior, oracles and pins are preserved except where listed.

Approving this specification is the owner's collapse of the decision packet to H. Rework names the change (for example M1). The decision record links this approval.

## Behavior

1. **Carrier.** New `implementations/claude/references/consumer-pm-profile.md` declares that the Claude package carries `methodology-consumer-pm/1.0.0` by reference. The full duty accounting (75 CV duties, 22 checklist rows), the 13 seeds, the command contracts and the held capacities live in the Codex carrier at `../codex/references/consumer-pm-profile.md`. The Claude carrier states only the Claude-native deltas:
   - invocation through the launchers or `python3 -B ${CLAUDE_PLUGIN_ROOT}/../codex/skills/pm/scripts/<cmd>.py`;
   - consent through AskUserQuestion;
   - explicit `model` on delegations;
   - no package hook;
   - the optional per-project hook recipe.
   It adds no duty and weakens none.
2. **Launchers.** Three new regular files `implementations/claude/bin/orient`, `bin/codemap` and `bin/markup-migrate` (layout kind `helper`), standard-library Python 3.9+. Each:
   - resolves its own real path, then the package root, then the sibling script `../codex/skills/pm/scripts/{orient,codemap,markup_migrate}.py`;
   - runs that script with the current interpreter and `-B`, passing every argument unchanged, with no current-directory default and no extra option;
   - returns the script's exit status.
   When the sibling script is missing or not a regular file inside the checkout, the launcher prints one `methodology-claude BLOCKED:` line naming the missing path to stderr and exits 2. It never searches another location. Full exoskeleton and LDD markup apply.
3. **Routing.** Mirror the profile-routing additions that Codex `bbd2696` made, in Claude form, pointing at the Claude carrier, the launchers and `../codex/skills/pm/templates/`:
   - `skills/pm`, `pm-bootstrap`, `pm-plan-batch`, `pm-run-batch`, `pm-handoff`;
   - `durable-layer`, `roadmap`, `document-protocol`, `greenfield-bootstrap`;
   - `semantic-exoskeleton`;
   - `agents/searcher.md` (owned codemap navigation).
   `pm-bootstrap` seeds from the 13 Codex templates under the profile instead of the five neutral forms when the profile is adopted. It keeps the neutral-form route for projects that do not adopt the profile.
4. **Optional per-project hook.** The carrier documents, and `pm-bootstrap` offers only under an explicit per-project grant, a machine-local `.claude/settings.local.json` SessionStart command that runs the absolute `orient` launcher on `$CLAUDE_PROJECT_DIR` and never fails the session. Nothing in this repository installs it.
5. **Tripwire.** New root test `tests/test_claude_consumer_bridge.py` pins the SHA-256 of the 18 Codex files Claude depends on: four scripts, 13 templates and the Codex carrier. A Codex change therefore fails until a reviewer re-pins it with a reason. The test also discriminates a one-byte mutation in an owned copy, naming the path.
6. **Release.** Claude 2.0.2 → 2.1.0. Members 59 → 64:
   - three launchers;
   - the carrier;
   - the new package test module `tests/test_consumer_profile.py`.
   Layout, the independent root oracle (`tests/test_claude_package.py`, expected list now taken from this specification) and the package contract counts move together. `run_state.py` and `session_start.py` change only `PACKAGE_VERSION`, and the C1 selectors follow.

## Business requirements

- **BR-1 CODEX:** Every byte under `implementations/codex/` stays identical to the baseline.
- **BR-2 NEUTRAL:** Neutral owners, FORMAT, registries, schema, six roles, wire and the root README Local use section are unchanged.
- **BR-3 CLAUDE PROTECTED:** The following are unchanged:
  - `hooks/hooks.json` (one SessionStart and one PreToolUse entry) and `hooks/guard_destructive.py`;
  - `workflows/feature-dev.js`;
  - the algorithms of `run_state.py` and the AST of `session_start.py`, except their version constant;
  - all existing assertions and negative controls, except the exact version, membership and count facts this specification changes.
- **BR-4 LAUNCHER CONTRACT:** Arguments pass through unchanged, the exit status passes through unchanged, and a missing sibling is BLOCKED with exit 2. There is no fallback to an installed or other copy, and no cwd default.
- **BR-5 NO CONSUMER EFFECT:** No consumer project, user setting, plugin configuration or global PATH is changed. Per-project migration and hook installation are later owner-granted tasks.
- **BR-6 COMPATIBILITY:** The launchers work under the system Python 3.9 and under the declared Python 3.12.

## Exact scope

MAY EDIT (create or modify):
- `implementations/claude/bin/{orient,codemap,markup-migrate}`;
- `implementations/claude/references/{consumer-pm-profile.md,package-layout.json,claude-runtime.md,adoption.md,handoffs.md,source-disposition.md}`;
- `implementations/claude/skills/{pm,pm-bootstrap,pm-plan-batch,pm-run-batch,pm-handoff,durable-layer,roadmap,document-protocol,greenfield-bootstrap,semantic-exoskeleton,devplan-protocol}/SKILL.md`;
- `implementations/claude/agents/searcher.md`;
- `implementations/claude/{README.md,.claude-plugin/plugin.json,Doxyfile}`;
- `implementations/claude/hooks/session_start.py` and `implementations/claude/skills/feature-dev/scripts/run_state.py` (version constant only);
- `implementations/claude/tests/{test_consumer_profile.py,test_package_contract.py,test_session_start.py,test_run_state.py,test_guide.md}` (new module, plus exact version and membership facts in the existing ones);
- root `tests/{test_claude_consumer_bridge.py,test_claude_package.py,test_c1_review_and_routing.py}` (new tripwire, membership list and version selectors);
- root `README.md` version line and `CHANGELOG.md`;
- the plan, run evidence and the maintainer records under `examples/pm-project/`.

DO NOT TOUCH:
- everything else, in particular `implementations/codex/**`, the neutral subjects, `bin/`, `tools/`, `runtime/`, `FORMAT.md` and `SPEC_VERSION`;
- `implementations/claude/hooks/hooks.json`, `implementations/claude/hooks/guard_destructive.py` and `implementations/claude/workflows/**`;
- the other skills and agents, `examples/flow-contract/**`;
- consumer projects, user and plugin settings.

## Acceptance criteria

- **AC1 CARRIER:** An independent review confirms:
  - the Claude carrier adds no duty and removes none relative to the Codex carrier and the neutral owners;
  - every reference resolves;
  - the deltas listed in Behavior 1 are the only differences.
- **AC2 LAUNCHERS:** Owned process-boundary tests on synthetic fixtures run each real launcher as a subprocess:
  - `orient PROJECT` and `orient PROJECT --check` on an adopted fixture: clean case exit 0, a defective case reports its row and non-zero;
  - `orient --portfolio` with explicit roots;
  - `codemap PROJECT TARGET` on a built fixture map;
  - `markup-migrate PROJECT --check`.
  Output and exit equal a direct `python3 -B` call of the Codex script with the same arguments. A missing sibling in an owned copy gives exit 2 and the BLOCKED line, and nothing else runs. A symlink to a launcher still resolves the real package. All of this runs on Python 3.9 and 3.12.
- **AC3 TRIPWIRE:** The root test passes on the baseline Codex bytes. It fails, naming the path, for a one-byte change in each of a script, a template and the carrier in owned copies.
- **AC4 ROUTING:** The package contract test asserts that the routed skills name the carrier and the launchers, and that every `${CLAUDE_PLUGIN_ROOT}` reference, including the `../codex/` ones, resolves.
- **AC5 LIVE:** A fresh headless Claude session is run with the M37 probe argv, Bash allowed only for the launchers, and the candidate copy loaded in place.
  - Under an explicit fixture grant on a fictional new project, it adopts the profile through `pm-bootstrap`: it materializes only granted seeds from the Codex templates, declares the profile, runs bare `orient --check` on the project and reports the actual rows.
  - An existing-project control keeps original files and links and refuses an ungranted overwrite.
  - Streams and before/after trees are retained.
- **AC6 REGRESSION:** The following all pass, with `implementations/codex/**` byte-identical to the baseline:
  - full root, Claude package and Codex package suites on `/opt/homebrew/bin/python3.12`;
  - the three adapters;
  - `bin/conform self` with a public-hygiene deny list;
  - `claude plugin validate`, with only the name warning;
  - silent Doxygen builds for root and the Claude package, with the new Python entities in XML.
- **AC7 FLOW:** feature-dev runs with:
  - independent QA covering all eight scans;
  - whole Review;
  - separately assigned Finalize.
  The result note and current records are reconciled afterwards. Integration remains the owner's separate decision.

## Follow-ups outside this slice

- Migrate each of the five consumer projects to the profile under its own owner grant (CONVENTIONS profile, AGENTS orient line, CLAUDE.md lines that claim plugin injection). Then disable the in-house plugins in the owner's settings.
- `pm-ingest-candidates` and `run_review.py` stay deferred by their earlier decision.

$END_BODY
$START_LINKS
**IMPLEMENTS:** M37C2_GOAL
**IMPACTS:** (none)
**REQUIRES:** decision packet in [m37-decision-c2-port](../notes/m37-decision-c2-port/README.md)
$END_LINKS
$END_ARTIFACT_M37C2_SPEC
$END_SECTION_SPEC
$END_DOC_M37_C2
