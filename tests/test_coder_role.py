# region MODULE_CONTRACT [DOMAIN(9): CoderContract; CONCEPT(9): Boundaries, FiniteCorpus, IndependentAssertions; TECH(6): pytest, re, hashlib]
## @modulecontract
## @purpose Expose finite structural defects in the shipped Coder body without claiming automated semantic fidelity.
## @scope Coder card, anchors, normative IDs, authority restrictions and generic disclosed-stub readiness; fixed structural controls.
## @input Read-only repository bytes and a separately fixed positive/negative prose corpus in this module.
## @output Named bounded defect observations and importance 7–10 diagnostics in the actual pytest stdout.
## @links [READS_DATA_FROM(9): roles/coder.md; USES_API(7): pytest.mark.parametrize; USES_API(6): re; USES_API(6): hashlib.sha256]
## @invariants
## - Fixtures do not mutate public sources and do not derive their expected obligations from a producer.
## - Expected structural refusals are results, not failed sessions; the existing session hooks own Anti-Loop accounting.
## - Matching sentences is finite mechanical evidence; independent actual-prose judgment remains required.
## @rationale
## Q: Why a fixed corpus in addition to the real role file?
## A: A control that accepted its own weakened fixture would conceal a defect; the same helper must distinguish fixed good/bad prose.
## Q: Why direct calls and pytest stdout?
## A: This is pure structural logic with a test-process sink, so subprocess wrappers and a second runtime channel are unnecessary.
## @changes
## LAST_CHANGE: [v1.0.0 - Reconcile only the independent neutral namespace/current facts; preserve original controls and full publication coverage; runtime checks pending.]
## @modulemap
## FUNC 7[Read shipped role bytes and expose identity without private text.] => _coder_text
## FUNC 8[Observe only fixed boundary/stub assertions and specific authority grants.] => _structural_failures
## FUNC 8[Check draft card, anchor placement and unique repository CODE allocation.] => test_coder_card_and_norm_structure
## FUNC 8[Reject explicit merge and inner-dispatch grants through the shipped-candidate helper.] => test_coder_boundaries_reject_authority_grants
## FUNC 8[Reject the finite substantive-stub prerequisite claim with and without disclosure.] => test_coder_document_stub_misuse_is_rejected
## FUNC 8[Differentiate an independent fixed positive corpus and its concrete weakened cases.] => test_coder_fixed_weakened_corpus_is_rejected
## @usecases
## - [test_coder_boundaries_reject_authority_grants]: Reviewer -> inspect actual rejection labels -> bounded authority evidence.
## - [test_coder_fixed_weakened_corpus_is_rejected]: Maintainer -> weaken a fixed fixture -> its specific expected result changes.
## @GREP_SUMMARY Coder, finite structural controls, draft card, CODE uniqueness, authority, disclosed stub prerequisite, semantic review boundary
## @STRUCTURE ▶ shipped bytes + fixed corpus → ⊕ structural observations → ◇ distinct expected labels → ⎋ independent meaning review

def _module_contract():
    pass
# endregion MODULE_CONTRACT


import hashlib
import re

import pytest

BOUNDARY = "Commit, merge, spawn or invoke another role, or self-certify as independent QA."
# BUG_FIX_CONTEXT: The document body is promoted; require the still-current generic stub prerequisite refusal, independently fixed below.
STUB = "Treat a disclosed stub as no substantive prerequisite."
MERGE_GRANT = "The Coder may merge the implementation without the parent."
DISPATCH_GRANT = "The Coder may spawn QA as an inner implementation role."
STUB_CLAIM = "A disclosed stub supplies a substantive prerequisite."
# Independently fixed obligations: never built from the shipped candidate's parsed data.
POSITIVE_BODY = (
    "- **CODE-603** MUST NOT: Commit, merge, spawn or invoke another role, or self-certify as independent QA.\n"
    "- **CODE-107** MUST: Treat a disclosed stub as no substantive prerequisite.\n"
)
FIXED_CORPUS = (
    ("positive", POSITIVE_BODY, set()),
    ("merge-grant", POSITIVE_BODY + "The Coder may merge the implementation without the parent.\n", {"MERGE_AUTHORITY_GRANT"}),
    ("inner-dispatch-grant", POSITIVE_BODY + "The Coder may spawn QA as an inner implementation role.\n", {"INNER_DISPATCH_GRANT"}),
    ("missing-prohibition", "- **CODE-603** MAY: Merge and invoke other roles.\n" +
     "- **CODE-107** MUST: Treat a disclosed stub as no substantive prerequisite.\n",
     {"BOUNDARY_CLAUSE_MISSING"}),
    ("missing-stub-disclosure", "- **CODE-603** MUST NOT: Commit, merge, spawn or invoke another role, or self-certify as independent QA.\n",
     {"STUB_DISCLOSURE_MISSING"}),
    ("substantive-stub-claim", POSITIVE_BODY + "A disclosed stub supplies a substantive prerequisite.\n", {"SUBSTANTIVE_STUB_CLAIM"}),
    ("replacement-stub-claim", "- **CODE-603** MUST NOT: Commit, merge, spawn or invoke another role, or self-certify as independent QA.\n" +
     "- **CODE-107** MUST: A disclosed stub supplies a substantive prerequisite.\n",
     {"STUB_DISCLOSURE_MISSING", "SUBSTANTIVE_STUB_CLAIM"}),
)


# region FUNC__coder_text [DOMAIN(8): CoderContract; CONCEPT(8): ActualBytes; TECH(5): pathlib, hashlib]
## @purpose Read shipped bytes with an actual identity before asserting any contract property.
## @uses hashlib.sha256
## @io Repository path -> UTF-8 role text
## @complexity 3
def _coder_text(repo_root):
    path = repo_root / "roles/coder.md"
    print("[IMP:7][_coder_text][READ] subject=roles/coder.md")
    try:
        data = path.read_bytes()
        text = data.decode("utf-8")
    except (OSError, UnicodeError) as error:
        print("[IMP:10][_coder_text][READ_ERROR] class=%s" % type(error).__name__)
        raise
    print("[IMP:9][_coder_text][IDENTITY] bytes=%d sha256=%s" % (len(data), hashlib.sha256(data).hexdigest()))
    return text
# endregion FUNC__coder_text


# region FUNC__structural_failures [DOMAIN(8): CoderContract; CONCEPT(9): FiniteObservation; TECH(5): str, re]
## @purpose Expose exactly the fixed authority/stub failure classes, leaving interpretation to independent review.
## @uses re.findall
## @io Supplied prose -> set of finite structural failure labels
## @complexity 4
def _structural_failures(text):
    print("[IMP:7][_structural_failures][INPUT] chars=%d" % len(text))
    clauses = re.findall(r"^- \*\*(CODE-\d+)\*\* (MUST NOT|MUST|MAY): (.+)$", text, re.M)
    failures = set()
    if not any(norm == "CODE-603" and level == "MUST NOT" and body.startswith(BOUNDARY) for norm, level, body in clauses):
        failures.add("BOUNDARY_CLAUSE_MISSING")
        print("[IMP:9][_structural_failures][BOUNDARY] required clause absent")
    if not any(norm == "CODE-107" and level == "MUST" and STUB in body for norm, level, body in clauses):
        failures.add("STUB_DISCLOSURE_MISSING")
        print("[IMP:9][_structural_failures][STUB] required disclosure absent")
    for phrase, label in ((MERGE_GRANT, "MERGE_AUTHORITY_GRANT"), (DISPATCH_GRANT, "INNER_DISPATCH_GRANT"), (STUB_CLAIM, "SUBSTANTIVE_STUB_CLAIM")):
        if phrase in text:
            failures.add(label)
            print("[IMP:9][_structural_failures][FIXED_REFUSAL] class=%s" % label)
    print("[IMP:9][_structural_failures][RESULT] clauses=%d failures=%s" % (len(clauses), sorted(failures)))
    return failures
# endregion FUNC__structural_failures


# region FUNC_test_coder_card_and_norm_structure [DOMAIN(8): CoderContract; CONCEPT(9): Format, UniqueNorms; TECH(5): pytest, re]
## @purpose Check actual card, anchor placement and repository-unique CODE IDs independently of the conformance producer.
## @uses _coder_text, re.findall
## @io Read-only repository and read_card fixture -> asserted structural facts
## @complexity 5
def test_coder_card_and_norm_structure(repo_root, read_card):
    text = _coder_text(repo_root)
    card, _body = read_card(repo_root / "roles/coder.md")
    anchors = re.findall(r"^<!-- anchor: (\S+) -->$", text, re.M)
    norms = re.findall(r"^- \*\*(CODE-\d+)\*\* (MUST NOT|SHOULD NOT|MUST|SHOULD|MAY): (.+)$", text, re.M)
    locations = []
    print("[IMP:7][test_coder_card_and_norm_structure][READ_SCOPE] neutral Markdown excluding tests/examples/builds/typed implementations")
    for path in sorted(repo_root.rglob("*.md")):
        relative = path.relative_to(repo_root)
        if relative.parts[0] in {".git", "tests", "examples", "doxygen_output", ".pytest_cache", "__pycache__", "implementations"}:
            continue
        if relative.as_posix() in {"README.md", "CHANGELOG.md"}:
            continue
        source = path.read_text(encoding="utf-8")
        locations.extend((norm, relative.as_posix()) for norm in re.findall(r"^- \*\*(CODE-\d+)\*\* ", source, re.M))
    ids = [norm for norm, _level, _text in norms]
    current_anchor = None
    unanchored = []
    for line in text.splitlines():
        if line.startswith("<!-- anchor: "):
            current_anchor = line
        if line.startswith("- **CODE-") and current_anchor is None:
            unanchored.append(line.split("**")[1])
    print("[IMP:9][test_coder_card_and_norm_structure][RESULT] card=%s anchors=%d norms=%d unique=%d locations=%d unanchored=%s" % (card, len(anchors), len(ids), len(set(ids)), len(locations), unanchored))
    assert card == {"id": "roles.coder", "title": "Coder", "status": "draft"}
    assert anchors == ["roles.coder." + suffix for suffix in ("inputs", "implementation", "verification", "deviations", "returns", "boundaries")]
    assert norms and len(ids) == len(set(ids))
    assert unanchored == []
    assert sorted(locations) == sorted((norm, "roles/coder.md") for norm in ids)
    assert _structural_failures(text) == set()
# endregion FUNC_test_coder_card_and_norm_structure


# region FUNC_test_coder_boundaries_reject_authority_grants [DOMAIN(8): CoderContract; CONCEPT(9): Authority; TECH(5): pytest]
## @purpose Refuse the fixed merge and inner-dispatch grants even when the original prohibition survives.
## @uses _coder_text, _structural_failures
## @io Real candidate text plus fixed grant -> specific structural rejection
## @complexity 3
@pytest.mark.parametrize("grant,expected", [(MERGE_GRANT, "MERGE_AUTHORITY_GRANT"), (DISPATCH_GRANT, "INNER_DISPATCH_GRANT")])
def test_coder_boundaries_reject_authority_grants(repo_root, grant, expected):
    candidate = _coder_text(repo_root)
    good = _structural_failures(candidate)
    bad = _structural_failures(candidate + "\n" + grant)
    print("[IMP:9][test_coder_boundaries_reject_authority_grants][RESULT] good=%s bad=%s expected=%s" % (sorted(good), sorted(bad), expected))
    assert good == set()
    assert bad == {expected}
# endregion FUNC_test_coder_boundaries_reject_authority_grants


# region FUNC_test_coder_document_stub_misuse_is_rejected [DOMAIN(8): CoderContract; CONCEPT(9): StubDisclosure; TECH(5): pytest]
## @purpose Distinguish surviving disclosure with a contradictory claim from disclosure replaced by that claim.
## @uses _coder_text, _structural_failures
## @io Real candidate and two concrete stub misuses -> specific structural rejections
## @complexity 4
def test_coder_document_stub_misuse_is_rejected(repo_root):
    candidate = _coder_text(repo_root)
    good = _structural_failures(candidate)
    contradictory = _structural_failures(candidate + "\n" + STUB_CLAIM)
    replaced = _structural_failures(candidate.replace(STUB, STUB_CLAIM))
    print("[IMP:9][test_coder_document_stub_misuse_is_rejected][RESULT] good=%s added=%s replaced=%s" % (sorted(good), sorted(contradictory), sorted(replaced)))
    assert good == set()
    assert contradictory == {"SUBSTANTIVE_STUB_CLAIM"}
    assert replaced == {"STUB_DISCLOSURE_MISSING", "SUBSTANTIVE_STUB_CLAIM"}
# endregion FUNC_test_coder_document_stub_misuse_is_rejected


# region FUNC_test_coder_fixed_weakened_corpus_is_rejected [DOMAIN(8): CoderContract; CONCEPT(9): Discrimination; TECH(5): pytest.mark.parametrize]
## @purpose Require the same helper to reject independent fixed weakened bodies rather than compare the producer to itself.
## @uses _structural_failures
## @io Fixed independent case, body and expected labels -> structural assertion
## @complexity 3
@pytest.mark.parametrize("name,body,expected", FIXED_CORPUS, ids=[case[0] for case in FIXED_CORPUS])
def test_coder_fixed_weakened_corpus_is_rejected(name, body, expected):
    observed = _structural_failures(body)
    print("[IMP:9][test_coder_fixed_weakened_corpus_is_rejected][RESULT] case=%s observed=%s expected=%s" % (name, sorted(observed), sorted(expected)))
    assert observed == expected
# endregion FUNC_test_coder_fixed_weakened_corpus_is_rejected
