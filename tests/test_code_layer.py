# region MODULE_CONTRACT [DOMAIN(9): CodeLayer, Markup, Documentation; CONCEPT(9): Exoskeleton, Regions, AntiLoop, Doxygen; TECH(6): pytest, ast, subprocess]
## @modulecontract
## @purpose To prove that the code of this repository keeps the layer its maintainers rely on: every Python module opens with
## the module contract before its imports, every definition sits in its region, the backend stays a layer that returns data
## and never prints, exits or parses arguments, only the standard library is imported, the test guide maps every acceptance
## criterion to tests that exist, the Anti-Loop ladder escalates in a real pytest session, the code map builds silently, and
## the repository carries the owner's complete fixed canonical MIT licence without any remote observation.
## @scope Every .py file under tools/ and tests/ and the extensionless launcher bin/conform; the Doxyfile, the .gitignore,
## tests/test_guide.md, the root LICENSE; owned Git configuration only in the explicit ordinary-clone regression.
## @input The repository on disk; a copy of it for the Doxygen build; a scratch project for the nested pytest session.
## @output One pass or fail per property of the code layer.
## @links [USES_API(8): ast; USES_API(8): subprocess; USES_API(6): doxygen; READS_DATA_FROM(7): tests/test_guide.md; READS_DATA_FROM(6): Doxyfile]
## @links_to_spec AC-11, AC-P1, AC-P7
## @invariants
## - Structural checks read syntax trees/lines; license regressions invoke their actual owning assertion on isolated real files.
## - The Doxygen build and the nested pytest session run in a temporary copy, never in the repository.
## - A missing doxygen is a failure of the suite, not a skip: a skipped build would report green over nothing.
## @rationale
## Q: Why a syntax tree for the layer checks and not a text search?
## A: A text search cannot tell a print call from the word print in a comment or a string, and cannot find the end of a
## definition; the tree can, so a check neither misses a violation nor invents one.
## Q: Why a nested pytest session for the Anti-Loop ladder?
## A: The ladder lives in session hooks; only a real session reaches them, so a test that called the message function alone
## would leave the counter file and the printing unproved.
## @changes
## LAST_CHANGE: [v0.6.2 - M25A: independent full canonical MIT, no remote queries, damaged-body and real origin preservation controls.]
## - [v0.6.0 - Select current navigation by tags unless a complete adjacent legacy pair declares compatibility; keep known current modules forced.]
## @modulemap
## FUNC 6[The Python files under check] => _python_files
## FUNC 6[The pairs of region tags of a file] => _region_spans
## FUNC 6[The trace line of a test] => _trace
## FUNC 6[The names of all test functions] => _test_function_names
## FUNC 6[The rows of the acceptance table of the guide] => _guide_rows
## FUNC 6[The settings of the Doxyfile] => _doxyfile_settings
## FUNC 9[Every module opens with the contract before its imports] => test_every_python_module_has_the_exoskeleton_before_imports
## FUNC 8[Region tags are paired and named] => test_regions_are_balanced
## FUNC 8[Every top-level definition sits in its region] => test_top_level_definitions_sit_in_regions
## FUNC 8[The backend neither prints nor exits nor parses arguments] => test_backend_neither_prints_nor_exits_nor_parses_arguments
## FUNC 8[Only allowlisted modules are imported] => test_imports_are_in_the_allowlist
## FUNC 6[The interpreter is supported and the syntax is Python 3.9] => test_interpreter_is_supported
## FUNC 9[The guide maps every criterion to existing tests] => test_test_guide_maps_every_ac_to_existing_tests
## FUNC 6[The guide names the commands] => test_guide_names_the_commands
## FUNC 7[The guide's trace markers exist in the tool] => test_guide_markers_exist_in_the_tool_source
## FUNC 8[The ladder escalates in a real session] => test_anti_loop_ladder_escalates_and_stops
## FUNC 7[The Doxyfile covers the tree] => test_doxyfile_covers_tools_bin_tests
## FUNC 8[The build is silent and maps the tool] => test_doxygen_builds_silently_and_maps_the_tool
## FUNC 6[The output is ignored] => test_gitignore_ignores_doxygen_output
## FUNC 9[Complete fixed MIT with no remote observation] => test_code_layer.test_mit_license_and_no_remote
## FUNC 9[Real damaged bodies/file population fail, canonical restored] => test_code_layer.test_full_mit_license_rejects_damaged_bodies
## FUNC 9[Real origin clone passes without subprocess observation] => test_code_layer.test_mit_license_accepts_origin_without_remote_observation
## @usecases
## - [test_top_level_definitions_sit_in_regions]: Agent -> edits a function -> a definition left outside its region turns the suite red
## - [test_anti_loop_ladder_escalates_and_stops]: Agent -> fails the suite five times -> the fifth run tells it to stop and ask
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: code layer tests, exoskeleton before imports, region balance, ast top-level definitions, backend purity, import allowlist, test guide mapping, Anti-Loop nested pytest, Doxyfile, doxygen build, gitignore, complete canonical MIT, no remote observation
# STRUCTURE: ▶ files ┌tools, tests, bin/conform┐ → ⊕ ast ∧ lines → ◇ contract ≺ imports ∧ regions ⊇ defs ∧ backend ⊥ print → ⚡ nested pytest ×6 → ⚡ doxygen copy → ∑ guide rows → ⎋ assert

import ast
import json
import logging
import os
import pathlib
import re
import shutil
import subprocess
import sys
from typing import Dict, List, Set, Tuple

import pytest


CANONICAL_MIT = 'MIT License\n\nCopyright (c) 2026 agent-methodology contributors\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n'

ALL_MODULES = {
    "__future__", "argparse", "dataclasses", "datetime", "hashlib", "json", "logging", "os", "pathlib", "re", "secrets",
    "shutil", "stat", "sys", "typing", "conform", "conformlib",
}
TEST_ONLY_MODULES = {"subprocess", "ast", "pytest", "flow_contract_probe", "xml"}
REQUIRED_CONTRACT_TAGS = (
    "## @modulecontract", "## @purpose", "## @scope", "## @input", "## @output", "## @links", "## @invariants",
    "## @rationale", "## @changes", "## @modulemap", "## @usecases",
)
REGION_LINE_RE = re.compile(r"^\s*# (region|endregion) (\S+)")
GUIDE_TEST_NAME_RE = re.compile(r"test_[a-z0-9_]+")
CRITERIA = tuple("AC-%d" % n for n in range(1, 13)) + tuple("AC-P%d" % n for n in range(1, 8))
FINALIZE_ALLOWED = {"AC-10", "AC-P2", "AC-P5", "AC-P6"}
GUIDE_MARKERS = (
    "[run_self][VERDICT]", "[run_adapter][VERDICT]", "[canary_probe][BITE]", "[scan_tree][FINDING]",
    "[check_vendored][DRIFT]", "[main][EXIT]",
)
GUIDE_COMMANDS = (
    "python3 -m pytest tests -s -v",
    "doxygen Doxyfile",
    "bin/conform self --deny-list PRIVATE_DENY_LIST",
    "bin/conform adapter examples/adapter.example.json",
)
BACKEND_FORBIDDEN_CALLS = {"print", "exit", "quit", "input"}
BACKEND_FORBIDDEN_MODULES = {"argparse"}
BACKEND_FORBIDDEN_ATTRIBUTES = {("sys", "exit"), ("sys", "stdout"), ("sys", "stderr"), ("sys", "stdin"), ("sys", "argv")}
BACKEND_FORBIDDEN_NAMES = {"SystemExit", "StreamHandler", "basicConfig"}


# region FUNC__python_files [DOMAIN(7): CodeLayer; CONCEPT(8): FileSet; TECH(4): pathlib]
## @purpose The Python files under check: everything under tools/ except caches, every test module, and the launcher, which
## has no extension but is Python.
## @io pathlib.Path -> List[pathlib.Path]
## @complexity 3
def _python_files(root: pathlib.Path) -> List[pathlib.Path]:
    found = []
    for path in sorted((root / "tools").rglob("*.py")):
        if "__pycache__" not in path.parts:
            found.append(path)
    for path in sorted((root / "tests").glob("*.py")):
        found.append(path)
    found.append(root / "bin" / "conform")
    return found
# endregion FUNC__python_files


# region FUNC__region_spans [DOMAIN(8): CodeLayer; CONCEPT(9): Regions, Pairing; TECH(4): re]
## @purpose Pair the region tags of a file's lines into (name, first line, last line) spans, 1-based; the second list holds
## the problems found while pairing: an endregion with no open region, a mismatched name, a region never closed.
## @io List[str] -> Tuple[List[Tuple[str, int, int]], List[str]]
## @complexity 4
def _region_spans(lines: List[str]) -> Tuple[List[Tuple[str, int, int]], List[str]]:
    spans = []
    problems = []
    stack = []
    for index, line in enumerate(lines, start=1):
        found = REGION_LINE_RE.match(line)
        if not found:
            continue
        kind, name = found.group(1), found.group(2)
        if kind == "region":
            stack.append((name, index))
            continue
        if not stack:
            problems.append("line %d: endregion %s closes nothing" % (index, name))
            continue
        open_name, open_line = stack.pop()
        if open_name != name:
            problems.append("line %d: endregion %s closes region %s of line %d" % (index, name, open_name, open_line))
        spans.append((open_name, open_line, index))
    for open_name, open_line in stack:
        problems.append("line %d: region %s is never closed" % (open_line, open_name))
    return spans, problems
# endregion FUNC__region_spans


# region FUNC__trace [DOMAIN(6): TestHarness; CONCEPT(7): LDD, Trace; TECH(3): print]
## @purpose Print one importance-9 trace line before a test's asserts, so a red test shows what it looked at.
## @io (str, str, str) -> None
## @complexity 1
def _trace(test_name: str, block: str, text: str) -> None:
    print("[IMP:9][%s][%s] %s" % (test_name, block, text))
# endregion FUNC__trace


# region FUNC__test_function_names [DOMAIN(7): CodeLayer; CONCEPT(8): Guide, Names; TECH(4): ast]
## @purpose The names of the test functions defined at module level in every tests/test_*.py file.
## @io pathlib.Path -> Set[str]
## @complexity 3
def _test_function_names(root: pathlib.Path) -> Set[str]:
    names = set()
    for path in sorted((root / "tests").glob("test_*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and node.name.startswith("test_"):
                names.add(node.name)
    return names
# endregion FUNC__test_function_names


# region FUNC__guide_rows [DOMAIN(7): CodeLayer; CONCEPT(8): Guide, Table; TECH(4): str.split]
## @purpose The rows of the acceptance table of tests/test_guide.md as a map from the criterion id to its tests cell; a row
## is a line that opens with a pipe and an AC id.
## @io pathlib.Path -> Dict[str, str]
## @complexity 3
def _guide_rows(root: pathlib.Path) -> Dict[str, str]:
    rows = {}
    for line in (root / "tests" / "test_guide.md").read_text(encoding="utf-8").split("\n"):
        if not line.startswith("| AC-"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        rows[cells[0].split(" ")[0]] = cells[1]
    return rows
# endregion FUNC__guide_rows


# region FUNC__doxyfile_settings [DOMAIN(7): Documentation; CONCEPT(8): Doxyfile, Settings; TECH(4): str.partition]
## @purpose The settings of a Doxyfile as a map from key to the value string, without comments and blank lines and with the
## backslash continuation joined.
## @io pathlib.Path -> Dict[str, str]
## @complexity 4
def _doxyfile_settings(path: pathlib.Path) -> Dict[str, str]:
    settings = {}
    pending = ""
    for raw in path.read_text(encoding="utf-8").split("\n"):
        line = raw.strip()
        if not pending and (not line or line.startswith("#")):
            continue
        if line.endswith("\\"):
            pending += line[:-1].strip() + " "
            continue
        line = pending + line
        pending = ""
        key, _, value = line.partition("=")
        settings[key.strip()] = value.strip()
    return settings
# endregion FUNC__doxyfile_settings


# region FUNC_test_every_python_module_has_the_exoskeleton_before_imports [DOMAIN(9): CodeLayer; CONCEPT(9): Exoskeleton, FileTop; TECH(5): ast, lines]
## @purpose Prove the file-top order of every Python module: an optional shebang, the module contract region with its tags
## and the anchor function; known current modules and new tag-declared modules use in-contract navigation, while a complete
## adjacent standalone pair preserves legacy modules, including hybrids; all navigation precedes imports, with no module docstring.
## @io repo_root -> None
## @complexity 6
def test_every_python_module_has_the_exoskeleton_before_imports(repo_root):
    problems = []
    files = _python_files(repo_root)
    for path in files:
        name = str(path.relative_to(repo_root))
        text = path.read_text(encoding="utf-8")
        lines = text.split("\n")
        tree = ast.parse(text)
        cursor = 0
        if lines[0].startswith("#!"):
            if name != "bin/conform":
                problems.append("%s: a shebang on a module that is not the launcher" % name)
            cursor = 1
        if not lines[cursor].startswith("# region MODULE_CONTRACT"):
            problems.append("%s: line %d is not the MODULE_CONTRACT region" % (name, cursor + 1))
            continue
        end = -1
        for index in range(cursor, len(lines)):
            if lines[index].startswith("# endregion MODULE_CONTRACT"):
                end = index
                break
        if end < 0:
            problems.append("%s: MODULE_CONTRACT is never closed" % name)
            continue
        block = lines[cursor:end + 1]
        joined = "\n".join(block)
        positions = []
        for tag in REQUIRED_CONTRACT_TAGS:
            found = [n for n, line in enumerate(block) if line.startswith(tag)]
            if not found:
                problems.append("%s: contract tag %s is missing" % (name, tag))
            else:
                positions.append(found[0])
        if positions != sorted(positions):
            problems.append("%s: contract tags are out of order" % name)
        if "def _module_contract():" not in joined:
            problems.append("%s: the def _module_contract anchor is missing" % name)
        if block[-2].strip() != "pass" or not block[-3].startswith("def _module_contract():"):
            problems.append("%s: the anchor is not the last statement of the region" % name)
        # BUG_FIX_CONTEXT: Legacy hybrids also carry interior current tags; their complete adjacent legacy pair declares compatibility.
        # Known current modules remain forced so adding legacy lines cannot bypass their current-format assertions.
        if name in {"tests/test_skeleton.py", "tests/test_first_layer.py", "tests/test_flow_contract.py", "tests/flow_contract_probe.py", "tests/test_design_contract.py"} or (
            any(line.startswith(("## @GREP_SUMMARY ", "## @STRUCTURE ")) for line in block)
            and not (
                len(lines) >= end + 3
                and lines[end + 1].startswith("# GREP_SUMMARY: ")
                and lines[end + 2].startswith("# STRUCTURE: ")
            )
        ):
            _trace("test_every_python_module_has_the_exoskeleton_before_imports", "CURRENT_MARKUP", "checking in-contract navigation tags")
            tags = [line for line in block if line.startswith("## @")]
            if len(tags) < 2 or not tags[-2].startswith("## @GREP_SUMMARY ") or not tags[-1].startswith("## @STRUCTURE "):
                problems.append("%s: navigation tags are not the last contract tags" % name)
            if any(line.startswith(("# GREP_SUMMARY:", "# STRUCTURE:")) for line in lines):
                problems.append("%s: new module uses historical standalone navigation" % name)
        else:
            if len(lines) < end + 3 or not lines[end + 1].startswith("# GREP_SUMMARY: "):
                problems.append("%s: line %d is not the GREP_SUMMARY line" % (name, end + 2))
            if len(lines) < end + 3 or not lines[end + 2].startswith("# STRUCTURE: "):
                problems.append("%s: line %d is not the STRUCTURE line" % (name, end + 3))
        if ast.get_docstring(tree) is not None:
            problems.append("%s: a module docstring duplicates the contract purpose" % name)
        first_import = min(
            [node.lineno for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom)) and node.col_offset == 0]
            or [10 ** 9]
        )
        if first_import <= end + 3:
            problems.append("%s: an import stands at line %d, before the module markup ends" % (name, first_import))
        body_first = tree.body[0]
        if not (isinstance(body_first, ast.FunctionDef) and body_first.name == "_module_contract"):
            problems.append("%s: the first statement is not the _module_contract anchor" % name)
    _trace("test_every_python_module_has_the_exoskeleton_before_imports", "FILES", "checked %d files, %d problems" % (len(files), len(problems)))
    assert len(files) >= 12, "the file set is too small: %d" % len(files)
    assert problems == [], "\n".join(problems)
# endregion FUNC_test_every_python_module_has_the_exoskeleton_before_imports


# region FUNC_test_regions_are_balanced [DOMAIN(8): CodeLayer; CONCEPT(9): Regions, Balance; TECH(4): stack]
## @purpose Prove that region and endregion tags pair with the same name in every Python module, so that the log-to-code
## navigation and the patchers can trust them.
## @io repo_root -> None
## @complexity 4
def test_regions_are_balanced(repo_root):
    problems = []
    total = 0
    for path in _python_files(repo_root):
        spans, found = _region_spans(path.read_text(encoding="utf-8").split("\n"))
        total += len(spans)
        problems.extend("%s: %s" % (path.relative_to(repo_root), item) for item in found)
    _trace("test_regions_are_balanced", "PAIRS", "%d region pairs, %d problems" % (total, len(problems)))
    assert total > 100, "too few regions found: %d" % total
    assert problems == [], "\n".join(problems)
# endregion FUNC_test_regions_are_balanced


# region FUNC_test_top_level_definitions_sit_in_regions [DOMAIN(8): CodeLayer; CONCEPT(9): Regions, Definitions; TECH(5): ast]
## @purpose Prove that every top-level function and class sits between the region tags that carry its name (FUNC_ for a
## function, CLASS_ for a class, MODULE_CONTRACT for the anchor), that only comment lines lie between the region line and the
## definition, and that every method of a class sits in its own METHOD_ region inside the class region.
## @io repo_root -> None
## @complexity 7
def test_top_level_definitions_sit_in_regions(repo_root):
    problems = []
    checked = 0
    for path in _python_files(repo_root):
        name = str(path.relative_to(repo_root))
        text = path.read_text(encoding="utf-8")
        lines = text.split("\n")
        spans, _ = _region_spans(lines)
        by_name = {}
        for span_name, first, last in spans:
            by_name.setdefault(span_name, []).append((first, last))
        for node in ast.parse(text).body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                continue
            checked += 1
            start = min([node.lineno] + [item.lineno for item in node.decorator_list])
            if node.name == "_module_contract":
                expected = "MODULE_CONTRACT"
            elif isinstance(node, ast.ClassDef):
                expected = "CLASS_" + node.name
            else:
                expected = "FUNC_" + node.name
            homes = [(first, last) for first, last in by_name.get(expected, []) if first < start and last > node.end_lineno]
            if not homes:
                problems.append("%s: %s (line %d) is not inside a region %s" % (name, node.name, start, expected))
                continue
            first, last = max(homes)
            between = [line for line in lines[first:start - 1] if line.strip() and not line.startswith("#")]
            if between:
                problems.append("%s: code stands between the region line and %s" % (name, node.name))
            if not isinstance(node, ast.ClassDef):
                continue
            for member in node.body:
                if not isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                checked += 1
                member_start = min([member.lineno] + [item.lineno for item in member.decorator_list])
                inside = [
                    (a, b) for a, b in by_name.get("METHOD_" + member.name, [])
                    if a < member_start and b > member.end_lineno and a > first and b < last
                ]
                if not inside:
                    problems.append("%s: method %s.%s is not inside a METHOD_ region within its class region" % (name, node.name, member.name))
    _trace("test_top_level_definitions_sit_in_regions", "DEFS", "checked %d definitions, %d problems" % (checked, len(problems)))
    assert checked > 100, "too few definitions found: %d" % checked
    assert problems == [], "\n".join(problems)
# endregion FUNC_test_top_level_definitions_sit_in_regions


# region FUNC_test_backend_neither_prints_nor_exits_nor_parses_arguments [DOMAIN(9): CodeLayer; CONCEPT(9): Layers, Purity; TECH(5): ast]
## @purpose Prove that the backend package returns data: it has no print, exit, quit or input call, no SystemExit, no
## argparse, no standard stream, no stream handler and no logging configuration; those belong to the frontend.
## @io repo_root -> None
## @complexity 6
def test_backend_neither_prints_nor_exits_nor_parses_arguments(repo_root):
    problems = []
    files = sorted((repo_root / "tools" / "conformlib").glob("*.py"))
    for path in files:
        name = str(path.relative_to(repo_root))
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in BACKEND_FORBIDDEN_CALLS:
                problems.append("%s line %d: call to %s" % (name, node.lineno, node.func.id))
            if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
                if (node.value.id, node.attr) in BACKEND_FORBIDDEN_ATTRIBUTES:
                    problems.append("%s line %d: %s.%s" % (name, node.lineno, node.value.id, node.attr))
                if node.attr in BACKEND_FORBIDDEN_NAMES:
                    problems.append("%s line %d: %s" % (name, node.lineno, node.attr))
            if isinstance(node, ast.Name) and node.id in BACKEND_FORBIDDEN_NAMES:
                problems.append("%s line %d: %s" % (name, node.lineno, node.id))
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name.split(".")[0] in BACKEND_FORBIDDEN_MODULES:
                        problems.append("%s line %d: import %s" % (name, node.lineno, alias.name))
            if isinstance(node, ast.ImportFrom) and node.module and node.module.split(".")[0] in BACKEND_FORBIDDEN_MODULES:
                problems.append("%s line %d: import from %s" % (name, node.lineno, node.module))
    _trace("test_backend_neither_prints_nor_exits_nor_parses_arguments", "BACKEND", "%d backend files, %d problems" % (len(files), len(problems)))
    assert len(files) >= 5, "the backend has fewer files than expected: %d" % len(files)
    assert problems == [], "\n".join(problems)
# endregion FUNC_test_backend_neither_prints_nor_exits_nor_parses_arguments


# region FUNC_test_imports_are_in_the_allowlist [DOMAIN(8): CodeLayer; CONCEPT(9): Imports, StandardLibrary; TECH(5): ast]
## @purpose Prove that the tool imports only the standard library and its own packages, and that the test modules add only
## subprocess, ast and pytest; every import at any depth is checked, relative imports included.
## @io repo_root -> None
## @complexity 5
def test_imports_are_in_the_allowlist(repo_root):
    problems = []
    seen = set()
    for path in _python_files(repo_root):
        name = str(path.relative_to(repo_root))
        allowed = set(ALL_MODULES)
        if path.parent.name == "tests":
            allowed |= TEST_ONLY_MODULES
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            modules = []
            if isinstance(node, ast.Import):
                modules = [alias.name.split(".")[0] for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                modules = [node.module.split(".")[0]]
            for module in modules:
                seen.add(module)
                if module not in allowed:
                    problems.append("%s line %d: import of %s" % (name, node.lineno, module))
    _trace("test_imports_are_in_the_allowlist", "IMPORTS", "modules seen: %s" % ",".join(sorted(seen)))
    assert "pytest" in seen and "argparse" in seen, "the walk did not reach the tests and the frontend"
    assert problems == [], "\n".join(problems)
# endregion FUNC_test_imports_are_in_the_allowlist


# region FUNC_test_interpreter_is_supported [DOMAIN(7): CodeLayer; CONCEPT(8): Python39, Syntax; TECH(4): ast.parse]
## @purpose Prove that the suite runs on Python 3.9 or newer and that every source file parses with the grammar of 3.9, so a
## newer interpreter cannot hide a construct the supported one rejects.
## @io repo_root -> None
## @complexity 3
def test_interpreter_is_supported(repo_root):
    _trace("test_interpreter_is_supported", "VERSION", "interpreter %d.%d" % (sys.version_info[0], sys.version_info[1]))
    assert sys.version_info >= (3, 9)
    for path in _python_files(repo_root):
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path), feature_version=(3, 9))
# endregion FUNC_test_interpreter_is_supported


# region FUNC_test_test_guide_maps_every_ac_to_existing_tests [DOMAIN(9): CodeLayer; CONCEPT(9): Guide, Traceability; TECH(4): ast]
## @purpose Prove that tests/test_guide.md has a row for each of AC-1 to AC-12 and AC-P1 to AC-P7, that every test name in a
## row is a test function that exists, and that a row without a test is a finalize row only for the criteria that name a
## command of the finalize phase.
## @io repo_root -> None
## @complexity 6
def test_test_guide_maps_every_ac_to_existing_tests(repo_root):
    rows = _guide_rows(repo_root)
    existing = _test_function_names(repo_root)
    problems = []
    for criterion in CRITERIA:
        if criterion not in rows:
            problems.append("%s has no row" % criterion)
    for criterion, cell in rows.items():
        if criterion not in CRITERIA:
            problems.append("%s is not a criterion of the specification" % criterion)
        names = [name.split("[")[0] for name in GUIDE_TEST_NAME_RE.findall(cell)]
        if not names and "finalize" not in cell:
            problems.append("%s names no test and no finalize command" % criterion)
        if "finalize" in cell and criterion not in FINALIZE_ALLOWED:
            problems.append("%s leans on the finalize phase, which only %s may" % (criterion, sorted(FINALIZE_ALLOWED)))
        for name in names:
            if name not in existing:
                problems.append("%s names %s, which is no test function" % (criterion, name))
    _trace("test_test_guide_maps_every_ac_to_existing_tests", "GUIDE", "%d rows, %d test functions, %d problems" % (len(rows), len(existing), len(problems)))
    assert problems == [], "\n".join(problems)
# endregion FUNC_test_test_guide_maps_every_ac_to_existing_tests


# region FUNC_test_guide_names_the_commands [DOMAIN(7): CodeLayer; CONCEPT(8): Guide, Commands; TECH(3): str]
## @purpose Prove that the guide names the four commands an agent runs and the six trace markers it reads.
## @io repo_root -> None
## @complexity 2
def test_guide_names_the_commands(repo_root):
    text = (repo_root / "tests" / "test_guide.md").read_text(encoding="utf-8")
    missing = [item for item in GUIDE_COMMANDS + GUIDE_MARKERS if item not in text]
    _trace("test_guide_names_the_commands", "GUIDE", "missing: %s" % missing)
    assert missing == []
# endregion FUNC_test_guide_names_the_commands


# region FUNC_test_guide_markers_exist_in_the_tool_source [DOMAIN(8): CodeLayer; CONCEPT(9): Guide, Markers; TECH(3): str]
## @purpose Prove that each trace marker the guide tells an agent to look for is written by the tool's source, so the guide
## does not point at a line that is never printed.
## @io repo_root -> None
## @complexity 3
def test_guide_markers_exist_in_the_tool_source(repo_root):
    source = ""
    for path in sorted((repo_root / "tools").rglob("*.py")):
        if "__pycache__" not in path.parts:
            source += path.read_text(encoding="utf-8")
    missing = [marker for marker in GUIDE_MARKERS if marker not in source]
    _trace("test_guide_markers_exist_in_the_tool_source", "MARKERS", "missing: %s" % missing)
    assert missing == []
# endregion FUNC_test_guide_markers_exist_in_the_tool_source


# region FUNC_test_anti_loop_ladder_escalates_and_stops [DOMAIN(9): CodeLayer; CONCEPT(9): AntiLoop, Ladder, RealSession; TECH(6): subprocess, pytest]
## @purpose Prove the Anti-Loop ladder in a real pytest session: the advice function escalates from the checklist to the
## documentation hint, the looping warning and the stop; and five red sessions of a scratch project raise the counter file
## from 1 to 5 with the matching advice printed, a green session resets it to 0, and the next red session is attempt 1.
## @uses subprocess, sys.executable
## @io (anti_loop, repo_root, tmp_path) -> None
## @complexity 7
def test_anti_loop_ladder_escalates_and_stops(anti_loop, repo_root, tmp_path):
    assert "checklist" in anti_loop(1)
    assert anti_loop(2) == anti_loop(1)
    assert "attempt 3" in anti_loop(3) and "test_guide.md" in anti_loop(3)
    assert "attempt 4" in anti_loop(4) and "looping" in anti_loop(4)
    assert "STOP" in anti_loop(5) and anti_loop(9) == anti_loop(5)

    project = tmp_path / "proj"
    (project / "tests").mkdir(parents=True)
    shutil.copy(str(repo_root / "tests" / "conftest.py"), str(project / "tests" / "conftest.py"))
    (project / "pytest.ini").write_text("[pytest]\ntestpaths = tests\n", encoding="utf-8")
    (project / "tests" / "test_x.py").write_text(
        "import pathlib\n\n\ndef test_x():\n    assert pathlib.Path(__file__).with_name('green.flag').exists()\n",
        encoding="utf-8",
    )
    counter = project / "tests" / ".test_counter.json"
    env = dict(os.environ)
    env["PYTHONPATH"] = str(repo_root / "tools")
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env.pop("PYTEST_ADDOPTS", None)
    command = [sys.executable, "-m", "pytest", "-p", "no:cacheprovider", "-q", "tests"]

    def session():
        proc = subprocess.run(command, cwd=str(project), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        return proc.returncode, proc.stdout

    seen = []
    for attempt in range(1, 6):
        code, output = session()
        stored = json.loads(counter.read_text(encoding="utf-8"))["attempts"]
        seen.append(stored)
        _trace("test_anti_loop_ladder_escalates_and_stops", "ATTEMPT", "red session %d: exit=%d counter=%d" % (attempt, code, stored))
        assert code != 0
        assert stored == attempt
        assert "[ANTI-LOOP attempt %d]" % attempt in output
        if attempt <= 2:
            assert "Anti-Loop checklist" in output
        elif attempt == 3:
            assert "Anti-Loop, attempt 3" in output
        elif attempt == 4:
            assert "Anti-Loop, attempt 4" in output
        else:
            assert "STOP" in output
    (project / "tests" / "green.flag").write_text("green\n", encoding="utf-8")
    code, output = session()
    stored = json.loads(counter.read_text(encoding="utf-8"))["attempts"]
    _trace("test_anti_loop_ladder_escalates_and_stops", "RESET", "green session: exit=%d counter=%d" % (code, stored))
    assert code == 0 and stored == 0 and "ANTI-LOOP" not in output
    (project / "tests" / "green.flag").unlink()
    code, output = session()
    assert code != 0 and "[ANTI-LOOP attempt 1]" in output
    assert seen == [1, 2, 3, 4, 5]
# endregion FUNC_test_anti_loop_ladder_escalates_and_stops


# region FUNC_test_doxyfile_covers_tools_bin_tests [DOMAIN(8): Documentation; CONCEPT(8): Doxyfile, Coverage; TECH(4): Doxyfile]
## @purpose Prove that the Doxyfile reads tools, bin and tests recursively, includes the extensionless launcher and reads
## it as Python, writes XML into the ignored output directory, and stays quiet.
## @io repo_root -> None
## @complexity 4
def test_doxyfile_covers_tools_bin_tests(repo_root):
    settings = _doxyfile_settings(repo_root / "Doxyfile")
    _trace("test_doxyfile_covers_tools_bin_tests", "DOXYFILE", "INPUT=%s FILE_PATTERNS=%s" % (settings.get("INPUT"), settings.get("FILE_PATTERNS")))
    assert set(settings["INPUT"].split()) == {"tools", "bin", "tests"}
    assert {"*.py", "conform"} <= set(settings["FILE_PATTERNS"].split())
    assert "no_extension=Python" in settings["EXTENSION_MAPPING"].split()
    assert settings["RECURSIVE"] == "YES"
    assert settings["GENERATE_XML"] == "YES"
    assert settings["QUIET"] == "YES"
    assert settings["OUTPUT_DIRECTORY"] == "doxygen_output"
# endregion FUNC_test_doxyfile_covers_tools_bin_tests


# region FUNC_test_doxygen_builds_silently_and_maps_the_tool [DOMAIN(9): Documentation; CONCEPT(9): CodeMap, Build; TECH(5): doxygen, subprocess]
## @purpose Prove that doxygen is installed and builds the code map of a copy of the repository with exit 0 and no output
## line, and that the XML holds a file compound for the frontend and one for the extensionless launcher.
## @uses doxygen
## @io (repo_copy) -> None
## @complexity 5
def test_doxygen_builds_silently_and_maps_the_tool(repo_copy):
    binary = shutil.which("doxygen")
    assert binary is not None, "doxygen is not on the path: the build cannot be proved, and a skip would be a green test over nothing"
    proc = subprocess.run([binary, "Doxyfile"], cwd=str(repo_copy), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    lines = [line for line in proc.stdout.split("\n") if line.strip()]
    xml_dir = repo_copy / "doxygen_output" / "xml"
    mapped = set()
    for path in sorted(xml_dir.glob("*.xml")):
        text = path.read_text(encoding="utf-8")
        if re.search(r'<compounddef [^>]*kind="file"', text):
            found = re.search(r'<location file="([^"]+)"', text)
            if found:
                mapped.add(found.group(1))
    _trace("test_doxygen_builds_silently_and_maps_the_tool", "BUILD", "exit=%d output_lines=%d file_compounds=%d" % (proc.returncode, len(lines), len(mapped)))
    assert proc.returncode == 0
    assert lines == [], "doxygen printed %d lines" % len(lines)
    assert "tools/conform.py" in mapped
    assert "bin/conform" in mapped
# endregion FUNC_test_doxygen_builds_silently_and_maps_the_tool


# region FUNC_test_gitignore_ignores_doxygen_output [DOMAIN(7): Documentation; CONCEPT(8): Ignore, BuildOutput; TECH(4): git check-ignore]
## @purpose Prove that the repository's .gitignore makes git ignore the Doxygen output directory and the Anti-Loop counter,
## by asking git itself in a scratch repository that holds only the .gitignore.
## @uses git
## @io (repo_root, tmp_path) -> None
## @complexity 4
def test_gitignore_ignores_doxygen_output(repo_root, tmp_path):
    scratch = tmp_path / "ignore-probe"
    (scratch / "doxygen_output" / "xml").mkdir(parents=True)
    (scratch / "tests").mkdir()
    shutil.copy(str(repo_root / ".gitignore"), str(scratch / ".gitignore"))
    (scratch / "tests" / ".test_counter.json").write_text("{}\n", encoding="utf-8")
    subprocess.run(["git", "init", "-q"], cwd=str(scratch), check=True)
    results = {}
    for target in ("doxygen_output", "doxygen_output/xml", "tests/.test_counter.json"):
        proc = subprocess.run(["git", "check-ignore", "-q", target], cwd=str(scratch))
        results[target] = proc.returncode
    _trace("test_gitignore_ignores_doxygen_output", "IGNORE", "check-ignore exits: %s" % json.dumps(results, sort_keys=True))
    assert results == {"doxygen_output": 0, "doxygen_output/xml": 0, "tests/.test_counter.json": 0}
# endregion FUNC_test_gitignore_ignores_doxygen_output


# region FUNC_test_mit_license_and_no_remote [DOMAIN(9): Publication; CONCEPT(10): CanonicalMIT, NoRemoteObservation; TECH(7): pathlib]
## @purpose Assert exactly one regular root LICENSE with the complete fixed MIT oracle, without any Git/remote observation.
## @uses pathlib.Path.iterdir, pathlib.Path.is_symlink, pathlib.Path.is_file, pathlib.Path.read_bytes, logging.Logger.error
## @io repo_root actual Path. Returns None only for exactly one root license-family entry named LICENSE and exact canonical
##   UTF8 bytes including copyright/permission/condition/disclaimer/newline. Reads filesystem only; no subprocess, remote
##   query/logging, configuration write or origin restriction. AssertionError emits own IMP10 safe cause before propagation;
##   OSError on inaccessible filesystem is visible. Example: ordinary origin clone passes; missing disclaimer fails even
##   with unchanged MIT first line. Importance:9.
## @complexity 4
def test_mit_license_and_no_remote(repo_root):
    # START_BLOCK_Validation
    licences = sorted(path.name for path in repo_root.iterdir() if path.name.upper().startswith(("LICENSE", "LICENCE", "COPYING")))
    target = repo_root / "LICENSE"
    shape = licences == ["LICENSE"] and not target.is_symlink() and target.is_file()
    matches = shape and target.read_bytes() == CANONICAL_MIT.encode("utf-8")
    _trace("test_mit_license_and_no_remote", "LICENSE", "files=%d regular=%s canonical=%s" % (len(licences), shape, matches))
    if not matches:
        logging.getLogger(__name__).error("[IMP:10][test_mit_license_and_no_remote][REJECT] cause=canonical-license")
        raise AssertionError("exact regular canonical MIT license required")
    logging.getLogger(__name__).info("[IMP:9][test_mit_license_and_no_remote][VERIFIED] files=1 canonical=true queries=0")
    # END_BLOCK_Validation
# endregion FUNC_test_mit_license_and_no_remote

# region FUNC_test_full_mit_license_rejects_damaged_bodies [DOMAIN(9): Publication; CONCEPT(10): IndependentOracle; TECH(7): pytest]
## @purpose Exercise the actual owning license assertion against clause/copyright damage, truncation, missing/extra files and restore control.
## @uses test_code_layer.test_mit_license_and_no_remote, pytest.raises, pathlib.Path.write_bytes, pytest.LogCaptureFixture
## @io tmp_path owned Path and caplog capture. Returns None after each concrete changed filesystem fails the production
##   assertion with exactly one expected canonical-license ERROR, then restored complete original bytes pass without errors.
##   Fixed mutations cover copyright, permission, condition, disclaimer, first-line-only and missing/extra license. Own fixture
##   writes only; no product LICENSE edits, remote queries or skipped acceptance. AssertionError on failed discrimination.
##   Example: retaining MIT first line while changing disclaimer still rejects. Importance:9.
## @complexity 5
def test_full_mit_license_rejects_damaged_bodies(tmp_path, caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO)
    target = tmp_path / "LICENSE"
    original = CANONICAL_MIT.encode("utf-8")
    variants = [CANONICAL_MIT.replace("Copyright (c) 2026", "Copyright (c) 2025"),
                CANONICAL_MIT.replace("free of charge", "for a charge"),
                CANONICAL_MIT.replace("shall be included", "may be omitted"),
                CANONICAL_MIT.replace("WITHOUT WARRANTY", "WITH WARRANTY"), "MIT License\n"]
    for variant in variants:
        target.write_bytes(variant.encode("utf-8"))
        caplog.clear()
        with pytest.raises(AssertionError, match="canonical MIT"):
            test_mit_license_and_no_remote(tmp_path)
        errors = [(r.levelno, r.getMessage()) for r in caplog.records if r.levelno >= logging.ERROR]
        print("Actual license negative control", errors)
        assert errors == [(logging.ERROR, "[IMP:10][test_mit_license_and_no_remote][REJECT] cause=canonical-license")]
        target.write_bytes(original)
        caplog.clear()
        test_mit_license_and_no_remote(tmp_path)
        assert not [r for r in caplog.records if r.levelno >= logging.ERROR]
    for extra in (False, True):
        target.write_bytes(original)
        if extra: (tmp_path / "COPYING").write_text("extra\n")
        else: target.unlink()
        caplog.clear()
        with pytest.raises(AssertionError, match="canonical MIT"):
            test_mit_license_and_no_remote(tmp_path)
        errors = [r.getMessage() for r in caplog.records if r.levelno >= logging.ERROR]
        print("Actual license file-population negative control", errors)
        assert errors == ["[IMP:10][test_mit_license_and_no_remote][REJECT] cause=canonical-license"]
        if extra: (tmp_path / "COPYING").unlink()
        target.write_bytes(original)
        caplog.clear()
        test_mit_license_and_no_remote(tmp_path)
        assert target.read_bytes() == original and not [r for r in caplog.records if r.levelno >= logging.ERROR]
    _trace("test_full_mit_license_rejects_damaged_bodies", "RESTORED", "damaged bodies=5 file-population controls=2 protective canonical restored")
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_full_mit_license_rejects_damaged_bodies

# region FUNC_test_mit_license_accepts_origin_without_remote_observation [DOMAIN(9): Publication; CONCEPT(10): NoRemoteObservation; TECH(8): git, pytest]
## @purpose Verify the actual licensing assertion in a real ordinary origin clone with subprocess observation forbidden and origin preserved.
## @uses subprocess.run, test_code_layer.test_mit_license_and_no_remote, pytest.MonkeyPatch.setattr, pathlib.Path.read_bytes
## @io tmp_path owned Path, monkeypatch and caplog. Returns None after real local commit/ordinary clone setup, unchanged
##   cloned Git configuration bytes, zero invocation of forbidden production subprocess observer and zero unexpected errors.
##   Setup uses only owned Git repositories with explicit local identity, no global config/push/network. Production assertion
##   neither queries nor logs origin; setup config bytes are compared, not remote output. AssertionError on any query/mutation.
##   Example: clone's existing origin remains intact while complete MIT passes. Importance:9.
## @complexity 5
def test_mit_license_accepts_origin_without_remote_observation(tmp_path, monkeypatch, caplog):
    # START_BLOCK_BusinessLogic
    origin = tmp_path / "origin"
    origin.mkdir()
    (origin / "LICENSE").write_bytes(CANONICAL_MIT.encode("utf-8"))
    environment = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    environment.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_SYSTEM=os.devnull)
    for args in (["init", "-q"], ["add", "LICENSE"], ["-c", "user.name=Fixture", "-c", "user.email=fixture", "-c", "commit.gpgsign=false", "commit", "-q", "-m", "fixture"]):
        result = subprocess.run(["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-C", str(origin), *args], capture_output=True, env=environment)
        assert result.returncode == 0
    clone = tmp_path / "clone"
    result = subprocess.run(["git", "clone", "-q", "--no-hardlinks", str(origin), str(clone)], capture_output=True, env=environment)
    assert result.returncode == 0
    configuration = clone / ".git/config"
    original = configuration.read_bytes()
    assert b'[remote "origin"]' in original
    monkeypatch.setattr(subprocess, "run", lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("license assertion queried subprocess")))
    caplog.set_level(logging.INFO); caplog.clear()
    test_mit_license_and_no_remote(clone)
    errors = [r for r in caplog.records if r.levelno >= logging.ERROR]
    _trace("test_mit_license_accepts_origin_without_remote_observation", "PRESERVED", "ordinary origin clone passed; subprocess forbidden; configuration byte-equal")
    assert configuration.read_bytes() == original and not errors
    assert all(str(origin) not in r.getMessage() for r in caplog.records)
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_mit_license_accepts_origin_without_remote_observation
