# region MODULE_CONTRACT [DOMAIN(9): NeutralMethodology; CONCEPT(9): Approval, IndependentQA; TECH(6): pytest, re]
## @modulecontract
## @purpose Verify the first complete layer of neutral approval and QA contracts with independent readers.
## @scope Four subject cards, anchors, norm allocation, resolved restrictions, scans, registries and release records.
## @input Real repository files and synthetic mutations in pytest temporary storage.
## @output Assertion results and safe count/id traces in pytest stdout.
## @links [READS_DATA_FROM(9): process/gates.md, roles/_base.md, roles/qa.md, checks/qa-scans.md; USES_API(5): pytest]
## @invariants
## - The real repository is read-only; mutation probes use temporary storage only.
## - Assertions pin obligations independently of the implementation and require matching level and anchor.
## @rationale
## Q: Why a separate reader and synthetic negative cases?
## A: A checker must reject weakening independently of the production conformance parser.
## @changes
## LAST_CHANGE: [2.0.0 - M30 exact current release/census coupling; all prior cases/assertions/refusals retained.]
## Earlier: [1.1.0 - Reconcile current M19 boundary/release facts and paired source operands; preserve original assertions/pins/refusals/restoration; runtime checks pending.]
## @modulemap
## FUNC 7[read subject] => read_subject
## FUNC 7[require rule] => require_rule
## FUNC 7[assert call resolution] => assert_call_resolution
## FUNC 7[test subject cards and anchor order] => test_subject_cards_and_anchor_order
## FUNC 7[test subject norm floors and blocks] => test_subject_norm_floors_and_blocks
## FUNC 7[test gates require structured approval and declared fallback] => test_gates_require_structured_approval_and_declared_fallback
## FUNC 7[test cadence keeps two owner decisions] => test_cadence_keeps_two_owner_decisions
## FUNC 7[test QA reads judged change and relevant source before verdict] => test_qa_reads_judged_change_and_relevant_source_before_verdict
## FUNC 7[test traceability lint failure stops run and returns to owner] => test_traceability_lint_failure_stops_run_and_returns_to_owner
## FUNC 7[test registry requires every applicable scan and declared absence] => test_registry_requires_every_applicable_scan_and_declared_absence
## FUNC 7[test live calls resolve and cadence is declared] => test_live_calls_resolve_and_cadence_is_declared
## FUNC 7[test release and example adapter are current] => test_release_and_example_adapter_are_current
## FUNC 7[test each scan has purpose applicability evidence verdict and steps] => test_each_scan_has_purpose_applicability_evidence_verdict_and_steps
## FUNC 7[test finding code table preserves all catalogue classes] => test_finding_code_table_preserves_all_catalogue_classes
## FUNC 7[test content reader rejects missing norm negation reordered anchor and unresolved call] => test_content_reader_rejects_missing_norm_negation_reordered_anchor_and_unresolved_call
## @usecases
## - Maintainer -> removes a restriction, norm, anchor, scan or declaration -> the independent assertion fails.
## - Verifier -> runs the suite against the real files -> sees counts and the scope of structural evidence.
## @GREP_SUMMARY first layer, approval channels, cadence, scans, finding codes, registries, release, mutation guards
## @STRUCTURE read cards -> split anchors -> extract live norms and calls -> assert obligations -> reject synthetic weakening

def _module_contract():
    pass
# endregion MODULE_CONTRACT


import json
import re

import pytest

SUBJECTS = {
    "process/gates.md": ("process.gates", "GATE", 91, "decisions channel waiting cadence record spec-decision plan-mode result-evidence review result-decision git-hygiene terminal surfaces answer-handling".split()),
    "roles/_base.md": ("roles.base", "ROLE", 28, "preamble topology classifiers constitution boundaries return definitions".split()),
    "roles/qa.md": ("roles.qa", "QA", 41, "stance isolation inputs workflow diagnostic-trio verdict bug-report".split()),
    "checks/qa-scans.md": ("checks.qa-scans", "SCAN", 103, ["registry"] + [part for name in "green-test-trap quantitative-ac semantic-trace infra-dod side-effect-channel secret-leak real-path-shape discriminating-test".split() for part in (name, name + ".procedure")] + ["codes", "producer-mirror"]),
}
SCANS = "green-test-trap quantitative-ac semantic-trace infra-dod side-effect-channel secret-leak real-path-shape discriminating-test".split()
CODES = "GREEN_TEST_TRAP AC_UNMAPPED AC_QUANTITATIVE_FAIL SEMANTIC_TRACE_MISSING UNEXPECTED_ERROR_TRACE LDD_MISSING EXOSKELETON_MISSING EXOSKELETON_MISPLACED INFRA_HEALTHCHECK_BROKEN INFRA_STACK_FAILED INFRA_ENDPOINT_FAIL INFRA_PORT_HARDCODED INFRA_DOD_NOT_VERIFIED SIDE_EFFECT_CHANNEL_UNWIRED DELIVERY_CONTRACT_MISSING SECRET_LEAK VACUOUS_TEST QA_MUTATED_FILES MALFORMED_VERDICT TEST_DEFERRED EXTERNAL_DEPENDENCY HALLUCINATION_RISK".split()


# region FUNC_read_subject [DOMAIN(8): FirstLayer; CONCEPT(8): ContentVerification; TECH(4): pytest]
## @purpose read subject.
## @io Test inputs -> assertion or parsed content
## @complexity 4
def read_subject(path):
    print("[IMP:7][read_subject][READ] reading subject=%s" % path.name)
    text = path.read_text(encoding="utf-8")
    sections, norms, anchors = {}, {}, []
    current = None
    live = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            char = marker.group(1)[0]
            if fence is None:
                fence = char
            elif fence == char:
                fence = None
            continue
        if fence:
            continue
        hit = re.fullmatch(r"<!-- anchor: (\S+) -->", line)
        if hit:
            current = hit.group(1)
            assert current not in sections, "duplicate anchor"
            anchors.append(current)
            sections[current] = []
        hit = re.match(r"^- \*\*([A-Z]+-\d+)\*\* (MUST NOT|SHOULD NOT|MUST|SHOULD|MAY): (.+)$", line)
        if hit:
            assert current is not None and hit.group(1) not in norms, "unanchored or duplicate norm"
            norms[hit.group(1)] = (current, hit.group(2), hit.group(3))
        if current:
            sections[current].append(line)
        live.append(re.sub(r"`[^`]*`", "", line))
    assert fence is None, "unclosed fence"
    card = dict(re.findall(r"^([a-z-]+): (.+)$", text.split("---", 2)[1], re.M))
    calls = re.findall(r"\{\{(cap|param):([a-z0-9-]+)\}\}", "\n".join(live))
    print("[IMP:9][read_subject][PARSED] anchors=%d norms=%d calls=%d" % (len(anchors), len(norms), len(calls)))
    return card, anchors, norms, sections, calls
# endregion FUNC_read_subject


# region FUNC_require_rule [DOMAIN(8): FirstLayer; CONCEPT(8): ContentVerification; TECH(4): pytest]
## @purpose require rule.
## @io Test inputs -> assertion or parsed content
## @complexity 4
def require_rule(parsed, anchor, norm, level, fragments):
    print("[IMP:9][require_rule][CHECK] norm=%s" % norm)
    actual_anchor, actual_level, body = parsed[2][norm]
    assert actual_anchor == anchor and actual_level == level
    for fragment in fragments:
        assert fragment.lower() in body.lower(), "%s missing obligation: %s" % (norm, fragment)
# endregion FUNC_require_rule


# region FUNC_assert_call_resolution [DOMAIN(8): FirstLayer; CONCEPT(8): ContentVerification; TECH(4): pytest]
## @purpose assert call resolution.
## @io Test inputs -> assertion or parsed content
## @complexity 4
def assert_call_resolution(calls, declarations):
    print("[IMP:9][assert_call_resolution][CHECK] calls=%d" % len(calls))
    assert calls, "no live calls"
    for kind, name in calls:
        assert name in declarations[kind], "unresolved call"
# endregion FUNC_assert_call_resolution


# region FUNC_test_subject_cards_and_anchor_order [DOMAIN(8): FirstLayer; CONCEPT(8): ContentVerification; TECH(4): pytest]
## @purpose test subject cards and anchor order.
## @io Test inputs -> assertion or parsed content
## @complexity 4
def test_subject_cards_and_anchor_order(repo_root):
    print("[IMP:9][test_subject_cards_and_anchor_order][VERIFY] verifying first-layer contract")
    for path, (subject, _, _, suffixes) in SUBJECTS.items():
        card, anchors, _, _, _ = read_subject(repo_root / path)
        print("[IMP:9][test_subject_cards_and_anchor_order][CARD] subject=%s" % subject)
        assert card["id"] == subject and card["status"] == "draft"
        assert anchors == [subject + "." + suffix for suffix in suffixes]
        if path == "process/gates.md":
            assert card["skill-name"] == "gates"
            assert card["skill-when"] == "a specification is ready for the owner's approval, or a run ended with a verdict or another terminal status"
        elif path == "roles/qa.md":
            assert card["skill-name"] == "qa"
            assert card["skill-when"] == "the coder reported a slice complete and it needs an independent verdict"
        else:
            assert "skill-name" not in card and "skill-when" not in card
# endregion FUNC_test_subject_cards_and_anchor_order


# region FUNC_test_subject_norm_floors_and_blocks [DOMAIN(8): FirstLayer; CONCEPT(8): ContentVerification; TECH(4): pytest]
## @purpose test subject norm floors and blocks.
## @io Test inputs -> assertion or parsed content
## @complexity 4
def test_subject_norm_floors_and_blocks(repo_root):
    print("[IMP:9][test_subject_norm_floors_and_blocks][VERIFY] verifying first-layer contract")
    for path, (subject, prefix, floor, suffixes) in SUBJECTS.items():
        parsed = read_subject(repo_root / path)
        print("[IMP:9][test_subject_norm_floors_and_blocks][COUNT] norms=%d floor=%d" % (len(parsed[2]), floor))
        assert len(parsed[2]) >= floor
        blocks = [s for s in suffixes if not s.endswith(".procedure")]
        for norm, (anchor, _, _) in parsed[2].items():
            block = int(norm.split("-")[1]) // 100
            suffix = anchor[len(subject) + 1:].removesuffix(".procedure")
            if norm.startswith("CODER-"):
                assert path == "checks/qa-scans.md" and suffix == "producer-mirror" and block == 9
            else:
                assert norm.startswith(prefix + "-")
                assert block == blocks.index(suffix) + 1
# endregion FUNC_test_subject_norm_floors_and_blocks


# region FUNC_test_gates_require_structured_approval_and_declared_fallback [DOMAIN(8): FirstLayer; CONCEPT(8): ContentVerification; TECH(4): pytest]
## @purpose test gates require structured approval and declared fallback.
## @io Test inputs -> assertion or parsed content
## @complexity 4
def test_gates_require_structured_approval_and_declared_fallback(repo_root):
    print("[IMP:9][test_gates_require_structured_approval_and_declared_fallback][VERIFY] verifying first-layer contract")
    parsed = read_subject(repo_root / "process/gates.md")
    anchor = "process.gates.channel"
    expected = {
        "GATE-201": ("MUST", ["structured", "{{cap:ask-owner-structured}}", "{{cap:plan-mode}}"]),
        "GATE-202": ("MUST NOT", ["free-form chat", "declares", "mechanism"]),
        "GATE-203": ("MAY", ["no structured mechanism", "declared fallback", "verbatim", "version or hash", "scope", "who", "when", "ambiguous"]),
        "GATE-204": ("MUST", ["concrete artifact", "wait", "already answered"]),
        "GATE-205": ("MUST NOT", ["silence", "timeout", "default", "another agent", "tool result"]),
    }
    for norm, (level, fragments) in expected.items():
        require_rule(parsed, anchor, norm, level, fragments)
# endregion FUNC_test_gates_require_structured_approval_and_declared_fallback


# region FUNC_test_cadence_keeps_two_owner_decisions [DOMAIN(8): FirstLayer; CONCEPT(8): ContentVerification; TECH(4): pytest]
## @purpose test cadence keeps two owner decisions.
## @io Test inputs -> assertion or parsed content
## @complexity 4
def test_cadence_keeps_two_owner_decisions(repo_root):
    print("[IMP:9][test_cadence_keeps_two_owner_decisions][VERIFY] verifying first-layer contract")
    parsed = read_subject(repo_root / "process/gates.md")
    anchor = "process.gates.cadence"
    expected = {
        "GATE-401": ("MUST", ["batch", "class", "finish line", "stop conditions", "scope", "inherits"]),
        "GATE-402": ("MAY", ["owner", "separate"]),
        "GATE-403": ("MUST", ["approved scope", "irreversible", "unexplained"]),
        "GATE-404": ("MUST NOT", ["size", "waive", "gate"]),
        "GATE-405": ("MUST", ["reconnaissance", "result", "roadmap"]),
        "GATE-406": ("MUST", ["two owner decisions", "before any code", "concrete result", "live probe", "merge", "publish", "deploy", "{{param:gate-cadence}}"]),
        "GATE-407": ("MUST", ["S", "M", "L", "per-change", "reconnaissance", "specification"]),
        "GATE-408": ("MUST NOT", ["result decision", "in advance", "waive"]),
    }
    for norm, (level, fragments) in expected.items():
        require_rule(parsed, anchor, norm, level, fragments)
# endregion FUNC_test_cadence_keeps_two_owner_decisions


# region FUNC_test_qa_reads_judged_change_and_relevant_source_before_verdict [DOMAIN(8): FirstLayer; CONCEPT(9): QAInputs; TECH(4): pytest]
## @purpose Require the judge to read the delivered change and relevant source before judging, alongside project instructions.
## @io Repository root -> assertions over the real base and QA norms
## @complexity 3
def test_qa_reads_judged_change_and_relevant_source_before_verdict(repo_root):
    # BUG_FIX_CONTEXT: A shared instruction-read rule lost the QA-specific change/source prerequisite; pin both carriers.
    print("[IMP:9][test_qa_reads_judged_change_and_relevant_source_before_verdict][VERIFY] checking QA input prerequisites")
    base = read_subject(repo_root / "roles/_base.md")
    require_rule(base, "roles.base.topology", "ROLE-203", "MUST", ["Read applicable project instructions", "before acting"])
    qa = read_subject(repo_root / "roles/qa.md")
    require_rule(qa, "roles.qa.inputs", "QA-309", "MUST", ["Read the actual diff of the judged change", "including new files", "and relevant source before judging"])
# endregion FUNC_test_qa_reads_judged_change_and_relevant_source_before_verdict


# region FUNC_test_traceability_lint_failure_stops_run_and_returns_to_owner [DOMAIN(8): FirstLayer; CONCEPT(9): TerminalRouting; TECH(4): pytest]
## @purpose Require lint exit one to stop the cycle as a visual-gate failure and return the decision to the owner.
## @io Repository root -> assertions over the real terminal norm
## @complexity 3
def test_traceability_lint_failure_stops_run_and_returns_to_owner(repo_root):
    # BUG_FIX_CONTEXT: Naming a terminal status did not specify its lint-failure trigger or owner route; pin the full transition.
    print("[IMP:9][test_traceability_lint_failure_stops_run_and_returns_to_owner][VERIFY] checking lint failure routing")
    gates = read_subject(repo_root / "process/gates.md")
    require_rule(gates, "process.gates.terminal", "GATE-1210", "MUST", ["If the traceability lint exits 1", "SCOPE_CREEP", "UNKNOWN_BR", "UNCOVERED_REQUIREMENT", "stop the cycle as VISUAL_GATE_FAIL", "return to the owner for a decision"])
# endregion FUNC_test_traceability_lint_failure_stops_run_and_returns_to_owner


# region FUNC_test_registry_requires_every_applicable_scan_and_declared_absence [DOMAIN(8): FirstLayer; CONCEPT(8): ContentVerification; TECH(4): pytest]
## @purpose test registry requires every applicable scan and declared absence.
## @io Test inputs -> assertion or parsed content
## @complexity 4
def test_registry_requires_every_applicable_scan_and_declared_absence(repo_root):
    print("[IMP:9][test_registry_requires_every_applicable_scan_and_declared_absence][VERIFY] verifying first-layer contract")
    parsed = read_subject(repo_root / "checks/qa-scans.md")
    require_rule(parsed, "checks.qa-scans.registry", "SCAN-103", "MUST", ["every registry id", "PASS", "FAIL", "N/A", "BLOCKED", "reason", "evidence", "hint", "missing"])
    require_rule(parsed, "checks.qa-scans.registry", "SCAN-114", "MUST", ["eight"] + SCANS)
    require_rule(parsed, "checks.qa-scans.registry", "SCAN-115", "MUST", ["absent", "adapter", "reason", "trigger", "control run", "false positives", "undeclared gap"])
    qa = read_subject(repo_root / "roles/qa.md")
    require_rule(qa, "roles.qa.verdict", "QA-602", "MUST", ["full suite", "every applicable", "PASS", "measurable", "no required", "unverified", "deferred", "N/A", "reason"])
# endregion FUNC_test_registry_requires_every_applicable_scan_and_declared_absence


# region FUNC_test_live_calls_resolve_and_cadence_is_declared [DOMAIN(8): FirstLayer; CONCEPT(8): ContentVerification; TECH(4): pytest]
## @purpose test live calls resolve and cadence is declared.
## @io Test inputs -> assertion or parsed content
## @complexity 4
def test_live_calls_resolve_and_cadence_is_declared(repo_root):
    print("[IMP:9][test_live_calls_resolve_and_cadence_is_declared][VERIFY] verifying first-layer contract")
    declarations = {}
    for kind, relative in (("cap", "capabilities"), ("param", "parameters")):
        print("[IMP:7][test_live_calls_resolve_and_cadence_is_declared][READ] registry=%s" % kind)
        text = (repo_root / "runtime" / (relative + ".md")).read_text(encoding="utf-8")
        declarations[kind] = set(re.findall(r"^- \*\*" + kind + r":([^*]+)\*\*", text, re.M))
    calls = []
    for path in SUBJECTS:
        calls.extend(read_subject(repo_root / path)[4])
    print("[IMP:9][test_live_calls_resolve_and_cadence_is_declared][CHECK] parameters=%d" % len(declarations["param"]))
    assert "gate-cadence" in declarations["param"]
    assert_call_resolution(calls, declarations)
    assert ("param", "gate-cadence") in calls
# endregion FUNC_test_live_calls_resolve_and_cadence_is_declared


# region FUNC_test_release_and_example_adapter_are_current [DOMAIN(8): FirstLayer; CONCEPT(8): ContentVerification; TECH(4): pytest]
## @purpose Verify the current release/adapter while preserving the historical first-layer changelog obligations.
## @io Test inputs -> assertion or parsed content
## @complexity 4
def test_release_and_example_adapter_are_current(repo_root):
    print("[IMP:9][test_release_and_example_adapter_are_current][VERIFY] verifying first-layer contract")
    print("[IMP:7][test_release_and_example_adapter_are_current][READ] release records")
    version = (repo_root / "SPEC_VERSION").read_bytes()
    adapter = json.loads((repo_root / "examples/adapter.example.json").read_text(encoding="utf-8"))
    changes = (repo_root / "CHANGELOG.md").read_text(encoding="utf-8").split("## 0.2.0", 1)
    print("[IMP:9][test_release_and_example_adapter_are_current][CHECK] version bytes=%d" % len(version))
    assert version == b"3.0.2\n" and adapter["spec_version"] == "3.0.2"
    assert adapter["parameters"]["gate-cadence"] == "per-change"
    assert len(changes) == 2
    entry = changes[1].split("## ", 1)[0]
    assert all(path in entry for path in SUBJECTS)
    assert "gate-cadence" in entry
# endregion FUNC_test_release_and_example_adapter_are_current


# region FUNC_test_each_scan_has_purpose_applicability_evidence_verdict_and_steps [DOMAIN(8): FirstLayer; CONCEPT(8): ContentVerification; TECH(4): pytest]
## @purpose test each scan has purpose applicability evidence verdict and steps.
## @io Test inputs -> assertion or parsed content
## @complexity 4
def test_each_scan_has_purpose_applicability_evidence_verdict_and_steps(repo_root):
    print("[IMP:9][test_each_scan_has_purpose_applicability_evidence_verdict_and_steps][VERIFY] verifying first-layer contract")
    parsed = read_subject(repo_root / "checks/qa-scans.md")
    for scan in SCANS:
        anchor = "checks.qa-scans." + scan
        body = "\n".join(parsed[3][anchor])
        print("[IMP:9][test_each_scan_has_purpose_applicability_evidence_verdict_and_steps][CHECK] scan=%s" % scan)
        for label in ("Purpose:", "Applicability:", "Evidence:", "Verdict:"):
            assert label in body
        steps = [n for n, (a, _, _) in parsed[2].items() if a == anchor + ".procedure"]
        assert steps
        assert "FAIL" in body and ("BLOCKED" in body or scan not in ("infra-dod", "side-effect-channel"))
# endregion FUNC_test_each_scan_has_purpose_applicability_evidence_verdict_and_steps


# region FUNC_test_finding_code_table_preserves_all_catalogue_classes [DOMAIN(8): FirstLayer; CONCEPT(8): ContentVerification; TECH(4): pytest]
## @purpose test finding code table preserves all catalogue classes.
## @io Test inputs -> assertion or parsed content
## @complexity 4
def test_finding_code_table_preserves_all_catalogue_classes(repo_root):
    print("[IMP:9][test_finding_code_table_preserves_all_catalogue_classes][VERIFY] verifying first-layer contract")
    parsed = read_subject(repo_root / "checks/qa-scans.md")
    table = "\n".join(parsed[3]["checks.qa-scans.codes"])
    rows = re.findall(r"^\| `([^`]+)`(.*?)$", table, re.M)
    found = []
    for codes, columns in rows:
        found.extend(codes.split(" / "))
        assert len(columns.split("|")) >= 4 and len(columns.strip()) > 20
    print("[IMP:9][test_finding_code_table_preserves_all_catalogue_classes][CHECK] codes=%d" % len(found))
    assert found == CODES
    assert all("SCAN-%d" % n in parsed[2] for n in range(1001, 1022))
    assert "producer classifications" in table and "no new QA recognizer" in table
    assert "isolation" in table and "verdict shape" in table and "producer marker" in table
# endregion FUNC_test_finding_code_table_preserves_all_catalogue_classes


# region FUNC_test_content_reader_rejects_missing_norm_negation_reordered_anchor_and_unresolved_call [DOMAIN(8): FirstLayer; CONCEPT(8): ContentVerification; TECH(4): pytest]
## @purpose test content reader rejects missing norm negation reordered anchor and unresolved call.
## @io Test inputs -> assertion or parsed content
## @complexity 4
def test_content_reader_rejects_missing_norm_negation_reordered_anchor_and_unresolved_call(tmp_path):
    print("[IMP:9][test_content_reader_rejects_missing_norm_negation_reordered_anchor_and_unresolved_call][VERIFY] verifying first-layer contract")
    path = tmp_path / "sample.md"
    text = "---\nid: sample\nstatus: draft\n---\n<!-- anchor: sample.channel -->\n- **GATE-201** MUST NOT: Infer approval from silence.\n{{cap:ask-owner-structured}}\n<!-- anchor: sample.next -->\n"
    path.write_text(text, encoding="utf-8")
    print("[IMP:7][test_content_reader_rejects_missing_norm_negation_reordered_anchor_and_unresolved_call][WRITE] temporary sample")
    control = read_subject(path)
    require_rule(control, "sample.channel", "GATE-201", "MUST NOT", ["silence"])
    assert control[1] == ["sample.channel", "sample.next"]
    assert_call_resolution(control[4], {"cap": {"ask-owner-structured"}})
    for mutated in (text.replace("- **GATE-201** MUST NOT: Infer approval from silence.\n", ""), text.replace("MUST NOT", "MUST")):
        path.write_text(mutated, encoding="utf-8")
        with pytest.raises((AssertionError, KeyError)):
            require_rule(read_subject(path), "sample.channel", "GATE-201", "MUST NOT", ["silence"])
    path.write_text(text.replace("sample.channel", "sample.swap").replace("sample.next", "sample.channel").replace("sample.swap", "sample.next"), encoding="utf-8")
    print("[IMP:9][test_content_reader_rejects_missing_norm_negation_reordered_anchor_and_unresolved_call][REJECT] reordered anchors")
    with pytest.raises(AssertionError):
        assert read_subject(path)[1] == control[1]
    with pytest.raises(AssertionError):
        assert_call_resolution([("cap", "unresolved")], {"cap": {"ask-owner-structured"}})
# endregion FUNC_test_content_reader_rejects_missing_norm_negation_reordered_anchor_and_unresolved_call
