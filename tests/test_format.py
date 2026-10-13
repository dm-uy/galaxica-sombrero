# region MODULE_CONTRACT [DOMAIN(9): Format, Norms; CONCEPT(8): NormTable, Sections, SelfCheck; TECH(6): pytest, re]
## @modulecontract
## @purpose To prove that FORMAT.md states the format it promises: its card is valid, each of the 39 norms stands in the
## section the specification names with the level it names, each of the specification's items 2 to 7 has its own anchored
## section, the tool finds nothing wrong in the file, and the adapter registry cites every adapter norm.
## @scope FORMAT.md and runtime/adapters.md as text; one in-process run of the self mode over the repository.
## @input The repository on disk; the table of 39 (anchor, norm id, level) triples copied from the specification.
## @output Pass or fail per norm and per structural property; the counts printed before each assert.
## @links [READS_DATA_FROM(8): FORMAT.md, runtime/adapters.md; USES_API(6): conform.main through run_cli]
## @links_to_spec AC-2, AC-4
## @invariants
## - The table is a constant of the test: a norm that moves to another section or changes its level fails a named test.
## - The norms are read with a reader of this file that skips fenced blocks, independent of the tool it checks.
## @rationale
## Q: Why an independent norm reader here?
## A: If the test used the tool's reader, a reader that drops a norm would drop it from both sides and the test would pass.
## @changes
## LAST_CHANGE: [1.1.0 - Reconcile current M19 boundary/release facts and paired source operands; preserve original assertions/pins/refusals/restoration; runtime checks pending.]
## @modulemap
## FUNC 7[Read the norms outside fences as (anchor, id, level) triples] => read_norms
## FUNC 5[The card of FORMAT.md] => test_format_md_card
## FUNC 8[Each norm in its section with its level] => test_format_norm_in_its_section
## FUNC 7[FORMAT.md holds exactly the 39 norms in order] => test_format_md_holds_exactly_the_39_norms
## FUNC 6[Each spec item 2 to 7 has its own section] => test_each_spec_item_2_to_7_has_its_own_section
## FUNC 7[The tool finds no failure in FORMAT.md] => test_conform_self_gives_no_fail_on_format_md
## FUNC 6[The adapter file cites FMT-26 to FMT-38] => test_adapters_md_cites_every_adapter_norm
## @usecases
## - [test_format_norm_in_its_section]: Maintainer -> moves a norm to another section -> the test names the norm and the section
## - [test_conform_self_gives_no_fail_on_format_md]: QA agent -> runs the tool on the file that defines the format -> no FAIL row
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: FORMAT.md, 39 norms, norm table, anchored sections, spec items 2-7, self check, adapters.md citations, fence-aware reader
# STRUCTURE: ▶ NORM_TABLE(39) → ○ read FORMAT.md outside fences → ⊕ (anchor,id,level) → ◇ equals table ? → ⚡ self run → ∑ no FAIL on FORMAT.md → ⎋ assert

import json
import pathlib
import re
from typing import List, Tuple

import pytest

NORM_TABLE = [
    ("format.neutral-files", "FMT-1", "MUST"),
    ("format.card", "FMT-2", "MUST"),
    ("format.card", "FMT-3", "MUST"),
    ("format.card", "FMT-4", "MUST"),
    ("format.card", "FMT-5", "MUST"),
    ("format.card", "FMT-6", "MUST"),
    ("format.card", "FMT-7", "MAY"),
    ("format.card", "FMT-8", "MUST NOT"),
    ("format.anchor", "FMT-9", "MUST"),
    ("format.anchor", "FMT-10", "MUST"),
    ("format.anchor", "FMT-11", "MUST"),
    ("format.anchor", "FMT-12", "MUST NOT"),
    ("format.norm", "FMT-13", "MUST"),
    ("format.norm", "FMT-14", "MUST"),
    ("format.norm", "FMT-15", "MUST"),
    ("format.norm", "FMT-16", "MUST"),
    ("format.calls", "FMT-17", "MUST"),
    ("format.calls", "FMT-18", "MUST"),
    ("format.calls", "FMT-19", "MUST"),
    ("format.calls", "FMT-20", "MUST"),
    ("format.version", "FMT-21", "MUST"),
    ("format.version", "FMT-22", "MUST"),
    ("format.version", "FMT-23", "MUST"),
    ("format.version", "FMT-24", "MUST"),
    ("format.version", "FMT-25", "MUST"),
    ("format.adapter", "FMT-26", "MUST"),
    ("format.adapter", "FMT-27", "MUST"),
    ("format.adapter", "FMT-28", "MUST"),
    ("format.adapter", "FMT-29", "MUST"),
    ("format.adapter", "FMT-30", "MUST"),
    ("format.adapter", "FMT-31", "MUST"),
    ("format.adapter", "FMT-32", "MUST"),
    ("format.adapter", "FMT-33", "MUST"),
    ("format.adapter", "FMT-34", "MUST"),
    ("format.adapter", "FMT-35", "MUST NOT"),
    ("format.adapter", "FMT-36", "MUST"),
    ("format.adapter", "FMT-37", "SHOULD"),
    ("format.adapter", "FMT-38", "SHOULD"),
    ("format.examples", "FMT-39", "MUST"),
]

NORM_LINE = re.compile(r"^- \*\*([A-Z]+-[0-9]+)\*\* (MUST NOT|MUST|SHOULD NOT|SHOULD|MAY): ")
ANCHOR_LINE = re.compile(r"^<!-- anchor: (\S+) -->$")
ITEM_ANCHORS = {
    2: "format.card",
    3: "format.anchor",
    4: "format.norm",
    5: "format.calls",
    6: "format.version",
    7: "format.adapter",
}
ADAPTER_NORMS = ["FMT-%d" % n for n in range(26, 39)]


# region FUNC_read_norms [DOMAIN(8): Format, Norms; CONCEPT(9): NormReader, Fence; TECH(5): re]
## @purpose Read the norms of a Markdown file outside fenced blocks as (anchor, id, level) triples in file order, with the
## anchor that was last seen; an independent reader for the tests.
## @io pathlib.Path -> List[Tuple[str, str, str]]
## @complexity 4
def read_norms(path: pathlib.Path) -> List[Tuple[str, str, str]]:
    found = []
    anchor = ""
    fence_char = ""
    fence_len = 0
    for line in path.read_text(encoding="utf-8").split("\n"):
        stripped = line.lstrip()
        if fence_char:
            run = len(stripped) - len(stripped.lstrip(fence_char))
            if run >= fence_len and set(stripped.strip()) == {fence_char}:
                fence_char = ""
                fence_len = 0
            continue
        opened = re.match(r"^(`{3,}|~{3,})", stripped)
        if opened:
            fence_char = opened.group(1)[0]
            fence_len = len(opened.group(1))
            continue
        marker = ANCHOR_LINE.match(line)
        if marker:
            anchor = marker.group(1)
            continue
        norm = NORM_LINE.match(line)
        if norm:
            found.append((anchor, norm.group(1), norm.group(2)))
    return found
# endregion FUNC_read_norms


# region FUNC_test_format_md_card [DOMAIN(7): Format; CONCEPT(8): Card; TECH(4): pytest]
## @purpose Prove that FORMAT.md is a draft with the id format, a title and exactly the three mandatory keys.
## @io (pathlib.Path, Callable) -> None
## @complexity 2
def test_format_md_card(repo_root, read_card):
    card, _ = read_card(repo_root / "FORMAT.md")
    print("[IMP:9][test_format_md_card][RESULT] keys=%s status=%s" % (sorted(card), card.get("status")))
    assert sorted(card) == ["id", "status", "title"]
    assert card["id"] == "format"
    assert card["status"] == "draft"
    assert card["title"]
# endregion FUNC_test_format_md_card


# region FUNC_test_format_norm_in_its_section [DOMAIN(9): Format, Norms; CONCEPT(9): NormSection, Level; TECH(5): pytest.parametrize]
## @purpose Prove, for each of the 39 norms, that it stands under the anchor the specification names and has the level the
## specification names.
## @io (str, str, str, pathlib.Path) -> None
## @complexity 3
@pytest.mark.parametrize("anchor,norm_id,level", NORM_TABLE, ids=[row[1] for row in NORM_TABLE])
def test_format_norm_in_its_section(anchor, norm_id, level, repo_root):
    found = {n: (a, l) for a, n, l in read_norms(repo_root / "FORMAT.md")}
    print("[IMP:9][test_format_norm][RESULT] norm=%s expected=%s,%s found=%s" % (norm_id, anchor, level, found.get(norm_id)))
    assert found.get(norm_id) == (anchor, level)
# endregion FUNC_test_format_norm_in_its_section


# region FUNC_test_format_md_holds_exactly_the_39_norms [DOMAIN(8): Format, Norms; CONCEPT(9): NormCount; TECH(4): list]
## @purpose Prove that FORMAT.md holds exactly the 39 norms of the table, in the table's order, none more.
## @io pathlib.Path -> None
## @complexity 3
def test_format_md_holds_exactly_the_39_norms(repo_root):
    found = read_norms(repo_root / "FORMAT.md")
    ids = [n for _a, n, _l in found]
    print("[IMP:9][test_format_md_holds][COUNT] norms=%d" % len(found))
    assert len(NORM_TABLE) == 39
    assert ids == ["FMT-%d" % n for n in range(1, 40)]
    assert found == NORM_TABLE
# endregion FUNC_test_format_md_holds_exactly_the_39_norms


# region FUNC_test_each_spec_item_2_to_7_has_its_own_section [DOMAIN(8): Format; CONCEPT(8): SpecItems, Section; TECH(4): re]
## @purpose Prove that each of the specification's items 2 to 7 (card, anchors, norms, calls, versions, adapters) has its own
## anchor in FORMAT.md, used once, in that order, and that a heading follows the anchor line.
## @io pathlib.Path -> None
## @complexity 4
def test_each_spec_item_2_to_7_has_its_own_section(repo_root):
    lines = (repo_root / "FORMAT.md").read_text(encoding="utf-8").split("\n")
    order = []
    for index, line in enumerate(lines):
        marker = ANCHOR_LINE.match(line)
        if marker and marker.group(1) in ITEM_ANCHORS.values():
            following = [l for l in lines[index + 1:] if l.strip()][:1]
            assert following and following[0].startswith("## "), marker.group(1)
            order.append(marker.group(1))
    print("[IMP:9][test_each_spec_item][RESULT] sections=%s" % order)
    assert order == [ITEM_ANCHORS[n] for n in range(2, 8)]
# endregion FUNC_test_each_spec_item_2_to_7_has_its_own_section


# region FUNC_test_conform_self_gives_no_fail_on_format_md [DOMAIN(9): Format, SelfCheck; CONCEPT(9): Verdict; TECH(6): run_cli, json]
## @purpose Prove that the tool finds nothing wrong in the file that defines the format, and that the run counts all 1234 current norms.
## @uses run_cli, ldd_trajectory, deny_list
## @io (Callable, Tuple, Callable) -> None
## @complexity 4
def test_conform_self_gives_no_fail_on_format_md(run_cli, deny_list, ldd_trajectory):
    code, out, _err = run_cli(["self", "--deny-list", str(deny_list[0]), "--json"])
    lines = ldd_trajectory()
    report = json.loads(out)
    fails = [row for row in report["rows"] if row["status"] == "FAIL" and row["subject"] == "FORMAT.md"]
    print("[IMP:9][test_conform_self_format][RESULT] exit=%d norms=%s fails_on_format=%d" % (code, report["summary"]["population"].get("norms"), len(fails)))
    assert fails == []
    assert code == 0
    assert report["summary"]["population"]["norms"] == 1234
    assert any("[run_self][VERDICT]" in line for line in lines)
# endregion FUNC_test_conform_self_gives_no_fail_on_format_md


# region FUNC_test_adapters_md_cites_every_adapter_norm [DOMAIN(7): Format, Adapter; CONCEPT(8): Citation; TECH(4): str]
## @purpose Prove that the adapter registry cites each adapter norm FMT-26 to FMT-38 and holds no norm of its own.
## @io pathlib.Path -> None
## @complexity 3
def test_adapters_md_cites_every_adapter_norm(repo_root):
    path = repo_root / "runtime" / "adapters.md"
    text = path.read_text(encoding="utf-8")
    missing = [norm for norm in ADAPTER_NORMS if norm not in text]
    print("[IMP:9][test_adapters_md_cites][RESULT] missing=%s" % missing)
    assert missing == []
    assert read_norms(path) == []
# endregion FUNC_test_adapters_md_cites_every_adapter_norm
