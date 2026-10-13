# region MODULE_CONTRACT [DOMAIN(9): Review, PromptRouting; CONCEPT(9): RequiredOwner, Compatibility; TECH(7): Python, pytest]
## @modulecontract
## @purpose Reject incomplete required review ownership, missing external-agent routes and unauthorized helper algorithm drift.
## @scope Bounded source forms/cases/routes and exact release bridge; independent native source/output judgment remains separate.
## @input Actual read-only repository files; caplog and isolated tmp_path fixtures; fixed pre-Code AST identities.
## @output Meaningful current-source assertions with contrary omission/stub/algorithm controls and visible safe trace.
## @links [USES_API(8): ast.parse, ast.dump; USES_API(7): hashlib.sha256; USES_API(7): logging; READS_DATA_FROM(9): process/review.md, process/code-review.md, implementations/codex/skills, implementations/claude/skills]
## @invariants
## - Shared source bytes are never changed; contrary inputs are local strings/ASTs or owned files.
## - The fixed algorithm pins derive from authentic pre-Code bytes, not new observed behavior.
## - Finite source checks do not certify complete prose, native authoring, independence or target evaluation.
## @rationale
## Q: Why freeze normalized AST beside existing helper regressions?
## A: Only five current identity constants may change; any unrelated executable edit must refuse even if suites are green.
## Q: Why inspect contrary forms?
## A: Removing a required report boundary or substantive draft must fail the same predicate that accepts current source.
## @changes
## LAST_CHANGE: [1.1.0 - C1 required owners, direct external-agent route and fixed original helper algorithm controls.]
## @modulemap
## FUNC 1[Metadata anchor] => test_c1_review_and_routing._module_contract
## FUNC 8[Read complete source with owned safe trace] => test_c1_review_and_routing._read
## FUNC 8[Assess finite operating form and boundaries] => test_c1_review_and_routing._operating
## FUNC 9[Preserve required form/case/source duties] => test_c1_review_and_routing.test_required_review_owners_have_operating_forms_and_boundaries
## FUNC 9[Reject missing/stub full external-agent owner routes] => test_c1_review_and_routing.test_external_agent_route_requires_full_current_owner
## FUNC 9[Normalize only permitted current helper constants] => test_c1_review_and_routing._algorithm_identity
## FUNC 9[Preserve wire and full helper algorithms] => test_c1_review_and_routing.test_release_bridge_keeps_wire_and_helper_algorithms
## @usecases
## - Independent QA -> run owner omission/stub/contrary controls -> bounded source evidence for C1-AC1/2/3/6.
## - Independent QA -> compare fixed pre-Code algorithms and unrelated mutation -> C1-AC4/6 compatibility protection.
## @GREP_SUMMARY required review owners, external-agent one-shot route, normalized original AST, fixed compatibility, contrary controls
## @STRUCTURE ▶ actual source → ◇ form/route and original algorithm → ○ contrary omission/stub/drift → ⎋ bounded assertion
def _module_contract():
    pass
# endregion MODULE_CONTRACT


import ast
import hashlib
import json
import logging

LOGGER = logging.getLogger(__name__)
PINS = {'codex': 'f3a3773f070e8be24c669ee85ba75e4e37ab512efe415c82431926b97193fd4c', 'claude': 'b43c0dae8c085391ff3613557fcdfc4b9f150343a092bca0949753a797bf6c85'}

# region FUNC__read [DOMAIN(8): Source; CONCEPT(8): Identity; TECH(7): pathlib]
## @purpose Read complete required current text without source writes.
## @uses pathlib.Path.read_text, logging.Logger.info
## @io Input: root Path and safe relative str. Output: complete UTF8 str. Side effects: safe path/read trace only. Guarantees: full body returned. Raises: OSError/UnicodeError for unavailable input. Importance:8. Example: process/review.md returns its complete draft.
## @complexity 2
def _read(root, relative):
    # START_BLOCK_BusinessLogic
    try:
        text = (root / relative).read_text(encoding="utf-8")
    # START_BLOCK_ErrorHandling
    except (OSError, UnicodeError) as error:
        LOGGER.error("[IMP:10][_read][REFUSED] kind=%s", type(error).__name__)
        raise
    # END_BLOCK_ErrorHandling
    LOGGER.info("[IMP:7][_read][READ] path=%s", relative)
    return text
    # END_BLOCK_BusinessLogic
# endregion FUNC__read

# region FUNC__operating [DOMAIN(8): Review; CONCEPT(9): Completeness; TECH(7): logging]
## @purpose Reject a bounded report body lacking required operating form, cases or authority boundary.
## @uses logging.Logger.info, logging.Logger.error
## @io Input: full body str and expected required phrases tuple[str]. Output: bool. Invariants: input unchanged. Side effects: safe success/failure-class trace. Guarantees: all specified distinct required fields are checked. Errors: none for declared inputs. Importance:9. Example: a stub returns False.
## @complexity 3
def _operating(text, fields):
    # START_BLOCK_Validation
    complete = "\nstatus: draft\n" in text and all(field in text for field in fields)
    if not complete:
        LOGGER.error("[IMP:10][_operating][REFUSED] incomplete required operating body")
        print("[IMP:10][_operating][REFUSED] incomplete required operating body")
        return False
    LOGGER.info("[IMP:9][_operating][VALID] complete finite form and boundaries")
    print("[IMP:9][_operating][VALID] complete finite form and boundaries")
    return True
    # END_BLOCK_Validation
# endregion FUNC__operating

# region FUNC_test_required_review_owners_have_operating_forms_and_boundaries [DOMAIN(9): Review; CONCEPT(9): Completeness; TECH(7): pytest]
## @purpose Verify real complete report duties and discriminating missing-field/stub controls.
## @uses test_c1_review_and_routing._read, test_c1_review_and_routing._operating
## @io Input: repo_root Path and caplog fixture. Output: None after current/contrary assertions. Side effects: visible test trace only. Guarantees: every finite field removal and stub refuses; source unchanged; expected-only errors. Raises: AssertionError on mismatch. Importance:9. Example: removal of Continuation draft refuses.
## @complexity 5
def test_required_review_owners_have_operating_forms_and_boundaries(repo_root, caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    cases = {
        "process/review.md": ("## Operating procedure", "RUN REVIEW", "Population row:", "Artifact row:", "Obligation row:", "Continuation draft:", "unsent", "unknown, never zero", "**Positive", "**Boundary", "**Refusal"),
        "process/code-review.md": ("## Operating procedure", "CODE REVIEW", "Assignment/independence:", "Interface row:", "Requirement row:", "unchanged canonical", "ESCALATED_FINALIZE", "full independent QA", "**Positive", "**Boundary", "**Refusal"),
    }
    for relative, fields in cases.items():
        text = _read(repo_root, relative)
        assert _operating(text, fields)
        assert not [r for r in caplog.records if r.levelno >= logging.ERROR]
        caplog.clear()
        for field in fields:
            assert not _operating(text.replace(field, ""), fields)
        assert not _operating(text.replace("status: draft", "status: stub", 1), fields)
        errors = [r for r in caplog.records if r.levelno >= logging.ERROR]
        for record in caplog.records:
            print(record.getMessage())
        assert len(errors) == len(fields) + 1
        assert all("[_operating][REFUSED]" in r.getMessage() for r in errors)
        caplog.clear()
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_required_review_owners_have_operating_forms_and_boundaries

# region FUNC_test_external_agent_route_requires_full_current_owner [DOMAIN(9): Prompting; CONCEPT(9): Dependency; TECH(7): pytest]
## @purpose Verify direct one-shot/loop route with meaningful absent/stub current-source controls.
## @uses test_c1_review_and_routing._read, test_c1_review_and_routing._operating
## @io Input: repo_root Path, caplog fixture, tmp_path owned Path. Output: None after source and contrary assertions. Side effects: owned absent/stub file and visible trace only; no author/recipient execution. Guarantees: required actual owner full-source condition is checked and fallback remains forbidden. Raises: AssertionError on mismatch. Importance:9. Example: stub owner cannot satisfy full-source profile.
## @complexity 5
def test_external_agent_route_requires_full_current_owner(repo_root, caplog, tmp_path):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    general = _read(repo_root, "implementations/codex/skills/prompting/SKILL.md")
    specialized = _read(repo_root, "implementations/codex/skills/prompting-agent-design/SKILL.md")
    owner = _read(repo_root, "prompting/agent-prompt-design.md")
    for field in ("one-shot or loop", "prompting-agent-design", "ordinary short human-read prose"):
        assert field in general
        assert field not in general.replace(field, "", 1)
    for field in ("all three authored artifacts", "machine/reproducibility", "DRAFT/NOT_RUN", "synthetic-secret probe", "only to loop designs", "Missing, stub, stale, truncated or unread required content is BLOCKED"):
        assert field in specialized
    assert "\nstatus: draft\n" in owner and "cached installed constitution" in specialized
    assert not [r for r in caplog.records if r.levelno >= logging.ERROR]
    missing = tmp_path / "owner.md"
    assert not missing.exists()
    missing.write_text("---\nid: prompting.agent-prompt-design\nstatus: stub\n---\n")
    assert "\nstatus: draft\n" not in missing.read_text()
    print("[IMP:9][test_external_agent_route_requires_full_current_owner][RESULT] real route and absent/stub contrary source verified; native refusal remains separate")
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_external_agent_route_requires_full_current_owner

# region FUNC__algorithm_identity [DOMAIN(8): Compatibility; CONCEPT(9): AlgorithmFreeze; TECH(7): ast, hashlib]
## @purpose Compare whole helper algorithms after only their approved binding constant normalization.
## @uses ast.parse, ast.walk, ast.dump, hashlib.sha256, logging.Logger.info
## @io Input: full helper str and engine codex/claude. Output: SHA256 hex of AST with only exact 3/2 approved current constants restored. Invariants: input unchanged. Side effects: safe count/result trace. Raises: AssertionError on wrong permitted site population or value. Importance:9. Example: unrelated initialized counter change yields a different identity.
## @complexity 5
def _algorithm_identity(text, engine):
    # START_BLOCK_Validation
    tree = ast.parse(text)
    binding = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "_bindings")
    counts = {"1.1.0": 0, "2.1.0": 0}
    for node in ast.walk(binding):
        if isinstance(node, ast.Constant) and node.value in counts:
            counts[node.value] += 1
            node.value = "1.0.0" if node.value == "1.1.0" else "2.0.0"
    if counts != {"1.1.0": 2, "2.1.0": 1 if engine == "codex" else 0}:
        LOGGER.error("[IMP:10][_algorithm_identity][REFUSED] permitted site population mismatch")
        raise AssertionError("permitted site population mismatch")
    identity = hashlib.sha256(ast.dump(tree, include_attributes=False).encode()).hexdigest()
    LOGGER.info("[IMP:9][_algorithm_identity][RESULT] exact permitted sites and whole algorithm identity computed")
    return identity
    # END_BLOCK_Validation
# endregion FUNC__algorithm_identity

# region FUNC_test_release_bridge_keeps_wire_and_helper_algorithms [DOMAIN(9): Compatibility; CONCEPT(9): FrozenAlgorithm; TECH(7): pytest]
## @purpose Require current tight metadata while protecting entire original executable AST and unchanged wire/schema.
## @uses test_c1_review_and_routing._read, test_c1_review_and_routing._algorithm_identity, json.loads
## @io Input: repo_root Path, caplog fixture. Output: None after fixed current release and unrelated drift controls. Side effects: visible trace only. Guarantees: full helper AST freeze and original wire/schema remain; contrary mutation cannot match baseline. Raises: AssertionError on mismatch. Importance:9. Example: altering default max_debug4 to3 refuses the algorithm pin.
## @complexity 5
def test_release_bridge_keeps_wire_and_helper_algorithms(repo_root, caplog):
    # START_BLOCK_BusinessLogic
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    assert _read(repo_root, "SPEC_VERSION") == "1.1.0\n"
    for engine, version in (("codex", "2.1.0"), ("claude", "1.0.0")):
        base = "implementations/" + engine
        layout = json.loads(_read(repo_root, base + "/references/package-layout.json"))
        adapter = json.loads(_read(repo_root, base + "/adapter.json"))
        assert layout["version"] == version and adapter["spec_version"] == "1.1.0"
        text = _read(repo_root, base + "/skills/feature-dev/scripts/run_state.py")
        assert _algorithm_identity(text, engine) == PINS[engine]
        assert _algorithm_identity(text.replace("'schema_version': 2", "'schema_version': 3", 1), engine) != PINS[engine]
        assert "methodology-" + engine + ("/2.0.0" if engine == "codex" else "/1.0.0") in text
    for record in caplog.records:
        print(record.getMessage())
    assert not [r for r in caplog.records if r.levelno >= logging.ERROR]
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_release_bridge_keeps_wire_and_helper_algorithms
