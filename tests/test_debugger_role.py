# region MODULE_CONTRACT [DOMAIN(9): DebuggerContract; CONCEPT(9): FiniteControls, Authority, Returns; TECH(6): pytest, re, hashlib]
## @modulecontract
## @purpose Detect bounded structural and authority losses in the real shipped Debugger contract.
## @scope Draft card, anchors, unique DBG IDs, resolved calls and five explicitly weakened contract families.
## @input Read-only role/registry bytes and independently pinned obligation fragments and weakened text fixtures.
## @output Finite refusal labels and safe importance 7–10 observations delivered to actual pytest stdout.
## @links [READS_DATA_FROM(9): roles/debugger.md, runtime/capabilities.md, runtime/parameters.md; USES_API(6): pytest, re, hashlib]
## @invariants
## - Expected clauses and refusal labels are fixed here, never generated from producer output.
## - Negative fixtures alter in-memory text only; the same bounded checker accepts shipped positive bytes.
## - These exact controls establish no general semantic validator or complete source-fidelity judgment.
## - Existing session hooks own Anti-Loop; expected fixture refusals are passing assertions, not red sessions.
## @rationale
## Q: Why inspect actual shipped bytes and explicit weakened variants with one helper?
## A: A producer-self-comparison could approve its own weakened output; fixed obligations expose specific losses.
## Q: Why direct calls and visible stdout?
## A: Pure text logic has the test process as its sink; no subprocess or external delivery claim is necessary.
## @changes
## LAST_CHANGE: [v1.0.0 - Reconcile only the independent neutral namespace/current facts; preserve original controls and full publication coverage; runtime checks pending.]
## @modulemap
## FUNC 7[Read real role bytes and expose their identity.] => _debugger_text
## FUNC 6[Select live Markdown outside fences.] => _live_lines
## FUNC 8[Observe independently pinned restrictions and exact explicit grants.] => _contract_failures
## FUNC 8[Verify draft card, anchors and repository-wide DBG allocation.] => test_debugger_card_and_norm_structure
## FUNC 8[Resolve actual role calls against unchanged registries.] => test_debugger_calls_resolve
## FUNC 9[Accept shipped restrictions and status-dependent evidence.] => test_debugger_shipped_boundaries_and_returns
## FUNC 9[Refuse each explicit weakened real-text fixture with a specific label.] => test_debugger_finite_weakened_fixtures
## @usecases
## - [test_debugger_card_and_norm_structure]: Maintainer -> change card or allocation -> finite assertion exposes the drift.
## - [test_debugger_finite_weakened_fixtures]: Reviewer -> weaken an actual contract clause -> its independently expected label appears.
## @GREP_SUMMARY Debugger, finite controls, shipped bytes, draft card, scope, DBG uniqueness, no refunds, FIXED evidence, full QA, disclosed stubs
## @STRUCTURE shipped bytes → live structure + fixed obligations → explicit weakened variants → distinct refusals → independent semantic review

def _module_contract():
    pass
# endregion MODULE_CONTRACT


import hashlib
import re

import pytest

ANCHORS = ["roles.debugger." + part for part in
           ("inputs", "findings", "context", "diagnosis", "repair", "regression", "verification", "returns", "boundaries")]
DBG_IDS = ["DBG-%d" % (block * 100 + offset) for block, size in
           ((1, 7), (2, 3), (3, 4), (4, 5), (5, 4), (6, 5), (7, 4), (8, 4), (9, 5))
           for offset in range(1, size + 1)]
NORM = re.compile(r"^- \*\*([A-Z]+-\d+)\*\* (MUST NOT|SHOULD NOT|MUST|SHOULD|MAY): (.+)$")
# Independently pinned approved obligations; do not regenerate from role text or a producer's report.
OBLIGATIONS = {
    "INNER_AUTHORITY_BOUNDARY_MISSING": ("DBG-901", "MUST NOT", (
        "Commit, merge, spawn or invoke another role, self-dispatch or self-certify as independent QA.",)),
    "SCOPE_AUDIT_MISSING": ("DBG-704", "MUST", (
        "Audit actual changed paths, including added, modified, deleted and untracked files",
        "against assigned scope rather than trust filesTouched alone")),
    "TARGET_SCOPE_MISSING": ("DBG-902", "MUST", (
        "Write only inside the assigned absolute target and authorized paths",
        "approved specification, framework subjects and other repositories remain read-only")),
    "SPEND_PRESERVATION_MISSING": ("DBG-903", "MUST NOT", (
        "Reset or refund cumulative Debug spend or separate Anti-Loop counters to hide failures.",)),
    "FIXED_EVIDENCE_MISSING": ("DBG-802", "MUST", (
        "FIXED includes nonempty rootCause, fix, filesTouched, postFixAudit and testSummary",
        "actual regression evidence", "current origin, input/candidate identities and consumed entry",
        "a status-only FIXED is invalid")),
    "FULL_INDEPENDENT_QA_MISSING": ("DBG-804", "MUST", (
        "every candidate-changing FIXED", "renewed full independent QA under the same run/history",
        "filesTouched and testSummary never restrict or replace that full independent QA")),
    "STUB_DISCLOSURE_MISSING": ("DBG-107", "MUST", (
        "bodies are current substantive core",
        "detailed lifecycle, prompting and learning bodies remain disclosed deferred subjects")),
}
AUTHORITY_PREFIX = "Commit, merge, spawn or invoke another role, self-dispatch or self-certify as independent QA."
SPEND_PREFIX = "Reset or refund cumulative Debug spend or separate Anti-Loop counters to hide failures."
FIXED_PREFIX = "FIXED includes nonempty rootCause, fix, filesTouched, postFixAudit and testSummary"
QA_PREFIX = "filesTouched and testSummary never restrict or replace that full independent QA"
STUB_PREFIX = "detailed lifecycle, prompting and learning bodies remain disclosed deferred subjects"
# Five families, with both dispatch and merge instances; vocabulary/protective clauses remain recognizable.
WEAKENINGS = (
    ("inner-dispatch", "", "The Debugger may spawn QA as an inner role.", "INNER_DISPATCH_GRANT"),
    ("merge", "", "The Debugger may merge without the parent.", "MERGE_GRANT"),
    ("refund", SPEND_PREFIX, "Refund cumulative Debug spend after a worker failure; retain Anti-Loop context.",
     "SPEND_PRESERVATION_MISSING"),
    ("status-only-fixed", FIXED_PREFIX, "FIXED accepts status alone; rootCause, fix, filesTouched, postFixAudit and testSummary are optional",
     "FIXED_EVIDENCE_MISSING"),
    ("files-touched-qa", QA_PREFIX, "filesTouched and testSummary restrict that full independent QA to filesTouched",
     "FULL_INDEPENDENT_QA_MISSING"),
    ("implemented-stub", STUB_PREFIX, "detailed lifecycle, prompting and learning bodies supply implemented substantive protocol bodies",
     "STUB_DISCLOSURE_MISSING"),
)


# region FUNC__debugger_text [DOMAIN(8): DebuggerContract; CONCEPT(8): CurrentBytes; TECH(5): pathlib, hashlib]
## @purpose Read and identify the actual shipped contract without exposing source prose in diagnostics.
## @io pathlib.Path -> str
## @complexity 3
def _debugger_text(root):
    path = root / "roles/debugger.md"
    print("[IMP:7][_debugger_text][READ] subject=roles/debugger.md")
    try:
        data = path.read_bytes()
        text = data.decode("utf-8")
    except (OSError, UnicodeError) as error:
        print("[IMP:10][_debugger_text][READ_ERROR] subject=roles/debugger.md kind=%s" % type(error).__name__)
        raise
    print("[IMP:9][_debugger_text][IDENTITY] bytes=%d sha256=%s" % (len(data), hashlib.sha256(data).hexdigest()))
    return text
# endregion FUNC__debugger_text


# region FUNC__live_lines [DOMAIN(7): DebuggerContract; CONCEPT(8): LiveMarkdown; TECH(5): re]
## @purpose Ignore fenced examples when inspecting live anchors, declarations and calls.
## @io str -> list[str]
## @complexity 3
def _live_lines(text):
    lines = []
    fence = ""
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if not fence:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = ""
            continue
        if not fence:
            lines.append(line)
    print("[IMP:9][_live_lines][PARSED] live_lines=%d open_fence=%s" % (len(lines), bool(fence)))
    if fence:
        print("[IMP:10][_live_lines][INVALID] unclosed fence")
        raise ValueError("unclosed fence")
    return lines
# endregion FUNC__live_lines


# region FUNC__contract_failures [DOMAIN(9): DebuggerContract; CONCEPT(9): FiniteRefusal; TECH(5): re]
## @purpose Refuse only the fixed obligation losses and explicit grants named in this bounded corpus.
## @io str -> set[str]
## @complexity 4
def _contract_failures(text):
    norms = {}
    for line in _live_lines(text):
        found = NORM.match(line)
        if found:
            norms[found.group(1)] = (found.group(2), found.group(3))
    failures = set()
    for label, (norm, level, fragments) in OBLIGATIONS.items():
        actual_level, body = norms.get(norm, ("", ""))
        valid = actual_level == level and all(fragment in body for fragment in fragments)
        print("[IMP:9][_contract_failures][OBLIGATION] norm=%s valid=%s" % (norm, valid))
        if not valid:
            failures.add(label)
            print("[IMP:10][_contract_failures][REFUSED] label=%s" % label)
    for sentence, label in (("The Debugger may spawn QA as an inner role.", "INNER_DISPATCH_GRANT"),
                            ("The Debugger may merge without the parent.", "MERGE_GRANT")):
        if sentence in text:
            failures.add(label)
            print("[IMP:10][_contract_failures][REFUSED] label=%s" % label)
    print("[IMP:9][_contract_failures][RESULT] failures=%s" % sorted(failures))
    return failures
# endregion FUNC__contract_failures


# region FUNC_test_debugger_card_and_norm_structure [DOMAIN(8): DebuggerContract; CONCEPT(9): Card, Allocation; TECH(5): re]
## @purpose Pin the real draft card, anchored allocation and unique live repository DBG declarations.
## @io pathlib.Path -> None
## @complexity 4
def test_debugger_card_and_norm_structure(repo_root):
    text = _debugger_text(repo_root)
    card_lines = text.split("---", 2)[1].strip().splitlines()
    card = dict(line.split(": ", 1) for line in card_lines)
    live = _live_lines(text)
    anchors = re.findall(r"^<!-- anchor: (\S+) -->$", "\n".join(live), re.M)
    declarations = []
    current = None
    for line in live:
        marker = re.fullmatch(r"<!-- anchor: (\S+) -->", line)
        if marker:
            current = marker.group(1)
        norm = NORM.match(line)
        if norm:
            declarations.append((norm.group(1), current))
    all_dbg = []
    print("[IMP:7][test_debugger_card_and_norm_structure][READ] neutral Markdown allocation")
    for path in sorted(repo_root.rglob("*.md")):
        rel = path.relative_to(repo_root)
        if rel.parts[0] in {".git", "tests", "examples", "doxygen_output", "__pycache__", ".pytest_cache", "implementations"}:
            continue
        for line in _live_lines(path.read_text(encoding="utf-8")):
            found = NORM.match(line)
            if found and found.group(1).startswith("DBG-"):
                all_dbg.append(found.group(1))
    print("[IMP:9][test_debugger_card_and_norm_structure][RESULT] anchors=%d norms=%d repository_dbg=%d" %
          (len(anchors), len(declarations), len(all_dbg)))
    assert text.startswith("---\n") and len(card_lines) == len(card)
    assert card == {"id": "roles.debugger", "title": "Debugger", "status": "draft", "skill-name": "debugger",
                    "skill-when": "the parent assigns a current actionable implementation failure for counted diagnosis and repair"}
    assert anchors == ANCHORS
    assert [norm for norm, _ in declarations] == DBG_IDS
    assert all(anchor == ANCHORS[int(norm.split("-")[1]) // 100 - 1] for norm, anchor in declarations)
    assert sorted(all_dbg) == sorted(DBG_IDS)
    assert len(all_dbg) == len(set(all_dbg))
# endregion FUNC_test_debugger_card_and_norm_structure


# region FUNC_test_debugger_calls_resolve [DOMAIN(8): DebuggerContract; CONCEPT(8): Calls; TECH(5): re]
## @purpose Resolve real live calls against unchanged capability and parameter declarations.
## @io pathlib.Path -> None
## @complexity 3
def test_debugger_calls_resolve(repo_root):
    live = "\n".join(re.sub(r"`[^`]*`", "", line) for line in _live_lines(_debugger_text(repo_root)))
    calls = re.findall(r"\{\{(cap|param):([a-z][a-z0-9-]*)\}\}", live)
    declarations = {}
    for kind, file in (("cap", "capabilities"), ("param", "parameters")):
        print("[IMP:7][test_debugger_calls_resolve][READ] registry=%s" % file)
        registry = (repo_root / "runtime" / (file + ".md")).read_text(encoding="utf-8")
        declarations[kind] = set(re.findall(r"^- \*\*" + kind + r":([^*]+)\*\*", registry, re.M))
    unresolved = [(kind, name) for kind, name in calls if name not in declarations[kind]]
    print("[IMP:9][test_debugger_calls_resolve][RESULT] calls=%d unresolved=%s" % (len(calls), unresolved))
    assert calls
    assert unresolved == []
# endregion FUNC_test_debugger_calls_resolve


# region FUNC_test_debugger_shipped_boundaries_and_returns [DOMAIN(9): DebuggerContract; CONCEPT(9): Positive; TECH(5): pytest]
## @purpose Accept actual shipped restrictions using independently fixed obligations rather than producer expectations.
## @io pathlib.Path -> None
## @complexity 2
def test_debugger_shipped_boundaries_and_returns(repo_root):
    failures = _contract_failures(_debugger_text(repo_root))
    print("[IMP:9][test_debugger_shipped_boundaries_and_returns][RESULT] actual=%s expected=[]" % sorted(failures))
    assert failures == set()
# endregion FUNC_test_debugger_shipped_boundaries_and_returns


# region FUNC_test_debugger_finite_weakened_fixtures [DOMAIN(9): DebuggerContract; CONCEPT(10): DiscriminatingControl; TECH(5): pytest.parametrize]
## @purpose Verify each concrete loss changes the same helper's result on actual weakened shipped text.
## @io (str, str, str, str, pathlib.Path) -> None
## @complexity 3
@pytest.mark.parametrize("case,old,new,expected", WEAKENINGS, ids=[item[0] for item in WEAKENINGS])
def test_debugger_finite_weakened_fixtures(case, old, new, expected, repo_root):
    positive = _debugger_text(repo_root)
    positive_failures = _contract_failures(positive)
    print("[IMP:9][test_debugger_finite_weakened_fixtures][TRIGGER] case=%s matches=%d" %
          (case, positive.count(old) if old else 0))
    assert positive_failures == set()
    if old:
        assert positive.count(old) == 1, "fixed trigger must match actual role once"
        negative = positive.replace(old, new, 1)
    else:
        negative = positive + "\n" + new + "\n"
    failures = _contract_failures(negative)
    print("[IMP:9][test_debugger_finite_weakened_fixtures][RESULT] case=%s sha256=%s actual=%s expected=%s" %
          (case, hashlib.sha256(negative.encode()).hexdigest(), sorted(failures), expected))
    assert negative != positive
    assert failures == {expected}
# endregion FUNC_test_debugger_finite_weakened_fixtures
