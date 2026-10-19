# region MODULE_CONTRACT [DOMAIN(9): PackageBoundary; CONCEPT(10): IndependentAssembly, PublicCoverage; TECH(7): Python, pytest]
## @modulecontract
## @purpose Verify the shipped typed Claude Code package's complete declared assembly independently of the package's own
##   checks and of the production neutral classifier, and prove that the unchanged publication scan reaches its native
##   carriers.
## @scope Exact specified package paths, kinds, profile and role locations; declared sibling packages; detached-neutral,
##   malformed, unsafe and linked refusals on owned copies; privacy canaries in agent, hook, workflow and harness carriers.
## @input Current complete canonical source and isolated owned copies; the M37 specification's 64-path list as the
##   independent expected input.
## @output Assertions over real source paths and metadata; visible validation and failure trajectories; exact restoration.
## @links [USES_API(8): pathlib, json, logging, subprocess; READS_DATA_FROM(9): implementations/claude/references/package-layout.json;
##   USES_API(7): bin/conform self (subprocess)]
## @links_to_spec examples/pm-project/specs/m22-claude-package.md AC-M22-1, AC-M22-2; examples/pm-project/specs/m37-claude-consumer-profile.md Behavior 6
## @invariants
## - Original source is read-only; negative controls change only owned copies and restore full bytes and numeric modes.
## - The 64 expected paths come from the approved specification, never from the observed layout file.
## - Assembly does not prove that a live session read or obeyed the neutral owners.
## @rationale
## Q: Why a second, root-level oracle when the package has its own contract test?
## A: The package test is part of the producer; this independent oracle rejects missing, extra, sibling and unsafe members
##    from outside the package, exactly as the Codex package is judged.
## Q: Why call the shipped conform launcher instead of a scanner of our own?
## A: The scanner and its canaries are the shipped privacy contract; running the real CLI proves the new carrier families
##    are in the same traversal without a second scanner.
## @changes
## LAST_CHANGE: [2.1.0 - M37 consumer-profile membership 64 (three bin launchers, carrier, package test) and Claude 2.1.0 selectors; earlier 2.0.0 - M30 exact current release/census coupling; all prior cases/assertions/refusals retained.]
## Earlier: [1.1.0 - M22 Claude package assembly oracle, refusals and publication-channel coverage.]
## @modulemap
## FUNC 7[Run the shipped conform self launcher on a copy] => test_claude_package._publication_process
## FUNC 4[Output forms of a planted value] => test_claude_package._forms
## FUNC 9[Independent package assembly, profile and path judgment] => test_claude_package._package_assembly
## FUNC 8[Expose owned important records before assertions] => test_claude_package._show_trace
## FUNC 9[Complete package and declared sibling set] => test_claude_package.test_complete_claude_package
## FUNC 9[Missing/extra/sibling/unsafe/detached/linked refusals] => test_claude_package.test_claude_package_refusals
## FUNC 10[Privacy canaries bite in native Claude carriers] => test_claude_package.test_claude_publication_channels
## @usecases
## - [test_complete_claude_package]: Owner → check the exact package population → 64 members, 28 skills, 6 roles, 7 helpers.
## - [test_claude_package_refusals]: QA → perturb owned package membership → defect refused, source restored.
## - [test_claude_publication_channels]: Owner → plant canaries in native carriers → the shipped scan fails each one.
## @GREP_SUMMARY Claude package, independent inventory, 64 paths, typed namespace, colocated-in-place, siblings, unsafe paths, publication canaries
## @STRUCTURE ▶ canonical source → ◇ 64-path/profile match → ⊕ positive result → ○ owned mutations → ◇ refuse → ⎋ restore → ○ canaries → ◇ scan FAIL
def _module_contract():
    pass
# endregion MODULE_CONTRACT



import json
import logging
import pathlib
import re
import stat
import subprocess

import pytest

LOGGER = logging.getLogger(__name__)
GENERATED = {"__pycache__", ".pytest_cache", "doxygen_output", ".DS_Store"}
DECLARED_PACKAGES = {"codex", "claude", "dsh"}
CORE = ("concepts/principles.md", "roles/_base.md", "code/exoskeleton.md", "code/ldd.md", "code/doxygen.md", "code/tests.md")
ROLES = {name: "agents/" + name + ".md" for name in ("architect", "coder", "debugger", "qa", "reviewer", "searcher")}
TOPICS = ("analyzer", "ax-ui-contract", "brainstorm", "brownfield-spec-template", "code-review", "data-transform",
          "devplan-protocol", "document-protocol", "durable-layer", "feature-dev", "graph-protocol", "greenfield-bootstrap",
          "hitl-gates", "pm", "pm-bootstrap", "pm-handoff", "pm-plan-batch", "pm-review-run", "pm-run-batch",
          "prod-log-vacuum", "prompting", "prompting-agent-design", "prompting-decompose", "prompting-markup",
          "prompting-verify", "roadmap", "semantic-exoskeleton", "spec-recon")
FIXED = {
    ".claude-plugin/plugin.json": "plugin-manifest", "Doxyfile": "config", "README.md": "documentation",
    "adapter.json": "adapter", "bin/codemap": "helper", "bin/markup-migrate": "helper", "bin/orient": "helper",
    "examples/smoke-spec.md": "example", "hooks/guard_destructive.py": "helper",
    "hooks/hooks.json": "hook-config", "hooks/session_start.py": "helper", "pytest.ini": "config",
    "references/adoption.md": "documentation", "references/claude-runtime.md": "documentation",
    "references/consumer-pm-profile.md": "documentation", "references/handoffs.md": "documentation", "references/package-layout.json": "layout",
    "references/source-disposition.md": "documentation",
    "skills/devplan-protocol/scripts/visual_gate_lint.py": "helper", "skills/feature-dev/scripts/run_state.py": "helper",
    "tests/test_consumer_profile.py": "test", "tests/test_guard.py": "test", "tests/test_guide.md": "test-guide",
    "tests/test_package_contract.py": "test",
    "tests/test_run_state.py": "test", "tests/test_session_start.py": "test", "tests/test_visual_gate.py": "test",
    "tests/test_workflow.py": "test", "tests/workflow_harness.mjs": "test", "workflows/feature-dev.js": "workflow",
}
EXPECTED_KINDS = dict(FIXED)
EXPECTED_KINDS.update({path: "role" for path in ROLES.values()})
EXPECTED_KINDS.update({"skills/%s/SKILL.md" % topic: "skill" for topic in TOPICS})
EXPECTED_PATHS = tuple(sorted(EXPECTED_KINDS))
# The shipped canary kinds and their scan rules, as the publication contract in tests/test_scan.py defines them.
CANARY_RULES = (("posix-home", "scan.home-path"), ("windows-home", "scan.home-path"), ("tilde", "scan.home-relative"),
                ("email", "scan.email"), ("deny-token", "scan.deny-token"))
FP_DETAIL_RE = re.compile(r"^line (\d+) fp=(\d+):([0-9a-f]{8})$")


# region FUNC__publication_process [DOMAIN(9): Publication; CONCEPT(9): RealDelivery; TECH(6): subprocess]
## @purpose Deliver the real launcher's JSON report and trace for an isolated copy through the shipped CLI.
## @uses subprocess.run
## @io (pathlib.Path repo_root, pathlib.Path copy, pathlib.Path deny) -> subprocess.CompletedProcess
## @complexity 2
def _publication_process(repo_root, copy, deny):
    argv = [str(repo_root / "bin" / "conform"), "self", "--root", str(copy), "--deny-list", str(deny),
            "--log-level", "DEBUG", "--json"]
    return subprocess.run(argv, cwd=str(copy.parent), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          universal_newlines=True)
# endregion FUNC__publication_process


# region FUNC__forms [DOMAIN(8): Privacy; CONCEPT(9): ValueForms, NoContent; TECH(4): json]
## @purpose Every form a planted value could take in an output: as it is, and as JSON writes it inside a string.
## @uses json.dumps
## @io str -> list[str]
## @complexity 1
def _forms(value):
    return [value, json.dumps(value)[1:-1]]
# endregion FUNC__forms


# region FUNC__package_assembly [DOMAIN(9): Package; CONCEPT(10): IndependentOracle; TECH(7): pathlib, json]
## @purpose Refuse an incomplete or unsafe Claude package before reporting the independently specified complete profile.
## @uses pathlib.Path.read_text, pathlib.Path.rglob, json.loads, logging.Logger.info, logging.Logger.error
## @io Input: root pathlib.Path of a complete co-located source. Output: sorted list of the 64 declared relative paths.
##   Side effects: reads and a safe trajectory only. Raises: ValueError for malformed layout, duplicate/unsafe path,
##   missing/extra/sibling package or detached neutral dependency; OSError/UnicodeError for unreadable files.
## @complexity 7
def _package_assembly(root):
    operation, ordinal = "Binding", -1
    try:
        # START_BLOCK_Validation
        LOGGER.info("[IMP:7][_package_assembly][READ] read co-located Claude package binding")
        package = root / "implementations/claude"
        if not package.is_dir() or package.is_symlink():
            raise ValueError("regular owned co-located package directory required")
        if set(p.name for p in package.parent.iterdir() if p.name != ".DS_Store") != DECLARED_PACKAGES:
            raise ValueError("unknown sibling package")
        if not (root / "SPEC_VERSION").is_file() or (root / "SPEC_VERSION").read_text() != "3.0.2\n":
            raise ValueError("unsupported detached neutral dependency")
        if not all((root / rel).is_file() and "status: draft\n" in (root / rel).read_text() for rel in CORE):
            raise ValueError("missing substantive neutral core")
        operation = "Layout"
        layout = json.loads((package / "references/package-layout.json").read_text())
        if (not isinstance(layout, dict) or set(layout) != {"package", "version", "profile", "files", "roles"}
                or layout.get("package") != "methodology-claude" or layout.get("version") != "2.1.1"
                or layout.get("profile") != "colocated-in-place" or layout.get("roles") != ROLES):
            raise ValueError("unsupported package profile")
        rows = layout.get("files")
        if not isinstance(rows, list) or not rows:
            raise ValueError("complete declared file list required")
        declared = []
        operation = "Member"
        for ordinal, row in enumerate(rows):
            if (not isinstance(row, dict) or set(row) != {"path", "kind"} or not isinstance(row.get("path"), str)
                    or not isinstance(row.get("kind"), str) or not row["kind"].strip()):
                raise ValueError("path/kind record required")
            relative = row["path"]
            posix = pathlib.PurePosixPath(relative)
            if (not relative or "\\" in relative or posix.is_absolute()
                    or any(part in (".", "..") for part in relative.split("/")) or posix.as_posix() != relative):
                raise ValueError("unsafe package path")
            if row["kind"] != EXPECTED_KINDS.get(relative):
                raise ValueError("package member kind differs from the approved specification")
            path = package / relative
            if (any(parent.is_symlink() for parent in [path] + list(path.parents)[:len(posix.parts) - 1])
                    or not path.is_file() or package.resolve() not in path.resolve().parents):
                raise ValueError("missing or nonregular contained package member")
            declared.append(relative)
            LOGGER.info("[IMP:8][_package_assembly][MEMBER_VALID] ordinal=%d", ordinal)
        if declared != sorted(declared) or len(set(declared)) != len(declared) or tuple(declared) != EXPECTED_PATHS:
            raise ValueError("declared package membership differs from the approved specification")
        operation, ordinal = "Population", -1
        actual = []
        for path in package.rglob("*"):
            relative = path.relative_to(package)
            if path.is_symlink():
                raise ValueError("symbolic package member")
            if any(part in GENERATED for part in relative.parts):
                continue
            if path.is_file():
                actual.append(relative.as_posix())
            elif not path.is_dir():
                raise ValueError("special package member")
        if tuple(sorted(actual)) != EXPECTED_PATHS:
            raise ValueError("missing or undeclared actual package member")
        operation = "Metadata"
        plugin = json.loads((package / ".claude-plugin/plugin.json").read_text())
        if plugin.get("name") != "methodology-claude" or plugin.get("version") != "2.1.1":
            raise ValueError("native metadata identity mismatch")
        LOGGER.info("[IMP:9][_package_assembly][VALIDATION_SUCCESS] members=%d", len(actual))
        return declared
        # END_BLOCK_Validation
    # START_BLOCK_ErrorHandling
    except (OSError, UnicodeError, ValueError, TypeError) as error:
        LOGGER.error("[IMP:10][_package_assembly][FAILURE] operation=%s ordinal=%d kind=%s", operation, ordinal, type(error).__name__)
        raise
    # END_BLOCK_ErrorHandling
# endregion FUNC__package_assembly


# region FUNC__show_trace [DOMAIN(8): Tests; CONCEPT(9): AccessibleTrajectory; TECH(6): logging]
## @purpose Expose this module's important records before the assertions.
## @uses builtins.print
## @io Input: captured records. Output: None; visible same-process stdout only.
## @complexity 2
def _show_trace(records):
    for record in records:
        if record.name == LOGGER.name and any("[IMP:%d]" % n in record.getMessage() for n in range(7, 11)):
            print(record.getMessage())
# endregion FUNC__show_trace


# region FUNC_test_complete_claude_package [DOMAIN(9): Boundary; CONCEPT(10): RealFilesystem; TECH(7): pytest]
## @purpose Verify the actual complete package population and the declared sibling set from the canonical source.
## @uses test_claude_package._package_assembly, test_claude_package._show_trace
## @io Input: repo_root and caplog. Output: None after the exact 64/28/6/7 population and the sibling set are confirmed.
## @complexity 3
def test_complete_claude_package(repo_root, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    declared = _package_assembly(repo_root)
    _show_trace(caplog.records)
    kinds = [EXPECTED_KINDS[p] for p in declared]
    assert len(declared) == 64 and kinds.count("skill") == 28 and kinds.count("role") == 6 and kinds.count("helper") == 7
    assert {p.name for p in (repo_root / "implementations").iterdir() if p.name != ".DS_Store"} == DECLARED_PACKAGES
    assert any("[VALIDATION_SUCCESS]" in r.getMessage() for r in caplog.records)
    assert not [r for r in caplog.records if r.levelno >= logging.ERROR]
# endregion FUNC_test_complete_claude_package


# region FUNC_test_claude_package_refusals [DOMAIN(9): Package; CONCEPT(10): DiscriminatingRefusal, Restoration; TECH(7): pytest]
## @purpose Reject real owned assembly defects while preserving untouched members and restoring complete originals.
## @uses test_claude_package._package_assembly, test_claude_package._show_trace, pathlib.Path.write_bytes, pathlib.Path.chmod
## @io Input: complete owned repo_copy and caplog. Output: None after every case refuses and the copy is restored.
## @complexity 6
def test_claude_package_refusals(repo_copy, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    package = repo_copy / "implementations/claude"
    manifest = package / "references/package-layout.json"
    original, mode = manifest.read_bytes(), stat.S_IMODE(manifest.stat().st_mode)
    witness = package / "agents/qa.md"
    witness_bytes = witness.read_bytes()
    cases = ("missing", "extra", "sibling", "unsafe", "absolute", "duplicate", "profile", "detached", "linked",
             "malformed", "wrong-kind", "package-runtime", "roles")
    for case in cases:
        caplog.clear()
        altered = json.loads(original)
        target, saved = None, None
        try:
            if case == "missing":
                target = package / "hooks/session_start.py"
                saved = (target.read_bytes(), stat.S_IMODE(target.stat().st_mode))
                target.unlink()
            elif case == "extra":
                target = package / "agents/undeclared.md"
                target.write_text("undeclared public member\n")
            elif case == "package-runtime":
                target = package / ".methodology"
                target.mkdir()
                (target / "state.json").write_text("{}\n")
            elif case == "sibling":
                target = package.parent / "unknown-engine"
                target.mkdir()
            elif case == "detached":
                target = repo_copy / "SPEC_VERSION"
                saved = (target.read_bytes(), stat.S_IMODE(target.stat().st_mode))
                target.unlink()
            elif case == "linked":
                target = package / "linked-member"
                target.symlink_to(witness)
            elif case == "malformed":
                manifest.write_text("{")
            else:
                if case == "unsafe":
                    altered["files"][0]["path"] = "../escape.txt"
                elif case == "absolute":
                    altered["files"][0]["path"] = "/escaping.txt"
                elif case == "duplicate":
                    altered["files"].append(dict(altered["files"][0]))
                elif case == "profile":
                    altered["profile"] = "detached-cached"
                elif case == "wrong-kind":
                    altered["files"][0]["kind"] = "documentation"
                elif case == "roles":
                    altered["roles"]["qa"] = "agents/coder.md"
                manifest.write_text(json.dumps(altered))
            with pytest.raises(ValueError):
                _package_assembly(repo_copy)
            _show_trace(caplog.records)
            errors = [r for r in caplog.records if r.levelno >= logging.ERROR]
            print("[IMP:9][test_claude_package_refusals][REFUSED] case=%s errors=%d" % (case, len(errors)))
            assert len(errors) == 1 and "[_package_assembly][FAILURE]" in errors[0].getMessage()
            assert witness.read_bytes() == witness_bytes
        finally:
            manifest.write_bytes(original)
            manifest.chmod(mode)
            if target is not None:
                if case == "package-runtime":
                    (target / "state.json").unlink()
                    target.rmdir()
                elif target.is_dir() and not target.is_symlink():
                    target.rmdir()
                elif target.exists() or target.is_symlink():
                    target.unlink()
                if saved is not None:
                    target.write_bytes(saved[0])
                    target.chmod(saved[1])
        if saved is not None:
            assert target.read_bytes() == saved[0] and stat.S_IMODE(target.stat().st_mode) == saved[1]
        caplog.clear()
        assert tuple(_package_assembly(repo_copy)) == EXPECTED_PATHS
        assert manifest.read_bytes() == original and stat.S_IMODE(manifest.stat().st_mode) == mode
    # An ambient, git-ignored macOS .DS_Store beside the packages is not a sibling package.
    ambient = package.parent / ".DS_Store"
    try:
        ambient.write_bytes(b"\x00")
        caplog.clear()
        accepted = _package_assembly(repo_copy)
        print("[IMP:9][test_claude_package_refusals][AMBIENT_ACCEPTED] members=%d" % len(accepted))
        assert tuple(accepted) == EXPECTED_PATHS
    finally:
        ambient.unlink()
# endregion FUNC_test_claude_package_refusals


# region FUNC_test_claude_publication_channels [DOMAIN(10): Publication; CONCEPT(10): NativeCoverage, Restoration; TECH(7): pytest, subprocess]
## @purpose Prove every existing privacy canary bites in each native Claude carrier family through the unchanged shipped
##   scanner and real CLI, with full restoration.
## @uses test_claude_package._publication_process, test_claude_package._forms, pathlib.Path.read_bytes, pathlib.Path.write_bytes, json.loads
## @io Input: repo_root, owned repo_copy, deny/canary fixtures and one native relative path. Output: None after each exact
##   refusal and restoration. Side effects: owned copy only.
## @complexity 5
@pytest.mark.parametrize("relative", [
    "agents/qa.md", "hooks/hooks.json", "hooks/session_start.py", "workflows/feature-dev.js",
    "tests/workflow_harness.mjs", "skills/pm-handoff/SKILL.md", "adapter.json",
])
def test_claude_publication_channels(relative, repo_root, repo_copy, deny_list, canary_values):
    target = repo_copy / "implementations/claude" / relative
    original, mode = target.read_bytes(), target.stat().st_mode & 0o777
    baseline = _publication_process(repo_root, repo_copy, deny_list[0])
    print("[IMP:9][test_claude_publication_channels][BASELINE] carrier=%s exit=%d" % (relative, baseline.returncode))
    assert baseline.returncode == 0
    for kind, rule in CANARY_RULES:
        value = canary_values[kind]
        try:
            target.write_bytes(original + b"\n" + value.encode("utf-8") + b"\n")
            result = _publication_process(repo_root, repo_copy, deny_list[0])
            report = json.loads(result.stdout)
            fails = [r for r in report["rows"] if r["status"] == "FAIL"]
            print("[IMP:9][test_claude_publication_channels][REFUSAL] carrier=%s kind=%s exit=%d failures=%d"
                  % (relative, kind, result.returncode, len(fails)))
            assert result.returncode == 1 and len(fails) == 1
            assert fails[0]["rule"] == rule and fails[0]["subject"] == "implementations/claude/" + relative
            assert FP_DETAIL_RE.match(fails[0]["detail"])
            for form in _forms(value):
                assert form not in result.stdout and form not in result.stderr
        finally:
            target.write_bytes(original)
            target.chmod(mode)
        assert target.read_bytes() == original
    restored = _publication_process(repo_root, repo_copy, deny_list[0])
    assert restored.returncode == 0
# endregion FUNC_test_claude_publication_channels
