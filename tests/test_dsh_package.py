# region MODULE_CONTRACT [DOMAIN(9): PackageBoundary; CONCEPT(10): IndependentAssembly, PublicCoverage; TECH(7): Python, pytest]
## @modulecontract
## @purpose Verify the shipped typed DSH package's complete declared assembly independently of the production neutral classifier.
## @scope Exact declared package paths/profile/role locations and ordinary-versus-native Markdown boundary; malformed membership/profile/path controls.
## @input Current complete canonical public source and isolated owned copies; fixed accepted-plan inventory as independent expected input.
## @output Assertions over actual source paths, profile and metadata; visible own validation/failure trajectories and exact negative restoration.
## @links [USES_API(8): pathlib, json, logging; READS_DATA_FROM(9): implementations/dsh/references/package-layout.json]
## @invariants
## - Original source is read-only; negative controls affect only owned copies and restore original full bytes/numeric modes.
## - The expected member population derives from the accepted package design, never from the observed producer result or the imported neutral classifier.
## - The map file itself is deliberately outside the population it enumerates; the oracle names it explicitly.
## - Package assembly does not prove semantic full-rule adoption, human authority or actual native execution.
## @rationale
## Q: Why a separate package oracle?
## A: Neutral exclusion cannot prove native completeness; bidirectional independent membership rejects missing, extra and sibling packages.
## Q: Why retain an outside-namespace negative?
## A: The native exception is typed and scoped; an ordinary malformed Markdown file must still fail the actual common checker.
## @changes
## LAST_CHANGE: [3.0.1 - Initial DSH package: 75 expected members, bundle manifest and composition files, six role carriers and 27 skill entries.]
## @modulemap
## FUNC 9[Independent actual package assembly/profile/path judgment] => test_dsh_package._package_assembly
## FUNC 8[Expose owning important captured records before assertions] => test_dsh_package._show_trace
## FUNC 9[Actual neutral/native boundary and valid complete package] => test_dsh_package.test_neutral_boundary_and_complete_package
## FUNC 9[Missing/extra/sibling/unsafe/detached assembly controls] => test_dsh_package.test_package_assembly_refusals
## @usecases
## - [test_neutral_boundary_and_complete_package]: Owner -> check exact actual source populations -> native docs separated and ordinary malformed prose refused.
## - [test_package_assembly_refusals]: QA -> perturb owned package membership/profile -> rejected real defect and fully restored source.
## @GREP_SUMMARY package, independent inventory, typed namespace, source profile, siblings, unsafe paths, restoration
## @STRUCTURE canonical source -> independent member/profile match -> positive result -> owned mutations -> refuse -> restore
def _module_contract():
    pass
# endregion MODULE_CONTRACT



import json
import logging
import pathlib
import stat

import pytest

LOGGER = logging.getLogger(__name__)
GENERATED = {"__pycache__", ".pytest_cache", "doxygen_output"}
# Declared implementation packages of this repository; any other sibling is refused.
DECLARED_PACKAGES = {"codex", "claude", "dsh"}
CORE = ("concepts/principles.md", "roles/_base.md", "code/exoskeleton.md", "code/ldd.md", "code/doxygen.md", "code/tests.md")
ROLES = {name: "roles/" + name + ".md" for name in ("architect", "coder", "debugger", "qa", "reviewer", "searcher")}
# The package map is not a member of the population it enumerates; the oracle names it here.
MAP = "references/package-layout.json"

EXPECTED_KINDS = {
    '.dsh-plugin/plugin.json': 'plugin-manifest',
    'Doxyfile': 'config',
    'README.md': 'documentation',
    'adapter.json': 'adapter',
    'cordis.patch.yml': 'config',
    'examples/smoke-spec.md': 'example',
    'package.json': 'plugin-manifest',
    'pytest.ini': 'config',
    'references/adoption.md': 'documentation',
    'references/consumer-pm-profile.md': 'documentation',
    'references/dsh-runtime.md': 'documentation',
    'references/dsh-subagent-workflow.md': 'documentation',
    'references/handoffs.md': 'documentation',
    'references/package-layout.json': 'layout',
    'references/source-disposition.md': 'documentation',
    'roles/architect.md': 'role',
    'roles/coder.md': 'role',
    'roles/debugger.md': 'role',
    'roles/qa.md': 'role',
    'roles/reviewer.md': 'role',
    'roles/searcher.md': 'role',
    'skills/analyzer/SKILL.md': 'skill',
    'skills/ax-ui-contract/SKILL.md': 'skill',
    'skills/brainstorm/SKILL.md': 'skill',
    'skills/brownfield-spec-template/SKILL.md': 'skill',
    'skills/code-review/SKILL.md': 'skill',
    'skills/data-transform/SKILL.md': 'skill',
    'skills/devplan-protocol/SKILL.md': 'skill',
    'skills/devplan-protocol/scripts/visual_gate_lint.py': 'helper',
    'skills/document-protocol/SKILL.md': 'skill',
    'skills/durable-layer/SKILL.md': 'skill',
    'skills/feature-dev/SKILL.md': 'skill',
    'skills/feature-dev/scripts/run_state.py': 'helper',
    'skills/graph-protocol/SKILL.md': 'skill',
    'skills/greenfield-bootstrap/SKILL.md': 'skill',
    'skills/hitl-gates/SKILL.md': 'skill',
    'skills/pm-bootstrap/SKILL.md': 'skill',
    'skills/pm-handoff/SKILL.md': 'skill',
    'skills/pm-plan-batch/SKILL.md': 'skill',
    'skills/pm-run-batch/SKILL.md': 'skill',
    'skills/pm/SKILL.md': 'skill',
    'skills/pm/scripts/codemap.py': 'helper',
    'skills/pm/scripts/consumer_files.py': 'helper',
    'skills/pm/scripts/markup_migrate.py': 'helper',
    'skills/pm/scripts/orient.py': 'helper',
    'skills/pm/templates/AGENTS.md': 'documentation',
    'skills/pm/templates/CLAUDE.md': 'documentation',
    'skills/pm/templates/CONVENTIONS.md': 'documentation',
    'skills/pm/templates/DEC.md': 'documentation',
    'skills/pm/templates/Doxyfile': 'config',
    'skills/pm/templates/HANDOFF.md': 'documentation',
    'skills/pm/templates/OPEN_QUESTIONS.md': 'documentation',
    'skills/pm/templates/RECON.md': 'documentation',
    'skills/pm/templates/ROADMAP.md': 'documentation',
    'skills/pm/templates/SPEC.md': 'documentation',
    'skills/pm/templates/TASKS.md': 'documentation',
    'skills/pm/templates/VISION.md': 'documentation',
    'skills/pm/templates/gitignore': 'config',
    'skills/prod-log-vacuum/SKILL.md': 'skill',
    'skills/prompting-agent-design/SKILL.md': 'skill',
    'skills/prompting-decompose/SKILL.md': 'skill',
    'skills/prompting-markup/SKILL.md': 'skill',
    'skills/prompting-verify/SKILL.md': 'skill',
    'skills/prompting/SKILL.md': 'skill',
    'skills/roadmap/SKILL.md': 'skill',
    'skills/semantic-exoskeleton/SKILL.md': 'skill',
    'skills/spec-recon/SKILL.md': 'skill',
    'tests/test_adoption.py': 'test',
    'tests/test_codemap.py': 'test',
    'tests/test_consumer_files.py': 'test',
    'tests/test_consumer_pm.py': 'test',
    'tests/test_guide.md': 'test-guide',
    'tests/test_markup_migrate.py': 'test',
    'tests/test_native_contract.py': 'test',
    'tests/test_run_state.py': 'test',
    'tests/test_visual_gate.py': 'test',
}


EXPECTED_PATHS = tuple(sorted(EXPECTED_KINDS))


# region FUNC__package_assembly [DOMAIN(9): Package; CONCEPT(10): IndependentOracle; TECH(7): pathlib, json]
## @purpose Refuse incomplete or unsafe actual package assembly before reporting the independently specified complete profile.
## @uses pathlib.Path.read_text, pathlib.Path.rglob, json.loads, logging.Logger.info, logging.Logger.error
## @io Input: root pathlib.Path of complete co-located source. Output: sorted list of75 exact declared relative paths.
##   Side effects: source reads and safe structured trajectory only; no source/state mutation. Guarantees: exact planned membership/profile/roles and regular contained paths; no claim of mental adoption or sandboxing.
##   Raises: ValueError for malformed layout, duplicate/unsafe path, missing/extra/sibling package or detached neutral dependency; OSError/UnicodeError for unreadable files.
##   System importance:10 for complete source boundary. Example: the current complete co-located package returns its sorted75path set.
## @complexity 7
def _package_assembly(root):
    operation, ordinal = "Binding", -1
    try:
        # START_BLOCK_Validation
        LOGGER.info("[IMP:7][_package_assembly][READ] read co-located package binding")
        package = root / "implementations/dsh"
        if not package.is_dir() or package.is_symlink():
            raise ValueError("regular owned co-located package directory required")
        if set(p.name for p in package.parent.iterdir() if p.name != ".DS_Store") != DECLARED_PACKAGES:
            raise ValueError("unknown sibling package")
        if not (root / "SPEC_VERSION").is_file() or (root / "SPEC_VERSION").read_text() != "3.0.1\n":
            raise ValueError("unsupported detached neutral dependency")
        if not all((root / rel).is_file() and "status: draft\n" in (root / rel).read_text() for rel in CORE):
            raise ValueError("missing substantive neutral core")
        operation = "Layout"
        layout = json.loads((package / MAP).read_text())
        if not isinstance(layout, dict) or set(layout) != {"package", "version", "profile", "files", "roles"} or layout.get("package") != "methodology-dsh" or layout.get("version") != "3.0.1" or layout.get("profile") != "colocated-explicit-source" or layout.get("roles") != ROLES:
            raise ValueError("unsupported package profile")
        rows = layout.get("files")
        if not isinstance(rows, list) or not rows:
            raise ValueError("complete declared file list required")
        declared = []
        operation = "Member"
        for ordinal, row in enumerate(rows):
            if not isinstance(row, dict) or set(row) != {"path", "kind"} or not isinstance(row.get("path"), str) or not isinstance(row.get("kind"), str) or not row["kind"].strip():
                raise ValueError("path/kind record required without circular hashes")
            relative = row["path"]
            posix = pathlib.PurePosixPath(relative)
            if not relative or "\\" in relative or posix.is_absolute() or any(p in (".", "..") for p in relative.split("/")) or posix.as_posix() != relative:
                raise ValueError("unsafe package path")
            if row["kind"] != EXPECTED_KINDS.get(relative):
                raise ValueError("package member kind differs from accepted design")
            path = package / relative
            if any(parent.is_symlink() for parent in [path] + list(path.parents)[:len(posix.parts) - 1]) or not path.is_file() or package.resolve() not in path.resolve().parents:
                raise ValueError("missing or nonregular contained package member")
            declared.append(relative)
            LOGGER.info("[IMP:9][_package_assembly][MEMBER_VALID] ordinal=%d", ordinal)
        if declared != sorted(declared) or len(set(declared)) != len(declared) or tuple(declared) != tuple(p for p in EXPECTED_PATHS if p != MAP):
            raise ValueError("declared package membership differs from accepted design")
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
        plugin = json.loads((package / ".dsh-plugin/plugin.json").read_text())
        if plugin.get("name") != "methodology-dsh" or plugin.get("version") != "3.0.1":
            raise ValueError("native metadata identity mismatch")
        bundle = json.loads((package / "package.json").read_text())
        if bundle.get("name") != "@methodology/dsh" or bundle.get("dsh", {}).get("bundle", {}).get("patch") != "./cordis.patch.yml":
            raise ValueError("bundle manifest mismatch")
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
## @purpose Expose actual owning important records before the test assertions.
## @uses builtins.print
## @io Input: captured real records. Output: None. Side effects: visible same-process stdout only; no external sink. Guarantees: only this module's importance7-10 records exposed. Raises: none under supplied LogRecord input. System importance:8. Example: expose assembly validation and failure records.
## @complexity 2
def _show_trace(records):
    for record in records:
        if record.name == LOGGER.name and any("[IMP:%d]" % n in record.getMessage() for n in range(7, 11)):
            print(record.getMessage())
# endregion FUNC__show_trace


# region FUNC_test_neutral_boundary_and_complete_package [DOMAIN(9): Boundary; CONCEPT(10): RealFilesystem; TECH(7): pytest]
## @purpose Verify the actual complete shipped package and scoped neutral boundary through real source and the actual common checker.
## @uses test_dsh_package._package_assembly, test_dsh_package._show_trace, conformlib.markdown.list_neutral_files, run_cli
## @io Input: current canonical repo_root, owned repo_copy/tmp_path and actual caplog/runner/deny fixture. Output: None after exact75/71/69/2 and malformed ordinary-root refusal.
##   Side effects: only owned bad Markdown created then removed; real checker output and visible critical trace. Guarantees: original tree untouched; expected membership is independent. Raises: AssertionError for incorrect source/boundary/verdict. System importance:9. Example: native SKILL cards are excluded, ordinary bad card fails.
## @complexity 5
def test_neutral_boundary_and_complete_package(repo_root, repo_copy, caplog, run_cli, deny_list):
    from conformlib.markdown import list_neutral_files
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    declared = _package_assembly(repo_root)
    produced = set(list_neutral_files(str(repo_root)))
    expected = {p.relative_to(repo_root).as_posix() for p in repo_root.rglob("*.md") if p.relative_to(repo_root).parts[0] not in {".git", "tests", "examples", "implementations", "doxygen_output", "__pycache__", ".pytest_cache"} and p.relative_to(repo_root).as_posix() not in {"README.md", "CHANGELOG.md"}}
    _show_trace(caplog.records)
    assert produced == expected and len(produced) == 71
    assert len(declared) == 75 and sum(p.startswith("skills/") and p.endswith("/SKILL.md") for p in declared) == 27
    assert sum(p.startswith("roles/") for p in declared) == 6 and sum("/scripts/" in p and p.endswith(".py") for p in declared) == 6
    assert any("[VALIDATION_SUCCESS]" in r.getMessage() for r in caplog.records)
    assert not [r for r in caplog.records if r.levelno >= logging.ERROR]
    statuses = [(repo_root / p).read_text().split("status: ", 1)[1].split("\n", 1)[0] for p in expected]
    assert statuses.count("draft") == 69 and statuses.count("stub") == 2
    control_code, control_out, _ = run_cli(["self", "--root", str(repo_copy), "--deny-list", str(deny_list[0]), "--json"])
    print("[IMP:9][test_neutral_boundary_and_complete_package][CONTROL] exit=%d" % control_code)
    assert control_code == 0
    target = repo_copy / "ordinary-malformed.md"
    assert not target.exists()
    try:
        target.write_text("ordinary Markdown without a neutral card\n")
        code, output, _ = run_cli(["self", "--root", str(repo_copy), "--deny-list", str(deny_list[0]), "--json"])
        hits = [row for row in json.loads(output)["rows"] if row["rule"] == "card.present" and row["subject"] == target.name and row["status"] == "FAIL"]
        print("[IMP:9][test_neutral_boundary_and_complete_package][REFUSAL] exit=%d hits=%d" % (code, len(hits)))
        assert code == 1 and hits
    finally:
        target.unlink(missing_ok=True)
    restored, _, _ = run_cli(["self", "--root", str(repo_copy), "--deny-list", str(deny_list[0]), "--json"])
    assert restored == 0 and not target.exists()
# endregion FUNC_test_neutral_boundary_and_complete_package


# region FUNC_test_package_assembly_refusals [DOMAIN(9): Package; CONCEPT(10): DiscriminatingRefusal, Restoration; TECH(7): pytest]
## @purpose Reject real owned assembly defects while preserving every untouched package sibling and restoring complete originals.
## @uses test_dsh_package._package_assembly, test_dsh_package._show_trace, pathlib.Path.write_bytes, pathlib.Path.chmod
## @io Input: complete owned repo_copy and caplog. Output: None after missing/extra/sibling/unsafe/duplicate/profile/detached/linked cases refuse and restore.
##   Side effects: owned mutations with exact bytes/modes restored; safe visible failure trace. Guarantees: expected failures own their importance10 and no unrelated error. Raises: AssertionError for nonrefusal or restoration loss. System importance:9. Example: an extra package file fails even when the declaration remains valid.
## @complexity 6
def test_package_assembly_refusals(repo_copy, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    package = repo_copy / "implementations/dsh"
    manifest = package / MAP
    original, mode = manifest.read_bytes(), stat.S_IMODE(manifest.stat().st_mode)
    sibling = package / "roles/qa.md"
    sibling_bytes, sibling_mode = sibling.read_bytes(), stat.S_IMODE(sibling.stat().st_mode)
    cases = ("missing", "extra", "sibling", "unsafe", "absolute", "duplicate", "profile", "detached", "linked", "malformed", "missing-declaration", "kind", "wrong-kind", "package-output", "package-runtime", "map-member", "plugin-identity")
    for case in cases:
        caplog.clear()
        altered = json.loads(original)
        target = None
        saved = None
        try:
            if case == "missing":
                target = package / "roles/coder.md"
                saved = (target.read_bytes(), stat.S_IMODE(target.stat().st_mode))
                target.unlink()
            elif case == "extra":
                target = package / "undeclared.txt"
                target.write_text("unaccounted public member\n")
            elif case in ("package-output", "package-runtime"):
                folder = package / ("output" if case == "package-output" else ".methodology")
                folder.mkdir()
                target = folder / "newfile"
                target.write_text("undeclared package runtime effect\n")
            elif case == "sibling":
                target = package.parent / "unknown-engine"
                target.mkdir()
            elif case == "unsafe":
                altered["files"][0]["path"] = "../escape.txt"
                manifest.write_text(json.dumps(altered))
            elif case == "absolute":
                altered["files"][0]["path"] = "/escaping.txt"
                manifest.write_text(json.dumps(altered))
            elif case == "malformed":
                manifest.write_text("{")
            elif case == "missing-declaration":
                altered["files"].pop()
                manifest.write_text(json.dumps(altered))
            elif case == "kind":
                altered["files"][0]["kind"] = ""
                manifest.write_text(json.dumps(altered))
            elif case == "wrong-kind":
                altered["files"][0]["kind"] = "documentation"
                manifest.write_text(json.dumps(altered))
            elif case == "duplicate":
                altered["files"].append(dict(altered["files"][0]))
                manifest.write_text(json.dumps(altered))
            elif case == "profile":
                altered["profile"] = "detached-cached"
                manifest.write_text(json.dumps(altered))
            elif case == "map-member":
                altered["files"].append({"path": MAP, "kind": "layout"})
                manifest.write_text(json.dumps(altered))
            elif case == "plugin-identity":
                target = package / ".dsh-plugin/plugin.json"
                saved = (target.read_bytes(), stat.S_IMODE(target.stat().st_mode))
                changed = json.loads(target.read_text())
                changed["name"] = "methodology-other"
                target.write_text(json.dumps(changed))
            elif case == "detached":
                target = repo_copy / "SPEC_VERSION"
                saved = (target.read_bytes(), stat.S_IMODE(target.stat().st_mode))
                target.unlink()
            elif case == "linked":
                target = package / "linked-member"
                target.symlink_to(sibling)
            with pytest.raises(ValueError):
                _package_assembly(repo_copy)
            _show_trace(caplog.records)
            errors = [r for r in caplog.records if r.levelno >= logging.ERROR]
            assert len(errors) == 1 and "[_package_assembly][FAILURE]" in errors[0].getMessage()
            assert sibling.read_bytes() == sibling_bytes and stat.S_IMODE(sibling.stat().st_mode) == sibling_mode
        finally:
            manifest.write_bytes(original)
            manifest.chmod(mode)
            if target is not None:
                if target.is_dir() and not target.is_symlink():
                    target.rmdir()
                else:
                    target.unlink(missing_ok=True)
                if saved is not None:
                    target.write_bytes(saved[0])
                    target.chmod(saved[1])
                if case in ("package-output", "package-runtime"):
                    target.parent.rmdir()
        if saved is not None:
            print("[IMP:9][test_package_assembly_refusals][RESTORED_TARGET] case=%s bytes_equal=%s mode_equal=%s" %
                  (case, target.read_bytes() == saved[0], stat.S_IMODE(target.stat().st_mode) == saved[1]))
            assert target.read_bytes() == saved[0]
            assert stat.S_IMODE(target.stat().st_mode) == saved[1]
        caplog.clear()
        restored = _package_assembly(repo_copy)
        _show_trace(caplog.records)
        assert tuple(restored) == tuple(p for p in EXPECTED_PATHS if p != MAP)
        assert manifest.read_bytes() == original and stat.S_IMODE(manifest.stat().st_mode) == mode
        assert not [r for r in caplog.records if r.levelno >= logging.ERROR]
# endregion FUNC_test_package_assembly_refusals
