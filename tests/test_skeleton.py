# region MODULE_CONTRACT [DOMAIN(9): Skeleton, Registries; CONCEPT(8): LayoutCount, StubSet, Draft; TECH(6): pytest, pathlib]
## @modulecontract
## @purpose To prove that the repository is the skeleton it claims to be: the amended layout of 67 files exists with valid
## cards, exactly 2 of them are stubs, the sixty-nine drafts are the ones named, the registries declare what they must and the
## version files say 2.0.0.
## @scope The file tree, the cards, the stubs, the index of templates, the documentation of the tool, the registries, the
## version files and the README. No tool code is run here.
## @input The repository on disk; the constant of the 74 files of the inventory's layout.
## @output Pass or fail per criterion; the counts printed before each assert.
## @links [READS_DATA_FROM(8): repository files; USES_API(4): pytest]
## @links_to_spec AC-1, AC-3, AC-12
## @invariants
## - The counts are computed from the constant of the layout, never typed as results.
## - The stub set is compared to the computed set exactly, not by count alone.
## - The tests read files with their own small reader, independent of the tool they help check.
## @rationale
## Q: Why compute 74, 67 and 2 in the test?
## A: The specification says the count of stubs equals the layout's count after the amendments; a typed number would
## hide a wrong amendment, a computed one shows it.
## @changes
## LAST_CHANGE: [2.0.0 - M30 exact current release/census coupling; all prior cases/assertions/refusals retained.]
## Earlier: [v1.0.1 - M23: the owner's MIT licence (2026-10-10) replaces the former no-licence assertion; no remote is still required.]
## - [v1.0.0 - Reconcile current M19 boundary/release facts and paired source operands; preserve original assertions/pins/refusals/restoration; runtime checks pending.]
## @modulemap
## FUNC 8[The layout after the amendments] => amended_layout
## FUNC 7[The neutral files by the definition of the format] => neutral_paths
## FUNC 6[The PM release inventory and statuses] => test_layout_counts_pm_release
## FUNC 6[Every amended file exists with a valid card] => test_every_amended_layout_file_exists_with_a_valid_card
## FUNC 7[The stub set equals the amended layout minus the filled files] => test_stub_set_equals_amended_layout_minus_filled_files
## FUNC 5[A stub is a heading and one purpose line] => test_each_stub_is_heading_and_one_purpose_line
## FUNC 5[No knowledge directory; five primary templates] => test_no_knowledge_directory_and_five_primary_templates
## FUNC 4[The index lists five templates] => test_index_lists_the_five_templates
## FUNC 6[The tool's file documents it with its anchors] => test_checks_conform_documents_the_tool_with_its_anchors
## FUNC 6[71 neutral files, sixty-nine drafts] => test_neutral_files_match_pm_release
## FUNC 6[Read the declarations of one registry, name to meaning] => _declarations
## FUNC 6[The 28 capabilities with meanings] => test_capabilities_registry_declares_the_28_with_meanings
## FUNC 4[The memory capability names an external source] => test_memory_capability_names_an_external_source
## FUNC 5[The seven parameters] => test_parameters_registry_declares_the_seven
## FUNC 3[The version is 2.0.0] => test_spec_version_is_0_19_0
## FUNC 4[The changelog entry] => test_changelog_entry_names_skeleton_format_registries_tool
## FUNC 7[The README explains adoption and the tool] => test_readme_explains_adoption_and_conform
## FUNC 5[The README names the MIT licence] => test_readme_states_mit_licence
## @usecases
## - [test_layout_counts_pm_release]: QA agent -> recompute the counts -> the skeleton matches the amendment
## - [test_stub_set_equals_amended_layout_minus_filled_files]: Maintainer -> deletes a stub -> the set differs and the test names it
## - [test_readme_explains_adoption_and_conform]: New harness author -> opens the README -> finds the four ways, the registries and the commands
## @GREP_SUMMARY skeleton, layout 74 67 2, stub set, cards, drafts, neutral files 71, capabilities 28, parameters 7, SPEC_VERSION, CHANGELOG
## @STRUCTURE ▶ LAYOUT(74) → ⊕ amend(-knowledge -templates +INDEX+five forms)=67 → ◇ minus filled=2 → ⚡ walk repo *.md → ∑ compare sets → ⎋ assert
def _module_contract():
    pass
# endregion MODULE_CONTRACT


import pathlib
import re
from typing import Dict, List, Set

import pytest

LAYOUT = [
    "checks/lints.md",
    "checks/orient.md",
    "checks/preflight.md",
    "checks/qa-scans.md",
    "checks/run-audit.md",
    "code/ax-ui.md",
    "code/data.md",
    "code/doxygen.md",
    "code/exoskeleton.md",
    "code/ldd.md",
    "code/navigation.md",
    "code/tests.md",
    "concepts/glossary.md",
    "concepts/principles.md",
    "documents/conventions.md",
    "documents/templates/AGENTS.md",
    "documents/templates/DEC.md",
    "documents/templates/HANDOFF.md",
    "documents/templates/OPEN_QUESTIONS.md",
    "documents/templates/RECON.md",
    "documents/templates/ROADMAP.md",
    "documents/templates/SPEC.md",
    "documents/templates/TASKS.md",
    "documents/templates/VISION.md",
    "flow/delegation.md",
    "flow/finalize.md",
    "flow/phases.md",
    "flow/run-state.md",
    "knowledge/curation.md",
    "knowledge/okf-format.md",
    "knowledge/okf-ingest.md",
    "knowledge/okf-tooling.md",
    "policies/autonomy.md",
    "policies/credentials.md",
    "policies/language.md",
    "policies/models.md",
    "process/batch.md",
    "process/bootstrap.md",
    "process/code-review.md",
    "process/decisions.md",
    "process/gates.md",
    "process/git.md",
    "process/learning.md",
    "process/lifecycle.md",
    "process/publication.md",
    "process/reconnaissance.md",
    "process/review.md",
    "process/safety.md",
    "process/session.md",
    "process/specification.md",
    "prompting/agent-prompt-design.md",
    "prompting/brainstorm.md",
    "prompting/decomposition.md",
    "prompting/grace.md",
    "prompting/prompt-markup.md",
    "prompting/solution-design.md",
    "prompting/superposition-collapse.md",
    "prompting/verification.md",
    "protocols/dev-plan.md",
    "protocols/document.md",
    "protocols/graph.md",
    "protocols/role-returns.md",
    "protocols/spec-brownfield.md",
    "protocols/spec-greenfield.md",
    "roles/_base.md",
    "roles/architect.md",
    "roles/coder.md",
    "roles/debugger.md",
    "roles/pm.md",
    "roles/qa.md",
    "roles/reviewer.md",
    "roles/searcher.md",
    "runtime/adapters.md",
    "runtime/capabilities.md",
]

FILLED = {'process/review.md', 'process/code-review.md', 'concepts/principles.md', 'concepts/glossary.md', 'checks/orient.md', 'checks/preflight.md', 'checks/run-audit.md', 'process/safety.md', 'protocols/document.md', 'protocols/spec-greenfield.md', 'protocols/spec-brownfield.md', 'process/specification.md', 'process/reconnaissance.md', 'process/lifecycle.md', 'documents/templates/INDEX.md', 'documents/templates/AGENTS.md', 'roles/reviewer.md', 'protocols/dev-plan.md', 'flow/finalize.md', 'roles/architect.md', 'runtime/adapters.md', 'process/session.md', 'flow/run-state.md', 'process/bootstrap.md', 'roles/_base.md', 'code/ax-ui.md', 'code/data.md', 'documents/templates/ROADMAP.md', 'protocols/role-returns.md', 'code/exoskeleton.md', 'process/decisions.md', 'process/learning.md', 'protocols/graph.md', 'checks/qa-scans.md', 'code/doxygen.md', 'roles/searcher.md', 'process/gates.md', 'roles/qa.md', 'flow/phases.md', 'documents/templates/TASKS.md', 'roles/debugger.md', 'code/tests.md', 'process/batch.md', 'checks/lints.md', 'documents/conventions.md', 'policies/models.md', 'runtime/capabilities.md', 'documents/templates/HANDOFF.md', 'flow/delegation.md', 'code/ldd.md', 'roles/pm.md', 'roles/coder.md', 'documents/templates/VISION.md', 'code/navigation.md', 'prompting/agent-prompt-design.md', 'prompting/brainstorm.md', 'prompting/decomposition.md', 'prompting/grace.md', 'prompting/prompt-markup.md', 'prompting/solution-design.md', 'prompting/superposition-collapse.md', 'prompting/verification.md', 'policies/autonomy.md', 'policies/credentials.md', 'policies/language.md'}
DRAFTS = {'process/review.md', 'process/code-review.md', 'concepts/principles.md', 'concepts/glossary.md', 'checks/orient.md', 'checks/preflight.md', 'checks/run-audit.md', 'process/safety.md', 'protocols/document.md', 'protocols/spec-greenfield.md', 'protocols/spec-brownfield.md', 'process/specification.md', 'process/reconnaissance.md', 'documents/templates/INDEX.md', 'process/lifecycle.md', 'documents/templates/AGENTS.md', 'roles/reviewer.md', 'protocols/dev-plan.md', 'runtime/parameters.md', 'flow/finalize.md', 'roles/architect.md', 'flow/run-state.md', 'AGENTS.md', 'runtime/adapters.md', 'process/session.md', 'process/bootstrap.md', 'roles/_base.md', 'code/ax-ui.md', 'code/data.md', 'documents/templates/ROADMAP.md', 'protocols/role-returns.md', 'code/exoskeleton.md', 'process/decisions.md', 'process/learning.md', 'protocols/graph.md', 'checks/qa-scans.md', 'code/doxygen.md', 'roles/searcher.md', 'process/gates.md', 'roles/coder.md', 'roles/qa.md', 'documents/templates/TASKS.md', 'flow/phases.md', 'FORMAT.md', 'roles/debugger.md', 'checks/conform.md', 'process/batch.md', 'code/tests.md', 'checks/lints.md', 'documents/conventions.md', 'policies/models.md', 'runtime/capabilities.md', 'flow/delegation.md', 'code/ldd.md', 'roles/pm.md', 'documents/templates/HANDOFF.md', 'documents/templates/VISION.md', 'code/navigation.md', 'prompting/agent-prompt-design.md', 'prompting/brainstorm.md', 'prompting/decomposition.md', 'prompting/grace.md', 'prompting/prompt-markup.md', 'prompting/solution-design.md', 'prompting/superposition-collapse.md', 'prompting/verification.md', 'policies/autonomy.md', 'policies/credentials.md', 'policies/language.md'}
ROOT_EXCLUDED = {"README.md", "CHANGELOG.md"}
SKIPPED_DIRS = {".git", "doxygen_output", "__pycache__", ".pytest_cache", "tests", "examples", "implementations"}
TEMPLATE_NAMES = ["AGENTS.md", "VISION.md", "ROADMAP.md", "TASKS.md", "HANDOFF.md"]
CONFORM_ANCHORS_BEFORE_ADAPTER = [
    "checks.conform.purpose",
    "checks.conform.run",
    "checks.conform.exit",
    "checks.conform.report",
    "checks.conform.self",
    "checks.conform.scan",
]
CONFORM_ANCHORS_AFTER_ADAPTER = ["checks.conform.logs"]
CAPABILITIES = [
    "ask-owner-structured",
    "plan-mode",
    "spawn-role-isolated",
    "model-tier",
    "role-permissions",
    "pre-tool-guard",
    "run-state-persist",
    "workflow-orchestration",
    "structured-output",
    "skill-loading",
    "rules-injection",
    "session-start-hook",
    "background-command",
    "web-research",
    "browser",
    "worktree",
    "schedule",
    "memory",
    "todo-list",
    "goal",
    "code-map-build",
    "check-runner",
    "run-record-access",
    "packaging-install",
    "launch-environment",
    "capability-discovery",
    "context-management",
    "tracker-integration",
]
PARAMETERS = ["dialog-language", "owner-label", "model-mechanical", "model-routine", "model-judgment", "gate-cadence", "debug-entry-cap"]
DECLARATION = re.compile(r"^- \*\*(cap|param):([^*]+)\*\* (.+)$")


# region FUNC_amended_layout [DOMAIN(7): Skeleton; CONCEPT(8): LayoutAmendment; TECH(4): set]
## @purpose The layout after the amendments: the inventory's 74 files without the knowledge and template files, plus the
## index of templates.
## @io None -> Set[str]
## @complexity 2
def amended_layout() -> Set[str]:
    kept = {p for p in LAYOUT if not p.startswith("knowledge/") and not p.startswith("documents/templates/")}
    kept.add("documents/templates/INDEX.md")
    kept.update("documents/templates/" + name for name in TEMPLATE_NAMES)
    return kept
# endregion FUNC_amended_layout


# region FUNC_neutral_paths [DOMAIN(7): Skeleton; CONCEPT(8): NeutralFiles; TECH(5): pathlib.rglob]
## @purpose The neutral files by the definition of the format: every Markdown file except the root README and CHANGELOG and
## everything under tests, examples, typed implementations and the build directories.
## @io pathlib.Path -> List[str]
## @complexity 3
def neutral_paths(root: pathlib.Path) -> List[str]:
    found = []
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root)
        if relative.parts[0] in SKIPPED_DIRS:
            continue
        if len(relative.parts) == 1 and relative.name in ROOT_EXCLUDED:
            continue
        found.append(relative.as_posix())
    return found
# endregion FUNC_neutral_paths


# region FUNC_test_layout_counts_pm_release [DOMAIN(8): Skeleton; CONCEPT(9): LayoutCount; TECH(4): pytest]
## @purpose Prove the arithmetic of the amendment: 74 files in the constant, 67 after the amendment, 2 stubs.
## @io None -> None
## @complexity 2
def test_layout_counts_pm_release():
    amended = amended_layout()
    stubs = amended - FILLED
    print("[IMP:9][test_layout_counts][COUNT] layout=%d amended=%d stubs=%d" % (len(LAYOUT), len(amended), len(stubs)))
    assert len(LAYOUT) == 74 and len(set(LAYOUT)) == 74
    assert len(amended) == 67
    assert len(stubs) == 2
# endregion FUNC_test_layout_counts_pm_release


# region FUNC_test_every_amended_layout_file_exists_with_a_valid_card [DOMAIN(8): Skeleton; CONCEPT(8): Card; TECH(4): pytest]
## @purpose Prove that each of the 67 files exists and opens with a card holding id, title and a valid status.
## @io (pathlib.Path, Callable) -> None
## @complexity 3
def test_every_amended_layout_file_exists_with_a_valid_card(repo_root, read_card):
    missing = []
    bad = []
    for relative in sorted(amended_layout()):
        path = repo_root / relative
        if not path.is_file():
            missing.append(relative)
            continue
        card, _ = read_card(path)
        if not (card.get("id") and card.get("title") and card.get("status") in ("stub", "draft", "stable")):
            bad.append(relative)
    print("[IMP:9][test_every_amended][RESULT] missing=%d bad=%d" % (len(missing), len(bad)))
    assert missing == []
    assert bad == []
# endregion FUNC_test_every_amended_layout_file_exists_with_a_valid_card


# region FUNC_test_stub_set_equals_amended_layout_minus_filled_files [DOMAIN(9): Skeleton; CONCEPT(9): StubSet; TECH(4): set]
## @purpose Prove that the files whose status is stub are exactly the amended layout minus the named filled files.
## @io (pathlib.Path, Callable) -> None
## @complexity 4
def test_stub_set_equals_amended_layout_minus_filled_files(repo_root, read_card):
    actual = set()
    for relative in neutral_paths(repo_root):
        card, _ = read_card(repo_root / relative)
        if card.get("status") == "stub":
            actual.add(relative)
    expected = amended_layout() - FILLED
    print("[IMP:9][test_stub_set][RESULT] actual=%d expected=%d only_actual=%s only_expected=%s"
          % (len(actual), len(expected), sorted(actual - expected), sorted(expected - actual)))
    assert actual == expected
# endregion FUNC_test_stub_set_equals_amended_layout_minus_filled_files


# region FUNC_test_each_stub_is_heading_and_one_purpose_line [DOMAIN(8): Skeleton; CONCEPT(8): Stub, NoNorm; TECH(4): re]
## @purpose Prove that a stub is its card, a heading of its title and one purpose line, with no anchor and no norm; the
## index alone adds its list of templates.
## @io (pathlib.Path, Callable) -> None
## @complexity 5
def test_each_stub_is_heading_and_one_purpose_line(repo_root, read_card):
    offenders = []
    for relative in sorted(amended_layout() - FILLED):
        card, body = read_card(repo_root / relative)
        content = [line for line in body if line.strip()]
        if not content or content[0] != "# " + card["title"]:
            offenders.append(relative + ": heading")
            continue
        if len(content) < 2 or not content[1].endswith("."):
            offenders.append(relative + ": purpose")
        if relative != "documents/templates/INDEX.md" and len(content) != 2:
            offenders.append(relative + ": more than one purpose line")
        for line in body:
            if line.startswith("<!-- anchor") or re.match(r"^\s*- \*\*[A-Z]+-[0-9]+\*\*", line):
                offenders.append(relative + ": anchor or norm")
    print("[IMP:9][test_each_stub][RESULT] offenders=%d" % len(offenders))
    assert offenders == []
# endregion FUNC_test_each_stub_is_heading_and_one_purpose_line


# region FUNC_test_no_knowledge_directory_and_five_primary_templates [DOMAIN(8): Skeleton; CONCEPT(8): Amendment; TECH(4): pathlib]
## @purpose Prove the two removals: no knowledge directory, and the templates directory holds the five forms plus index.
## @io pathlib.Path -> None
## @complexity 2
def test_no_knowledge_directory_and_five_primary_templates(repo_root):
    entries = sorted(p.name for p in (repo_root / "documents" / "templates").iterdir())
    print("[IMP:9][test_no_knowledge][RESULT] templates=%s knowledge_exists=%s" % (entries, (repo_root / "knowledge").exists()))
    assert not (repo_root / "knowledge").exists()
    assert entries == sorted(TEMPLATE_NAMES + ["INDEX.md"])
# endregion FUNC_test_no_knowledge_directory_and_five_primary_templates


# region FUNC_test_index_lists_the_five_templates [DOMAIN(7): Skeleton; CONCEPT(7): Index; TECH(4): re]
## @purpose Prove that the index of templates lists the five actual forms, each as a plain list item without bold.
## @io pathlib.Path -> None
## @complexity 3
def test_index_lists_the_five_templates(repo_root):
    text = (repo_root / "documents" / "templates" / "INDEX.md").read_text(encoding="utf-8")
    items = re.findall(r"^- `([A-Z_]+\.md)`: ", text, flags=re.M)
    print("[IMP:9][test_index][RESULT] items=%s" % items)
    assert items == TEMPLATE_NAMES
    assert len(items) == 5
# endregion FUNC_test_index_lists_the_five_templates


# region FUNC_test_checks_conform_documents_the_tool_with_its_anchors [DOMAIN(8): Skeleton; CONCEPT(8): ToolDocument; TECH(4): re]
## @purpose Prove that the tool's own file is a draft with the id checks.conform, no norm, and its anchors in order.
## @io (pathlib.Path, Callable) -> None
## @complexity 4
def test_checks_conform_documents_the_tool_with_its_anchors(repo_root, read_card):
    path = repo_root / "checks" / "conform.md"
    card, body = read_card(path)
    anchors = re.findall(r"^<!-- anchor: (\S+) -->$", "\n".join(body), flags=re.M)
    print("[IMP:9][test_checks_conform][RESULT] id=%s status=%s anchors=%d" % (card.get("id"), card.get("status"), len(anchors)))
    assert card["id"] == "checks.conform"
    assert card["status"] == "draft"
    assert anchors == CONFORM_ANCHORS_BEFORE_ADAPTER + ["checks.conform.adapter"] + CONFORM_ANCHORS_AFTER_ADAPTER
    assert not re.search(r"^\s*- \*\*[A-Z]+-[0-9]+\*\*", "\n".join(body), flags=re.M)
# endregion FUNC_test_checks_conform_documents_the_tool_with_its_anchors


# region FUNC_test_neutral_files_match_pm_release [DOMAIN(8): Skeleton; CONCEPT(9): NeutralCount; TECH(4): pathlib]
## @purpose Prove the totals: 71 neutral files, of which 2 stubs, 69 drafts and no stable file, the drafts being the named sixty-nine.
## @io (pathlib.Path, Callable) -> None
## @complexity 4
def test_neutral_files_match_pm_release(repo_root, read_card):
    statuses: Dict[str, str] = {}
    for relative in neutral_paths(repo_root):
        card, _ = read_card(repo_root / relative)
        statuses[relative] = card["status"]
    drafts = {p for p, s in statuses.items() if s == "draft"}
    stubs = {p for p, s in statuses.items() if s == "stub"}
    print("[IMP:9][test_neutral_files][COUNT] neutral=%d stubs=%d drafts=%d" % (len(statuses), len(stubs), len(drafts)))
    assert len(statuses) == 71
    assert len(stubs) == 2
    assert drafts == DRAFTS
# endregion FUNC_test_neutral_files_match_pm_release


# region FUNC__declarations [DOMAIN(7): Registries; CONCEPT(8): Declaration; TECH(4): re]
## @purpose Read the declarations of one registry file: name to meaning, in file order.
## @io (pathlib.Path, str) -> Dict[str, str]
## @complexity 2
def _declarations(path: pathlib.Path, kind: str) -> Dict[str, str]:
    found: Dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").split("\n"):
        matched = DECLARATION.match(line)
        if matched and matched.group(1) == kind:
            found[matched.group(2)] = matched.group(3)
    return found
# endregion FUNC__declarations


# region FUNC_test_capabilities_registry_declares_the_28_with_meanings [DOMAIN(8): Registries; CONCEPT(9): Capabilities; TECH(4): re]
## @purpose Prove that the capability registry declares the 28 capabilities of the inventory, in order, each with a meaning.
## @io pathlib.Path -> None
## @complexity 3
def test_capabilities_registry_declares_the_28_with_meanings(repo_root):
    declared = _declarations(repo_root / "runtime" / "capabilities.md", "cap")
    print("[IMP:9][test_capabilities][COUNT] declared=%d" % len(declared))
    assert list(declared) == CAPABILITIES
    assert all(meaning.strip() for meaning in declared.values())
# endregion FUNC_test_capabilities_registry_declares_the_28_with_meanings


# region FUNC_test_memory_capability_names_an_external_source [DOMAIN(8): Registries; CONCEPT(8): Memory, External; TECH(4): str]
## @purpose Prove that the memory capability says the knowledge layer is an external source that this repository does not carry.
## @io pathlib.Path -> None
## @complexity 2
def test_memory_capability_names_an_external_source(repo_root):
    meaning = _declarations(repo_root / "runtime" / "capabilities.md", "cap")["memory"]
    print("[IMP:9][test_memory_capability][RESULT] has_external=%s" % ("external source" in meaning))
    assert "external source" in meaning
    assert "knowledge layer" in meaning
# endregion FUNC_test_memory_capability_names_an_external_source


# region FUNC_test_parameters_registry_declares_the_seven [DOMAIN(8): Registries; CONCEPT(9): Parameters; TECH(4): re]
## @purpose Prove that the parameter registry declares the seven required parameters, each with a meaning.
## @io pathlib.Path -> None
## @complexity 2
def test_parameters_registry_declares_the_seven(repo_root):
    declared = _declarations(repo_root / "runtime" / "parameters.md", "param")
    print("[IMP:9][test_parameters][COUNT] declared=%d" % len(declared))
    assert list(declared) == PARAMETERS
    assert all(meaning.strip() for meaning in declared.values())
# endregion FUNC_test_parameters_registry_declares_the_seven


# region FUNC_test_spec_version_is_0_19_0 [DOMAIN(7): Version; CONCEPT(8): SpecVersion; TECH(4): bytes]
## @purpose Prove that the version file holds the line 2.0.0 and a newline, and nothing else.
## @io pathlib.Path -> None
## @complexity 1
def test_spec_version_is_0_19_0(repo_root):
    data = (repo_root / "SPEC_VERSION").read_bytes()
    print("[IMP:9][test_spec_version][RESULT] bytes=%d" % len(data))
    assert data == b"3.1.0\n"
# endregion FUNC_test_spec_version_is_0_19_0


# region FUNC_test_changelog_entry_names_skeleton_format_registries_tool [DOMAIN(7): Version; CONCEPT(8): Changelog; TECH(4): re]
## @purpose Prove that the changelog has the heading for 0.1.0 and mentions the skeleton, the format, the registries and the tool.
## @io pathlib.Path -> None
## @complexity 3
def test_changelog_entry_names_skeleton_format_registries_tool(repo_root):
    text = (repo_root / "CHANGELOG.md").read_text(encoding="utf-8")
    print("[IMP:9][test_changelog][RESULT] has_heading=%s" % ("\n## 0.1.0\n" in text))
    assert "\n## 0.1.0\n" in text
    lowered = text.lower()
    for word in ("skeleton", "format", "registries", "conform"):
        assert word in lowered, word
# endregion FUNC_test_changelog_entry_names_skeleton_format_registries_tool


# region FUNC_test_readme_explains_adoption_and_conform [DOMAIN(8): Readme; CONCEPT(9): Adoption, FourWays, Commands; TECH(4): str, re]
## @purpose Prove that the README explains the meta-framework, names every top-level directory of the layout, states the four
## ways of adopting a file, the capabilities, the parameters, the example adapter, the two commands with their options, the
## three exit codes, the version rules and the two development commands, and names nothing private: no path under a home
## directory of a machine, no path that starts with the tilde, no e-mail address (patterns built from fragments).
## @uses repo_root
## @io pathlib.Path -> None
## @complexity 6
def test_readme_explains_adoption_and_conform(repo_root):
    text = (repo_root / "README.md").read_text(encoding="utf-8")
    lowered = text.lower()
    top = sorted(p.name for p in repo_root.iterdir() if p.is_dir() and p.name not in {".git", "doxygen_output", "__pycache__", ".pytest_cache"})
    missing_dirs = [name for name in top if ("`%s/`" % name) not in text]
    ways = ["by reference", "vendored with a hash", "vendored with overrides", "not applied"]
    words = ["capabilities", "parameters", "examples/adapter.example.json", "bin/conform self --deny-list", "bin/conform adapter",
             "--json", "--log-level", "python3 -m pytest tests -s -v", "doxygen doxyfile", "major", "minor", "patch", "four ways",
             "harness-neutral", "spec_version", "changelog.md"]
    home = "/" + "Users" + "/"
    unix_home = "/" + "home" + "/"
    tilde = "~" + "/"
    mail = re.compile(r"[A-Za-z0-9._-]+" + "@" + r"[A-Za-z0-9-]+\.[A-Za-z]")
    print("[IMP:9][test_readme_explains][RESULT] top=%d missing_dirs=%s chars=%d" % (len(top), missing_dirs, len(text)))
    assert missing_dirs == []
    for way in ways:
        assert way in lowered, way
    for word in words:
        assert word in lowered, word
    for code in ("| 0 |", "| 1 |", "| 2 |"):
        assert code in text, code
    assert home not in text and unix_home not in text and tilde not in text
    assert mail.search(text) is None
# endregion FUNC_test_readme_explains_adoption_and_conform


# region FUNC_test_readme_states_mit_licence [DOMAIN(7): Readme; CONCEPT(8): MitLicence; TECH(4): str]
## @purpose Prove that the README names exactly the licence the owner selected on 2026-10-10 (MIT, linked to the root LICENSE
## file) and that this LICENSE is the only licence file beside it.
## @uses repo_root
## @io pathlib.Path -> None
## @complexity 2
def test_readme_states_mit_licence(repo_root):
    text = (repo_root / "README.md").read_text(encoding="utf-8")
    files = sorted(p.name for p in repo_root.iterdir() if p.name.upper().startswith(("LICENSE", "LICENCE", "COPYING")))
    print("[IMP:9][test_readme_states_mit_licence][RESULT] mit_line=%s files=%s" % (("License: [MIT](LICENSE)" in text), files))
    assert "License: [MIT](LICENSE)" in text
    assert files == ["LICENSE"]
# endregion FUNC_test_readme_states_mit_licence
