# region MODULE_CONTRACT [DOMAIN(9): DesignContract; CONCEPT(9): Plan, XML, ReferenceIdentity, Coverage; TECH(6): pytest, xml]
## @modulecontract
## @purpose Exercise finite shipped plan/XML/reference bytes and expose distinct defects for independent meaning review.
## @scope The design-contract examples and the four draft contract bodies; no general-purpose validator or product runtime.
## @input Real repository fixture bytes, registry hashes, embedded XML and original review inputs.
## @output Actual XML parser failures, structural observations and before-assert diagnostics; no semantic PASS judgment.
## @links [READS_DATA_FROM(9): examples/design-contract; READS_DATA_FROM(9): protocols/graph.md; USES_API(8): xml.etree.ElementTree]
## @links_to_spec ARCH-401, PLAN-101–104, PLAN-301–308, PLAN-401–404, GRAPH-101–303
## @invariants Definitions exclude metadata and typed references; malformed and semantic defects stay distinct.
## @rationale Finite fixture assertions establish observable facts, while independent judges retain source-fidelity decisions.
## @changes
## LAST_CHANGE: [v0.5.0 - Inspect actual diagram/operation alignment and FILE-derived definition collisions; retain real-byte negative evidence.]
## @modulemap
## FUNC 8[Expose actual fixture identity and observed condition before assertions.] => _trace
## FUNC 8[Parse only a named shipped fixture through the actual XML parser.] => _xml
## FUNC 8[Compare embedded plan XML to the shipped graph and verify actual entity fields and paired boundaries.] => test_plan_xml_definitions
## FUNC 8[Exercise local edge resolution and all three BR membership obligations on actual positive graphs.] => test_positive_links_and_coverage
## FUNC 8[Hash real source/map bytes and resolve the declared entity and exact source line.] => test_brownfield_reference_identity
## FUNC 8[Observe the actual parser refusal of the malformed shipped bytes.] => test_malformed_xml_fails_real_parser
## FUNC 8[Differentiate exact duplicate definitions from normalized distinct spelling collisions.] => test_identity_negatives_are_distinct
## FUNC 8[Prove the unresolved target remains a local Link and has no implicit external identity.] => test_dangling_link_stays_local
## FUNC 8[Check separate missing registry, fabricated entity, stale map and stale source defects.] => test_reference_negatives_discriminate
## FUNC 8[Observe each concrete satisfaction failure without treating greenfield as a waiver.] => test_satisfaction_negatives_discriminate
## FUNC 8[Read actual clauses and concrete review inputs; leave semantic outcomes to independent judgment.] => test_semantic_case_and_control_inputs_exist
## FUNC 8[Inspect draft cards, anchors, normative IDs and declared calls on actual four bodies] => test_design_bodies_have_contract_structure
## FUNC 8[Compare finite diagrams to actual graph relationships, satisfaction and scenario operations] => test_plan_diagrams_follow_actual_graph
## @usecases
## - [test_brownfield_reference_identity]: Judge -> inspect map/hash/lookup -> actual existing reference evidence is visible.
## - [test_satisfaction_negatives_discriminate]: Judge -> compare BR defects -> greenfield retains all three coverage checks.
## @GREP_SUMMARY finite design fixtures, actual XML, hash identity, paired plan markers, BR coverage, distinct negatives, semantic inputs
## @STRUCTURE ▶ actual fixture bytes → ⚡ XML parser → ∑ definitions/edges/hash/lookup → ◇ distinct asserted conditions → ⎋ independent semantic judgment
def _module_contract():
    pass
# endregion MODULE_CONTRACT


import hashlib
import json
import re
import xml.etree.ElementTree as XML

import pytest


# region FUNC__trace [DOMAIN(8): DesignContract; CONCEPT(8): FixtureEvidence; TECH(5): pytest, xml]
## @purpose Expose actual fixture identity and observed condition before assertions.
## @io Actual fixture bytes -> observed condition
## @complexity 5
def _trace(name, block, detail):
    print("[IMP:9][%s][%s] %s" % (name, block, detail))
# endregion FUNC__trace


# region FUNC__xml [DOMAIN(8): DesignContract; CONCEPT(8): FixtureEvidence; TECH(5): pytest, xml]
## @purpose Parse only a named shipped fixture through the actual XML parser.
## @io Actual fixture bytes -> observed condition
## @complexity 5
def _xml(repo_root, name):
    data = (repo_root / "examples/design-contract" / name).read_bytes()
    _trace("_xml", "PARSE", "file=%s bytes=%d sha256=%s" % (name, len(data), hashlib.sha256(data).hexdigest()))
    return XML.fromstring(data)
# endregion FUNC__xml


# region FUNC_test_plan_xml_definitions [DOMAIN(8): DesignContract; CONCEPT(8): FixtureEvidence; TECH(5): pytest, xml]
## @purpose Compare embedded plan XML to the shipped graph and verify actual entity fields and paired boundaries.
## @io Actual fixture bytes -> observed condition
## @complexity 5
@pytest.mark.parametrize("name,count", [("greenfield", 3), ("brownfield", 2)])
def test_plan_xml_definitions(repo_root, name, count):
    text = (repo_root / "examples/design-contract" / (name + "-plan.md")).read_text()
    embedded = re.search(r"```xml\n(.*?)\n```", text, re.S).group(1)
    graph = _xml(repo_root, name + ".xml")
    definitions = [node for node in graph if "FILE" in node.attrib]
    _trace("test_plan_xml_definitions", "PLAN", "name=%s definitions=%d" % (name, len(definitions)))
    assert XML.tostring(XML.fromstring(embedded)) == XML.tostring(graph)
    assert len(definitions) == count and len({node.tag for node in definitions}) == count
    assert graph[0].attrib["TYPE"] == "PROJECT_INFO"
    for node in [graph[0]] + definitions:
        assert all(node.find(tag) is not None and node.find(tag).text.strip() for tag in ("keywords", "terms", "annotation"))
    for marker in ("DEV_PLAN", "DOCUMENT_PLAN"):
        assert text.count("$START_" + marker) == text.count("$END_" + marker) == 1
        assert text.index("$START_" + marker) < text.index("$END_" + marker)
    assert all("### %d." % index in text for index in range(1, 7))
    assert all(label in text for label in ("PURPOSE:", "RATIONALE:", "VERIFICATION CONTRACT:", "Original scenario requirements", "output/result.json", "open/write/close", "real-operation proof", "NOT RUN"))
# endregion FUNC_test_plan_xml_definitions


# region FUNC_test_positive_links_and_coverage [DOMAIN(8): DesignContract; CONCEPT(8): FixtureEvidence; TECH(5): pytest, xml]
## @purpose Exercise local edge resolution and all three BR membership obligations on actual positive graphs.
## @io Actual fixture bytes -> observed condition
## @complexity 5
@pytest.mark.parametrize("name", ["greenfield", "brownfield"])
def test_positive_links_and_coverage(repo_root, name):
    graph = _xml(repo_root, name + ".xml")
    definitions = {node.tag: node for node in graph if "FILE" in node.attrib}
    pairs = [(node.tag, link.attrib["TARGET"]) for node in definitions.values() for link in node.findall("CrossLinks/Link")]
    satisfaction = [node.attrib["satisfies"].split(",") for node in definitions.values()]
    covered = {br.strip() for values in satisfaction for br in values}
    _trace("test_positive_links_and_coverage", "EDGES", "edges=%s covered=%s" % (pairs, sorted(covered)))
    assert all(target in definitions for _, target in pairs)
    assert all(values and all(re.fullmatch(r"BR-[1-3]", br.strip()) for br in values) for values in satisfaction)
    assert covered == {"BR-1", "BR-2", "BR-3"}
    if name == "brownfield":
        assert len(graph.find("order_py").findall("annotation")) == 2
        assert len(graph.find("order_py").findall("CrossLinks/Link")) == 2
# endregion FUNC_test_positive_links_and_coverage


# region FUNC_test_brownfield_reference_identity [DOMAIN(8): DesignContract; CONCEPT(8): FixtureEvidence; TECH(5): pytest, xml]
## @purpose Hash real source/map bytes and resolve the declared entity and exact source line.
## @io Actual fixture bytes -> observed condition
## @complexity 5
def test_brownfield_reference_identity(repo_root):
    base = repo_root / "examples/design-contract"
    identity = json.loads((base / "existing-map.identity.json").read_bytes())
    graph = _xml(repo_root, "brownfield.xml")
    mapping = _xml(repo_root, identity["mapPath"])
    source = (base / identity["sourceIdentity"]["path"]).read_bytes()
    lookup = identity["lookupEvidence"][0]
    node = mapping.find(lookup["mapElement"])
    external = graph.find("order_py/CrossLinks/ExternalLink")
    reference = graph.find("ExistingNodeRef")
    _trace("test_brownfield_reference_identity", "LOOKUP", "entity=%s source_line=%d found=%s" % (lookup["entity"], lookup["sourceLine"], node is not None))
    assert hashlib.sha256((base / identity["mapPath"]).read_bytes()).hexdigest() == identity["sha256"]
    assert hashlib.sha256(source).hexdigest() == identity["sourceIdentity"]["sha256"] == mapping.attrib["SOURCE_SHA256"]
    assert source.decode().splitlines()[lookup["sourceLine"] - 1] == lookup["sourceText"]
    assert node is not None and node.tag == external.attrib["TARGET"] == reference.attrib["NAME"] == lookup["entity"]
    assert external.attrib["SOURCE"] == reference.attrib["SOURCE"] == identity["id"]
    assert external.attrib["TYPE"] == "READS_DATA_FROM"
# endregion FUNC_test_brownfield_reference_identity


# region FUNC_test_malformed_xml_fails_real_parser [DOMAIN(8): DesignContract; CONCEPT(8): FixtureEvidence; TECH(5): pytest, xml]
## @purpose Observe the actual parser refusal of the malformed shipped bytes.
## @io Actual fixture bytes -> observed condition
## @complexity 5
def test_malformed_xml_fails_real_parser(repo_root):
    _trace("test_malformed_xml_fails_real_parser", "EXPECTED_PARSE_ERROR", "fixture=malformed.xml")
    with pytest.raises(XML.ParseError):
        _xml(repo_root, "malformed.xml")
# endregion FUNC_test_malformed_xml_fails_real_parser


# region FUNC_test_identity_negatives_are_distinct [DOMAIN(8): DesignContract; CONCEPT(8): FixtureEvidence; TECH(5): pytest, xml]
## @purpose Differentiate exact duplicate definitions from normalized distinct spelling collisions.
## @io Actual fixture bytes -> observed condition
## @complexity 5
def test_identity_negatives_are_distinct(repo_root):
    duplicate = _xml(repo_root, "duplicate-definition.xml")
    names = [node.tag for node in duplicate if "FILE" in node.attrib]
    collision = _xml(repo_root, "normalization-collision.xml")
    collided_definitions = [node for node in collision if node.tag == "pkg_reader_py" and "FILE" in node.attrib]
    originals = [node.attrib["FILE"].rsplit("/", 1)[1] for node in collided_definitions]
    normalized = [name.replace(".", "_").replace(" ", "_") for name in originals]
    actual_definition_ids = [node.tag for node in collided_definitions]
    _trace("test_identity_negatives_are_distinct", "IDENTITIES", "definitions=%s original=%s normalized=%s" % (names, originals, normalized))
    assert len(names) != len(set(names))
    assert len(originals) == len(set(originals)) == 2
    assert originals == ["pkg.reader.py", "pkg reader.py"]
    assert normalized == actual_definition_ids == ["pkg_reader_py", "pkg_reader_py"]
    assert len(set(normalized)) == 1
# endregion FUNC_test_identity_negatives_are_distinct


# region FUNC_test_dangling_link_stays_local [DOMAIN(8): DesignContract; CONCEPT(8): FixtureEvidence; TECH(5): pytest, xml]
## @purpose Prove the unresolved target remains a local Link and has no implicit external identity.
## @io Actual fixture bytes -> observed condition
## @complexity 5
def test_dangling_link_stays_local(repo_root):
    graph = _xml(repo_root, "dangling-local.xml")
    names = {node.tag for node in graph if "FILE" in node.attrib}
    dangling = [link for link in graph.findall(".//Link") if link.attrib["TARGET"] not in names]
    _trace("test_dangling_link_stays_local", "UNRESOLVED", "targets=%s" % [link.attrib["TARGET"] for link in dangling])
    assert len(dangling) == 1 and dangling[0].attrib["TARGET"] == "absent_py"
    assert "SOURCE" not in dangling[0].attrib and graph.find(".//ExternalLink") is None
# endregion FUNC_test_dangling_link_stays_local


# region FUNC_test_reference_negatives_discriminate [DOMAIN(8): DesignContract; CONCEPT(8): FixtureEvidence; TECH(5): pytest, xml]
## @purpose Check separate missing registry, fabricated entity, stale map and stale source defects.
## @io Actual fixture bytes -> observed condition
## @complexity 5
def test_reference_negatives_discriminate(repo_root):
    base = repo_root / "examples/design-contract"
    identity = json.loads((base / "existing-map.identity.json").read_bytes())
    missing = _xml(repo_root, "missing-map.xml")
    fabricated = _xml(repo_root, "fabricated-reference.xml")
    mapping = _xml(repo_root, "existing-map.xml")
    target = fabricated.find(".//ExternalLink").attrib["TARGET"]
    stale_map = json.loads((base / "stale-map.identity.json").read_bytes())
    stale_source = json.loads((base / "stale-source.identity.json").read_bytes())
    _trace("test_reference_negatives_discriminate", "IDENTITY", "missing_source=%s fabricated=%s" % (missing.find(".//ExternalLink").attrib["SOURCE"], target))
    assert missing.find(".//ExternalLink").attrib["SOURCE"] != identity["id"]
    assert mapping.find(".//" + target) is None
    assert stale_map["sha256"] != hashlib.sha256((base / identity["mapPath"]).read_bytes()).hexdigest()
    assert stale_source["sourceIdentity"]["sha256"] != hashlib.sha256((base / identity["sourceIdentity"]["path"]).read_bytes()).hexdigest()
    assert stale_map["sourceIdentity"] == identity["sourceIdentity"] and stale_source["sha256"] == identity["sha256"]
# endregion FUNC_test_reference_negatives_discriminate


# region FUNC_test_satisfaction_negatives_discriminate [DOMAIN(8): DesignContract; CONCEPT(8): FixtureEvidence; TECH(5): pytest, xml]
## @purpose Observe each concrete satisfaction failure without treating greenfield as a waiver.
## @io Actual fixture bytes -> observed condition
## @complexity 5
def test_satisfaction_negatives_discriminate(repo_root):
    graphs = {name: _xml(repo_root, name + ".xml") for name in ("missing-satisfaction", "empty-satisfaction", "non-br-satisfaction", "unknown-br", "uncovered-br")}
    _trace("test_satisfaction_negatives_discriminate", "BR_CONDITIONS", "fixtures=%s" % sorted(graphs))
    assert "satisfies" not in graphs["missing-satisfaction"].find("order_py").attrib
    assert graphs["empty-satisfaction"].find("order_py").attrib["satisfies"] == ""
    assert graphs["non-br-satisfaction"].find("order_py").attrib["satisfies"] == "AC-2"
    assert graphs["unknown-br"].find("order_py").attrib["satisfies"] == "BR-99"
    coverage = {node.attrib["satisfies"] for node in graphs["uncovered-br"] if "FILE" in node.attrib}
    assert "BR-2" not in coverage and coverage == {"BR-1", "BR-3"}
# endregion FUNC_test_satisfaction_negatives_discriminate


# region FUNC_test_semantic_case_and_control_inputs_exist [DOMAIN(8): DesignContract; CONCEPT(8): FixtureEvidence; TECH(5): pytest, xml]
## @purpose Read actual clauses and concrete review inputs; leave semantic outcomes to independent judgment.
## @io Actual fixture bytes -> observed condition
## @complexity 5
def test_semantic_case_and_control_inputs_exist(repo_root):
    text = (repo_root / "examples/design-contract/README.md").read_text()
    controls = text.split("## Six actual prose controls for independent review")[1]
    case_ids = re.findall(r"\| (S-[0-9]{2}) ", text)
    norms = re.findall(r"(?:PLAN|GRAPH|ARCH|RECON)-[0-9]{3}", controls)
    clauses = "\n".join((repo_root / path).read_text() for path in ("roles/architect.md", "protocols/dev-plan.md", "process/reconnaissance.md", "protocols/graph.md"))
    _trace("test_semantic_case_and_control_inputs_exist", "REVIEW_INPUTS", "cases=%s controls=%d named_norms=%s" % (case_ids, len(re.findall(r"^\d\.", controls, re.M)), norms))
    assert case_ids == ["S-%02d" % number for number in range(1, 15)]
    assert len(re.findall(r"^\d\.", controls, re.M)) == 6
    assert all(norm in clauses for norm in norms)
    assert "not precomputed PASS" in text and "actual altered prose" in controls
# endregion FUNC_test_semantic_case_and_control_inputs_exist


# region FUNC_test_design_bodies_have_contract_structure [DOMAIN(9): DesignContract; CONCEPT(9): Format, Norms, Calls; TECH(5): re]
## @purpose Inspect actual four draft bodies and declared calls; syntax evidence alone grants no readiness.
## @io Actual body, FORMAT and registry bytes -> scoped structural assertions
## @complexity 5
@pytest.mark.parametrize("path,identity,prefix", [("roles/architect.md", "roles.architect", "ARCH"), ("protocols/dev-plan.md", "protocols.dev-plan", "PLAN"), ("process/reconnaissance.md", "process.reconnaissance", "RECON"), ("protocols/graph.md", "protocols.graph", "GRAPH")])
def test_design_bodies_have_contract_structure(repo_root, path, identity, prefix):
    text = (repo_root / path).read_text()
    format_text = (repo_root / "FORMAT.md").read_text()
    registry = (repo_root / "runtime/capabilities.md").read_text()
    anchors = re.findall(r"<!-- anchor: ([a-z0-9.-]+) -->", text)
    norms = re.findall(r"^- \*\*([A-Z]+-[0-9]{3})\*\* MUST(?: NOT)?: (.+)$", text, re.M)
    calls = re.findall(r"\{\{cap:([a-z0-9-]+)\}\}", text)
    _trace("test_design_bodies_have_contract_structure", "FORMAT", "path=%s anchors=%d norms=%d calls=%s sha256=%s" % (path, len(anchors), len(norms), calls, hashlib.sha256(text.encode()).hexdigest()))
    assert text.startswith("---\nid: " + identity + "\n") and "\nstatus: draft\n---\n" in text
    assert anchors and len(anchors) == len(set(anchors)) and all(anchor.startswith(identity + ".") for anchor in anchors)
    assert norms and len(norms) == len({name for name, _ in norms})
    assert all(name.startswith(prefix + "-") and clause.strip() for name, clause in norms)
    assert all(call in registry for call in calls)
    assert "FMT-" in format_text and "{{cap:" in format_text
# endregion FUNC_test_design_bodies_have_contract_structure
# region FUNC_test_plan_diagrams_follow_actual_graph [DOMAIN(9): DesignContract; CONCEPT(9): DiagramFidelity, Operations; TECH(5): re, xml]
## @purpose Compare actual finite diagram source relationships and satisfaction to XML, and the brownfield operation to its verified reference.
## @io Two shipped plans and their graphs -> actual projection relationships
## @complexity 6
@pytest.mark.parametrize("name", ["greenfield", "brownfield"])
def test_plan_diagrams_follow_actual_graph(repo_root, name):
    text = (repo_root / "examples/design-contract" / (name + "-plan.md")).read_text()
    graph = _xml(repo_root, name + ".xml")
    diagrams = re.findall(r"```mermaid\n(.*?)\n```", text, re.S)
    trace, structure, sequence = diagrams
    definitions = [node for node in graph if "FILE" in node.attrib]
    xml_trace = {(node.tag, br.strip()) for node in definitions for br in node.attrib["satisfies"].split(",")}
    rendered_trace = {(node, alias.replace("_", "-")) for node, alias in re.findall(r"(\w+) - satisfies -> (BR_\d+)", trace)}
    xml_edges = {(node.tag, link.attrib["TYPE"], link.attrib["TARGET"]) for node in definitions for link in node.findall("CrossLinks/Link") + node.findall("CrossLinks/ExternalLink")}
    rendered_edges = set(re.findall(r"(\w+) -->\|([A-Z_]+)\| (\w+)", structure))
    expected_entities = {node.tag for node in definitions} | {node.attrib["NAME"] for node in graph.findall("ExistingNodeRef")}
    rendered_entities = set(re.findall(r"^    (\w+)\[", structure, re.M))
    participants = set(re.findall(r"^    participant (\w+)$", sequence, re.M))
    _trace("test_plan_diagrams_follow_actual_graph", "PROJECTIONS", "name=%s trace=%s edges=%s entities=%s" % (name, sorted(rendered_trace), sorted(rendered_edges), sorted(rendered_entities)))
    assert len(diagrams) == 3 and trace.startswith("requirementDiagram") and structure.startswith("flowchart LR") and sequence.startswith("sequenceDiagram")
    assert xml_trace == rendered_trace
    assert xml_edges == rendered_edges and rendered_entities == expected_entities == participants
    assert len(re.findall(r"requirement BR_\d+ ", trace)) == 3
    assert len(re.findall(r"id: BR-[1-3]", trace)) == len(re.findall(r"text: .+", trace)) == trace.count("risk: low") == trace.count("verifymethod: test") == 3
    assert "Open/write/close output/result.json" in sequence and "Surface I/O errors" in sequence
    if name == "brownfield":
        assert "src/reader.py" not in text and "reader operation" not in text
        assert "test_record_values -> order operation using the verified unchanged store_lookup_FUNC" in text
        assert "order_py->>store_lookup_FUNC: Lookup records through unchanged API" in sequence
        assert "store_lookup_FUNC-->>order_py: Return records unchanged" in sequence
        assert "Two identical Link metadata occurrences" in structure
        assert "mechanical visual gate SKIPPED" in text
    else:
        assert "reader_py->>order_py: Supply records" in sequence and "order_py->>writer_py: Supply ordered records" in sequence
# endregion FUNC_test_plan_diagrams_follow_actual_graph
