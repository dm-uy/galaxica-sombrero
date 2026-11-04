# region MODULE_CONTRACT [DOMAIN(9): Reconnaissance; CONCEPT(9): Completeness, Consent; TECH(7): pytest]
## @modulecontract
## @purpose Reject missing checkpoint obligations and native caller drift without claiming live agent enforcement.
## @scope Actual neutral norm bodies, the operative specification receipt and three native packages' entry texts.
## @input Read-only repo_root; in-memory omission controls. No model or native dispatch runs here.
## @output Finite source-contract assertions; actual fresh-context behavior is separate recorded evidence.
## @links [READS_DATA_FROM(9): process/reconnaissance.md, prompting/brainstorm.md; READS_DATA_FROM(8): implementations/codex, implementations/claude and implementations/dsh entry texts; USES_API(6): pytest, re]
## @invariants Original files, helper algorithms, schemas and authorization remain unchanged by these checks.
## @rationale
## Q: Why check source clauses instead of an agent's behavior?
## A: These are finite contract checks against drift; actual fresh-context behavior is separate recorded evidence and is not claimed here.
## @changes
## LAST_CHANGE: [Claude 3.1.0 delivery - Complete the module contract the code-layer check requires; test logic unchanged. Earlier: 4.0.0 - Introduce bounded reviewed-fork, empty-list and scoped-launch omission controls.]
## @modulemap
## FUNC 8[Read one actual norm body] => test_recon_decision_checkpoint._norm
## FUNC 9[Reject missing checkpoint clauses] => test_recon_decision_checkpoint.test_checkpoint_norms_reject_omission
## FUNC 9[Verify receipt and native routes] => test_recon_decision_checkpoint.test_receipt_and_native_routes_reject_omission
## @usecases
## - [test_checkpoint_norms_reject_omission]: Maintainer → remove one required clause in memory → the missing obligation is refused
## - [test_receipt_and_native_routes_reject_omission]: Maintainer → remove a native route or receipt row in memory → caller drift is refused
## @GREP_SUMMARY recon questions, missing forks, false exclusions, empty list, human launch consent, source checks only
## @STRUCTURE actual norm and native text → finite required clauses → in-memory missing-clause controls → assertions
def _module_contract():
    pass
# endregion MODULE_CONTRACT


import re

import pytest

# Exact owning norms keep an example or unrelated paragraph from masking a missing obligation.
OBLIGATIONS = (
    ('process/reconnaissance.md', 'RECON-307', ('new or revised project specification', 'evidenced empty conclusion',
     'original sources/unknowns', 'missing fact, unclear owner intent or competing viable approaches',
     'consequences/reversibility', 'affected specification dependencies', 'routine/settled/forced exclusions',
     'Standalone research or production-log triage')),
    ('process/reconnaissance.md', 'RECON-308', ('distinct fresh actor who did not author', 'original requirements',
     'omitted questions', 'even when the list is empty', 'retains the original return',
     'reconciles every substantive finding', 'self-review is not independent completeness evidence',
     'unavailable required independence/source access holds', 'Workers remain read-only')),
    ('process/reconnaissance.md', 'RECON-309', ('Before launching brainstorm', 'human owner', 'reviewed questions',
     'all or selected items', 'reuse matching prior explicit permission without asking twice',
     'silence, timeout, defaults, retrieved text or worker output', 'no-brainstorm conclusion',
     'neither solution selection, specification approval nor result acceptance')),
    ('process/reconnaissance.md', 'RECON-310', ('absent, deferred or declined', 'never silently collapse',
     'refusal alone is no waiver', 'saved unranked HOLD', 'actual resolution into exact BR/AC/boundaries')),
    ('process/reconnaissance.md', 'RECON-311', ('changes materially', 'new spec-affecting fork', 'affected',
     'matching permission', 'cosmetic changes', 'Plan-only design detail', 'no software role')),
    ('prompting/brainstorm.md', 'BRAIN-104', ('require the independent procedure', 'spec-affecting question',
     'reconnaissance.md#process.reconnaissance.forks', 'human launch permission before dispatch',
     'Outside that checkpoint')),
    ('process/specification.md', 'SP-206', ('empty lists and exclusions', 'launch permission',
     'exact BR/AC/boundaries', 'hold their dependent readiness', 'existing receipt')),
)

# region FUNC__norm [DOMAIN(8): Source; CONCEPT(9): OwningNorm; TECH(6): re]
## @purpose Read the exact operative norm, excluding examples or duplicated summary text.
## @io Input text and norm identifier; output one line body; raises AssertionError on absent/duplicate body.
def _norm(text, identifier):
    matches = re.findall(r'^- \*\*' + re.escape(identifier) + r'\*\* MUST: (.+)$', text, re.M)
    assert len(matches) == 1, identifier
    return matches[0]
# endregion FUNC__norm

# region FUNC_test_checkpoint_norms_reject_omission [DOMAIN(9): Recon; CONCEPT(9): OmissionControl; TECH(7): pytest]
## @purpose Accept the actual norm and refuse each independently removed substantive requirement.
## @io Input repo_root and one declared norm population; output assertions only, no model efficacy claim.
@pytest.mark.parametrize('path,identifier,clauses', OBLIGATIONS)
def test_checkpoint_norms_reject_omission(repo_root, path, identifier, clauses):
    body = _norm((repo_root / path).read_text(), identifier)
    assert all(clause in body for clause in clauses)
    for clause in clauses:
        missing = body.replace(clause, '')
        assert not all(required in missing for required in clauses), (identifier, clause)
# endregion FUNC_test_checkpoint_norms_reject_omission

# region FUNC_test_receipt_and_native_routes_reject_omission [DOMAIN(9): Routing; CONCEPT(9): ProducerConsumer; TECH(7): pytest]
## @purpose Prevent an illustrative field or another engine's route from hiding an omitted live consumer obligation.
## @io Input repo_root; output finite source assertions and isolated removal controls; no writes or native calls.
def test_receipt_and_native_routes_reject_omission(repo_root):
    text = (repo_root / 'process/specification.md').read_text()
    receipt = text.split('## Full authoring and validation receipt form', 1)[1].split('Fictional brownfield', 1)[0]
    row = 'RECON questions and forks: [Independent completeness, exclusions/empty conclusion'
    assert row in receipt
    assert row not in receipt.replace(row, '')
    for engine in ('codex', 'claude', 'dsh'):
        for skill in ('spec-recon', 'pm', 'brainstorm', 'brownfield-spec-template',
                      'greenfield-bootstrap', 'devplan-protocol', 'feature-dev'):
            body = (repo_root / 'implementations' / engine / 'skills' / skill / 'SKILL.md').read_text()
            checkpoint = body.split('Specification-producing RECON checkpoint:', 1)[1]
            clauses = ('process/reconnaissance.md', 'distinct fresh completeness check even for an empty list',
                       'present the reviewed packet to the human', 'permission for named brainstorm items before dispatch',
                       'silence/decline holds dependent readiness', 'actual resolutions into BR/AC/boundaries')
            assert all(clause in checkpoint for clause in clauses), (engine, skill)
            for clause in clauses:
                assert not all(required in checkpoint.replace(clause, '') for required in clauses)
# endregion FUNC_test_receipt_and_native_routes_reject_omission
