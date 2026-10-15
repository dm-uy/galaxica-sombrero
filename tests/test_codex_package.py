# region MODULE_CONTRACT [DOMAIN(9): PackageBoundary; CONCEPT(10): IndependentAssembly, PublicCoverage; TECH(7): Python, pytest]
## @modulecontract
## @purpose Verify the shipped typed Codex package's complete declared assembly independently of the production neutral classifier.
## @scope Exact planned package paths/profile/role locations and ordinary-versus-native Markdown boundary; malformed membership/profile/path controls.
## @input Current complete canonical public source and isolated owned copies; fixed accepted-plan inventory as independent expected input.
## @output Assertions over actual source paths, profile and metadata; visible own validation/failure trajectories and exact negative restoration.
## @links [USES_API(8): pathlib, json, logging; READS_DATA_FROM(9): implementations/codex/references/package-layout.json]
## @invariants
## - Original source is read-only; negative controls affect only owned copies and restore original full bytes/numeric modes.
## - Expected73 paths derive from the accepted design, never from the observed producer result or imported neutral classifier.
## - Package assembly does not prove semantic full-rule adoption, human authority or actual native execution.
## @rationale
## Q: Why a separate package oracle?
## A: Neutral exclusion cannot prove native completeness; bidirectional independent membership rejects missing, extra and sibling packages.
## Q: Why retain an outside-namespace negative?
## A: The native exception is typed and scoped; an ordinary malformed Markdown file must still fail the actual common checker.
## @changes
## LAST_CHANGE: [2.0.0 - M30 exact current release/census coupling; all prior cases/assertions/refusals retained.]
## Earlier: [v1.0.1 - M22: the declared sibling set is {codex, claude} (an ambient, git-ignored macOS .DS_Store beside them is not a sibling); an unknown sibling is still refused. Earlier: exact M19 package/boundary checks with independent73-path oracle and restored contrary inputs.]
## @modulemap
## FUNC 9[Independent actual package assembly/profile/path judgment] => test_codex_package._package_assembly
## FUNC 8[Expose owning important captured records before assertions] => test_codex_package._show_trace
## FUNC 9[Actual neutral/native boundary and valid complete package] => test_codex_package.test_neutral_boundary_and_complete_package
## FUNC 9[Missing/extra/sibling/unsafe/detached assembly controls] => test_codex_package.test_package_assembly_refusals
## @usecases
## - [test_neutral_boundary_and_complete_package]: Owner -> check exact actual source populations -> native docs separated and ordinary malformed prose refused.
## - [test_package_assembly_refusals]: QA -> perturb owned package membership/profile -> rejected real defect and fully restored source.
## @GREP_SUMMARY package, independent inventory,73paths, typed namespace, source profile, siblings, unsafe paths, restoration
## @STRUCTURE ▶ canonical source → ◇ independent73path/profile match → ⊕ positive result → ○ owned mutations → ◇ refuse → ⎋ restore
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
# Declared implementation packages of this repository; any other sibling is refused (M22 added the Claude package).
DECLARED_PACKAGES = {"codex", "claude"}
CORE = ("concepts/principles.md", "roles/_base.md", "code/exoskeleton.md", "code/ldd.md", "code/doxygen.md", "code/tests.md")
ROLES = {name: "roles/" + name + ".md" for name in ("architect", "coder", "debugger", "qa", "reviewer", "searcher")}
EXPECTED_PATHS = ('.codex-plugin/plugin.json', 'Doxyfile', 'README.md', 'adapter.json', 'examples/smoke-spec.md', 'pytest.ini', 'references/adoption.md', 'references/codex-runtime.md', 'references/consumer-pm-profile.md', 'references/handoffs.md', 'references/package-layout.json', 'references/source-disposition.md', 'roles/architect.md', 'roles/coder.md', 'roles/debugger.md', 'roles/qa.md', 'roles/reviewer.md', 'roles/searcher.md', 'skills/analyzer/SKILL.md', 'skills/ax-ui-contract/SKILL.md', 'skills/brainstorm/SKILL.md', 'skills/brownfield-spec-template/SKILL.md', 'skills/code-review/SKILL.md', 'skills/data-transform/SKILL.md', 'skills/devplan-protocol/SKILL.md', 'skills/devplan-protocol/scripts/visual_gate_lint.py', 'skills/document-protocol/SKILL.md', 'skills/durable-layer/SKILL.md', 'skills/feature-dev/SKILL.md', 'skills/feature-dev/scripts/run_state.py', 'skills/graph-protocol/SKILL.md', 'skills/greenfield-bootstrap/SKILL.md', 'skills/hitl-gates/SKILL.md', 'skills/pm-bootstrap/SKILL.md', 'skills/pm-handoff/SKILL.md', 'skills/pm-plan-batch/SKILL.md', 'skills/pm-run-batch/SKILL.md', 'skills/pm/SKILL.md', 'skills/pm/scripts/codemap.py', 'skills/pm/scripts/consumer_files.py', 'skills/pm/scripts/markup_migrate.py', 'skills/pm/scripts/orient.py', 'skills/pm/templates/AGENTS.md', 'skills/pm/templates/CLAUDE.md', 'skills/pm/templates/CONVENTIONS.md', 'skills/pm/templates/DEC.md', 'skills/pm/templates/Doxyfile', 'skills/pm/templates/HANDOFF.md', 'skills/pm/templates/OPEN_QUESTIONS.md', 'skills/pm/templates/RECON.md', 'skills/pm/templates/ROADMAP.md', 'skills/pm/templates/SPEC.md', 'skills/pm/templates/TASKS.md', 'skills/pm/templates/VISION.md', 'skills/pm/templates/gitignore', 'skills/prod-log-vacuum/SKILL.md', 'skills/prompting-agent-design/SKILL.md', 'skills/prompting-decompose/SKILL.md', 'skills/prompting-markup/SKILL.md', 'skills/prompting-verify/SKILL.md', 'skills/prompting/SKILL.md', 'skills/roadmap/SKILL.md', 'skills/semantic-exoskeleton/SKILL.md', 'skills/spec-recon/SKILL.md', 'tests/test_adoption.py', 'tests/test_codemap.py', 'tests/test_consumer_files.py', 'tests/test_consumer_pm.py', 'tests/test_guide.md', 'tests/test_markup_migrate.py', 'tests/test_native_contract.py', 'tests/test_run_state.py', 'tests/test_visual_gate.py')


EXPECTED_KINDS = {path: ("skill" if path.endswith("/SKILL.md") else
                         "role" if path.startswith("roles/") else
                         "helper" if "/scripts/" in path else
                         "test-guide" if path == "tests/test_guide.md" else
                         "test" if path.startswith("tests/") else
                         "config" if path in ("Doxyfile", "pytest.ini", "skills/pm/templates/Doxyfile", "skills/pm/templates/gitignore") else
                         "plugin-manifest" if path == ".codex-plugin/plugin.json" else
                         "adapter" if path == "adapter.json" else
                         "layout" if path == "references/package-layout.json" else
                         "example" if path.startswith("examples/") else "documentation")
                  for path in EXPECTED_PATHS}

# region FUNC__package_assembly [DOMAIN(9): Package; CONCEPT(10): IndependentOracle; TECH(7): pathlib, json]
## @purpose Refuse incomplete or unsafe actual package assembly before reporting the independently specified complete profile.
## @uses pathlib.Path.read_text, pathlib.Path.rglob, json.loads, logging.Logger.info, logging.Logger.error
## @io Input: root pathlib.Path of complete co-located source. Output: sorted list of73 exact declared relative paths.
##   Side effects: source reads and safe structured trajectory only; no source/state mutation. Guarantees: exact planned membership/profile/roles and regular contained paths; no claim of mental adoption or sandboxing.
##   Raises: ValueError for malformed layout, duplicate/unsafe path, missing/extra/sibling package or detached neutral dependency; OSError/UnicodeError for unreadable files.
##   System importance:10 for complete source boundary. Example: the current complete co-located package returns its sorted73path set.
## @complexity 7
def _package_assembly(root):
    operation, ordinal = "Binding", -1
    try:
        # START_BLOCK_Validation
        LOGGER.info("[IMP:7][_package_assembly][READ] read co-located package binding")
        package = root / "implementations/codex"
        if not package.is_dir() or package.is_symlink():
            raise ValueError("regular owned co-located package directory required")
        if set(p.name for p in package.parent.iterdir() if p.name != ".DS_Store") != DECLARED_PACKAGES:
            raise ValueError("unknown sibling package")
        if not (root / "SPEC_VERSION").is_file() or (root / "SPEC_VERSION").read_text() != "3.0.1\n":
            raise ValueError("unsupported detached neutral dependency")
        if not all((root / rel).is_file() and "status: draft\n" in (root / rel).read_text() for rel in CORE):
            raise ValueError("missing substantive neutral core")
        operation = "Layout"
        layout = json.loads((package / "references/package-layout.json").read_text())
        if not isinstance(layout, dict) or set(layout) != {"package", "version", "profile", "files", "roles"} or layout.get("package") != "methodology-codex" or layout.get("version") != "3.0.1" or layout.get("profile") != "colocated-explicit-source" or layout.get("roles") != ROLES:
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
        if declared != sorted(declared) or len(set(declared)) != len(declared) or tuple(declared) != EXPECTED_PATHS:
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
        plugin = json.loads((package / ".codex-plugin/plugin.json").read_text())
        if plugin.get("name") != "methodology-codex" or plugin.get("version") != "3.0.1":
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
## @purpose Expose actual owning important records before the test assertions.
## @uses builtins.print
## @io Input: captured real records. Output: None. Side effects: visible same-process stdout only; no external sink. Guarantees: only this module's importance7–10 records exposed. Raises: none under supplied LogRecord input. System importance:8. Example: expose assembly validation and failure records.
## @complexity 2
def _show_trace(records):
    for record in records:
        if record.name == LOGGER.name and any("[IMP:%d]" % n in record.getMessage() for n in range(7, 11)):
            print(record.getMessage())
# endregion FUNC__show_trace

# region FUNC_test_neutral_boundary_and_complete_package [DOMAIN(9): Boundary; CONCEPT(10): RealFilesystem; TECH(7): pytest]
## @purpose Verify the actual complete shipped package and scoped neutral boundary through real source and the actual common checker.
## @uses test_codex_package._package_assembly, test_codex_package._show_trace, conformlib.markdown.list_neutral_files, run_cli
## @io Input: current canonical repo_root, owned repo_copy/tmp_path and actual caplog/runner/deny fixture. Output: None after exact73/71/69/2 and malformed ordinary-root refusal.
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
    assert len(declared) == 73 and sum(p.startswith("skills/") and p.endswith("/SKILL.md") for p in declared) == 27
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
## @uses test_codex_package._package_assembly, test_codex_package._show_trace, pathlib.Path.write_bytes, pathlib.Path.chmod
## @io Input: complete owned repo_copy and caplog. Output: None after missing/extra/sibling/unsafe/duplicate/profile/detached/linked cases refuse and restore.
##   Side effects: owned mutations with exact bytes/modes restored; safe visible failure trace. Guarantees: expected failures own their importance10 and no unrelated error. Raises: AssertionError for nonrefusal or restoration loss. System importance:9. Example: an extra package file fails even when the declaration remains valid.
## @complexity 6
def test_package_assembly_refusals(repo_copy, caplog):
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    package = repo_copy / "implementations/codex"
    manifest = package / "references/package-layout.json"
    original, mode = manifest.read_bytes(), stat.S_IMODE(manifest.stat().st_mode)
    sibling = package / "roles/qa.md"
    sibling_bytes, sibling_mode = sibling.read_bytes(), stat.S_IMODE(sibling.stat().st_mode)
    cases = ("missing", "extra", "sibling", "unsafe", "absolute", "duplicate", "profile", "detached", "linked", "malformed", "missing-declaration", "kind", "wrong-kind", "package-output", "package-runtime")
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
        assert tuple(restored) == EXPECTED_PATHS
        assert manifest.read_bytes() == original and stat.S_IMODE(manifest.stat().st_mode) == mode
        assert not [r for r in caplog.records if r.levelno >= logging.ERROR]
# endregion FUNC_test_package_assembly_refusals
