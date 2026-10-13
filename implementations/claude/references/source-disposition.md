# Source disposition — methodology-claude 1.0.0

This table describes Claude-native technical duties under neutral labels S1–S8. Private source reconnaissance, exact locators and byte identities are unavailable in this public tree. The labels do not assert a complete source transfer. Every rule the package applies comes from current neutral owners; older variants do not become competing rules. Native mechanics and wording are reconciled as detailed below.

Dispositions: **adapted** (reworked into a package member under the current neutral contracts), **superseded** (the duty is carried by a neutral owner or another member; the source is not copied), **outside** (not part of the methodology package; stays in its own home), **omitted** (deliberately not carried, with the reason).

## Source to package

| Source | Item | Disposition | Package member or reason |
|---|---|---|---|
| S1 | Five role agents (architect, coder, debugger, qa, searcher) | adapted | `agents/*.md`: frontmatter mechanics (model, tools) kept; duties re-sourced from `roles/*.md`; old five-scan QA, root-only Finalize and missing Review replaced by the current owners. A sixth carrier, `reviewer`, is new. |
| S1 | Exoskeleton constitution (global rule) | superseded | `concepts/principles.md`, `code/exoskeleton.md`, `code/ldd.md`, `code/doxygen.md`, `code/tests.md`, `code/navigation.md` via `skills/semantic-exoskeleton`; Claude Code plugins cannot ship global rules, so the SessionStart hook and every carrier carry the reading duty. |
| S1 | Subagent model-tier rule | superseded | `policies/models.md`; tiers bound in `adapter.json` parameters and carrier frontmatter. |
| S1 | Protocol skills ax-ui-contract, brownfield-spec-template, data-transform, devplan-protocol, document-protocol, graph-protocol | adapted | Same-named `skills/*/SKILL.md` entries pointing at `code/ax-ui.md`, `protocols/spec-brownfield.md`, `code/data.md`, `protocols/dev-plan.md`, `protocols/document.md`, `protocols/graph.md`. |
| S1 | Decision-protocol skill and its decision-record lint | superseded / omitted | Duty carried by `process/decisions.md` through `skills/brainstorm`; the lint script has no tests and its skeleton differs from the neutral decision profiles. |
| S1 | Visual-gate lint v1.0 | superseded | `skills/devplan-protocol/scripts/visual_gate_lint.py`, taken from the tested Codex package helper. |
| S1 | Workflow spine feature-dev | adapted | `workflows/feature-dev.js`: Workflow API usage, schemas and null guard kept; phase set, eight named scans, Review, separately assigned Finalize, cumulative Debug cap with 0 valid and the recorder step follow the current owners. |
| S2 | PM skills pm-bootstrap, pm-plan-batch, pm-run-batch, pm-handoff, pm-review-run | adapted | Same-named owner-invoked commands under `skills/`, pointing at `process/bootstrap.md`, `process/batch.md`, `process/session.md`, `checks/run-audit.md` and their neighbours. |
| S2 | PM skill pm-ingest-candidates and the candidates ledger | omitted | Systematic learning is owner-deferred (M13); lightweight error recording in project notes remains the practice. |
| S2 | SessionStart orientation script | superseded | `hooks/session_start.py` (new, binding check and record presence); the full Orient assessment is the root's duty under `checks/orient.md`. |
| S2 | PreToolUse destructive-command guard | adapted | `hooks/guard_destructive.py`: decision rules and precision kept; active whenever the package is loaded; read-only agent types extended to the package judges. |
| S2 | Project conventions, manifest, document templates | superseded | `documents/conventions.md`, `documents/templates/*` and `process/*`. |
| S2 | Code-map query, markup migration, run-review scripts | outside | Useful tools with their own tests, not needed to bind the methodology; candidates for a later package increment by separate decision. |
| S3 | Prompting skills and commands (agent-prompt, brainstorm, contract, design, verify-fact, methodology router) | superseded | `prompting/*.md` through `skills/prompting*`, `skills/brainstorm` and `skills/semantic-exoskeleton`. |
| S3 | Brainstorm and architect ensemble agents | superseded | `prompting/brainstorm.md`, `prompting/superposition-collapse.md`; the root dispatches a role or a general subagent when a fork needs independent hypotheses. |
| S3 | Book-derived prompting knowledge graph | omitted | Not authored by the project; the neutral prompting owners are re-authored independently. |
| S4 | Newer twin of S1 (six scans, in-spine visual gate, install scripts, runbook) | superseded | Same as S1; its in-spine visual gate informed `workflows/feature-dev.js`. Install scripts are replaced by in-place loading. The runbook is owner-specific. |
| S4 | Twin for another engine and the original donor copy | outside | Belongs to another harness, not to the Claude package. |
| S5 | brainstorm, roadmap, graph-protocol | superseded | `skills/brainstorm`, `skills/roadmap`, `skills/graph-protocol` with neutral owners. |
| S5 | Git and tracker flow, OKF toolkit, repository triage, anatomy and pathology audits, intake audit | outside | General-purpose tools; OKF is the external knowledge layer that the neutral capability registry places outside this repository. |
| S6 | Experience recall and record | outside | Cross-project memory outside the repository (`cap:memory`); not activated by this package. |
| S7 | Launchers for another engine | outside | Another harness. |
| S8 | Owner working defaults and the personal memory hook | outside | User-level preferences remain the owner's; the package changes no user configuration. |

## Package to source (converse)

| Package member | Origin |
|---|---|
| `.claude-plugin/plugin.json`, `README.md`, `adapter.json`, `references/*` | New, modelled on the Codex package structure. |
| `agents/*.md` | S1/S4 mechanics, neutral role owners. |
| `skills/*/SKILL.md` (23 parity topics) | Codex package topic set and owners; S1, S3, S5 triggers. |
| `skills/pm-*/SKILL.md` (5) | S2 command set; neutral process owners. |
| `skills/feature-dev/scripts/run_state.py` | Codex package helper: the schema-2 run-state contract is shared; the package identity is this package's, and the candidate inventory now follows git's ignore rules with a declared fallback (M22 Debug entries 2 and 3), with package-specific behavior and tests retained. The Codex helper also has Gitignore-aware inventory after M25A; see Known limits. |
| `skills/devplan-protocol/scripts/visual_gate_lint.py` | Codex package helper. |
| `hooks/hooks.json`, `hooks/session_start.py` | New. |
| `hooks/guard_destructive.py` | S2 guard, adapted. |
| `workflows/feature-dev.js` | S1/S4 spine, adapted. |
| `tests/*`, `Doxyfile`, `pytest.ini`, `examples/smoke-spec.md` | New for this package; the run-state, visual-gate and guard tests port their sources' cases. |

## Known limits

The run-state helpers share the state contract but are not asserted to behave identically. Both have Gitignore-aware candidate inventory. M25A Codex source uses tracked-priority cached/nonignored-other enumeration at a confirmed Git top-level, a declared nonGit/subdirectory/unavailableGit fallback, and refusal on confirmed unusable enumeration. Its coupled inventory/baseline observation clears inherited GIT_* steering and disables optional locks/fsmonitor; this bounded protection does not claim every repository program is disabled. Claude retains its own fallback and tests. Byte equality proves only bytes; private source origin and acceptance evidence is unavailable here and no complete-transfer claim follows. The Codex-derived helpers duplicate code between the two packages; extracting a shared helper is a separate decision because it changes the Codex package.
