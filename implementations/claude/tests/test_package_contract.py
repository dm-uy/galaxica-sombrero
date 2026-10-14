# region MODULE_CONTRACT [DOMAIN(9): PackageContract, NativeClaude; CONCEPT(9): IndependentOracle, InPlaceBinding; TECH(7): Python, pytest, json]
## @modulecontract
## @purpose Prove that the shipped methodology-claude package is complete and bound in place: the declared layout equals the
##   real members, the adapter accounts the real neutral population and registries, every role carrier and skill entry carries
##   the agreed frontmatter, and every `${CLAUDE_PLUGIN_ROOT}` reference resolves to a real file.
## @scope Package layout and kinds, plugin manifest identity, adapter coverage (71 files, 28 capabilities, 7 parameters),
##   adoption carrier coverage, agent model/tool contract, skill topic set and frontmatter, owner-reference resolution,
##   hooks wiring and workflow identity.
## @input The real package directory and the real neutral checkout two levels above it; read only.
## @output Assertions and a visible IMP:7-10 trajectory printed before them; no file is written.
## @links [READS_DATA_FROM(9): references/package-layout.json, adapter.json, agents/*.md, skills/*/SKILL.md, hooks/hooks.json;
##   READS_DATA_FROM(8): runtime/capabilities.md, runtime/parameters.md, SPEC_VERSION, implementations/codex/skills]
## @links_to_spec examples/pm-project/specs/m22-claude-package.md AC-M22-1, AC-M22-2, AC-M22-3
## @invariants
## - Expected agent models and tools, the 28 topics and the neutral population are derived independently of the producer
##   files they judge (from the specification table, the Codex topic directory and the neutral registries).
## - The tests never modify the package or the neutral checkout.
## - A structural pass proves assembly and reference resolution, not that a live session read or obeyed the owners.
## @rationale
## Q: Why recompute the neutral population instead of trusting adapter.json?
## A: The adapter is the producer under test; FMT-1 membership is recomputed from the checkout so a dropped or invented
##    neutral path fails.
## Q: Why a line parser for frontmatter instead of PyYAML?
## A: The package is stdlib-only; carrier and skill frontmatter is deliberately flat, and the parser refuses nesting.
## @changes
## LAST_CHANGE: [2.0.0 - M30 exact current release/census coupling; all prior cases/assertions/refusals retained.]
## Earlier: [2.0.0 - Initial M22 package contract oracle.]
## @modulemap
## FUNC 6[Read flat frontmatter and body of a Markdown carrier] => _frontmatter
## FUNC 8[Recompute the neutral Markdown population under FMT-1] => _neutral_population
## FUNC 7[Resolve every ${CLAUDE_PLUGIN_ROOT} reference of a text] => _unresolved_references
## FUNC 5[Print owned important trace before assertions] => _show
## FUNC 9[Layout equals real members, kinds and roles] => test_layout_matches_members
## FUNC 8[Manifest and adapter identity and coverage] => test_manifest_and_adapter
## FUNC 9[Agent carriers frontmatter, tools and owners] => test_agent_carriers
## FUNC 9[Skill entries topic set, frontmatter and owners] => test_skill_entries
## FUNC 7[Hooks wiring and workflow identity] => test_hooks_and_workflow
## @usecases
## - [test_layout_matches_members]: QA → compare declared and real package members → missing or undeclared member refused
## - [test_agent_carriers]: QA → check each role's model and tools → a judge with Edit or a delegating role refused
## - [test_skill_entries]: QA → resolve every owner reference → a broken neutral pointer refused
## @GREP_SUMMARY package contract, layout, adapter coverage, agents frontmatter, skills, CLAUDE_PLUGIN_ROOT, hooks, workflow, oracle
## @STRUCTURE ▶ package+neutral roots → ◇ layout ≡ members → ◇ adapter ≡ registries → ○ agents ∋ model/tools/owners → ○ skills ∋ frontmatter/owners → ◇ hooks/workflow → ⎋ assertions
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import json
import logging
import pathlib
import re

LOGGER = logging.getLogger(__name__)
PACKAGE = pathlib.Path(__file__).resolve().parents[1]
NEUTRAL = PACKAGE.parents[1]
GENERATED = {"__pycache__", ".pytest_cache", "doxygen_output", ".DS_Store"}
CORE = ("concepts/principles.md", "roles/_base.md", "code/exoskeleton.md", "code/ldd.md", "code/doxygen.md", "code/tests.md")
READ_TOOLS = ["Read", "Glob", "Grep"]
WRITE_TOOLS = ["Read", "Glob", "Grep", "Write", "Edit", "Bash", "TodoWrite", "Skill", "WebSearch", "WebFetch"]
AGENTS = {
    "architect": ("opus", WRITE_TOOLS),
    "coder": ("sonnet", WRITE_TOOLS),
    "debugger": ("sonnet", WRITE_TOOLS),
    "qa": ("sonnet", ["Read", "Glob", "Grep", "Bash", "TodoWrite", "Skill"]),
    "reviewer": ("opus", ["Read", "Glob", "Grep", "Bash", "Skill"]),
    "searcher": ("haiku", READ_TOOLS),
}
JUDGES = ("qa", "reviewer", "searcher")
LIFECYCLE = ("pm-bootstrap", "pm-handoff", "pm-plan-batch", "pm-review-run", "pm-run-batch")
REFERENCE = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}/([A-Za-z0-9_./*-]+)")


# region FUNC__frontmatter [DOMAIN(7): Markdown; CONCEPT(7): FlatCard; TECH(5): str]
## @purpose Give the flat frontmatter keys and the body of a carrier so that each contract field can be judged exactly.
## @uses pathlib.Path.read_text
## @io pathlib.Path -> (dict[str, str], str). Raises ValueError for a missing, unclosed or nested frontmatter.
## @complexity 4
def _frontmatter(path):
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        LOGGER.error("[IMP:10][_frontmatter][PARSE] path=%s reason=no closed frontmatter", path.name)
        raise ValueError("frontmatter missing in " + str(path))
    end = lines[1:].index("---") + 1
    fields = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if line.startswith((" ", "\t", "-")) or ":" not in line:
            LOGGER.error("[IMP:10][_frontmatter][PARSE] path=%s reason=nested or malformed line", path.name)
            raise ValueError("nested frontmatter in " + str(path))
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, "\n".join(lines[end + 1:])
# endregion FUNC__frontmatter


# region FUNC__neutral_population [DOMAIN(8): NeutralMembership; CONCEPT(8): FMT1; TECH(5): pathlib]
## @purpose Recompute the neutral Markdown files of the checkout under FMT-1, independently of the adapter under test.
## @uses pathlib.Path.rglob
## @io None -> set[str] of repository-relative paths.
## @complexity 3
def _neutral_population():
    skipped = {".git", "tests", "examples", "implementations", "doxygen_output", "__pycache__", ".pytest_cache", ".kilo"}
    found = set()
    for path in NEUTRAL.rglob("*.md"):
        relative = path.relative_to(NEUTRAL)
        if relative.parts[0] in skipped or relative.as_posix() in {"README.md", "CHANGELOG.md"}:
            continue
        found.add(relative.as_posix())
    LOGGER.info("[IMP:7][_neutral_population][SCAN] neutral=%d", len(found))
    return found
# endregion FUNC__neutral_population


# region FUNC__unresolved_references [DOMAIN(8): InPlaceBinding; CONCEPT(9): ReferenceResolution; TECH(6): re]
## @purpose List every `${CLAUDE_PLUGIN_ROOT}` reference of a text that does not resolve to a real file, so that a broken
##   owner pointer is caught before a session follows it.
## @uses re.Pattern.findall, pathlib.Path.glob
## @io str -> (int references, list[str] unresolved). Wildcard references must match at least one file.
## @complexity 4
def _unresolved_references(text):
    targets = REFERENCE.findall(text)
    missing = []
    for raw in targets:
        target = raw.rstrip(".")
        if "*" in target:
            if not list(PACKAGE.glob(target)) and not list(NEUTRAL.glob(target.replace("../../", "", 1))):
                missing.append(target)
            continue
        if not (PACKAGE / target).resolve().exists():
            missing.append(target)
    return len(targets), missing
# endregion FUNC__unresolved_references


# region FUNC__show [DOMAIN(5): Tests; CONCEPT(6): VisibleTrace; TECH(4): print]
## @purpose Expose this module's important records before the assertions that depend on them.
## @uses builtins.print
## @io list[logging.LogRecord] -> None
## @complexity 2
def _show(records):
    for record in records:
        if record.name == LOGGER.name and any("[IMP:%d]" % n in record.getMessage() for n in range(7, 11)):
            print(record.getMessage())
# endregion FUNC__show


# region FUNC_test_layout_matches_members [DOMAIN(9): PackageAssembly; CONCEPT(9): Completeness; TECH(6): json]
## @purpose Refuse a package whose declared layout differs from its real members, kinds or role map.
## @uses json.loads, pathlib.Path.rglob
## @io caplog -> None
## @complexity 5
def test_layout_matches_members(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    layout = json.loads((PACKAGE / "references/package-layout.json").read_text(encoding="utf-8"))
    declared = [row["path"] for row in layout["files"]]
    actual = sorted(p.relative_to(PACKAGE).as_posix() for p in PACKAGE.rglob("*")
                    if p.is_file() and not GENERATED.intersection(p.relative_to(PACKAGE).parts))
    LOGGER.info("[IMP:9][test_layout_matches_members][COMPARE] declared=%d actual=%d", len(declared), len(actual))
    _show(caplog.records)
    assert set(layout) == {"package", "version", "profile", "files", "roles"}
    assert (layout["package"], layout["version"], layout["profile"]) == ("methodology-claude", "2.0.0", "colocated-in-place")
    assert declared == sorted(declared) and len(set(declared)) == len(declared) == 59
    assert sorted(set(actual) - set(declared)) == [] and sorted(set(declared) - set(actual)) == []
    assert layout["roles"] == {name: "agents/%s.md" % name for name in AGENTS}
    kinds = {row["path"]: row["kind"] for row in layout["files"]}
    assert sum(k == "skill" for k in kinds.values()) == 28 and sum(k == "role" for k in kinds.values()) == 6
    assert sum(k == "helper" for k in kinds.values()) == 4
    assert all(kinds[p] == "role" for p in kinds if p.startswith("agents/"))
    assert not any(p.is_symlink() for p in PACKAGE.rglob("*"))
# endregion FUNC_test_layout_matches_members


# region FUNC_test_manifest_and_adapter [DOMAIN(9): Adapter; CONCEPT(9): PointwiseCoverage; TECH(6): json, re]
## @purpose Prove the manifest identity and that the adapter accounts exactly the recomputed neutral files and the
##   declared registries, with every via carrier naming its neutral path.
## @uses json.loads, re.findall
## @io caplog -> None
## @complexity 6
def test_manifest_and_adapter(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    plugin = json.loads((PACKAGE / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    adapter = json.loads((PACKAGE / "adapter.json").read_text(encoding="utf-8"))
    neutral = _neutral_population()
    capabilities = set(re.findall(r"^- \*\*cap:([a-z0-9-]+)\*\*", (NEUTRAL / "runtime/capabilities.md").read_text(), re.M))
    parameters = set(re.findall(r"^- \*\*param:([a-z0-9-]+)\*\*", (NEUTRAL / "runtime/parameters.md").read_text(), re.M))
    adoption = (PACKAGE / "references/adoption.md").read_text(encoding="utf-8")
    unnamed = [path for path in adapter["files"] if "`%s`" % path not in adoption]
    LOGGER.info("[IMP:9][test_manifest_and_adapter][COVERAGE] files=%d neutral=%d caps=%d params=%d unnamed=%d",
                len(adapter["files"]), len(neutral), len(adapter["capabilities"]), len(adapter["parameters"]), len(unnamed))
    _show(caplog.records)
    assert plugin["name"] == "methodology-claude" and plugin["version"] == "2.0.0" and plugin["license"] == "MIT"
    assert not plugin["name"].startswith(("claude", "anthropic"))
    assert adapter["harness"] == "methodology-claude" and adapter["spec_root"] == "../../"
    assert adapter["spec_version"] == (NEUTRAL / "SPEC_VERSION").read_text().strip() == "3.0.0"
    assert set(adapter["files"]) == neutral and len(neutral) == 71
    assert all(rule == {"mode": "reference", "via": "references/adoption.md"} for rule in adapter["files"].values())
    assert unnamed == []
    assert set(adapter["capabilities"]) == capabilities and len(capabilities) == 28
    assert all(cap.get("mechanism", "").strip() and cap.get("fallback", "").strip() for cap in adapter["capabilities"].values())
    assert set(adapter["parameters"]) == parameters and len(parameters) == 7
    assert adapter["parameters"]["debug-entry-cap"] == "4"
    assert all(model in adapter["parameters"]["model-" + tier] for tier, model in
               (("mechanical", "haiku"), ("routine", "sonnet"), ("judgment", "opus")))
# endregion FUNC_test_manifest_and_adapter


# region FUNC_test_agent_carriers [DOMAIN(9): Roles; CONCEPT(10): HardToolLimits, ModelTier; TECH(6): pathlib]
## @purpose Refuse a role carrier with a wrong model or tool list, a judge able to edit, any role able to delegate, or an
##   owner pointer that does not resolve in place.
## @uses test_package_contract._frontmatter, test_package_contract._unresolved_references
## @io caplog -> None
## @complexity 6
def test_agent_carriers(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    found = sorted(p.stem for p in (PACKAGE / "agents").glob("*.md"))
    problems = []
    for name, (model, tools) in AGENTS.items():
        fields, body = _frontmatter(PACKAGE / "agents" / (name + ".md"))
        listed = [t.strip() for t in fields.get("tools", "").split(",") if t.strip()]
        count, missing = _unresolved_references(body)
        LOGGER.info("[IMP:8][test_agent_carriers][CARRIER] role=%s model=%s tools=%d refs=%d unresolved=%d",
                    name, fields.get("model"), len(listed), count, len(missing))
        if fields.get("name") != name or fields.get("model") != model or listed != tools or not fields.get("description"):
            problems.append(name + ": frontmatter")
        if {"Agent", "Task"} & set(listed) or (name in JUDGES and {"Edit", "Write", "NotebookEdit"} & set(listed)):
            problems.append(name + ": forbidden tool")
        for owner in ("references/claude-runtime.md", "../../roles/_base.md", "../../roles/%s.md" % name):
            if "${CLAUDE_PLUGIN_ROOT}/" + owner not in body:
                problems.append(name + ": owner " + owner)
        problems.extend(name + ": core " + core for core in CORE if "${CLAUDE_PLUGIN_ROOT}/../../" + core not in body)
        problems.extend(name + ": unresolved " + m for m in missing)
    LOGGER.info("[IMP:9][test_agent_carriers][RESULT] roles=%d problems=%d", len(found), len(problems))
    _show(caplog.records)
    assert found == sorted(AGENTS)
    assert problems == []
# endregion FUNC_test_agent_carriers


# region FUNC_test_skill_entries [DOMAIN(9): Skills; CONCEPT(9): TopicParity, InPlaceOwners; TECH(6): pathlib]
## @purpose Refuse a skill set that loses Codex topic parity or the five lifecycle commands, or an entry whose frontmatter,
##   invocation mode or owner pointers are wrong.
## @uses test_package_contract._frontmatter, test_package_contract._unresolved_references
## @io caplog -> None
## @complexity 6
def test_skill_entries(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    parity = sorted(p.name for p in (NEUTRAL / "implementations/codex/skills").iterdir() if p.is_dir() and p.name not in LIFECYCLE)
    topics = sorted(p.name for p in (PACKAGE / "skills").iterdir() if p.is_dir())
    problems = []
    for topic in topics:
        fields, body = _frontmatter(PACKAGE / "skills" / topic / "SKILL.md")
        count, missing = _unresolved_references(body)
        neutral_refs = body.count("${CLAUDE_PLUGIN_ROOT}/../../")
        LOGGER.info("[IMP:8][test_skill_entries][ENTRY] topic=%s refs=%d neutral=%d unresolved=%d",
                    topic, count, neutral_refs, len(missing))
        if fields.get("name") != topic or not fields.get("description"):
            problems.append(topic + ": frontmatter")
        if (fields.get("disable-model-invocation") == "true") != (topic in LIFECYCLE):
            problems.append(topic + ": invocation mode")
        if neutral_refs < 1 or "${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md" not in body:
            problems.append(topic + ": owners")
        problems.extend(topic + ": unresolved " + m for m in missing)
    LOGGER.info("[IMP:9][test_skill_entries][RESULT] topics=%d parity=%d problems=%d", len(topics), len(parity), len(problems))
    _show(caplog.records)
    assert len(parity) == 23 and topics == sorted(parity + list(LIFECYCLE))
    assert problems == []
# endregion FUNC_test_skill_entries


# region FUNC_test_hooks_and_workflow [DOMAIN(8): Hooks, Workflow; CONCEPT(8): Wiring; TECH(6): json, re]
## @purpose Prove that the hooks file wires SessionStart and the Bash PreToolUse guard to the shipped scripts through the
##   plugin root, and that the workflow spine declares its expected identity.
## @uses json.loads, re.search
## @io caplog -> None
## @complexity 4
def test_hooks_and_workflow(caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    hooks = json.loads((PACKAGE / "hooks/hooks.json").read_text(encoding="utf-8"))["hooks"]
    start = [h["command"] for entry in hooks.get("SessionStart", []) for h in entry["hooks"]]
    guard = [h["command"] for entry in hooks.get("PreToolUse", []) if entry.get("matcher") == "Bash" for h in entry["hooks"]]
    workflow = (PACKAGE / "workflows/feature-dev.js").read_text(encoding="utf-8")
    LOGGER.info("[IMP:9][test_hooks_and_workflow][WIRING] start=%d guard=%d", len(start), len(guard))
    _show(caplog.records)
    assert len(start) == 1 and "${CLAUDE_PLUGIN_ROOT}/hooks/session_start.py" in start[0]
    assert len(guard) == 1 and "${CLAUDE_PLUGIN_ROOT}/hooks/guard_destructive.py" in guard[0]
    assert all("|| true" not in command for command in start + guard)
    assert re.search(r"export const meta = \{\s*name: 'feature-dev-workflow'", workflow)
# endregion FUNC_test_hooks_and_workflow
