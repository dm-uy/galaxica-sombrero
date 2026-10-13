# region MODULE_CONTRACT [DOMAIN(9): F2, Contracts; CONCEPT(9): EquivalentSupports, Conditions, Provenance; TECH(7): pytest, pathlib, hashlib, json]
## @modulecontract
## @purpose Verify source-fixed complete preparation authority and overview responsibilities with reviewed equivalent supports;
## observe actual typed synthetic inputs and deliver full fixture/refusal/restoration evidence.
## @scope Read-only public sources and protected consumers; all runtime fixture writes remain inside owned pytest tmp_path.
## @input Complete current Markdown, independent fixed intentions, reviewed support spans and typed physical synthetic evidence.
## @output Exact assertions and real-process LDD; full files, numeric modes, independently intended and actually observed reasons.
## @links [READS_DATA_FROM(9): process/bootstrap.md; READS_DATA_FROM(9): roles/_base.md; READS_DATA_FROM(8): README.md; USES_API(7): conformlib.markdown.load_neutral_tree]
## @links_to_spec AC-F2-1, AC-F2-2, AC-F2-3, AC-F2-4, AC-F2-6
## @invariants
## - Complete independent meanings precede producer output; current prose and observed failures never discover expectations.
## - True duty loss removes all reviewed applicable supports; redundant-only deletion stays green and partial siblings survive.
## - Shared component loss has an exact independently justified related reason set rather than a forced literal singleton.
## - Conditional facts and physical provenance derive observations separately from expected outcomes; unknown evidence is no N/A grant.
## - Finite supported spans are not an unrestricted prose solver, human consent authority, operational checker or adoption engine.
## - Full files and actual modes/hashes are read back and restored; protected real source, existing hooks and counters remain untouched.
## @rationale
## Q: Why not remove one required literal and force one failure?
## A: Equivalent duties can survive elsewhere, and a shared lost component can affect more than one complete responsibility.
## Q: Why separate typed facts, physical records and expectations?
## A: Fenced scenario labels yield no observation; expected status and an origin label cannot supply real prerequisite evidence.
## @changes
## LAST_CHANGE: [v1.0.0 - Reconcile current M19 boundary/release facts and paired source operands; preserve original assertions/pins/refusals/restoration; runtime checks pending.]
## BUG_FIX_CONTEXT: QA found fenced labels discarded before evaluation and three one-literal negatives with surviving equivalent duties.
## BUG_FIX_CONTEXT: Reviewed source supports and independent related reasons distinguish redundant removal from actual loss; typed records expose absent versus unmet triggers.
## BUG_FIX_CONTEXT: Public prose and fixed policy stay unchanged; renewed independent semantic judgment and actual formal checks remain required.
## @modulemap
## FUNC 8[Read complete actual source surfaces with their physical hashes and numeric modes] => _read_surfaces
## FUNC 8[Check actual Bootstrap cards anchors populations and overview links] => test_f2_structure_and_public_links
## FUNC 8[Require complete source-fixed current responsibility supports without live contrary grants] => test_f2_complete_current_interfaces
## FUNC 8[Retain protected bytes and same-version current rules beyond the optional QA repeat economy] => test_f2_unchanged_contract_boundaries
## FUNC 8[Separate actual live mandatory clauses from fences and reject ambiguous duplicate norms] => _parse_live
## FUNC 8[Check one reviewed support at its actual path norm level and live clause] => _support_matches
## FUNC 8[Derive exact complete responsibility failures across reviewed equivalent supports and force-qualified components] => _contract_failures
## FUNC 8[Apply independently fixed full component-loss spans to owned copies and count each real trigger] => _apply_recipe
## FUNC 8[Read fixed intended reason sets without consulting detector outputs] => _expected_refusals
## FUNC 8[Deliver and read back complete actual fixture files hashes bytes and numeric modes] => _deliver_surfaces
## FUNC 8[Distinguish redundant wording from real duty loss and deliver exact related reasons retained partials and full restoration] => _write_fixture_pair
## FUNC 8[Associate a synthetic record with actual trusted source bytes current artifact action actor and scope] => _provenance_issue
## FUNC 8[Derive bounded conditional observations from actual fixture facts and physical evidence without using expected verdicts] => _observe_case
## FUNC 8[Persist full factual and expected carriers then compute and read back actual observations and prove annotations have no authority] => _deliver_case
## FUNC 8[Check every fixed condition with full physical equivalence-aware omission contrary redundancy and restoration fixtures] => test_f2_isolated_required_conditions
## FUNC 8[Discriminate seven requested-action families with actual typed facts N/A missing evidence and valid synthetic counterparts] => test_f2_conditional_counterparts
## FUNC 8[Keep fence exclusion as its own regression with full live-grant and hidden-required file controls] => test_f2_fenced_examples
## FUNC 8[Prove actual brief loss retains durable state and complete surfaces restore original bytes and modes] => test_f2_fixture_delivery_and_restoration
## @usecases
## - [_module_contract]: Doxygen exposes the full current module contract and actual locations.
## - [_read_surfaces]: Read complete actual source surfaces with their physical hashes and numeric modes; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [test_f2_structure_and_public_links]: Check actual Bootstrap cards anchors populations and overview links; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [test_f2_complete_current_interfaces]: Require complete source-fixed current responsibility supports without live contrary grants; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [test_f2_unchanged_contract_boundaries]: Retain protected bytes and same-version current rules beyond the optional QA repeat economy; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [_parse_live]: Separate actual live mandatory clauses from fences and reject ambiguous duplicate norms; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [_support_matches]: Check one reviewed support at its actual path norm level and live clause; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [_contract_failures]: Derive exact complete responsibility failures across reviewed equivalent supports and force-qualified components; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [_apply_recipe]: Apply independently fixed full component-loss spans to owned copies and count each real trigger; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [_expected_refusals]: Read fixed intended reason sets without consulting detector outputs; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [_deliver_surfaces]: Deliver and read back complete actual fixture files hashes bytes and numeric modes; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [_write_fixture_pair]: Distinguish redundant wording from real duty loss and deliver exact related reasons retained partials and full restoration; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [_provenance_issue]: Associate a synthetic record with actual trusted source bytes current artifact action actor and scope; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [_observe_case]: Derive bounded conditional observations from actual fixture facts and physical evidence without using expected verdicts; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [_deliver_case]: Persist full factual and expected carriers then compute and read back actual observations and prove annotations have no authority; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [test_f2_isolated_required_conditions]: Check every fixed condition with full physical equivalence-aware omission contrary redundancy and restoration fixtures; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [test_f2_conditional_counterparts]: Discriminate seven requested-action families with actual typed facts N/A missing evidence and valid synthetic counterparts; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [test_f2_fenced_examples]: Keep fence exclusion as its own regression with full live-grant and hidden-required file controls; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## - [test_f2_fixture_delivery_and_restoration]: Prove actual brief loss retains durable state and complete surfaces restore original bytes and modes; actual valid support succeeds, the named unsupported or mismatched condition refuses, and missing or corrupt evidence never supplies authority.
## @GREP_SUMMARY F2 equivalent duties fixed full reasons partial siblings actual typed facts physical provenance N/A refusal gap restoration protected boundaries
## @STRUCTURE Complete live sources → reviewed supports ∧ independent intentions → real copy-local component loss or redundant removal → exact related refusals ∧ retained partials; typed factual files → observed branch/prerequisites → fixed expected comparison → full readback/restoration; independent prose QA remains separate
def _module_contract():
    pass
# endregion MODULE_CONTRACT


# Imports follow the full module markup with protected spacing.

import hashlib
import json
import pathlib
import re
import stat

from conformlib.markdown import load_neutral_tree, parse_markdown


CONDITIONS = [{'key': 'BOOT101_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-101',
  'level': 'MUST',
  'required_clause': 'Read the actual accessible code and source facts before classifying preparation.',
  'contrary_grant': 'Preparation may be classified without reading available code or source facts.',
  'refusal': 'REJECT_BOOT101_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual accessible code and source facts; '
            'retain Classify from actual code, instructions, briefs and durable/Git facts.',
  'independent_id': 'P01.1',
  'meaning': 'actual accessible code and source facts',
  'parent': 'Classify from actual code, instructions, briefs and durable/Git facts.'},
 {'key': 'BOOT101_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-101',
  'level': 'MUST',
  'required_clause': 'Read the actual applicable hidden and project agent instructions before preparing inputs.',
  'contrary_grant': 'Preparation may disregard applicable hidden or project agent instructions.',
  'refusal': 'REJECT_BOOT101_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual hidden/project agent instructions; '
            'retain Classify from actual code, instructions, briefs and durable/Git facts.',
  'independent_id': 'P01.2',
  'meaning': 'actual hidden/project agent instructions',
  'parent': 'Classify from actual code, instructions, briefs and durable/Git facts.'},
 {'key': 'BOOT101_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-101',
  'level': 'MUST',
  'required_clause': 'Read the actual complete brief and durable project state before deriving preparation inputs.',
  'contrary_grant': 'Preparation may derive inputs without reading the actual brief or durable state.',
  'refusal': 'REJECT_BOOT101_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual brief and durable state; retain '
            'Classify from actual code, instructions, briefs and durable/Git facts.',
  'independent_id': 'P01.3',
  'meaning': 'actual brief and durable state',
  'parent': 'Classify from actual code, instructions, briefs and durable/Git facts.'},
 {'key': 'BOOT101_C4',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-101',
  'level': 'MUST',
  'required_clause': 'Inspect actual Git and applicable map facts and declare the available access scope.',
  'contrary_grant': 'Preparation may invent Git or map facts and assume unrestricted access.',
  'refusal': 'REJECT_BOOT101_C4',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual Git/map/access facts where '
            'applicable; retain Classify from actual code, instructions, briefs and durable/Git facts.',
  'independent_id': 'P01.4',
  'meaning': 'actual Git/map/access facts where applicable',
  'parent': 'Classify from actual code, instructions, briefs and durable/Git facts.'},
 {'key': 'BOOT102_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-102',
  'level': 'MUST',
  'required_clause': 'Classify an existing executable codebase as existing code requiring applicable migration or '
                     'reconstruction.',
  'contrary_grant': 'Existing executable code may be classified as a new product.',
  'refusal': 'REJECT_BOOT102_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: existing executable code classification; '
            'retain Existing executable code with missing documents remains existing-code conventions migration, never '
            'greenfield by absence alone.',
  'independent_id': 'P02.1',
  'meaning': 'existing executable code classification',
  'parent': 'Existing executable code with missing documents remains existing-code conventions migration, never '
            'greenfield by absence alone.'},
 {'key': 'BOOT102_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-102',
  'level': 'MUST',
  'required_clause': 'Missing durable documents alone never make an existing codebase greenfield.',
  'contrary_grant': 'Missing durable documents alone make an existing codebase greenfield.',
  'refusal': 'REJECT_BOOT102_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: missing-document absence is not greenfield '
            'evidence; retain Existing executable code with missing documents remains existing-code conventions '
            'migration, never greenfield by absence alone.',
  'independent_id': 'P02.2',
  'meaning': 'missing-document absence is not greenfield evidence',
  'parent': 'Existing executable code with missing documents remains existing-code conventions migration, never '
            'greenfield by absence alone.'},
 {'key': 'BOOT102_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-102',
  'level': 'MUST',
  'required_clause': 'Use new-product preparation only for a genuinely new product supported by actual inputs.',
  'contrary_grant': 'New-product preparation may be presumed without a genuinely new-product trigger.',
  'refusal': 'REJECT_BOOT102_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: genuinely new-product trigger; retain '
            'Existing executable code with missing documents remains existing-code conventions migration, never '
            'greenfield by absence alone.',
  'independent_id': 'P02.3',
  'meaning': 'genuinely new-product trigger',
  'parent': 'Existing executable code with missing documents remains existing-code conventions migration, never '
            'greenfield by absence alone.'},
 {'key': 'BOOT103_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-103',
  'level': 'MUST',
  'required_clause': 'Treat an owner-requested conventions migration as its actual bounded preparation trigger.',
  'contrary_grant': 'An unrelated feature request automatically triggers conventions migration.',
  'refusal': 'REJECT_BOOT103_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual requested conventions-migration '
            'trigger; retain Recognize applicable new-product versus owner-requested conventions migration '
            'preparation.',
  'independent_id': 'P03.1',
  'meaning': 'actual requested conventions-migration trigger',
  'parent': 'Recognize applicable new-product versus owner-requested conventions migration preparation.'},
 {'key': 'BOOT103_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-103',
  'level': 'MUST',
  'required_clause': 'Require a matching bounded preparation grant before preparation writes.',
  'contrary_grant': 'Any preparation trigger grants unrestricted preparation writes.',
  'refusal': 'REJECT_BOOT103_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: matching bounded preparation grant; retain '
            'Recognize applicable new-product versus owner-requested conventions migration preparation.',
  'independent_id': 'P03.2',
  'meaning': 'matching bounded preparation grant',
  'parent': 'Recognize applicable new-product versus owner-requested conventions migration preparation.'},
 {'key': 'BOOT104_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-104',
  'level': 'MUST',
  'required_clause': 'Keep spine inventory read-only.',
  'contrary_grant': 'Spine inventory may write durable files.',
  'refusal': 'REJECT_BOOT104_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: inventory remains read-only; retain '
            'Read-only spine inventory reports preparation needs; it cannot perform preparation writes.',
  'independent_id': 'P04.1',
  'meaning': 'inventory remains read-only',
  'parent': 'Read-only spine inventory reports preparation needs; it cannot perform preparation writes.'},
 {'key': 'BOOT104_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-104',
  'level': 'MUST',
  'required_clause': 'Return discovered preparation needs to the authorized parent.',
  'contrary_grant': 'Spine inventory may hide preparation needs from its authorized parent.',
  'refusal': 'REJECT_BOOT104_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: preparation needs are returned to its '
            'authorized parent; retain Read-only spine inventory reports preparation needs; it cannot perform '
            'preparation writes.',
  'independent_id': 'P04.2',
  'meaning': 'preparation needs are returned to its authorized parent',
  'parent': 'Read-only spine inventory reports preparation needs; it cannot perform preparation writes.'},
 {'key': 'BOOT104_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-104',
  'level': 'MUST',
  'required_clause': 'Obtain separate preparation write authority for the actual affected files.',
  'contrary_grant': 'Read-only inventory automatically grants preparation write authority.',
  'refusal': 'REJECT_BOOT104_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: separate preparation write grant; retain '
            'Read-only spine inventory reports preparation needs; it cannot perform preparation writes.',
  'independent_id': 'P04.3',
  'meaning': 'separate preparation write grant',
  'parent': 'Read-only spine inventory reports preparation needs; it cannot perform preparation writes.'},
 {'key': 'BOOT105_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-105',
  'level': 'MUST',
  'required_clause': 'Read the complete original brief rather than substituting a guessed summary.',
  'contrary_grant': 'A guessed summary may replace the complete original brief.',
  'refusal': 'REJECT_BOOT105_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: complete actual original brief; retain Read '
            'the complete actual brief and non-negotiables before deriving preparation choices.',
  'independent_id': 'P05.1',
  'meaning': 'complete actual original brief',
  'parent': 'Read the complete actual brief and non-negotiables before deriving preparation choices.'},
 {'key': 'BOOT105_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-105',
  'level': 'MUST',
  'required_clause': 'Read every original non-negotiable constraint before preparing choices.',
  'contrary_grant': 'Preparation may ignore an original non-negotiable constraint.',
  'refusal': 'REJECT_BOOT105_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: all original non-negotiables; retain Read '
            'the complete actual brief and non-negotiables before deriving preparation choices.',
  'independent_id': 'P05.2',
  'meaning': 'all original non-negotiables',
  'parent': 'Read the complete actual brief and non-negotiables before deriving preparation choices.'},
 {'key': 'BOOT106_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-106',
  'level': 'MUST',
  'required_clause': 'Recover settled answers and choices with their actual decision provenance.',
  'contrary_grant': 'Preparation may guess settled answers without their decision provenance.',
  'refusal': 'REJECT_BOOT106_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: existing settled answer/choice provenance; '
            'retain Reuse settled answers/choices; ask only material ungranted gaps and never reopen settled direction '
            'by default.',
  'independent_id': 'P06.1',
  'meaning': 'existing settled answer/choice provenance',
  'parent': 'Reuse settled answers/choices; ask only material ungranted gaps and never reopen settled direction by '
            'default.'},
 {'key': 'BOOT106_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-106',
  'level': 'MUST',
  'required_clause': 'Reuse matching settled answers without redundant re-asking or silent replacement.',
  'contrary_grant': 'Preparation may re-ask or silently replace a matching settled answer.',
  'refusal': 'REJECT_BOOT106_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: no redundant re-ask or silent replacement; '
            'retain Reuse settled answers/choices; ask only material ungranted gaps and never reopen settled direction '
            'by default.',
  'independent_id': 'P06.2',
  'meaning': 'no redundant re-ask or silent replacement',
  'parent': 'Reuse settled answers/choices; ask only material ungranted gaps and never reopen settled direction by '
            'default.'},
 {'key': 'BOOT106_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-106',
  'level': 'MUST',
  'required_clause': 'Stop and route only genuine material ungranted gaps to their decision owner.',
  'contrary_grant': 'Preparation may silently settle a genuine material ungranted gap.',
  'refusal': 'REJECT_BOOT106_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: only genuine material ungranted gaps '
            'stop/route; retain Reuse settled answers/choices; ask only material ungranted gaps and never reopen '
            'settled direction by default.',
  'independent_id': 'P06.3',
  'meaning': 'only genuine material ungranted gaps stop/route',
  'parent': 'Reuse settled answers/choices; ask only material ungranted gaps and never reopen settled direction by '
            'default.'},
 {'key': 'BOOT107_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-107',
  'level': 'MUST',
  'required_clause': 'State what the product does and the original human purpose it serves.',
  'contrary_grant': 'Preparation may omit what the product does or whose purpose it serves.',
  'refusal': 'REJECT_BOOT107_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: product purpose/what it does; retain '
            'Prepare product purpose/audience and one falsifiable user-visible first value.',
  'independent_id': 'P07.1',
  'meaning': 'product purpose/what it does',
  'parent': 'Prepare product purpose/audience and one falsifiable user-visible first value.'},
 {'key': 'BOOT107_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-107',
  'level': 'MUST',
  'required_clause': 'State the actual intended audience.',
  'contrary_grant': 'Preparation may leave the intended audience unspecified.',
  'refusal': 'REJECT_BOOT107_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual intended audience; retain Prepare '
            'product purpose/audience and one falsifiable user-visible first value.',
  'independent_id': 'P07.2',
  'meaning': 'actual intended audience',
  'parent': 'Prepare product purpose/audience and one falsifiable user-visible first value.'},
 {'key': 'BOOT107_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-107',
  'level': 'MUST',
  'required_clause': 'State one falsifiable user-visible first value and its observable pass condition.',
  'contrary_grant': 'An unfalsifiable benefit may count as a complete first-value handoff.',
  'refusal': 'REJECT_BOOT107_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: falsifiable user-visible first value/pass '
            'condition; retain Prepare product purpose/audience and one falsifiable user-visible first value.',
  'independent_id': 'P07.3',
  'meaning': 'falsifiable user-visible first value/pass condition',
  'parent': 'Prepare product purpose/audience and one falsifiable user-visible first value.'},
 {'key': 'BOOT108_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-108',
  'level': 'MUST',
  'required_clause': 'Retain every binding original non-negotiable in the prepared handoff.',
  'contrary_grant': 'Preparation may drop a binding original constraint from the handoff.',
  'refusal': 'REJECT_BOOT108_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: every actual binding non-negotiable '
            'survives prepared output; retain Retain the original non-negotiables in the prepared handoff.',
  'independent_id': 'P08.1',
  'meaning': 'every actual binding non-negotiable survives prepared output',
  'parent': 'Retain the original non-negotiables in the prepared handoff.'},
 {'key': 'BOOT109_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-109',
  'level': 'MUST',
  'required_clause': 'Carry source-backed settled stack, storage and transport choices as inputs.',
  'contrary_grant': 'Preparation may invent a latest stack, storage or transport choice as settled input.',
  'refusal': 'REJECT_BOOT109_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: source-backed settled '
            'stack/storage/transport inputs; retain Provide source-backed settled stack rationale/constraints and '
            'binding version facts where relevant; do not guess provider defaults.',
  'independent_id': 'P09.1',
  'meaning': 'source-backed settled stack/storage/transport inputs',
  'parent': 'Provide source-backed settled stack rationale/constraints and binding version facts where relevant; do '
            'not guess provider defaults.'},
 {'key': 'BOOT109_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-109',
  'level': 'MUST',
  'required_clause': 'Carry the rationale and binding constraints for those settled technical choices.',
  'contrary_grant': 'Preparation may omit the rationale or binding constraints for settled technical choices.',
  'refusal': 'REJECT_BOOT109_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: rationale and binding constraints; retain '
            'Provide source-backed settled stack rationale/constraints and binding version facts where relevant; do '
            'not guess provider defaults.',
  'independent_id': 'P09.2',
  'meaning': 'rationale and binding constraints',
  'parent': 'Provide source-backed settled stack rationale/constraints and binding version facts where relevant; do '
            'not guess provider defaults.'},
 {'key': 'BOOT109_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-109',
  'level': 'MUST',
  'required_clause': 'Verify load-bearing version facts when relevant before handing them to the next role.',
  'contrary_grant': 'Preparation may guess a relevant load-bearing version fact.',
  'refusal': 'REJECT_BOOT109_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: verified load-bearing versions when '
            'relevant; retain Provide source-backed settled stack rationale/constraints and binding version facts '
            'where relevant; do not guess provider defaults.',
  'independent_id': 'P09.3',
  'meaning': 'verified load-bearing versions when relevant',
  'parent': 'Provide source-backed settled stack rationale/constraints and binding version facts where relevant; do '
            'not guess provider defaults.'},
 {'key': 'BOOT110_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-110',
  'level': 'MUST',
  'required_clause': 'Carry the smallest approved included MVP boundary before Code.',
  'contrary_grant': 'Code may begin before the included MVP boundary is approved.',
  'refusal': 'REJECT_BOOT110_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: smallest approved included MVP; retain '
            'Carry the smallest approved MVP boundary, explicit exclusions and dependencies before Code.',
  'independent_id': 'P10.1',
  'meaning': 'smallest approved included MVP',
  'parent': 'Carry the smallest approved MVP boundary, explicit exclusions and dependencies before Code.'},
 {'key': 'BOOT110_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-110',
  'level': 'MUST',
  'required_clause': 'State deliberately deferred capabilities and actual dependencies.',
  'contrary_grant': 'Preparation may hide deliberately deferred capabilities or dependencies.',
  'refusal': 'REJECT_BOOT110_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: deliberately deferred '
            'capabilities/dependencies; retain Carry the smallest approved MVP boundary, explicit exclusions and '
            'dependencies before Code.',
  'independent_id': 'P10.2',
  'meaning': 'deliberately deferred capabilities/dependencies',
  'parent': 'Carry the smallest approved MVP boundary, explicit exclusions and dependencies before Code.'},
 {'key': 'BOOT110_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-110',
  'level': 'MUST',
  'required_clause': 'Settle the applicable boundary before coding rather than expanding it during implementation.',
  'contrary_grant': 'Implementation may add unchosen capabilities while the boundary remains unsettled.',
  'refusal': 'REJECT_BOOT110_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: boundary settled before coding; retain '
            'Carry the smallest approved MVP boundary, explicit exclusions and dependencies before Code.',
  'independent_id': 'P10.3',
  'meaning': 'boundary settled before coding',
  'parent': 'Carry the smallest approved MVP boundary, explicit exclusions and dependencies before Code.'},
 {'key': 'BOOT111_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-111',
  'level': 'MUST',
  'required_clause': 'Name the real probe transport, path and delivery sink required by the next role.',
  'contrary_grant': 'A mock probe transport may be presented as the real delivery sink.',
  'refusal': 'REJECT_BOOT111_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: real probe transport/path/sink; retain '
            'Provide a real probe transport/path/sink and pass condition with actual access limitations.',
  'independent_id': 'P11.1',
  'meaning': 'real probe transport/path/sink',
  'parent': 'Provide a real probe transport/path/sink and pass condition with actual access limitations.'},
 {'key': 'BOOT111_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-111',
  'level': 'MUST',
  'required_clause': 'Name the probe scenario and measurable pass condition.',
  'contrary_grant': 'Preparation may hand off a probe without a scenario or measurable pass condition.',
  'refusal': 'REJECT_BOOT111_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: scenario and measurable pass condition; '
            'retain Provide a real probe transport/path/sink and pass condition with actual access limitations.',
  'independent_id': 'P11.2',
  'meaning': 'scenario and measurable pass condition',
  'parent': 'Provide a real probe transport/path/sink and pass condition with actual access limitations.'},
 {'key': 'BOOT111_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-111',
  'level': 'MUST',
  'required_clause': 'Disclose actual probe access limits and unverified outcomes.',
  'contrary_grant': 'Unavailable probe access may be described as a verified operational outcome.',
  'refusal': 'REJECT_BOOT111_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual access/unverified limitations; '
            'retain Provide a real probe transport/path/sink and pass condition with actual access limitations.',
  'independent_id': 'P11.3',
  'meaning': 'actual access/unverified limitations',
  'parent': 'Provide a real probe transport/path/sink and pass condition with actual access limitations.'},
 {'key': 'BOOT112_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-112',
  'level': 'MUST',
  'required_clause': 'Complete measured current reconnaissance before drafting a dependent specification.',
  'contrary_grant': 'A dependent specification may be drafted before measured current reconnaissance.',
  'refusal': 'REJECT_BOOT112_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: measured current RECON before dependent '
            'spec; retain Measured current RECON precedes dependent specification and supplies actual '
            'evidence/limitations.',
  'independent_id': 'P12.1',
  'meaning': 'measured current RECON before dependent spec',
  'parent': 'Measured current RECON precedes dependent specification and supplies actual evidence/limitations.'},
 {'key': 'BOOT112_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-112',
  'level': 'MUST',
  'required_clause': 'Hand off the actual reconnaissance path, measurements, evidence and limitations.',
  'contrary_grant': 'A dependent specification may rely on reconnaissance memory without an actual evidence path or '
                    'limitations.',
  'refusal': 'REJECT_BOOT112_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual path/measurements/evidence and '
            'limitations; retain Measured current RECON precedes dependent specification and supplies actual '
            'evidence/limitations.',
  'independent_id': 'P12.2',
  'meaning': 'actual path/measurements/evidence and limitations',
  'parent': 'Measured current RECON precedes dependent specification and supplies actual evidence/limitations.'},
 {'key': 'BOOT113_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-113',
  'level': 'MUST',
  'required_clause': 'Preserve every actually required relevant reconnaissance lane and original requirement '
                     'quantifier.',
  'contrary_grant': 'Preparation may omit a required relevant reconnaissance lane or weaken an original quantifier.',
  'refusal': 'REJECT_BOOT113_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: every actually required relevant RECON '
            'lane/quantifier; retain Preserve existing RECON applicability/quantifiers, verify load-bearing facts, '
            'distinguish actual input from fixtures.',
  'independent_id': 'P13.1',
  'meaning': 'every actually required relevant RECON lane/quantifier',
  'parent': 'Preserve existing RECON applicability/quantifiers, verify load-bearing facts, distinguish actual input '
            'from fixtures.'},
 {'key': 'BOOT113_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-113',
  'level': 'MUST',
  'required_clause': 'Verify relevant load-bearing external facts against actual sources.',
  'contrary_grant': 'Preparation may adopt a guessed load-bearing external fact.',
  'refusal': 'REJECT_BOOT113_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: verified load-bearing relevant external '
            'facts; retain Preserve existing RECON applicability/quantifiers, verify load-bearing facts, distinguish '
            'actual input from fixtures.',
  'independent_id': 'P13.2',
  'meaning': 'verified load-bearing relevant external facts',
  'parent': 'Preserve existing RECON applicability/quantifiers, verify load-bearing facts, distinguish actual input '
            'from fixtures.'},
 {'key': 'BOOT113_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-113',
  'level': 'MUST',
  'required_clause': 'Distinguish actual operational input from fixture or synthetic input explicitly.',
  'contrary_grant': 'Fixture or synthetic input may be labelled measured operational input.',
  'refusal': 'REJECT_BOOT113_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual data versus fixture/synthetic '
            'labels; retain Preserve existing RECON applicability/quantifiers, verify load-bearing facts, distinguish '
            'actual input from fixtures.',
  'independent_id': 'P13.3',
  'meaning': 'actual data versus fixture/synthetic labels',
  'parent': 'Preserve existing RECON applicability/quantifiers, verify load-bearing facts, distinguish actual input '
            'from fixtures.'},
 {'key': 'BOOT114_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-114',
  'level': 'MUST',
  'required_clause': 'Seed only applicable missing durable or specification inputs within explicit existing file '
                     'authority.',
  'contrary_grant': 'Preparation may seed an existing or ungranted durable file.',
  'refusal': 'REJECT_BOOT114_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: only applicable missing authorized '
            'carriers; retain Seed only applicable missing authorized durable/spec inputs at dictated truth homes; '
            'detailed templates remain deferred.',
  'independent_id': 'P14.1',
  'meaning': 'only applicable missing authorized carriers',
  'parent': 'Seed only applicable missing authorized durable/spec inputs at dictated truth homes; detailed templates '
            'remain deferred.'},
 {'key': 'BOOT114_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-114',
  'level': 'MUST',
  'required_clause': 'Use the actual dictated one-truth locations for each prepared input.',
  'contrary_grant': 'Preparation may create a competing truth copy at an invented location.',
  'refusal': 'REJECT_BOOT114_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual dictated one-truth locations; retain '
            'Seed only applicable missing authorized durable/spec inputs at dictated truth homes; detailed templates '
            'remain deferred.',
  'independent_id': 'P14.2',
  'meaning': 'actual dictated one-truth locations',
  'parent': 'Seed only applicable missing authorized durable/spec inputs at dictated truth homes; detailed templates '
            'remain deferred.'},
 {'key': 'BOOT114_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-114',
  'level': 'MUST',
  'required_clause': 'Preserve existing content and history without overwriting them.',
  'contrary_grant': 'Preparation may overwrite existing content or history.',
  'refusal': 'REJECT_BOOT114_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: existing content/history is not '
            'overwritten; retain Seed only applicable missing authorized durable/spec inputs at dictated truth homes; '
            'detailed templates remain deferred.',
  'independent_id': 'P14.3',
  'meaning': 'existing content/history is not overwritten',
  'parent': 'Seed only applicable missing authorized durable/spec inputs at dictated truth homes; detailed templates '
            'remain deferred.'},
 {'key': 'BOOT114_C4',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-114',
  'level': 'MUST',
  'required_clause': 'Leave detailed document templates and lifecycle bodies at their declared later homes.',
  'contrary_grant': 'Minimum preparation completes every detailed template and lifecycle body.',
  'refusal': 'REJECT_BOOT114_C4',
  'reason': 'Required responsibility is missing, weakened or contradicted: detailed template/body home remains '
            'deferred; retain Seed only applicable missing authorized durable/spec inputs at dictated truth homes; '
            'detailed templates remain deferred.',
  'independent_id': 'P14.4',
  'meaning': 'detailed template/body home remains deferred',
  'parent': 'Seed only applicable missing authorized durable/spec inputs at dictated truth homes; detailed templates '
            'remain deferred.'},
 {'key': 'BOOT115_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-115',
  'level': 'MUST',
  'required_clause': 'Preserve the original human owner intent in prepared inputs.',
  'contrary_grant': 'The preparer agent goal may replace the original human owner intent.',
  'refusal': 'REJECT_BOOT115_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: original owner intent preserved; retain '
            'Preserve original owner intent and initial checkpoint in the prepared inputs.',
  'independent_id': 'P15.1',
  'meaning': 'original owner intent preserved',
  'parent': 'Preserve original owner intent and initial checkpoint in the prepared inputs.'},
 {'key': 'BOOT115_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-115',
  'level': 'MUST',
  'required_clause': 'Carry the actual initial checkpoint into the prepared handoff.',
  'contrary_grant': 'Preparation may replace the actual initial checkpoint with a guessed checkpoint.',
  'refusal': 'REJECT_BOOT115_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual initial checkpoint in handoff; '
            'retain Preserve original owner intent and initial checkpoint in the prepared inputs.',
  'independent_id': 'P15.2',
  'meaning': 'actual initial checkpoint in handoff',
  'parent': 'Preserve original owner intent and initial checkpoint in the prepared inputs.'},
 {'key': 'BOOT116_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-116',
  'level': 'MUST',
  'required_clause': 'Discover actual Git state and any applicable initialization need.',
  'contrary_grant': 'Preparation may assume a repository initialization need without inspecting actual Git state.',
  'refusal': 'REJECT_BOOT116_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual Git state/discovered need; retain '
            'Git initialization and commits need matching actual authority; inner preparation gets none automatically.',
  'independent_id': 'P16.1',
  'meaning': 'actual Git state/discovered need',
  'parent': 'Git initialization and commits need matching actual authority; inner preparation gets none '
            'automatically.'},
 {'key': 'BOOT116_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-116',
  'level': 'MUST',
  'required_clause': 'Require matching actual permission for Git initialization or commit, or return the missing grant '
                     'explicitly.',
  'contrary_grant': 'Applicable preparation automatically grants Git initialization and commit permission.',
  'refusal': 'REJECT_BOOT116_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: matching init/commit permission or explicit '
            'missing grant; retain Git initialization and commits need matching actual authority; inner preparation '
            'gets none automatically.',
  'independent_id': 'P16.2',
  'meaning': 'matching init/commit permission or explicit missing grant',
  'parent': 'Git initialization and commits need matching actual authority; inner preparation gets none '
            'automatically.'},
 {'key': 'BOOT116_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-116',
  'level': 'MUST',
  'required_clause': 'Keep integration authority with the authorized parent rather than the inner preparer.',
  'contrary_grant': 'An inner preparer may integrate its own result.',
  'refusal': 'REJECT_BOOT116_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: inner role gets no automatic integration '
            'right; retain Git initialization and commits need matching actual authority; inner preparation gets none '
            'automatically.',
  'independent_id': 'P16.3',
  'meaning': 'inner role gets no automatic integration right',
  'parent': 'Git initialization and commits need matching actual authority; inner preparation gets none '
            'automatically.'},
 {'key': 'BOOT117_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-117',
  'level': 'MUST',
  'required_clause': 'Resolve applicable initialization and ignore-hygiene prerequisites from actual project inputs.',
  'contrary_grant': 'Preparation may ignore an applicable initialization or ignore-hygiene prerequisite.',
  'refusal': 'REJECT_BOOT117_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual applicable initialization/ignore '
            'hygiene prerequisite; retain Expose required initialization/ignore hygiene as prepared input or an '
            'explicit unresolved prerequisite; preserve existing ignore rules and do not import detailed pattern '
            'bodies.',
  'independent_id': 'P17.1',
  'meaning': 'actual applicable initialization/ignore hygiene prerequisite',
  'parent': 'Expose required initialization/ignore hygiene as prepared input or an explicit unresolved prerequisite; '
            'preserve existing ignore rules and do not import detailed pattern bodies.'},
 {'key': 'BOOT117_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-117',
  'level': 'MUST',
  'required_clause': 'Preserve existing ignore and exclusion rules.',
  'contrary_grant': 'Preparation may replace existing ignore and exclusion rules with a blanket generated list.',
  'refusal': 'REJECT_BOOT117_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: existing ignore/exclusion rules preserved; '
            'retain Expose required initialization/ignore hygiene as prepared input or an explicit unresolved '
            'prerequisite; preserve existing ignore rules and do not import detailed pattern bodies.',
  'independent_id': 'P17.2',
  'meaning': 'existing ignore/exclusion rules preserved',
  'parent': 'Expose required initialization/ignore hygiene as prepared input or an explicit unresolved prerequisite; '
            'preserve existing ignore rules and do not import detailed pattern bodies.'},
 {'key': 'BOOT117_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-117',
  'level': 'MUST',
  'required_clause': 'Return missing hygiene as an explicit unresolved gap with its owning next action.',
  'contrary_grant': 'Preparation may claim completion while required hygiene is absent without an owning next action.',
  'refusal': 'REJECT_BOOT117_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: missing hygiene returned as explicit '
            'gap/owning next step; retain Expose required initialization/ignore hygiene as prepared input or an '
            'explicit unresolved prerequisite; preserve existing ignore rules and do not import detailed pattern '
            'bodies.',
  'independent_id': 'P17.3',
  'meaning': 'missing hygiene returned as explicit gap/owning next step',
  'parent': 'Expose required initialization/ignore hygiene as prepared input or an explicit unresolved prerequisite; '
            'preserve existing ignore rules and do not import detailed pattern bodies.'},
 {'key': 'BOOT117_C4',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-117',
  'level': 'MUST',
  'required_clause': 'Leave detailed ignore patterns and initializer implementation to the declared later or runtime '
                     'homes.',
  'contrary_grant': 'Minimum preparation implements the complete ignore-pattern and initializer engine.',
  'refusal': 'REJECT_BOOT117_C4',
  'reason': 'Required responsibility is missing, weakened or contradicted: detailed pattern/initializer body remains '
            'deferred; retain Expose required initialization/ignore hygiene as prepared input or an explicit '
            'unresolved prerequisite; preserve existing ignore rules and do not import detailed pattern bodies.',
  'independent_id': 'P17.4',
  'meaning': 'detailed pattern/initializer body remains deferred',
  'parent': 'Expose required initialization/ignore hygiene as prepared input or an explicit unresolved prerequisite; '
            'preserve existing ignore rules and do not import detailed pattern bodies.'},
 {'key': 'BOOT118_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-118',
  'level': 'MUST',
  'required_clause': 'Exclude secret values from prepared artifacts and logs.',
  'contrary_grant': 'Preparation may copy secret values into artifacts or logs.',
  'refusal': 'REJECT_BOOT118_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: secret values excluded from prepared '
            'artifacts; retain Preserve secret-safety and concurrent/foreign truth boundaries during authorized '
            'preparation.',
  'independent_id': 'P18.1',
  'meaning': 'secret values excluded from prepared artifacts',
  'parent': 'Preserve secret-safety and concurrent/foreign truth boundaries during authorized preparation.'},
 {'key': 'BOOT118_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-118',
  'level': 'MUST',
  'required_clause': 'Respect actual concurrency and single-writer constraints.',
  'contrary_grant': 'Preparation may disregard an applicable single-writer constraint.',
  'refusal': 'REJECT_BOOT118_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual concurrency/single-writer '
            'constraints; retain Preserve secret-safety and concurrent/foreign truth boundaries during authorized '
            'preparation.',
  'independent_id': 'P18.2',
  'meaning': 'actual concurrency/single-writer constraints',
  'parent': 'Preserve secret-safety and concurrent/foreign truth boundaries during authorized preparation.'},
 {'key': 'BOOT118_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-118',
  'level': 'MUST',
  'required_clause': 'Preserve foreign changes and their existing truth.',
  'contrary_grant': 'Preparation may overwrite foreign changes to force readiness.',
  'refusal': 'REJECT_BOOT118_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: foreign changes and truth preserved; retain '
            'Preserve secret-safety and concurrent/foreign truth boundaries during authorized preparation.',
  'independent_id': 'P18.3',
  'meaning': 'foreign changes and truth preserved',
  'parent': 'Preserve secret-safety and concurrent/foreign truth boundaries during authorized preparation.'},
 {'key': 'BOOT119_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-119',
  'level': 'MUST',
  'required_clause': 'Identify the actual needed baseline, map and checker configuration.',
  'contrary_grant': 'Preparation may claim readiness without identifying a required baseline, map or checker '
                    'configuration.',
  'refusal': 'REJECT_BOOT119_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: needed baseline/map/checker configuration; '
            'retain Identify actual needed baseline/map/checker configuration and project-resolved paths; detailed '
            'generation bodies remain at their homes.',
  'independent_id': 'P19.1',
  'meaning': 'needed baseline/map/checker configuration',
  'parent': 'Identify actual needed baseline/map/checker configuration and project-resolved paths; detailed generation '
            'bodies remain at their homes.'},
 {'key': 'BOOT119_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-119',
  'level': 'MUST',
  'required_clause': 'Associate the actual source and map using project-resolved paths.',
  'contrary_grant': 'Preparation may invent a universal source or map path.',
  'refusal': 'REJECT_BOOT119_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual source/map association and resolved '
            'paths; retain Identify actual needed baseline/map/checker configuration and project-resolved paths; '
            'detailed generation bodies remain at their homes.',
  'independent_id': 'P19.2',
  'meaning': 'actual source/map association and resolved paths',
  'parent': 'Identify actual needed baseline/map/checker configuration and project-resolved paths; detailed generation '
            'bodies remain at their homes.'},
 {'key': 'BOOT119_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-119',
  'level': 'MUST',
  'required_clause': 'Report missing required configuration explicitly as unavailable.',
  'contrary_grant': 'Missing required configuration may be reported as already present.',
  'refusal': 'REJECT_BOOT119_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: missing configuration explicitly '
            'unavailable; retain Identify actual needed baseline/map/checker configuration and project-resolved paths; '
            'detailed generation bodies remain at their homes.',
  'independent_id': 'P19.3',
  'meaning': 'missing configuration explicitly unavailable',
  'parent': 'Identify actual needed baseline/map/checker configuration and project-resolved paths; detailed generation '
            'bodies remain at their homes.'},
 {'key': 'BOOT119_C4',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-119',
  'level': 'MUST',
  'required_clause': 'Leave detailed baseline, map and checker generator implementations at their declared homes.',
  'contrary_grant': 'Minimum preparation implements every detailed baseline, map and checker generator.',
  'refusal': 'REJECT_BOOT119_C4',
  'reason': 'Required responsibility is missing, weakened or contradicted: detailed generator implementation remains '
            'later; retain Identify actual needed baseline/map/checker configuration and project-resolved paths; '
            'detailed generation bodies remain at their homes.',
  'independent_id': 'P19.4',
  'meaning': 'detailed generator implementation remains later',
  'parent': 'Identify actual needed baseline/map/checker configuration and project-resolved paths; detailed generation '
            'bodies remain at their homes.'},
 {'key': 'BOOT120_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-120',
  'level': 'MUST',
  'required_clause': 'Run a checker only when it is actually available, applicable and authorized.',
  'contrary_grant': 'Preparation may run an unavailable, inapplicable or unauthorized checker.',
  'refusal': 'REJECT_BOOT120_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: checker actually '
            'available/applicable/authorized; retain Run only an actually available authorized applicable checker and '
            'preserve its measured outcome or every remaining rule/gap and owning action.',
  'independent_id': 'P20.1',
  'meaning': 'checker actually available/applicable/authorized',
  'parent': 'Run only an actually available authorized applicable checker and preserve its measured outcome or every '
            'remaining rule/gap and owning action.'},
 {'key': 'BOOT120_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-120',
  'level': 'MUST',
  'required_clause': 'Retain the actual measured checker output and input identity.',
  'contrary_grant': 'A checker call without measured output or input identity may count as verification.',
  'refusal': 'REJECT_BOOT120_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual measured checker output/identity; '
            'retain Run only an actually available authorized applicable checker and preserve its measured outcome or '
            'every remaining rule/gap and owning action.',
  'independent_id': 'P20.2',
  'meaning': 'actual measured checker output/identity',
  'parent': 'Run only an actually available authorized applicable checker and preserve its measured outcome or every '
            'remaining rule/gap and owning action.'},
 {'key': 'BOOT120_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-120',
  'level': 'MUST',
  'required_clause': 'Retain every remaining rule failure or gap and its owning next action.',
  'contrary_grant': 'Preparation may suppress a remaining checker failure or gap.',
  'refusal': 'REJECT_BOOT120_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: every remaining rule/gap and owning next '
            'action; retain Run only an actually available authorized applicable checker and preserve its measured '
            'outcome or every remaining rule/gap and owning action.',
  'independent_id': 'P20.3',
  'meaning': 'every remaining rule/gap and owning next action',
  'parent': 'Run only an actually available authorized applicable checker and preserve its measured outcome or every '
            'remaining rule/gap and owning action.'},
 {'key': 'BOOT120_C4',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-120',
  'level': 'MUST',
  'required_clause': 'Never report an unavailable or failed required check as PASS.',
  'contrary_grant': 'An unavailable or failed required check may be reported as PASS.',
  'refusal': 'REJECT_BOOT120_C4',
  'reason': 'Required responsibility is missing, weakened or contradicted: missing/failed check never PASS; retain Run '
            'only an actually available authorized applicable checker and preserve its measured outcome or every '
            'remaining rule/gap and owning action.',
  'independent_id': 'P20.4',
  'meaning': 'missing/failed check never PASS',
  'parent': 'Run only an actually available authorized applicable checker and preserve its measured outcome or every '
            'remaining rule/gap and owning action.'},
 {'key': 'BOOT121_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-121',
  'level': 'MUST',
  'required_clause': 'Route an actual in-scope preparation defect through the existing authorized repair path.',
  'contrary_grant': 'Preparation may hide an actual in-scope preparation defect.',
  'refusal': 'REJECT_BOOT121_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual in-scope preparation defect route; '
            'retain Keep in-scope preparation defects and unconfirmed/content-losing gaps separate; stop dependent '
            'destructive or ungranted work.',
  'independent_id': 'P21.1',
  'meaning': 'actual in-scope preparation defect route',
  'parent': 'Keep in-scope preparation defects and unconfirmed/content-losing gaps separate; stop dependent '
            'destructive or ungranted work.'},
 {'key': 'BOOT121_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-121',
  'level': 'MUST',
  'required_clause': 'Stop dependent content-losing migration instead of deleting truth to force readiness.',
  'contrary_grant': 'Preparation may delete existing truth to force migration readiness.',
  'refusal': 'REJECT_BOOT121_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: content-losing migration stopped; retain '
            'Keep in-scope preparation defects and unconfirmed/content-losing gaps separate; stop dependent '
            'destructive or ungranted work.',
  'independent_id': 'P21.2',
  'meaning': 'content-losing migration stopped',
  'parent': 'Keep in-scope preparation defects and unconfirmed/content-losing gaps separate; stop dependent '
            'destructive or ungranted work.'},
 {'key': 'BOOT121_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-121',
  'level': 'MUST',
  'required_clause': 'Stop dependent work on an unconfirmed material decision and return its owner.',
  'contrary_grant': 'Preparation may collapse an unconfirmed material decision to force completion.',
  'refusal': 'REJECT_BOOT121_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: unconfirmed material decision stopped; '
            'retain Keep in-scope preparation defects and unconfirmed/content-losing gaps separate; stop dependent '
            'destructive or ungranted work.',
  'independent_id': 'P21.3',
  'meaning': 'unconfirmed material decision stopped',
  'parent': 'Keep in-scope preparation defects and unconfirmed/content-losing gaps separate; stop dependent '
            'destructive or ungranted work.'},
 {'key': 'BOOT122_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-122',
  'level': 'MUST',
  'required_clause': 'Return actual prepared artifact identities.',
  'contrary_grant': 'Guessed prepared artifact identities may count as delivered output.',
  'refusal': 'REJECT_BOOT122_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual prepared artifact identities; retain '
            'Return actual prepared identities, outcomes, gaps/refusals, owning scope and next authorized step through '
            'existing returns.',
  'independent_id': 'P22.1',
  'meaning': 'actual prepared artifact identities',
  'parent': 'Return actual prepared identities, outcomes, gaps/refusals, owning scope and next authorized step through '
            'existing returns.'},
 {'key': 'BOOT122_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-122',
  'level': 'MUST',
  'required_clause': 'Return measured outcomes and every remaining gap or refusal.',
  'contrary_grant': 'Preparation may return success while hiding a remaining gap or refusal.',
  'refusal': 'REJECT_BOOT122_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: measured outcomes and remaining '
            'gaps/refusals; retain Return actual prepared identities, outcomes, gaps/refusals, owning scope and next '
            'authorized step through existing returns.',
  'independent_id': 'P22.2',
  'meaning': 'measured outcomes and remaining gaps/refusals',
  'parent': 'Return actual prepared identities, outcomes, gaps/refusals, owning scope and next authorized step through '
            'existing returns.'},
 {'key': 'BOOT122_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-122',
  'level': 'MUST',
  'required_clause': 'Return the owning scope and next authorized action.',
  'contrary_grant': 'Preparation may return unrestricted next-action authority.',
  'refusal': 'REJECT_BOOT122_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: owning scope and next authorized action; '
            'retain Return actual prepared identities, outcomes, gaps/refusals, owning scope and next authorized step '
            'through existing returns.',
  'independent_id': 'P22.3',
  'meaning': 'owning scope and next authorized action',
  'parent': 'Return actual prepared identities, outcomes, gaps/refusals, owning scope and next authorized step through '
            'existing returns.'},
 {'key': 'BOOT122_C4',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-122',
  'level': 'MUST',
  'required_clause': 'Use existing return contracts and keep concrete result approval separate from preparation '
                     'completion.',
  'contrary_grant': 'Preparation completion grants integration approval or a new return schema.',
  'refusal': 'REJECT_BOOT122_C4',
  'reason': 'Required responsibility is missing, weakened or contradicted: existing return structure and separate '
            'result authority; retain Return actual prepared identities, outcomes, gaps/refusals, owning scope and '
            'next authorized step through existing returns.',
  'independent_id': 'P22.4',
  'meaning': 'existing return structure and separate result authority',
  'parent': 'Return actual prepared identities, outcomes, gaps/refusals, owning scope and next authorized step through '
            'existing returns.'},
 {'key': 'BOOT123_C1',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-123',
  'level': 'MUST',
  'required_clause': 'Convey settled constraints as inputs to the next assigned role.',
  'contrary_grant': 'Preparation may silently replace settled constraints in the next role input.',
  'refusal': 'REJECT_BOOT123_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: prepared settled constraints; retain '
            'Preparation conveys constraints and inputs; assigned technical architecture/implementation/repair remain '
            'with their roles.',
  'independent_id': 'P23.1',
  'meaning': 'prepared settled constraints',
  'parent': 'Preparation conveys constraints and inputs; assigned technical architecture/implementation/repair remain '
            'with their roles.'},
 {'key': 'BOOT123_C2',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-123',
  'level': 'MUST',
  'required_clause': 'Leave technical architecture authorship to the assigned Architect.',
  'contrary_grant': 'The preparer may author technical architecture without that role assignment.',
  'refusal': 'REJECT_BOOT123_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: technical design stays assigned Architect; '
            'retain Preparation conveys constraints and inputs; assigned technical architecture/implementation/repair '
            'remain with their roles.',
  'independent_id': 'P23.2',
  'meaning': 'technical design stays assigned Architect',
  'parent': 'Preparation conveys constraints and inputs; assigned technical architecture/implementation/repair remain '
            'with their roles.'},
 {'key': 'BOOT123_C3',
  'path': 'process/bootstrap.md',
  'norm': 'BOOT-123',
  'level': 'MUST',
  'required_clause': 'Leave implementation and repair to assigned Code and Debug roles.',
  'contrary_grant': 'The preparer may implement or repair without Code or Debug assignment.',
  'refusal': 'REJECT_BOOT123_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: Code/Debug repairs stay assigned roles; '
            'retain Preparation conveys constraints and inputs; assigned technical architecture/implementation/repair '
            'remain with their roles.',
  'independent_id': 'P23.3',
  'meaning': 'Code/Debug repairs stay assigned roles',
  'parent': 'Preparation conveys constraints and inputs; assigned technical architecture/implementation/repair remain '
            'with their roles.'},
 {'key': 'ROLE105_PRECEDENCE_C1',
  'path': 'roles/_base.md',
  'norm': 'ROLE-105',
  'level': 'MUST',
  'required_clause': 'Resolve the actual governing owner, project, host and runtime precedence.',
  'contrary_grant': 'A runtime label alone overrides the actual governing owner or project rule.',
  'refusal': 'REJECT_ROLE105_PRECEDENCE_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual owner/project/runtime precedence; '
            'retain Resolve actual owner/project/runtime precedence, permission boundaries and capability mechanisms.',
  'independent_id': 'A01.1',
  'meaning': 'actual owner/project/runtime precedence',
  'parent': 'Resolve actual owner/project/runtime precedence, permission boundaries and capability mechanisms.'},
 {'key': 'ROLE105_PRECEDENCE_C2',
  'path': 'roles/_base.md',
  'norm': 'ROLE-105',
  'level': 'MUST',
  'required_clause': 'Read the resolved commands, permission boundaries and capability mechanisms.',
  'contrary_grant': 'Tool availability may replace reading the resolved runtime contract.',
  'refusal': 'REJECT_ROLE105_PRECEDENCE_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: read resolved '
            'commands/permission/capability contract; retain Resolve actual owner/project/runtime precedence, '
            'permission boundaries and capability mechanisms.',
  'independent_id': 'A01.2',
  'meaning': 'read resolved commands/permission/capability contract',
  'parent': 'Resolve actual owner/project/runtime precedence, permission boundaries and capability mechanisms.'},
 {'key': 'ROLE105_PRECEDENCE_C3',
  'path': 'roles/_base.md',
  'norm': 'ROLE-105',
  'level': 'MUST',
  'required_clause': 'Preserve any applicable stricter project rule.',
  'contrary_grant': 'A runtime capability waives an applicable stricter project rule.',
  'refusal': 'REJECT_ROLE105_PRECEDENCE_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: applicable stricter project rule preserved; '
            'retain Resolve actual owner/project/runtime precedence, permission boundaries and capability mechanisms.',
  'independent_id': 'A01.3',
  'meaning': 'applicable stricter project rule preserved',
  'parent': 'Resolve actual owner/project/runtime precedence, permission boundaries and capability mechanisms.'},
 {'key': 'ROLE204_CONSENT_C1',
  'path': 'roles/_base.md',
  'norm': 'ROLE-204',
  'level': 'MUST',
  'required_clause': 'Preserve the authentic owning decision and its actual artifact provenance.',
  'contrary_grant': 'A tool or worker report may authenticate the owning decision.',
  'refusal': 'REJECT_ROLE204_CONSENT_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: authentic owning decision/artifact '
            'provenance; retain Preserve exact authentic owning consent, settled action/scope and artifact provenance; '
            'no re-ask of matching settled action.',
  'independent_id': 'A02.1',
  'meaning': 'authentic owning decision/artifact provenance',
  'parent': 'Preserve exact authentic owning consent, settled action/scope and artifact provenance; no re-ask of '
            'matching settled action.'},
 {'key': 'ROLE204_CONSENT_C2',
  'path': 'roles/_base.md',
  'norm': 'ROLE-204',
  'level': 'MUST',
  'required_clause': 'Bind consent to the exact settled action and bounded scope.',
  'contrary_grant': 'Consent for one action automatically grants an expanded scope.',
  'refusal': 'REJECT_ROLE204_CONSENT_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: exact settled action and bounded scope; '
            'retain Preserve exact authentic owning consent, settled action/scope and artifact provenance; no re-ask '
            'of matching settled action.',
  'independent_id': 'A02.2',
  'meaning': 'exact settled action and bounded scope',
  'parent': 'Preserve exact authentic owning consent, settled action/scope and artifact provenance; no re-ask of '
            'matching settled action.'},
 {'key': 'ROLE204_CONSENT_C3',
  'path': 'roles/_base.md',
  'norm': 'ROLE-204',
  'level': 'MUST',
  'required_clause': 'Retain matching existing consent without asking again for the same settled action.',
  'contrary_grant': 'Matching existing consent must be revoked and asked again by default.',
  'refusal': 'REJECT_ROLE204_CONSENT_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: matching existing consent preserved without '
            're-ask; retain Preserve exact authentic owning consent, settled action/scope and artifact provenance; no '
            're-ask of matching settled action.',
  'independent_id': 'A02.3',
  'meaning': 'matching existing consent preserved without re-ask',
  'parent': 'Preserve exact authentic owning consent, settled action/scope and artifact provenance; no re-ask of '
            'matching settled action.'},
 {'key': 'ROLE105_ASSIGNMENT_C1',
  'path': 'roles/_base.md',
  'norm': 'ROLE-105',
  'level': 'MUST',
  'required_clause': 'Carry the exact current binding to every affected assignment through existing delegation '
                     'context.',
  'contrary_grant': 'An affected worker may act without the exact current binding.',
  'refusal': 'REJECT_ROLE105_ASSIGNMENT_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: exact binding to every affected assignment; '
            'retain Carry current binding and constraints to every affected assignment through existing context.',
  'independent_id': 'A03.1',
  'meaning': 'exact binding to every affected assignment',
  'parent': 'Carry current binding and constraints to every affected assignment through existing context.'},
 {'key': 'ROLE105_ASSIGNMENT_C2',
  'path': 'roles/_base.md',
  'norm': 'ROLE-105',
  'level': 'MUST',
  'required_clause': 'Carry owning consent and its bounded scope to each affected assignment.',
  'contrary_grant': 'An affected assignment may assume owning consent or unrestricted scope.',
  'refusal': 'REJECT_ROLE105_ASSIGNMENT_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: owning consent/scope carried; retain Carry '
            'current binding and constraints to every affected assignment through existing context.',
  'independent_id': 'A03.2',
  'meaning': 'owning consent/scope carried',
  'parent': 'Carry current binding and constraints to every affected assignment through existing context.'},
 {'key': 'ROLE105_ASSIGNMENT_C3',
  'path': 'roles/_base.md',
  'norm': 'ROLE-105',
  'level': 'MUST',
  'required_clause': 'Carry task-specific negative constraints and the effective channel condition to affected '
                     'assignments.',
  'contrary_grant': 'An affected assignment may omit negative constraints or the effective channel condition.',
  'refusal': 'REJECT_ROLE105_ASSIGNMENT_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: negative constraints and effective channel '
            'condition carried; retain Carry current binding and constraints to every affected assignment through '
            'existing context.',
  'independent_id': 'A03.3',
  'meaning': 'negative constraints and effective channel condition carried',
  'parent': 'Carry current binding and constraints to every affected assignment through existing context.'},
 {'key': 'ROLE105_DEFAULT_C1',
  'path': 'roles/_base.md',
  'norm': 'ROLE-105',
  'level': 'MUST',
  'required_clause': 'Retain the structured default whenever its governing condition applies.',
  'contrary_grant': 'Free-form chat is approval under an applicable strict structured default without a valid owning '
                    'deviation.',
  'refusal': 'REJECT_ROLE105_DEFAULT_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: structured default when its governing '
            'condition holds; retain Retain structured default and the declared conditional absent-mechanism fallback.',
  'independent_id': 'A04.1',
  'meaning': 'structured default when its governing condition holds',
  'parent': 'Retain structured default and the declared conditional absent-mechanism fallback.'},
 {'key': 'ROLE105_DEFAULT_C2',
  'path': 'roles/_base.md',
  'norm': 'ROLE-105',
  'level': 'MUST',
  'required_clause': 'Use the declared absent-mechanism fallback only under its actual absence condition.',
  'contrary_grant': 'A present structured mechanism may be treated as absent merely because a fallback exists.',
  'refusal': 'REJECT_ROLE105_DEFAULT_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: declared absent-mechanism fallback only '
            'under its real condition; retain Retain structured default and the declared conditional absent-mechanism '
            'fallback.',
  'independent_id': 'A04.2',
  'meaning': 'declared absent-mechanism fallback only under its real condition',
  'parent': 'Retain structured default and the declared conditional absent-mechanism fallback.'},
 {'key': 'ROLE105_DEFAULT_C3',
  'path': 'roles/_base.md',
  'norm': 'ROLE-105',
  'level': 'MUST',
  'required_clause': 'Retain complete authentic approval evidence for an applicable fallback.',
  'contrary_grant': 'An applicable fallback may accept ambiguous words without authentic approval evidence.',
  'refusal': 'REJECT_ROLE105_DEFAULT_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: complete authentic approval evidence; '
            'retain Retain structured default and the declared conditional absent-mechanism fallback.',
  'independent_id': 'A04.3',
  'meaning': 'complete authentic approval evidence',
  'parent': 'Retain structured default and the declared conditional absent-mechanism fallback.'},
 {'key': 'ROLE105_SESSION_C1',
  'path': 'roles/_base.md',
  'norm': 'ROLE-105',
  'level': 'MUST',
  'required_clause': 'Use an effective-undelivered session fallback only from an authentic owning-session record of '
                     'that condition.',
  'contrary_grant': 'A guessed undelivered session permits free-form approval.',
  'refusal': 'REJECT_ROLE105_SESSION_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual owning session effective-undelivered '
            'condition; retain Effective-undelivered session fallback is conditional and expires when actual delivery '
            'returns.',
  'independent_id': 'A05.1',
  'meaning': 'actual owning session effective-undelivered condition',
  'parent': 'Effective-undelivered session fallback is conditional and expires when actual delivery returns.'},
 {'key': 'ROLE105_SESSION_C2',
  'path': 'roles/_base.md',
  'norm': 'ROLE-105',
  'level': 'MUST',
  'required_clause': 'Apply that session fallback only while the recorded effective-undelivered condition holds.',
  'contrary_grant': 'A session fallback applies permanently beyond its actual condition.',
  'refusal': 'REJECT_ROLE105_SESSION_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: fallback only during that condition; retain '
            'Effective-undelivered session fallback is conditional and expires when actual delivery returns.',
  'independent_id': 'A05.2',
  'meaning': 'fallback only during that condition',
  'parent': 'Effective-undelivered session fallback is conditional and expires when actual delivery returns.'},
 {'key': 'ROLE105_SESSION_C3',
  'path': 'roles/_base.md',
  'norm': 'ROLE-105',
  'level': 'MUST',
  'required_clause': 'Expire the session fallback when actual structured delivery returns.',
  'contrary_grant': 'A stale session fallback remains valid after structured delivery returns.',
  'refusal': 'REJECT_ROLE105_SESSION_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: restored delivery expires the fallback; '
            'retain Effective-undelivered session fallback is conditional and expires when actual delivery returns.',
  'independent_id': 'A05.3',
  'meaning': 'restored delivery expires the fallback',
  'parent': 'Effective-undelivered session fallback is conditional and expires when actual delivery returns.'},
 {'key': 'ROLE105_DEVIATION_C1',
  'path': 'roles/_base.md',
  'norm': 'ROLE-105',
  'level': 'MUST',
  'required_clause': 'Use an actual existing section anchor for a pointwise adoption deviation.',
  'contrary_grant': 'A pointwise adoption deviation may omit its actual section anchor.',
  'refusal': 'REJECT_ROLE105_DEVIATION_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: existing actual section anchor; retain '
            'Applicable pointwise adoption deviations use the existing anchored reason/owner/end-condition contract.',
  'independent_id': 'A06.1',
  'meaning': 'existing actual section anchor',
  'parent': 'Applicable pointwise adoption deviations use the existing anchored reason/owner/end-condition contract.'},
 {'key': 'ROLE105_DEVIATION_C2',
  'path': 'roles/_base.md',
  'norm': 'ROLE-105',
  'level': 'MUST',
  'required_clause': 'Record the deviation reason and owning authority.',
  'contrary_grant': 'A pointwise adoption deviation may omit its reason or owning authority.',
  'refusal': 'REJECT_ROLE105_DEVIATION_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: reason and owning authority; retain '
            'Applicable pointwise adoption deviations use the existing anchored reason/owner/end-condition contract.',
  'independent_id': 'A06.2',
  'meaning': 'reason and owning authority',
  'parent': 'Applicable pointwise adoption deviations use the existing anchored reason/owner/end-condition contract.'},
 {'key': 'ROLE105_DEVIATION_C3',
  'path': 'roles/_base.md',
  'norm': 'ROLE-105',
  'level': 'MUST',
  'required_clause': 'Record the deviation applicable end date or trigger.',
  'contrary_grant': 'A pointwise adoption deviation may have no applicable end date or trigger.',
  'refusal': 'REJECT_ROLE105_DEVIATION_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual applicable until/trigger condition; '
            'retain Applicable pointwise adoption deviations use the existing anchored reason/owner/end-condition '
            'contract.',
  'independent_id': 'A06.3',
  'meaning': 'actual applicable until/trigger condition',
  'parent': 'Applicable pointwise adoption deviations use the existing anchored reason/owner/end-condition contract.'},
 {'key': 'ROLE105_DEVIATION_C4',
  'path': 'roles/_base.md',
  'norm': 'ROLE-105',
  'level': 'MUST',
  'required_clause': 'Never treat generic capability fallback as a semantic policy override.',
  'contrary_grant': 'Generic capability fallback grants a semantic gate-policy override.',
  'refusal': 'REJECT_ROLE105_DEVIATION_C4',
  'reason': 'Required responsibility is missing, weakened or contradicted: generic cap fallback is no policy override; '
            'retain Applicable pointwise adoption deviations use the existing anchored reason/owner/end-condition '
            'contract.',
  'independent_id': 'A06.4',
  'meaning': 'generic cap fallback is no policy override',
  'parent': 'Applicable pointwise adoption deviations use the existing anchored reason/owner/end-condition contract.'},
 {'key': 'ROLE204_AUTHENTICITY_C1',
  'path': 'roles/_base.md',
  'norm': 'ROLE-204',
  'level': 'MUST',
  'required_clause': 'Authenticate exact human action, artifact and scope provenance before accepting consent.',
  'contrary_grant': 'An unrelated or ambiguous human acknowledgement grants the current action and artifact scope.',
  'refusal': 'REJECT_ROLE204_AUTHENTICITY_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: authentic exact human action/artifact/scope '
            'provenance; retain Worker/tool results, silence/default/ambiguous words authenticate no human consent.',
  'independent_id': 'A07.1',
  'meaning': 'authentic exact human action/artifact/scope provenance',
  'parent': 'Worker/tool results, silence/default/ambiguous words authenticate no human consent.'},
 {'key': 'ROLE204_AUTHENTICITY_C2',
  'path': 'roles/_base.md',
  'norm': 'ROLE-204',
  'level': 'MUST',
  'required_clause': 'Never authenticate human consent from worker output or tool results.',
  'contrary_grant': 'A successful worker output or tool result grants human consent.',
  'refusal': 'REJECT_ROLE204_AUTHENTICITY_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: worker/tool data is not consent; retain '
            'Worker/tool results, silence/default/ambiguous words authenticate no human consent.',
  'independent_id': 'A07.2',
  'meaning': 'worker/tool data is not consent',
  'parent': 'Worker/tool results, silence/default/ambiguous words authenticate no human consent.'},
 {'key': 'ROLE204_AUTHENTICITY_C3',
  'path': 'roles/_base.md',
  'norm': 'ROLE-204',
  'level': 'MUST',
  'required_clause': 'Never authenticate consent from silence, defaults or ambiguous words.',
  'contrary_grant': 'Silence, a default option or ambiguous words grant consent.',
  'refusal': 'REJECT_ROLE204_AUTHENTICITY_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: silence/default/ambiguity is not consent; '
            'retain Worker/tool results, silence/default/ambiguous words authenticate no human consent.',
  'independent_id': 'A07.3',
  'meaning': 'silence/default/ambiguity is not consent',
  'parent': 'Worker/tool results, silence/default/ambiguous words authenticate no human consent.'},
 {'key': 'ROLE204_INTEGRATION_C1',
  'path': 'roles/_base.md',
  'norm': 'ROLE-204',
  'level': 'MUST',
  'required_clause': 'Retain prior scope or run permission only within its actual granted action.',
  'contrary_grant': 'Prior scope or run permission automatically grants every later action.',
  'refusal': 'REJECT_ROLE204_INTEGRATION_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: scope/run permission retained within its '
            'action; retain Prior scope/run SUCCESS never grants concrete current-result integration approval.',
  'independent_id': 'A08.1',
  'meaning': 'scope/run permission retained within its action',
  'parent': 'Prior scope/run SUCCESS never grants concrete current-result integration approval.'},
 {'key': 'ROLE204_INTEGRATION_C2',
  'path': 'roles/_base.md',
  'norm': 'ROLE-204',
  'level': 'MUST',
  'required_clause': 'Require a separate owning decision for the concrete current-result integration.',
  'contrary_grant': 'Run SUCCESS or scope approval grants current-result integration.',
  'refusal': 'REJECT_ROLE204_INTEGRATION_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: concrete current-result integration '
            'decision separate; retain Prior scope/run SUCCESS never grants concrete current-result integration '
            'approval.',
  'independent_id': 'A08.2',
  'meaning': 'concrete current-result integration decision separate',
  'parent': 'Prior scope/run SUCCESS never grants concrete current-result integration approval.'},
 {'key': 'STATE501_C1',
  'path': 'flow/run-state.md',
  'norm': 'STATE-501',
  'level': 'MUST',
  'required_clause': 'Changes to the specification, plan, rules, adapter, approved scope or candidate invalidate '
                     'affected approval/verification evidence.',
  'contrary_grant': 'Changed required rules may be reused solely because the version label is unchanged.',
  'refusal': 'REJECT_STATE501_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual required rules identity despite same '
            'version; retain Unchanged version alone cannot prove unchanged required rules; shared MUST/current '
            'adoption defeats stale repeat reuse.',
  'independent_id': 'A09.1',
  'meaning': 'actual required rules identity despite same version',
  'parent': 'Unchanged version alone cannot prove unchanged required rules; shared MUST/current adoption defeats stale '
            'repeat reuse.'},
 {'key': 'ROLE103_C2',
  'path': 'roles/_base.md',
  'norm': 'ROLE-103',
  'level': 'MUST',
  'required_clause': 'Read the semantic-exoskeleton constitution in full before acting, including exoskeleton, LDD, '
                     'Doxygen and Test-Capture Antipattern rules; injected rules through {{cap:rules-injection}} still '
                     'require reading and override training defaults subject to project and owner precedence.',
  'contrary_grant': 'Required current rules may be skipped without reading or adoption.',
  'refusal': 'REJECT_ROLE103_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: complete current content read/adopted; '
            'retain Unchanged version alone cannot prove unchanged required rules; shared MUST/current adoption '
            'defeats stale repeat reuse.',
  'independent_id': 'A09.2',
  'meaning': 'complete current content read/adopted',
  'parent': 'Unchanged version alone cannot prove unchanged required rules; shared MUST/current adoption defeats stale '
            'repeat reuse.'},
 {'key': 'STATE502_C3',
  'path': 'flow/run-state.md',
  'norm': 'STATE-502',
  'level': 'MUST',
  'required_clause': 'After an authorized input amendment, reconcile applicable owner approval, re-establish the '
                     'current input locks and renew verification of affected work.',
  'contrary_grant': 'Changed required evidence may remain valid without renewed verification.',
  'refusal': 'REJECT_STATE502_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: changed required evidence renewed; retain '
            'Unchanged version alone cannot prove unchanged required rules; shared MUST/current adoption defeats stale '
            'repeat reuse.',
  'independent_id': 'A09.3',
  'meaning': 'changed required evidence renewed',
  'parent': 'Unchanged version alone cannot prove unchanged required rules; shared MUST/current adoption defeats stale '
            'repeat reuse.'},
 {'key': 'QA305_C4',
  'path': 'roles/qa.md',
  'norm': 'QA-305',
  'level': 'SHOULD',
  'required_clause': 'On a repeat call within the cycle, skip re-reading rules and skills only when the ruleset '
                     'version is unchanged; spend context on the bug report, failing output and named source delta.',
  'contrary_grant': 'Repeat calls may skip rules whose version has changed.',
  'refusal': 'REJECT_QA305_C4',
  'reason': 'Required responsibility is missing, weakened or contradicted: unchanged complete adopted rules may avoid '
            'duplicate fetching; retain Unchanged version alone cannot prove unchanged required rules; shared '
            'MUST/current adoption defeats stale repeat reuse.',
  'independent_id': 'A09.4',
  'meaning': 'unchanged complete adopted rules may avoid duplicate fetching',
  'parent': 'Unchanged version alone cannot prove unchanged required rules; shared MUST/current adoption defeats stale '
            'repeat reuse.'},
 {'key': 'OVERVIEW01_C1',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Intelligence selects appropriate models and reasoning through the current model policy and '
                     'assigned role contracts.',
  'contrary_grant': 'Intelligence has no responsibility or current interface.',
  'refusal': 'REJECT_OVERVIEW01_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: Intelligence responsibility and actual '
            'interface; retain Intelligence responsibility is visible with actual current model/reasoning interfaces '
            'and truthful runtime engine boundary.',
  'independent_id': 'R01.1',
  'meaning': 'Intelligence responsibility and actual interface',
  'parent': 'Intelligence responsibility is visible with actual current model/reasoning interfaces and truthful '
            'runtime engine boundary.'},
 {'key': 'OVERVIEW01_C2',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Inference and model execution engines are supplied by runtimes outside this repository.',
  'contrary_grant': 'This repository implements a working inference or model execution engine.',
  'refusal': 'REJECT_OVERVIEW01_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: external inference/model engine boundary; '
            'retain Intelligence responsibility is visible with actual current model/reasoning interfaces and truthful '
            'runtime engine boundary.',
  'independent_id': 'R01.2',
  'meaning': 'external inference/model engine boundary',
  'parent': 'Intelligence responsibility is visible with actual current model/reasoning interfaces and truthful '
            'runtime engine boundary.'},
 {'key': 'OVERVIEW02_C1',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Memory/Context supplies relevant instructions, durable state and verified knowledge pointers to '
                     'planning, execution and evaluation.',
  'contrary_grant': 'Memory/Context has no responsibility or interface.',
  'refusal': 'REJECT_OVERVIEW02_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: Memory/Context responsibility and '
            'actual/deferred interface; retain Memory/Context responsibility is visible and distinguishes supplied '
            'context from storage/retrieval/curation engines.',
  'independent_id': 'R02.1',
  'meaning': 'Memory/Context responsibility and actual/deferred interface',
  'parent': 'Memory/Context responsibility is visible and distinguishes supplied context from '
            'storage/retrieval/curation engines.'},
 {'key': 'OVERVIEW02_C2',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Storage, retrieval and curation engines remain external; detailed memory and learning bodies '
                     'remain deferred.',
  'contrary_grant': 'This repository implements working storage, retrieval and curation engines.',
  'refusal': 'REJECT_OVERVIEW02_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: external storage/retrieval/curation '
            'engines; retain Memory/Context responsibility is visible and distinguishes supplied context from '
            'storage/retrieval/curation engines.',
  'independent_id': 'R02.2',
  'meaning': 'external storage/retrieval/curation engines',
  'parent': 'Memory/Context responsibility is visible and distinguishes supplied context from '
            'storage/retrieval/curation engines.'},
 {'key': 'OVERVIEW03_C1',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Process/Orchestration assigns scoped work, preserves evidence and coordinates the existing owner '
                     'decisions.',
  'contrary_grant': 'Process/Orchestration has no responsibility.',
  'refusal': 'REJECT_OVERVIEW03_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: Process/Orchestration responsibility; '
            'retain Process/Orchestration responsibility points to actual role/phase/delegation/gate interfaces.',
  'independent_id': 'R03.1',
  'meaning': 'Process/Orchestration responsibility',
  'parent': 'Process/Orchestration responsibility points to actual role/phase/delegation/gate interfaces.'},
 {'key': 'OVERVIEW03_C2',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Current role, phase, delegation, state, finalization and gate subjects provide the process '
                     'interfaces.',
  'contrary_grant': 'Process links prove a deployed global orchestrator.',
  'refusal': 'REJECT_OVERVIEW03_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual current role/phase/delegation/gate '
            'interfaces; retain Process/Orchestration responsibility points to actual role/phase/delegation/gate '
            'interfaces.',
  'independent_id': 'R03.2',
  'meaning': 'actual current role/phase/delegation/gate interfaces',
  'parent': 'Process/Orchestration responsibility points to actual role/phase/delegation/gate interfaces.'},
 {'key': 'OVERVIEW04_C1',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Goal/Specification/Vision carries original human intent into measured specifications, planning '
                     'and result judgment.',
  'contrary_grant': 'Goal/Specification/Vision has no responsibility.',
  'refusal': 'REJECT_OVERVIEW04_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: Goal/Specification/Vision responsibility; '
            'retain Goal/Specification/Vision responsibility connects original intent to measured planning and '
            'current/deferred carriers.',
  'independent_id': 'R04.1',
  'meaning': 'Goal/Specification/Vision responsibility',
  'parent': 'Goal/Specification/Vision responsibility connects original intent to measured planning and '
            'current/deferred carriers.'},
 {'key': 'OVERVIEW04_C2',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Current PM, reconnaissance and plan interfaces use dictated durable carriers; detailed '
                     'specification and document bodies are current F4 drafts.',
  'contrary_grant': 'An agent goal may replace original human intent or a template link completes a deferred body.',
  'refusal': 'REJECT_OVERVIEW04_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: original intent and current/deferred '
            'planning carriers; retain Goal/Specification/Vision responsibility connects original intent to measured '
            'planning and current/deferred carriers.',
  'independent_id': 'R04.2',
  'meaning': 'original intent and current/deferred planning carriers',
  'parent': 'Goal/Specification/Vision responsibility connects original intent to measured planning and '
            'current/deferred carriers.'},
 {'key': 'OVERVIEW05_C1',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Feedback/Evaluation checks the actual result and feeds evidenced causes into improvement.',
  'contrary_grant': 'Feedback/Evaluation has no responsibility.',
  'refusal': 'REJECT_OVERVIEW05_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: Feedback/Evaluation responsibility; retain '
            'Feedback/Evaluation responsibility locates checks, independent review and causal improvement.',
  'independent_id': 'R05.1',
  'meaning': 'Feedback/Evaluation responsibility',
  'parent': 'Feedback/Evaluation responsibility locates checks, independent review and causal improvement.'},
 {'key': 'OVERVIEW05_C2',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Current QA, Reviewer, scan and conform interfaces provide independent evidenced checking; '
                     'learning bodies remain deferred.',
  'contrary_grant': 'A producer assertion counts as independent evaluation.',
  'refusal': 'REJECT_OVERVIEW05_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: independent evidenced current checking and '
            'causal improvement; retain Feedback/Evaluation responsibility locates checks, independent review and '
            'causal improvement.',
  'independent_id': 'R05.2',
  'meaning': 'independent evidenced current checking and causal improvement',
  'parent': 'Feedback/Evaluation responsibility locates checks, independent review and causal improvement.'},
 {'key': 'OVERVIEW06_C1',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'The delivery loop connects original intent, measured preparation, approved specification, '
                     'assigned design and work, independent evaluation and the resulting evidence.',
  'contrary_grant': 'The delivery loop may omit its producer-to-consumer handoffs.',
  'refusal': 'REJECT_OVERVIEW06_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: delivery loop producer/consumer links; '
            'retain Delivery loop follows original intent through actual work/evaluation and separate owner result '
            'decision.',
  'independent_id': 'R06.1',
  'meaning': 'delivery loop producer/consumer links',
  'parent': 'Delivery loop follows original intent through actual work/evaluation and separate owner result decision.'},
 {'key': 'OVERVIEW06_C2',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'The delivery loop retains a separate owner decision for the concrete result before integration.',
  'contrary_grant': 'Successful evaluation automatically integrates the result.',
  'refusal': 'REJECT_OVERVIEW06_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: separate concrete owner result decision; '
            'retain Delivery loop follows original intent through actual work/evaluation and separate owner result '
            'decision.',
  'independent_id': 'R06.2',
  'meaning': 'separate concrete owner result decision',
  'parent': 'Delivery loop follows original intent through actual work/evaluation and separate owner result decision.'},
 {'key': 'OVERVIEW07_C1',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'The methodology-learning loop connects observed failures and outcomes, causal analysis, '
                     'source-backed candidates, independent verification and an owning decision.',
  'contrary_grant': 'The methodology-learning loop omits evidence, verification or the owning decision.',
  'refusal': 'REJECT_OVERVIEW07_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: learning loop '
            'evidence/candidate/verification/owning decision; retain Methodology-learning loop preserves verified '
            'candidate-to-owning-decision feedback; it is not automatic external learning.',
  'independent_id': 'R07.1',
  'meaning': 'learning loop evidence/candidate/verification/owning decision',
  'parent': 'Methodology-learning loop preserves verified candidate-to-owning-decision feedback; it is not automatic '
            'external learning.'},
 {'key': 'OVERVIEW07_C2',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Unverified hypotheses and candidates never become policy or curated verified guidance '
                     'automatically.',
  'contrary_grant': 'An unverified hypothesis or candidate automatically becomes policy or curated verified guidance.',
  'refusal': 'REJECT_OVERVIEW07_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: no automatic unverified policy/curation; '
            'retain Methodology-learning loop preserves verified candidate-to-owning-decision feedback; it is not '
            'automatic external learning.',
  'independent_id': 'R07.2',
  'meaning': 'no automatic unverified policy/curation',
  'parent': 'Methodology-learning loop preserves verified candidate-to-owning-decision feedback; it is not automatic '
            'external learning.'},
 {'key': 'OVERVIEW07_C3',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'External knowledge transfer follows its separately authorized source and curation contract.',
  'contrary_grant': 'A learning candidate automatically authorizes external knowledge transfer or curation.',
  'refusal': 'REJECT_OVERVIEW07_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: external transfer limits; retain '
            'Methodology-learning loop preserves verified candidate-to-owning-decision feedback; it is not automatic '
            'external learning.',
  'independent_id': 'R07.3',
  'meaning': 'external transfer limits',
  'parent': 'Methodology-learning loop preserves verified candidate-to-owning-decision feedback; it is not automatic '
            'external learning.'},
 {'key': 'OVERVIEW08_C1',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Current F2 interfaces define bounded responsibilities without implementing their runtime '
                     'engines.',
  'contrary_grant': 'Current F2 interface links prove operational engine implementation.',
  'refusal': 'REJECT_OVERVIEW08_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: actual current F2 interfaces; retain '
            'Current F2 interfaces, completed F3/F4 and bounded prompting/policy bodies with wider F4/F5/F8 homes are distinct; a stub/link does not finish a '
            'body.',
  'independent_id': 'R08.1',
  'meaning': 'actual current F2 interfaces',
  'parent': 'Current F2 interfaces, completed F3/F4 and bounded prompting/policy bodies with wider F4/F5/F8 homes are distinct; a stub/link does not finish a '
            'body.'},
 {'key': 'OVERVIEW08_C2',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'The exoskeleton, navigation, Doxygen, LDD, tests, AX, data and lints bodies are current F3 bodies; document and greenfield/brownfield specification protocols plus shared specification validation are current F4 bodies; general decision lifecycle (DEC01) and full graph are current F4 bodies; confirmed conventions, lifecycle, batch and session procedures and five project forms are current bounded F4 drafts; eight prompting F5 and three autonomy/credentials/language policy bodies are current bounded drafts; six neutral readiness contracts for principles, glossary, Orient, preflight, run audit and conditional safety/recovery are current bounded drafts; wider F4 duties, learning F8, source completeness, operational adoption and publication remain explicit later or unresolved homes.',
  'contrary_grant': 'Detailed F3, F4, F5 and F8 bodies are complete in this release.',
  'refusal': 'REJECT_OVERVIEW08_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: specific detailed F3/F4/F5/F8 homes; retain '
            'Current F2 interfaces, completed F3/F4 and bounded prompting/policy bodies with wider F4/F5/F8 homes are distinct; a stub/link does not finish a '
            'body.',
  'independent_id': 'R08.2',
  'meaning': 'specific detailed F3/F4/F5/F8 homes',
  'parent': 'Current F2 interfaces, completed F3/F4 and bounded prompting/policy bodies with wider F4/F5/F8 homes are distinct; a stub/link does not finish a '
            'body.'},
 {'key': 'OVERVIEW08_C3',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'A stub or link never proves its detailed body completed.',
  'contrary_grant': 'A stub or link proves its detailed body completed.',
  'refusal': 'REJECT_OVERVIEW08_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: stub/link never claims completed body; '
            'retain Current F2 interfaces, completed F3/F4 and bounded prompting/policy bodies with wider F4/F5/F8 homes are distinct; a stub/link does not '
            'finish a body.',
  'independent_id': 'R08.3',
  'meaning': 'stub/link never claims completed body',
  'parent': 'Current F2 interfaces, completed F3/F4 and bounded prompting/policy bodies with wider F4/F5/F8 homes are distinct; a stub/link does not finish a '
            'body.'},
 {'key': 'OVERVIEW09_C1',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'One or multiple agents preserve existing authority, isolation and independent judgment.',
  'contrary_grant': 'Multiple agents may waive authority, isolation or independent judgment.',
  'refusal': 'REJECT_OVERVIEW09_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: authority and isolation/independence across '
            'topology; retain One or multiple agents retain existing '
            'authority/isolation/independence/safety/observability/time/economy/human control.',
  'independent_id': 'R09.1',
  'meaning': 'authority and isolation/independence across topology',
  'parent': 'One or multiple agents retain existing '
            'authority/isolation/independence/safety/observability/time/economy/human control.'},
 {'key': 'OVERVIEW09_C2',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Existing safety and observability constraints apply to either topology.',
  'contrary_grant': 'Multiple agents may waive existing safety or observability constraints.',
  'refusal': 'REJECT_OVERVIEW09_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: safety/observability constraints; retain '
            'One or multiple agents retain existing '
            'authority/isolation/independence/safety/observability/time/economy/human control.',
  'independent_id': 'R09.2',
  'meaning': 'safety/observability constraints',
  'parent': 'One or multiple agents retain existing '
            'authority/isolation/independence/safety/observability/time/economy/human control.'},
 {'key': 'OVERVIEW09_C3',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Existing time, economy and human-control constraints remain in force.',
  'contrary_grant': 'Multiple agents may waive time, economy or human control.',
  'refusal': 'REJECT_OVERVIEW09_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: time/economy/human control remains '
            'existing; retain One or multiple agents retain existing '
            'authority/isolation/independence/safety/observability/time/economy/human control.',
  'independent_id': 'R09.3',
  'meaning': 'time/economy/human control remains existing',
  'parent': 'One or multiple agents retain existing '
            'authority/isolation/independence/safety/observability/time/economy/human control.'},
 {'key': 'OVERVIEW10_C1',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Runtime adoption and propagated enforcement remain unproven.',
  'contrary_grant': 'This release proves runtime adoption and propagated enforcement.',
  'refusal': 'REJECT_OVERVIEW10_C1',
  'reason': 'Required responsibility is missing, weakened or contradicted: adoption/propagation unproven; retain '
            'Adoption, propagation, comparable real runs and publication remain explicitly unproven F6–F9 work.',
  'independent_id': 'R10.1',
  'meaning': 'adoption/propagation unproven',
  'parent': 'Adoption, propagation, comparable real runs and publication remain explicitly unproven F6–F9 work.'},
 {'key': 'OVERVIEW10_C2',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Comparable real runs, measured savings and reduced owner coordination effort remain unproven.',
  'contrary_grant': 'This release proves comparable real runs, savings or reduced owner coordination effort.',
  'refusal': 'REJECT_OVERVIEW10_C2',
  'reason': 'Required responsibility is missing, weakened or contradicted: comparable real runs/learning savings '
            'unproven; retain Adoption, propagation, comparable real runs and publication remain explicitly unproven '
            'F6–F9 work.',
  'independent_id': 'R10.2',
  'meaning': 'comparable real runs/learning savings unproven',
  'parent': 'Adoption, propagation, comparable real runs and publication remain explicitly unproven F6–F9 work.'},
 {'key': 'OVERVIEW10_C3',
  'path': 'README.md',
  'norm': '',
  'level': '',
  'required_clause': 'Operational F6–F9 work and publication remain pending their own evidence and authorization.',
  'contrary_grant': 'This release completes operational F6–F9 work or publication.',
  'refusal': 'REJECT_OVERVIEW10_C3',
  'reason': 'Required responsibility is missing, weakened or contradicted: publication and F6-F9 work pending; retain '
            'Adoption, propagation, comparable real runs and publication remain explicitly unproven F6–F9 work.',
  'independent_id': 'R10.3',
  'meaning': 'publication and F6-F9 work pending',
  'parent': 'Adoption, propagation, comparable real runs and publication remain explicitly unproven F6–F9 work.'}]

SUPPORTS = {'BOOT101_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-101',
                  'level': 'MUST',
                  'clause': 'Read the actual accessible code and source facts before classifying preparation.'}]],
 'BOOT101_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-101',
                  'level': 'MUST',
                  'clause': 'Read the actual applicable hidden and project agent instructions before preparing inputs.'}]],
 'BOOT101_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-101',
                  'level': 'MUST',
                  'clause': 'Read the actual complete brief'},
                 {'path': 'process/bootstrap.md',
                  'norm': 'BOOT-105',
                  'level': 'MUST',
                  'clause': 'Read the complete original brief rather than substituting a guessed summary.'}],
                [{'path': 'process/bootstrap.md', 'norm': 'BOOT-101', 'level': 'MUST', 'clause': 'durable project state'}]],
 'BOOT101_C4': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-101',
                  'level': 'MUST',
                  'clause': 'Inspect actual Git and applicable map facts and declare the available access scope.'}]],
 'BOOT102_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-102',
                  'level': 'MUST',
                  'clause': 'Classify an existing executable codebase as existing code requiring applicable migration or '
                            'reconstruction.'}]],
 'BOOT102_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-102',
                  'level': 'MUST',
                  'clause': 'Missing durable documents alone never make an existing codebase greenfield.'},
                 {'path': 'process/bootstrap.md',
                  'norm': 'BOOT-102',
                  'level': 'MUST',
                  'clause': 'Classify an existing executable codebase as existing code requiring applicable migration or '
                            'reconstruction.'},
                 {'path': 'process/bootstrap.md',
                  'norm': 'BOOT-102',
                  'level': 'MUST',
                  'clause': 'Use new-product preparation only for a genuinely new product supported by actual inputs.'}]],
 'BOOT102_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-102',
                  'level': 'MUST',
                  'clause': 'Use new-product preparation only for a genuinely new product supported by actual inputs.'}]],
 'BOOT103_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-103',
                  'level': 'MUST',
                  'clause': 'Treat an owner-requested conventions migration as its actual bounded preparation trigger.'}]],
 'BOOT103_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-103',
                  'level': 'MUST',
                  'clause': 'Require a matching bounded preparation grant before preparation writes.'}]],
 'BOOT104_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-104',
                  'level': 'MUST',
                  'clause': 'Keep spine inventory read-only.'}]],
 'BOOT104_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-104',
                  'level': 'MUST',
                  'clause': 'Return discovered preparation needs to the authorized parent.'}]],
 'BOOT104_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-104',
                  'level': 'MUST',
                  'clause': 'Obtain separate preparation write authority for the actual affected files.'}]],
 'BOOT105_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-105',
                  'level': 'MUST',
                  'clause': 'Read the complete original brief rather than substituting a guessed summary.'},
                 {'path': 'process/bootstrap.md',
                  'norm': 'BOOT-101',
                  'level': 'MUST',
                  'clause': 'Read the actual complete brief'}]],
 'BOOT105_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-105',
                  'level': 'MUST',
                  'clause': 'Read every original non-negotiable constraint before preparing choices.'}]],
 'BOOT106_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-106',
                  'level': 'MUST',
                  'clause': 'Recover settled answers and choices with their actual decision provenance.'}]],
 'BOOT106_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-106',
                  'level': 'MUST',
                  'clause': 'Reuse matching settled answers without redundant re-asking or silent replacement.'}]],
 'BOOT106_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-106',
                  'level': 'MUST',
                  'clause': 'Stop and route only genuine material ungranted gaps to their decision owner.'}]],
 'BOOT107_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-107',
                  'level': 'MUST',
                  'clause': 'State what the product does and the original human purpose it serves.'}]],
 'BOOT107_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-107',
                  'level': 'MUST',
                  'clause': 'State the actual intended audience.'}]],
 'BOOT107_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-107',
                  'level': 'MUST',
                  'clause': 'State one falsifiable user-visible first value and its observable pass condition.'}]],
 'BOOT108_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-108',
                  'level': 'MUST',
                  'clause': 'Retain every binding original non-negotiable in the prepared handoff.'}]],
 'BOOT109_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-109',
                  'level': 'MUST',
                  'clause': 'Carry source-backed settled stack, storage and transport choices as inputs.'}]],
 'BOOT109_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-109',
                  'level': 'MUST',
                  'clause': 'Carry the rationale and binding constraints for those settled technical choices.'}]],
 'BOOT109_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-109',
                  'level': 'MUST',
                  'clause': 'Verify load-bearing version facts when relevant before handing them to the next role.'}]],
 'BOOT110_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-110',
                  'level': 'MUST',
                  'clause': 'Carry the smallest approved included MVP boundary before Code.'}]],
 'BOOT110_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-110',
                  'level': 'MUST',
                  'clause': 'State deliberately deferred capabilities and actual dependencies.'}]],
 'BOOT110_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-110',
                  'level': 'MUST',
                  'clause': 'Settle the applicable boundary before coding rather than expanding it during implementation.'}]],
 'BOOT111_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-111',
                  'level': 'MUST',
                  'clause': 'Name the real probe transport, path and delivery sink required by the next role.'}]],
 'BOOT111_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-111',
                  'level': 'MUST',
                  'clause': 'Name the probe scenario and measurable pass condition.'}]],
 'BOOT111_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-111',
                  'level': 'MUST',
                  'clause': 'Disclose actual probe access limits and unverified outcomes.'}]],
 'BOOT112_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-112',
                  'level': 'MUST',
                  'clause': 'Complete measured current reconnaissance before drafting a dependent specification.'}]],
 'BOOT112_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-112',
                  'level': 'MUST',
                  'clause': 'Hand off the actual reconnaissance path, measurements, evidence and limitations.'}]],
 'BOOT113_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-113',
                  'level': 'MUST',
                  'clause': 'Preserve every actually required relevant reconnaissance lane and original requirement '
                            'quantifier.'}]],
 'BOOT113_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-113',
                  'level': 'MUST',
                  'clause': 'Verify relevant load-bearing external facts against actual sources.'}]],
 'BOOT113_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-113',
                  'level': 'MUST',
                  'clause': 'Distinguish actual operational input from fixture or synthetic input explicitly.'}]],
 'BOOT114_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-114',
                  'level': 'MUST',
                  'clause': 'Seed only applicable missing durable or specification inputs within explicit existing file '
                            'authority.'}]],
 'BOOT114_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-114',
                  'level': 'MUST',
                  'clause': 'Use the actual dictated one-truth locations for each prepared input.'}]],
 'BOOT114_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-114',
                  'level': 'MUST',
                  'clause': 'Preserve existing content and history without overwriting them.'}]],
 'BOOT114_C4': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-114',
                  'level': 'MUST',
                  'clause': 'Leave detailed document templates and lifecycle bodies at their declared later homes.'}]],
 'BOOT115_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-115',
                  'level': 'MUST',
                  'clause': 'Preserve the original human owner intent in prepared inputs.'}]],
 'BOOT115_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-115',
                  'level': 'MUST',
                  'clause': 'Carry the actual initial checkpoint into the prepared handoff.'}]],
 'BOOT116_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-116',
                  'level': 'MUST',
                  'clause': 'Discover actual Git state and any applicable initialization need.'}]],
 'BOOT116_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-116',
                  'level': 'MUST',
                  'clause': 'Require matching actual permission for Git initialization or commit, or return the missing grant '
                            'explicitly.'}]],
 'BOOT116_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-116',
                  'level': 'MUST',
                  'clause': 'Keep integration authority with the authorized parent rather than the inner preparer.'},
                 {'path': 'roles/_base.md',
                  'norm': 'ROLE-501',
                  'level': 'MUST NOT',
                  'clause': 'Commit or merge as an inner role; the parent orchestrator owns integration.'},
                 {'path': 'process/gates.md',
                  'norm': 'GATE-1004',
                  'level': 'MUST NOT',
                  'clause': 'Let inner role phases commit or merge; integration belongs to the parent.'}]],
 'BOOT117_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-117',
                  'level': 'MUST',
                  'clause': 'Resolve applicable initialization and ignore-hygiene prerequisites from actual project inputs.'}]],
 'BOOT117_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-117',
                  'level': 'MUST',
                  'clause': 'Preserve existing ignore and exclusion rules.'}]],
 'BOOT117_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-117',
                  'level': 'MUST',
                  'clause': 'Return missing hygiene as an explicit unresolved gap with its owning next action.'}]],
 'BOOT117_C4': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-117',
                  'level': 'MUST',
                  'clause': 'Leave detailed ignore patterns and initializer implementation to the declared later or runtime '
                            'homes.'}]],
 'BOOT118_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-118',
                  'level': 'MUST',
                  'clause': 'Exclude secret values from prepared artifacts and logs.'}]],
 'BOOT118_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-118',
                  'level': 'MUST',
                  'clause': 'Respect actual concurrency and single-writer constraints.'}]],
 'BOOT118_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-118',
                  'level': 'MUST',
                  'clause': 'Preserve foreign changes and their existing truth.'}]],
 'BOOT119_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-119',
                  'level': 'MUST',
                  'clause': 'Identify the actual needed baseline, map and checker configuration.'}]],
 'BOOT119_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-119',
                  'level': 'MUST',
                  'clause': 'Associate the actual source and map using project-resolved paths.'}]],
 'BOOT119_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-119',
                  'level': 'MUST',
                  'clause': 'Report missing required configuration explicitly as unavailable.'}]],
 'BOOT119_C4': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-119',
                  'level': 'MUST',
                  'clause': 'Leave detailed baseline, map and checker generator implementations at their declared homes.'}]],
 'BOOT120_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-120',
                  'level': 'MUST',
                  'clause': 'Run a checker only when it is actually available, applicable and authorized.'}]],
 'BOOT120_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-120',
                  'level': 'MUST',
                  'clause': 'Retain the actual measured checker output and input identity.'}]],
 'BOOT120_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-120',
                  'level': 'MUST',
                  'clause': 'Retain every remaining rule failure or gap and its owning next action.'}]],
 'BOOT120_C4': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-120',
                  'level': 'MUST',
                  'clause': 'Never report an unavailable or failed required check as PASS.'},
                 {'path': 'roles/_base.md',
                  'norm': 'ROLE-603',
                  'level': 'MUST NOT',
                  'clause': 'Claim that an unavailable check passed; report it unverified or blocked with its limitation.'}],
                [{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-120',
                  'level': 'MUST',
                  'clause': 'Never report an unavailable or failed required check as PASS.'}]],
 'BOOT121_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-121',
                  'level': 'MUST',
                  'clause': 'Route an actual in-scope preparation defect through the existing authorized repair path.'}]],
 'BOOT121_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-121',
                  'level': 'MUST',
                  'clause': 'Stop dependent content-losing migration instead of deleting truth to force readiness.'}]],
 'BOOT121_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-121',
                  'level': 'MUST',
                  'clause': 'Stop dependent work on an unconfirmed material decision and return its owner.'}]],
 'BOOT122_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-122',
                  'level': 'MUST',
                  'clause': 'Return actual prepared artifact identities.'}]],
 'BOOT122_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-122',
                  'level': 'MUST',
                  'clause': 'Return measured outcomes and every remaining gap or refusal.'}]],
 'BOOT122_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-122',
                  'level': 'MUST',
                  'clause': 'Return the owning scope and next authorized action.'}]],
 'BOOT122_C4': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-122',
                  'level': 'MUST',
                  'clause': 'Use existing return contracts and keep concrete result approval separate from preparation '
                            'completion.'}]],
 'BOOT123_C1': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-123',
                  'level': 'MUST',
                  'clause': 'Convey settled constraints as inputs to the next assigned role.'}]],
 'BOOT123_C2': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-123',
                  'level': 'MUST',
                  'clause': 'Leave technical architecture authorship to the assigned Architect.'}]],
 'BOOT123_C3': [[{'path': 'process/bootstrap.md',
                  'norm': 'BOOT-123',
                  'level': 'MUST',
                  'clause': 'Leave implementation and repair to assigned Code and Debug roles.'}]],
 'ROLE105_PRECEDENCE_C1': [[{'path': 'roles/_base.md',
                             'norm': 'ROLE-105',
                             'level': 'MUST',
                             'clause': 'Resolve the actual governing owner, project, host and runtime precedence.'}]],
 'ROLE105_PRECEDENCE_C2': [[{'path': 'roles/_base.md',
                             'norm': 'ROLE-105',
                             'level': 'MUST',
                             'clause': 'Read the resolved commands, permission boundaries and capability mechanisms.'},
                            {'path': 'roles/_base.md',
                             'norm': 'ROLE-105',
                             'level': 'MUST',
                             'clause': 'Read the adapter-resolved runtime contract covering commands, permission boundaries, '
                                       'existing authorization and capability mechanisms before acting.'}]],
 'ROLE105_PRECEDENCE_C3': [[{'path': 'roles/_base.md',
                             'norm': 'ROLE-105',
                             'level': 'MUST',
                             'clause': 'Preserve any applicable stricter project rule.'}]],
 'ROLE204_CONSENT_C1': [[{'path': 'roles/_base.md',
                          'norm': 'ROLE-204',
                          'level': 'MUST',
                          'clause': 'Preserve the authentic owning decision and its actual artifact provenance.'}]],
 'ROLE204_CONSENT_C2': [[{'path': 'roles/_base.md',
                          'norm': 'ROLE-204',
                          'level': 'MUST',
                          'clause': 'Bind consent to the exact settled action and bounded scope.'}]],
 'ROLE204_CONSENT_C3': [[{'path': 'roles/_base.md',
                          'norm': 'ROLE-204',
                          'level': 'MUST',
                          'clause': 'Retain matching existing consent without asking again for the same settled action.'},
                         {'path': 'roles/_base.md',
                          'norm': 'ROLE-204',
                          'level': 'MUST',
                          'clause': "Follow documented permission boundaries and the owner's existing authorization rather than "
                                    'asking again for settled actions or expanding scope.'}]],
 'ROLE105_ASSIGNMENT_C1': [[{'path': 'roles/_base.md',
                             'norm': 'ROLE-105',
                             'level': 'MUST',
                             'clause': 'Carry the exact current binding to every affected assignment through existing delegation '
                                       'context.'}]],
 'ROLE105_ASSIGNMENT_C2': [[{'path': 'roles/_base.md',
                             'norm': 'ROLE-105',
                             'level': 'MUST',
                             'clause': 'Carry owning consent and its bounded scope to each affected assignment.'}]],
 'ROLE105_ASSIGNMENT_C3': [[{'path': 'roles/_base.md',
                             'norm': 'ROLE-105',
                             'level': 'MUST',
                             'clause': 'Carry task-specific negative constraints and the effective channel condition to affected '
                                       'assignments.'}]],
 'ROLE105_DEFAULT_C1': [[{'path': 'roles/_base.md',
                          'norm': 'ROLE-105',
                          'level': 'MUST',
                          'clause': 'Retain the structured default whenever its governing condition applies.'},
                         {'path': 'process/gates.md',
                          'norm': 'GATE-201',
                          'level': 'MUST',
                          'clause': 'Pass a gate through a structured owner question using {{cap:ask-owner-structured}}, or the '
                                    'explicit approved exit of {{cap:plan-mode}}, subject to the declared fallback in GATE-203.'},
                         {'path': 'process/gates.md',
                          'norm': 'GATE-202',
                          'level': 'MUST NOT',
                          'clause': 'Treat a free-form chat message as approval where the adapter declares a structured question '
                                    'mechanism; agreement inside plan mode also does not exit that mode.'}]],
 'ROLE105_DEFAULT_C2': [[{'path': 'roles/_base.md',
                          'norm': 'ROLE-105',
                          'level': 'MUST',
                          'clause': 'Use the declared absent-mechanism fallback only under its actual absence condition.'},
                         {'path': 'process/gates.md',
                          'norm': 'GATE-203',
                          'level': 'MAY',
                          'clause': 'Accept explicit chat approval only where the adapter has no structured mechanism and names '
                                    'it as a declared fallback;'}]],
 'ROLE105_DEFAULT_C3': [[{'path': 'roles/_base.md',
                          'norm': 'ROLE-105',
                          'level': 'MUST',
                          'clause': 'Retain complete authentic approval evidence for an applicable fallback.'},
                         {'path': 'process/gates.md',
                          'norm': 'GATE-203',
                          'level': 'MAY',
                          'clause': "record the owner's words verbatim, artifact version or hash, scope, who and when"},
                         {'path': 'process/gates.md',
                          'norm': 'GATE-504',
                          'level': 'MUST',
                          'clause': 'Keep approval evidence in specification front matter and notes, with artifact identity and '
                                    "version or hash, scope, owner identity, timestamp and the owner's answer verbatim."}]],
 'ROLE105_SESSION_C1': [[{'path': 'roles/_base.md',
                          'norm': 'ROLE-105',
                          'level': 'MUST',
                          'clause': 'Use an effective-undelivered session fallback only from an authentic owning-session record '
                                    'of that condition.'}]],
 'ROLE105_SESSION_C2': [[{'path': 'roles/_base.md',
                          'norm': 'ROLE-105',
                          'level': 'MUST',
                          'clause': 'Apply that session fallback only while the recorded effective-undelivered condition '
                                    'holds.'}]],
 'ROLE105_SESSION_C3': [[{'path': 'roles/_base.md',
                          'norm': 'ROLE-105',
                          'level': 'MUST',
                          'clause': 'Expire the session fallback when actual structured delivery returns.'},
                         {'path': 'roles/_base.md',
                          'norm': 'ROLE-105',
                          'level': 'MUST',
                          'clause': 'Apply that session fallback only while the recorded effective-undelivered condition '
                                    'holds.'}]],
 'ROLE105_DEVIATION_C1': [[{'path': 'roles/_base.md',
                            'norm': 'ROLE-105',
                            'level': 'MUST',
                            'clause': 'Use an actual existing section anchor for a pointwise adoption deviation.'},
                           {'path': 'runtime/adapters.md',
                            'norm': '',
                            'level': '',
                            'clause': 'difference is an override: an anchor, a reason, an owner, and a date or a trigger.'},
                           {'path': 'runtime/adapters.md',
                            'norm': '',
                            'level': '',
                            'clause': '| `overrides[].anchor` | The anchor of the overridden section; it exists in the neutral '
                                      'file. | FMT-34 |'}]],
 'ROLE105_DEVIATION_C2': [[{'path': 'roles/_base.md',
                            'norm': 'ROLE-105',
                            'level': 'MUST',
                            'clause': 'Record the deviation reason and owning authority.'},
                           {'path': 'runtime/adapters.md',
                            'norm': '',
                            'level': '',
                            'clause': 'difference is an override: an anchor, a reason, an owner, and a date or a trigger.'},
                           {'path': 'runtime/adapters.md',
                            'norm': '',
                            'level': '',
                            'clause': '| `overrides[].reason` | Why the section differs. | FMT-34 |'}],
                          [{'path': 'roles/_base.md',
                            'norm': 'ROLE-105',
                            'level': 'MUST',
                            'clause': 'Record the deviation reason and owning authority.'},
                           {'path': 'runtime/adapters.md',
                            'norm': '',
                            'level': '',
                            'clause': 'difference is an override: an anchor, a reason, an owner, and a date or a trigger.'},
                           {'path': 'runtime/adapters.md',
                            'norm': '',
                            'level': '',
                            'clause': '| `overrides[].owner` | Who answers for the difference. | FMT-34 |'}]],
 'ROLE105_DEVIATION_C3': [[{'path': 'roles/_base.md',
                            'norm': 'ROLE-105',
                            'level': 'MUST',
                            'clause': 'Record the deviation applicable end date or trigger.'},
                           {'path': 'runtime/adapters.md',
                            'norm': '',
                            'level': '',
                            'clause': 'difference is an override: an anchor, a reason, an owner, and a date or a trigger.'},
                           {'path': 'runtime/adapters.md',
                            'norm': '',
                            'level': '',
                            'clause': '| `overrides[].until` | An ISO date; it must not lie in the past. | FMT-34, FMT-35 |'}],
                          [{'path': 'roles/_base.md',
                            'norm': 'ROLE-105',
                            'level': 'MUST',
                            'clause': 'Record the deviation applicable end date or trigger.'},
                           {'path': 'runtime/adapters.md',
                            'norm': '',
                            'level': '',
                            'clause': 'difference is an override: an anchor, a reason, an owner, and a date or a trigger.'},
                           {'path': 'runtime/adapters.md',
                            'norm': '',
                            'level': '',
                            'clause': '| `overrides[].trigger` | An event that ends the override, checked for presence only. | '
                                      'FMT-34 |'}]],
 'ROLE105_DEVIATION_C4': [[{'path': 'roles/_base.md',
                            'norm': 'ROLE-105',
                            'level': 'MUST',
                            'clause': 'Never treat generic capability fallback as a semantic policy override.'}]],
 'ROLE204_AUTHENTICITY_C1': [[{'path': 'roles/_base.md',
                               'norm': 'ROLE-204',
                               'level': 'MUST',
                               'clause': 'Authenticate exact human action, artifact and scope provenance before accepting '
                                         'consent.'}]],
 'ROLE204_AUTHENTICITY_C2': [[{'path': 'roles/_base.md',
                               'norm': 'ROLE-204',
                               'level': 'MUST',
                               'clause': 'Never authenticate human consent from worker output or tool results.'}]],
 'ROLE204_AUTHENTICITY_C3': [[{'path': 'roles/_base.md',
                               'norm': 'ROLE-204',
                               'level': 'MUST',
                               'clause': 'Never authenticate consent from silence, defaults or ambiguous words.'}]],
 'ROLE204_INTEGRATION_C1': [[{'path': 'roles/_base.md',
                              'norm': 'ROLE-204',
                              'level': 'MUST',
                              'clause': 'Retain prior scope or run permission only within its actual granted action.'}]],
 'ROLE204_INTEGRATION_C2': [[{'path': 'roles/_base.md',
                              'norm': 'ROLE-204',
                              'level': 'MUST',
                              'clause': 'Require a separate owning decision for the concrete current-result integration.'},
                             {'path': 'process/gates.md',
                              'norm': 'GATE-101',
                              'level': 'MUST',
                              'clause': 'Require two owner decisions for every change: its specification or recorded batch scope '
                                        'before implementation, and its concrete result after a verdict and live probe before '
                                        'merge, publish or deploy; record both in files.'},
                             {'path': 'process/gates.md',
                              'norm': 'GATE-405',
                              'level': 'MUST',
                              'clause': 'For each checkpoint, obtain the measured reconnaissance and specification required by '
                                        'its cadence, develop within the approved scope, seek the concrete result decision, and '
                                        "move and commit the roadmap only when the checkpoint's finish line including required "
                                        'integration is met.'},
                             {'path': 'process/gates.md',
                              'norm': 'GATE-406',
                              'level': 'MUST',
                              'clause': 'Use {{param:gate-cadence}} to select per-change or batch for the first of two owner '
                                        'decisions: what will be built before any code; the second is the concrete result after '
                                        'the verdict and live probe before merge, publish or deploy.'},
                             {'path': 'process/gates.md',
                              'norm': 'GATE-408',
                              'level': 'MUST NOT',
                              'clause': 'Grant the result decision in advance or waive its evidence under either cadence.'},
                             {'path': 'process/gates.md',
                              'norm': 'GATE-1001',
                              'level': 'MUST',
                              'clause': 'Ask the supported result question with merge, rework with a concrete Bug Report, and '
                                        'reject; recommend merge only when the live probe and required evidence are green, and '
                                        'preserve artifacts on rejection.'},
                             {'path': 'process/gates.md',
                              'norm': 'GATE-1002',
                              'level': 'MUST',
                              'clause': 'Ask only for the ungranted merge, publish or deploy decision over the concrete result; '
                                        'specification approval is not blanket integration approval.'},
                             {'path': 'process/gates.md',
                              'norm': 'GATE-1007',
                              'level': 'MUST',
                              'clause': 'After authorized integration, update roadmap checkboxes, position marker and notes, '
                                        'record actual results in the handoff and commit through the authorized parent; do not '
                                        'mark integration complete before the result decision.'},
                             {'path': 'flow/run-state.md',
                              'norm': 'STATE-703',
                              'level': 'MUST',
                              'clause': 'Record the concrete result decision separately from phase/run success. Keep '
                                        'failed/unavailable obligations and outstanding integration authority visible; only the '
                                        'actual owner decision under [gates](../process/gates.md) authorizes the applicable '
                                        'irreversible action.'},
                             {'path': 'process/gates.md',
                              'norm': 'GATE-102',
                              'level': 'MUST NOT',
                              'clause': 'Skip a gate or auto-approve it, even when the verdict appears obvious; both decisions '
                                        'require explicit owner consent and durable records, because treating the gate as a '
                                        'formality transfers ownership of the goal to the executor.'},
                             {'path': 'process/gates.md',
                              'norm': 'GATE-1205',
                              'level': 'MUST',
                              'clause': 'Return status, goal, plan and report paths, important validation and deviations through '
                                        '{{cap:structured-output}} or its declared fallback, routing any ungranted integration '
                                        'decision through the result gate.'}]],
 'STATE501_C1': [[{'path': 'flow/run-state.md',
                   'norm': 'STATE-501',
                   'level': 'MUST',
                   'clause': 'Changes to the specification, plan, rules, adapter, approved scope or candidate invalidate '
                             'affected approval/verification evidence.'}]],
 'ROLE103_C2': [[{'path': 'roles/_base.md',
                  'norm': 'ROLE-103',
                  'level': 'MUST',
                  'clause': 'Read the semantic-exoskeleton constitution in full before acting, including exoskeleton, LDD, '
                            'Doxygen and Test-Capture Antipattern rules; injected rules through {{cap:rules-injection}} still '
                            'require reading and override training defaults subject to project and owner precedence.'}]],
 'STATE502_C3': [[{'path': 'flow/run-state.md',
                   'norm': 'STATE-502',
                   'level': 'MUST',
                   'clause': 'After an authorized input amendment, reconcile applicable owner approval, re-establish the current '
                             'input locks and renew verification of affected work.'}]],
 'QA305_C4': [[{'path': 'roles/qa.md',
                'norm': 'QA-305',
                'level': 'SHOULD',
                'clause': 'On a repeat call within the cycle, skip re-reading rules and skills only when the ruleset version is '
                          'unchanged; spend context on the bug report, failing output and named source delta.'}]],
 'OVERVIEW01_C1': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Intelligence selects appropriate models and reasoning through the current model policy and '
                               'assigned role contracts.'}]],
 'OVERVIEW01_C2': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Inference and model execution engines are supplied by runtimes outside this repository.'}]],
 'OVERVIEW02_C1': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Memory/Context supplies relevant instructions, durable state and verified knowledge pointers to '
                               'planning, execution and evaluation.'}]],
 'OVERVIEW02_C2': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Storage, retrieval and curation engines remain external; detailed memory and learning bodies '
                               'remain deferred.'}]],
 'OVERVIEW03_C1': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Process/Orchestration assigns scoped work, preserves evidence and coordinates the existing owner '
                               'decisions.'}]],
 'OVERVIEW03_C2': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Current role, phase, delegation, state, finalization and gate subjects provide the process '
                               'interfaces.'}]],
 'OVERVIEW04_C1': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Goal/Specification/Vision carries original human intent into measured specifications, planning '
                               'and result judgment.'}]],
 'OVERVIEW04_C2': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Current PM, reconnaissance and plan interfaces use dictated durable carriers; detailed '
                               'specification and document bodies are current F4 drafts.'}]],
 'OVERVIEW05_C1': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Feedback/Evaluation checks the actual result and feeds evidenced causes into improvement.'}]],
 'OVERVIEW05_C2': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Current QA, Reviewer, scan and conform interfaces provide independent evidenced checking; '
                               'learning bodies remain deferred.'}]],
 'OVERVIEW06_C1': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'The delivery loop connects original intent, measured preparation, approved specification, '
                               'assigned design and work, independent evaluation and the resulting evidence.'}]],
 'OVERVIEW06_C2': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'The delivery loop retains a separate owner decision for the concrete result before '
                               'integration.'}]],
 'OVERVIEW07_C1': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'The methodology-learning loop connects observed failures and outcomes, causal analysis, '
                               'source-backed candidates, independent verification and an owning decision.'}]],
 'OVERVIEW07_C2': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Unverified hypotheses and candidates never become policy or curated verified guidance '
                               'automatically.'}]],
 'OVERVIEW07_C3': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'External knowledge transfer follows its separately authorized source and curation contract.'}]],
 'OVERVIEW08_C1': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Current F2 interfaces define bounded responsibilities without implementing their runtime '
                               'engines.'}]],
 'OVERVIEW08_C2': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'The exoskeleton, navigation, Doxygen, LDD, tests, AX, data and lints bodies are current F3 bodies; document and greenfield/brownfield specification protocols plus shared specification validation are current F4 bodies; general decision lifecycle (DEC01) and full graph are current F4 bodies; confirmed conventions, lifecycle, batch and session procedures and five project forms are current bounded F4 drafts; eight prompting F5 and three autonomy/credentials/language policy bodies are current bounded drafts; six neutral readiness contracts for principles, glossary, Orient, preflight, run audit and conditional safety/recovery are current bounded drafts; wider F4 duties, learning F8, source completeness, operational adoption and publication remain explicit later or unresolved homes.'},
                    {'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Current F3 bodies are [exoskeleton](code/exoskeleton.md), [navigation](code/navigation.md), [documentation](code/doxygen.md), [LDD](code/ldd.md), [tests](code/tests.md), [AX](code/ax-ui.md), [data](code/data.md) and [lints](checks/lints.md). Current F4 bodies are [document](protocols/document.md), [greenfield specification](protocols/spec-greenfield.md), [brownfield specification](protocols/spec-brownfield.md) and [shared specification validation](process/specification.md). General decision lifecycle (DEC01) at [decisions](process/decisions.md) and [full graph](protocols/graph.md) are current F4 bodies; [specification](process/specification.md) retains its validation contract. Confirmed [document conventions](documents/conventions.md), [lifecycle](process/lifecycle.md), [batches](process/batch.md) and [session](process/session.md) procedures and [five project forms](documents/templates/INDEX.md) are current bounded F4 drafts, with full editable forms and fictional filled examples. Current bounded F5 prompting bodies are [agent design](prompting/agent-prompt-design.md), [GRACE](prompting/grace.md), [brainstorm](prompting/brainstorm.md), [decomposition](prompting/decomposition.md), [prompt markup](prompting/prompt-markup.md), [solution design](prompting/solution-design.md), [superposition and collapse](prompting/superposition-collapse.md) and [verification](prompting/verification.md). Current remaining policy bodies are [autonomy](policies/autonomy.md), [credentials](policies/credentials.md) and [language](policies/language.md); [model policy](policies/models.md) retains all eighteen current norms. Current bounded readiness contracts are [principles](concepts/principles.md), [glossary](concepts/glossary.md), [Orient](checks/orient.md), [preflight](checks/preflight.md), [particular-run audit](checks/run-audit.md) and [conditional safety/recovery](process/safety.md), with complete reusable forms and fictional cases. These bounded drafts do not complete all F5 or wider F4, source completeness, learning/evaluation, adoption or publication duties. Detailed F8 learning homes are [improvement](process/learning.md) and [knowledge](process/learning.md).'}]],
 'OVERVIEW08_C3': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'A stub or link never proves its detailed body completed.'},
                    {'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'The remaining subjects have deferred bodies; an interface or link invokes a subject without proving its body complete, including the eight completed F3 bodies.'}]],
 'OVERVIEW09_C1': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'One or multiple agents preserve existing authority, isolation and independent judgment.'}]],
 'OVERVIEW09_C2': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Existing safety and observability constraints apply to either topology.'}]],
 'OVERVIEW09_C3': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Existing time, economy and human-control constraints remain in force.'}]],
 'OVERVIEW10_C1': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Runtime adoption and propagated enforcement remain unproven.'}]],
 'OVERVIEW10_C2': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Comparable real runs, measured savings and reduced owner coordination effort remain unproven.'}]],
 'OVERVIEW10_C3': [[{'path': 'README.md',
                     'norm': '',
                     'level': '',
                     'clause': 'Operational F6–F9 work and publication remain pending their own evidence and authorization.'}]]}

EDIT_PLANS = {'BOOT101_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Read the actual accessible code and source facts before classifying preparation.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT101_C1'],
                'redundant': None},
 'BOOT101_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Read the actual applicable hidden and project agent instructions before preparing inputs.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT101_C2'],
                'redundant': None},
 'BOOT101_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Read the actual complete brief and durable project state before deriving preparation '
                                     'inputs.',
                              'new': 'Read the actual complete brief before deriving preparation inputs.',
                              'expected_count': 1}],
                'expected_loss': ['BOOT101_C3'],
                'redundant': [{'path': 'process/bootstrap.md',
                               'old': 'Read the actual complete brief and durable project state before deriving preparation '
                                      'inputs.',
                               'new': 'Read the actual durable project state before deriving preparation inputs.',
                               'expected_count': 1}]},
 'BOOT101_C4': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Inspect actual Git and applicable map facts and declare the available access scope.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT101_C4'],
                'redundant': None},
 'BOOT102_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Classify an existing executable codebase as existing code requiring applicable migration '
                                     'or reconstruction.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT102_C1'],
                'redundant': None},
 'BOOT102_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Classify an existing executable codebase as existing code requiring applicable migration '
                                     'or reconstruction.',
                              'new': 'Classify an existing executable codebase as existing code requiring applicable migration '
                                     'or reconstruction, except where its durable documents are missing.',
                              'expected_count': 1},
                             {'path': 'process/bootstrap.md',
                              'old': 'Missing durable documents alone never make an existing codebase greenfield.',
                              'new': '',
                              'expected_count': 1},
                             {'path': 'process/bootstrap.md',
                              'old': 'Use new-product preparation only for a genuinely new product supported by actual inputs.',
                              'new': 'Use new-product preparation only when supported by actual inputs; outside the case of an '
                                     'existing executable codebase with missing durable documents, require a genuinely new '
                                     'product.',
                              'expected_count': 1}],
                'expected_loss': ['BOOT102_C1', 'BOOT102_C2', 'BOOT102_C3'],
                'redundant': [{'path': 'process/bootstrap.md',
                               'old': 'Missing durable documents alone never make an existing codebase greenfield.',
                               'new': '',
                               'expected_count': 1}]},
 'BOOT102_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Use new-product preparation only for a genuinely new product supported by actual inputs.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT102_C3'],
                'redundant': None},
 'BOOT103_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Treat an owner-requested conventions migration as its actual bounded preparation trigger.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT103_C1'],
                'redundant': None},
 'BOOT103_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Require a matching bounded preparation grant before preparation writes.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT103_C2'],
                'redundant': None},
 'BOOT104_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Keep spine inventory read-only.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT104_C1'],
                'redundant': None},
 'BOOT104_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Return discovered preparation needs to the authorized parent.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT104_C2'],
                'redundant': None},
 'BOOT104_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Obtain separate preparation write authority for the actual affected files.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT104_C3'],
                'redundant': None},
 'BOOT105_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Read the complete original brief rather than substituting a guessed summary.',
                              'new': '',
                              'expected_count': 1},
                             {'path': 'process/bootstrap.md',
                              'old': 'Read the actual complete brief and durable project state before deriving preparation '
                                     'inputs.',
                              'new': 'Read the actual durable project state before deriving preparation inputs.',
                              'expected_count': 1}],
                'expected_loss': ['BOOT101_C3', 'BOOT105_C1'],
                'redundant': [{'path': 'process/bootstrap.md',
                               'old': 'Read the complete original brief rather than substituting a guessed summary.',
                               'new': '',
                               'expected_count': 1}]},
 'BOOT105_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Read every original non-negotiable constraint before preparing choices.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT105_C2'],
                'redundant': None},
 'BOOT106_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Recover settled answers and choices with their actual decision provenance.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT106_C1'],
                'redundant': None},
 'BOOT106_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Reuse matching settled answers without redundant re-asking or silent replacement.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT106_C2'],
                'redundant': None},
 'BOOT106_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Stop and route only genuine material ungranted gaps to their decision owner.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT106_C3'],
                'redundant': None},
 'BOOT107_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'State what the product does and the original human purpose it serves.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT107_C1'],
                'redundant': None},
 'BOOT107_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'State the actual intended audience.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT107_C2'],
                'redundant': None},
 'BOOT107_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'State one falsifiable user-visible first value and its observable pass condition.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT107_C3'],
                'redundant': None},
 'BOOT108_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Retain every binding original non-negotiable in the prepared handoff.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT108_C1'],
                'redundant': None},
 'BOOT109_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Carry source-backed settled stack, storage and transport choices as inputs.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT109_C1'],
                'redundant': None},
 'BOOT109_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Carry the rationale and binding constraints for those settled technical choices.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT109_C2'],
                'redundant': None},
 'BOOT109_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Verify load-bearing version facts when relevant before handing them to the next role.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT109_C3'],
                'redundant': None},
 'BOOT110_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Carry the smallest approved included MVP boundary before Code.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT110_C1'],
                'redundant': None},
 'BOOT110_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'State deliberately deferred capabilities and actual dependencies.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT110_C2'],
                'redundant': None},
 'BOOT110_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Settle the applicable boundary before coding rather than expanding it during '
                                     'implementation.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT110_C3'],
                'redundant': None},
 'BOOT111_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Name the real probe transport, path and delivery sink required by the next role.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT111_C1'],
                'redundant': None},
 'BOOT111_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Name the probe scenario and measurable pass condition.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT111_C2'],
                'redundant': None},
 'BOOT111_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Disclose actual probe access limits and unverified outcomes.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT111_C3'],
                'redundant': None},
 'BOOT112_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Complete measured current reconnaissance before drafting a dependent specification.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT112_C1'],
                'redundant': None},
 'BOOT112_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Hand off the actual reconnaissance path, measurements, evidence and limitations.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT112_C2'],
                'redundant': None},
 'BOOT113_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Preserve every actually required relevant reconnaissance lane and original requirement '
                                     'quantifier.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT113_C1'],
                'redundant': None},
 'BOOT113_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Verify relevant load-bearing external facts against actual sources.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT113_C2'],
                'redundant': None},
 'BOOT113_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Distinguish actual operational input from fixture or synthetic input explicitly.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT113_C3'],
                'redundant': None},
 'BOOT114_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Seed only applicable missing durable or specification inputs within explicit existing file '
                                     'authority.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT114_C1'],
                'redundant': None},
 'BOOT114_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Use the actual dictated one-truth locations for each prepared input.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT114_C2'],
                'redundant': None},
 'BOOT114_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Preserve existing content and history without overwriting them.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT114_C3'],
                'redundant': None},
 'BOOT114_C4': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Leave detailed document templates and lifecycle bodies at their declared later homes.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT114_C4'],
                'redundant': None},
 'BOOT115_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Preserve the original human owner intent in prepared inputs.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT115_C1'],
                'redundant': None},
 'BOOT115_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Carry the actual initial checkpoint into the prepared handoff.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT115_C2'],
                'redundant': None},
 'BOOT116_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Discover actual Git state and any applicable initialization need.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT116_C1'],
                'redundant': None},
 'BOOT116_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Require matching actual permission for Git initialization or commit, or return the missing '
                                     'grant explicitly.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT116_C2'],
                'redundant': None},
 'BOOT116_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Keep integration authority with the authorized parent rather than the inner preparer.',
                              'new': '',
                              'expected_count': 1},
                             {'path': 'roles/_base.md',
                              'old': 'Commit or merge as an inner role; the parent orchestrator owns integration.',
                              'new': '',
                              'expected_count': 1},
                             {'path': 'process/gates.md',
                              'old': 'Let inner role phases commit or merge; integration belongs to the parent.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT116_C3'],
                'redundant': [{'path': 'process/bootstrap.md',
                               'old': 'Keep integration authority with the authorized parent rather than the inner preparer.',
                               'new': '',
                               'expected_count': 1}]},
 'BOOT117_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Resolve applicable initialization and ignore-hygiene prerequisites from actual project '
                                     'inputs.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT117_C1'],
                'redundant': None},
 'BOOT117_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Preserve existing ignore and exclusion rules.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT117_C2'],
                'redundant': None},
 'BOOT117_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Return missing hygiene as an explicit unresolved gap with its owning next action.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT117_C3'],
                'redundant': None},
 'BOOT117_C4': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Leave detailed ignore patterns and initializer implementation to the declared later or '
                                     'runtime homes.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT117_C4'],
                'redundant': None},
 'BOOT118_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Exclude secret values from prepared artifacts and logs.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT118_C1'],
                'redundant': None},
 'BOOT118_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Respect actual concurrency and single-writer constraints.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT118_C2'],
                'redundant': None},
 'BOOT118_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Preserve foreign changes and their existing truth.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT118_C3'],
                'redundant': None},
 'BOOT119_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Identify the actual needed baseline, map and checker configuration.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT119_C1'],
                'redundant': None},
 'BOOT119_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Associate the actual source and map using project-resolved paths.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT119_C2'],
                'redundant': None},
 'BOOT119_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Report missing required configuration explicitly as unavailable.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT119_C3'],
                'redundant': None},
 'BOOT119_C4': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Leave detailed baseline, map and checker generator implementations at their declared '
                                     'homes.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT119_C4'],
                'redundant': None},
 'BOOT120_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Run a checker only when it is actually available, applicable and authorized.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT120_C1'],
                'redundant': None},
 'BOOT120_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Retain the actual measured checker output and input identity.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT120_C2'],
                'redundant': None},
 'BOOT120_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Retain every remaining rule failure or gap and its owning next action.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT120_C3'],
                'redundant': None},
 'BOOT120_C4': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Never report an unavailable or failed required check as PASS.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT120_C4'],
                'redundant': None},
 'BOOT121_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Route an actual in-scope preparation defect through the existing authorized repair path.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT121_C1'],
                'redundant': None},
 'BOOT121_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Stop dependent content-losing migration instead of deleting truth to force readiness.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT121_C2'],
                'redundant': None},
 'BOOT121_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Stop dependent work on an unconfirmed material decision and return its owner.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT121_C3'],
                'redundant': None},
 'BOOT122_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Return actual prepared artifact identities.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT122_C1'],
                'redundant': None},
 'BOOT122_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Return measured outcomes and every remaining gap or refusal.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT122_C2'],
                'redundant': None},
 'BOOT122_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Return the owning scope and next authorized action.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT122_C3'],
                'redundant': None},
 'BOOT122_C4': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Use existing return contracts and keep concrete result approval separate from preparation '
                                     'completion.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT122_C4'],
                'redundant': None},
 'BOOT123_C1': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Convey settled constraints as inputs to the next assigned role.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT123_C1'],
                'redundant': None},
 'BOOT123_C2': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Leave technical architecture authorship to the assigned Architect.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT123_C2'],
                'redundant': None},
 'BOOT123_C3': {'omission': [{'path': 'process/bootstrap.md',
                              'old': 'Leave implementation and repair to assigned Code and Debug roles.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['BOOT123_C3'],
                'redundant': None},
 'ROLE105_PRECEDENCE_C1': {'omission': [{'path': 'roles/_base.md',
                                         'old': 'Resolve the actual governing owner, project, host and runtime precedence.',
                                         'new': '',
                                         'expected_count': 1}],
                           'expected_loss': ['ROLE105_PRECEDENCE_C1'],
                           'redundant': None},
 'ROLE105_PRECEDENCE_C2': {'omission': [{'path': 'roles/_base.md',
                                         'old': 'Read the resolved commands, permission boundaries and capability mechanisms.',
                                         'new': '',
                                         'expected_count': 1},
                                        {'path': 'roles/_base.md',
                                         'old': 'Read the adapter-resolved runtime contract covering commands, permission '
                                                'boundaries, existing authorization and capability mechanisms before acting.',
                                         'new': 'Read the adapter-resolved runtime contract covering existing authorization '
                                                'before acting.',
                                         'expected_count': 1}],
                           'expected_loss': ['ROLE105_PRECEDENCE_C2'],
                           'redundant': [{'path': 'roles/_base.md',
                                          'old': 'Read the resolved commands, permission boundaries and capability mechanisms.',
                                          'new': '',
                                          'expected_count': 1}]},
 'ROLE105_PRECEDENCE_C3': {'omission': [{'path': 'roles/_base.md',
                                         'old': 'Preserve any applicable stricter project rule.',
                                         'new': '',
                                         'expected_count': 1}],
                           'expected_loss': ['ROLE105_PRECEDENCE_C3'],
                           'redundant': None},
 'ROLE204_CONSENT_C1': {'omission': [{'path': 'roles/_base.md',
                                      'old': 'Preserve the authentic owning decision and its actual artifact provenance.',
                                      'new': '',
                                      'expected_count': 1}],
                        'expected_loss': ['ROLE204_CONSENT_C1'],
                        'redundant': None},
 'ROLE204_CONSENT_C2': {'omission': [{'path': 'roles/_base.md',
                                      'old': 'Bind consent to the exact settled action and bounded scope.',
                                      'new': '',
                                      'expected_count': 1}],
                        'expected_loss': ['ROLE204_CONSENT_C2'],
                        'redundant': None},
 'ROLE204_CONSENT_C3': {'omission': [{'path': 'roles/_base.md',
                                      'old': 'Retain matching existing consent without asking again for the same settled action.',
                                      'new': '',
                                      'expected_count': 1},
                                     {'path': 'roles/_base.md',
                                      'old': "Follow documented permission boundaries and the owner's existing authorization "
                                             'rather than asking again for settled actions or expanding scope.',
                                      'new': "Follow documented permission boundaries and the owner's existing authorization "
                                             'without expanding scope.',
                                      'expected_count': 1}],
                        'expected_loss': ['ROLE204_CONSENT_C3'],
                        'redundant': [{'path': 'roles/_base.md',
                                       'old': 'Retain matching existing consent without asking again for the same settled '
                                              'action.',
                                       'new': '',
                                       'expected_count': 1}]},
 'ROLE105_ASSIGNMENT_C1': {'omission': [{'path': 'roles/_base.md',
                                         'old': 'Carry the exact current binding to every affected assignment through existing '
                                                'delegation context.',
                                         'new': '',
                                         'expected_count': 1}],
                           'expected_loss': ['ROLE105_ASSIGNMENT_C1'],
                           'redundant': None},
 'ROLE105_ASSIGNMENT_C2': {'omission': [{'path': 'roles/_base.md',
                                         'old': 'Carry owning consent and its bounded scope to each affected assignment.',
                                         'new': '',
                                         'expected_count': 1}],
                           'expected_loss': ['ROLE105_ASSIGNMENT_C2'],
                           'redundant': None},
 'ROLE105_ASSIGNMENT_C3': {'omission': [{'path': 'roles/_base.md',
                                         'old': 'Carry task-specific negative constraints and the effective channel condition to '
                                                'affected assignments.',
                                         'new': '',
                                         'expected_count': 1}],
                           'expected_loss': ['ROLE105_ASSIGNMENT_C3'],
                           'redundant': None},
 'ROLE105_DEFAULT_C1': {'omission': [{'path': 'roles/_base.md',
                                      'old': 'Retain the structured default whenever its governing condition applies.',
                                      'new': '',
                                      'expected_count': 1},
                                     {'path': 'process/gates.md',
                                      'old': 'Pass a gate through a structured owner question using '
                                             '{{cap:ask-owner-structured}}, or the explicit approved exit of {{cap:plan-mode}}, '
                                             'subject to the declared fallback in GATE-203.',
                                      'new': '',
                                      'expected_count': 1},
                                     {'path': 'process/gates.md',
                                      'old': 'Treat a free-form chat message as approval where the adapter declares a structured '
                                             'question mechanism; agreement inside plan mode also does not exit that mode.',
                                      'new': '',
                                      'expected_count': 1}],
                        'expected_loss': ['ROLE105_DEFAULT_C1'],
                        'redundant': [{'path': 'roles/_base.md',
                                       'old': 'Retain the structured default whenever its governing condition applies.',
                                       'new': '',
                                       'expected_count': 1}]},
 'ROLE105_DEFAULT_C2': {'omission': [{'path': 'roles/_base.md',
                                      'old': 'Use the declared absent-mechanism fallback only under its actual absence '
                                             'condition.',
                                      'new': '',
                                      'expected_count': 1},
                                     {'path': 'process/gates.md',
                                      'old': 'Accept explicit chat approval only where the adapter has no structured mechanism '
                                             'and names it as a declared fallback;',
                                      'new': '',
                                      'expected_count': 1}],
                        'expected_loss': ['ROLE105_DEFAULT_C2'],
                        'redundant': [{'path': 'roles/_base.md',
                                       'old': 'Use the declared absent-mechanism fallback only under its actual absence '
                                              'condition.',
                                       'new': '',
                                       'expected_count': 1}]},
 'ROLE105_DEFAULT_C3': {'omission': [{'path': 'roles/_base.md',
                                      'old': 'Retain complete authentic approval evidence for an applicable fallback.',
                                      'new': '',
                                      'expected_count': 1},
                                     {'path': 'process/gates.md',
                                      'old': 'Accept explicit chat approval only where the adapter has no structured mechanism '
                                             "and names it as a declared fallback; record the owner's words verbatim, artifact "
                                             'version or hash, scope, who and when, and ask again on ambiguous wording instead '
                                             'of recording consent.',
                                      'new': 'Accept explicit chat approval only where the adapter has no structured mechanism '
                                             'and names it as a declared fallback; ask again on ambiguous wording instead of '
                                             'recording consent.',
                                      'expected_count': 1},
                                     {'path': 'process/gates.md',
                                      'old': 'Keep approval evidence in specification front matter and notes, with artifact '
                                             "identity and version or hash, scope, owner identity, timestamp and the owner's "
                                             'answer verbatim.',
                                      'new': 'For approvals other than an applicable fallback, keep approval evidence in '
                                             'specification front matter and notes, with artifact identity and version or hash, '
                                             "scope, owner identity, timestamp and the owner's answer verbatim.",
                                      'expected_count': 1}],
                        'expected_loss': ['ROLE105_DEFAULT_C3'],
                        'redundant': [{'path': 'roles/_base.md',
                                       'old': 'Retain complete authentic approval evidence for an applicable fallback.',
                                       'new': '',
                                       'expected_count': 1}]},
 'ROLE105_SESSION_C1': {'omission': [{'path': 'roles/_base.md',
                                      'old': 'Use an effective-undelivered session fallback only from an authentic '
                                             'owning-session record of that condition.',
                                      'new': '',
                                      'expected_count': 1}],
                        'expected_loss': ['ROLE105_SESSION_C1'],
                        'redundant': None},
 'ROLE105_SESSION_C2': {'omission': [{'path': 'roles/_base.md',
                                      'old': 'Apply that session fallback only while the recorded effective-undelivered '
                                             'condition holds.',
                                      'new': '',
                                      'expected_count': 1}],
                        'expected_loss': ['ROLE105_SESSION_C2'],
                        'redundant': None},
 'ROLE105_SESSION_C3': {'omission': [{'path': 'roles/_base.md',
                                      'old': 'Expire the session fallback when actual structured delivery returns.',
                                      'new': '',
                                      'expected_count': 1},
                                     {'path': 'roles/_base.md',
                                      'old': 'Apply that session fallback only while the recorded effective-undelivered '
                                             'condition holds.',
                                      'new': '',
                                      'expected_count': 1}],
                        'expected_loss': ['ROLE105_SESSION_C2', 'ROLE105_SESSION_C3'],
                        'redundant': [{'path': 'roles/_base.md',
                                       'old': 'Expire the session fallback when actual structured delivery returns.',
                                       'new': '',
                                       'expected_count': 1}]},
 'ROLE105_DEVIATION_C1': {'omission': [{'path': 'roles/_base.md',
                                        'old': 'Use an actual existing section anchor for a pointwise adoption deviation.',
                                        'new': '',
                                        'expected_count': 1},
                                       {'path': 'runtime/adapters.md',
                                        'old': 'difference is an override: an anchor, a reason, an owner, and a date or a '
                                               'trigger.',
                                        'new': 'difference is an override: a reason, an owner, and a date or a trigger.',
                                        'expected_count': 1},
                                       {'path': 'runtime/adapters.md',
                                        'old': '| `overrides[].anchor` | The anchor of the overridden section; it exists in the '
                                               'neutral file. | FMT-34 |',
                                        'new': '',
                                        'expected_count': 1}],
                          'expected_loss': ['ROLE105_DEVIATION_C1'],
                          'redundant': [{'path': 'roles/_base.md',
                                         'old': 'Use an actual existing section anchor for a pointwise adoption deviation.',
                                         'new': '',
                                         'expected_count': 1}]},
 'ROLE105_DEVIATION_C2': {'omission': [{'path': 'roles/_base.md',
                                        'old': 'Record the deviation reason and owning authority.',
                                        'new': '',
                                        'expected_count': 1},
                                       {'path': 'runtime/adapters.md',
                                        'old': 'difference is an override: an anchor, a reason, an owner, and a date or a '
                                               'trigger.',
                                        'new': 'difference is an override: an anchor and a date or a trigger.',
                                        'expected_count': 1},
                                       {'path': 'runtime/adapters.md',
                                        'old': '| `overrides[].reason` | Why the section differs. | FMT-34 |',
                                        'new': '',
                                        'expected_count': 1},
                                       {'path': 'runtime/adapters.md',
                                        'old': '| `overrides[].owner` | Who answers for the difference. | FMT-34 |',
                                        'new': '',
                                        'expected_count': 1}],
                          'expected_loss': ['ROLE105_DEVIATION_C2'],
                          'redundant': [{'path': 'roles/_base.md',
                                         'old': 'Record the deviation reason and owning authority.',
                                         'new': '',
                                         'expected_count': 1}]},
 'ROLE105_DEVIATION_C3': {'omission': [{'path': 'roles/_base.md',
                                        'old': 'Record the deviation applicable end date or trigger.',
                                        'new': '',
                                        'expected_count': 1},
                                       {'path': 'runtime/adapters.md',
                                        'old': 'difference is an override: an anchor, a reason, an owner, and a date or a '
                                               'trigger.',
                                        'new': 'difference is an override: an anchor, a reason and an owner.',
                                        'expected_count': 1},
                                       {'path': 'runtime/adapters.md',
                                        'old': '| `overrides[].until` | An ISO date; it must not lie in the past. | FMT-34, '
                                               'FMT-35 |',
                                        'new': '',
                                        'expected_count': 1},
                                       {'path': 'runtime/adapters.md',
                                        'old': '| `overrides[].trigger` | An event that ends the override, checked for presence '
                                               'only. | FMT-34 |',
                                        'new': '',
                                        'expected_count': 1}],
                          'expected_loss': ['ROLE105_DEVIATION_C3'],
                          'redundant': [{'path': 'roles/_base.md',
                                         'old': 'Record the deviation applicable end date or trigger.',
                                         'new': '',
                                         'expected_count': 1}]},
 'ROLE105_DEVIATION_C4': {'omission': [{'path': 'roles/_base.md',
                                        'old': 'Never treat generic capability fallback as a semantic policy override.',
                                        'new': '',
                                        'expected_count': 1}],
                          'expected_loss': ['ROLE105_DEVIATION_C4'],
                          'redundant': None},
 'ROLE204_AUTHENTICITY_C1': {'omission': [{'path': 'roles/_base.md',
                                           'old': 'Authenticate exact human action, artifact and scope provenance before '
                                                  'accepting consent.',
                                           'new': '',
                                           'expected_count': 1}],
                             'expected_loss': ['ROLE204_AUTHENTICITY_C1'],
                             'redundant': None},
 'ROLE204_AUTHENTICITY_C2': {'omission': [{'path': 'roles/_base.md',
                                           'old': 'Never authenticate human consent from worker output or tool results.',
                                           'new': '',
                                           'expected_count': 1}],
                             'expected_loss': ['ROLE204_AUTHENTICITY_C2'],
                             'redundant': None},
 'ROLE204_AUTHENTICITY_C3': {'omission': [{'path': 'roles/_base.md',
                                           'old': 'Never authenticate consent from silence, defaults or ambiguous words.',
                                           'new': '',
                                           'expected_count': 1}],
                             'expected_loss': ['ROLE204_AUTHENTICITY_C3'],
                             'redundant': None},
 'ROLE204_INTEGRATION_C1': {'omission': [{'path': 'roles/_base.md',
                                          'old': 'Retain prior scope or run permission only within its actual granted action.',
                                          'new': '',
                                          'expected_count': 1}],
                            'expected_loss': ['ROLE204_INTEGRATION_C1'],
                            'redundant': None},
 'ROLE204_INTEGRATION_C2': {'omission': [{'path': 'roles/_base.md',
                                          'old': 'Require a separate owning decision for the concrete current-result '
                                                 'integration.',
                                          'new': '',
                                          'expected_count': 1},
                                         {'path': 'process/gates.md',
                                          'old': 'Require two owner decisions for every change: its specification or recorded '
                                                 'batch scope before implementation, and its concrete result after a verdict and '
                                                 'live probe before merge, publish or deploy; record both in files.',
                                          'new': 'Require an owner decision for every change: its specification or recorded '
                                                 'batch scope before implementation; record that decision in files. Require a '
                                                 'verdict and live probe before merge, publish or deploy.',
                                          'expected_count': 1},
                                         {'path': 'process/gates.md',
                                          'old': 'For each checkpoint, obtain the measured reconnaissance and specification '
                                                 'required by its cadence, develop within the approved scope, seek the concrete '
                                                 "result decision, and move and commit the roadmap only when the checkpoint's "
                                                 'finish line including required integration is met.',
                                          'new': 'For each checkpoint, obtain the measured reconnaissance and specification '
                                                 'required by its cadence, develop within the approved scope, move and commit '
                                                 "the roadmap only when the checkpoint's finish line including required "
                                                 'integration is met.',
                                          'expected_count': 1},
                                         {'path': 'process/gates.md',
                                          'old': 'Use {{param:gate-cadence}} to select per-change or batch for the first of two '
                                                 'owner decisions: what will be built before any code; the second is the '
                                                 'concrete result after the verdict and live probe before merge, publish or '
                                                 'deploy.',
                                          'new': 'Use {{param:gate-cadence}} to select per-change or batch for the owner '
                                                 'decision: what will be built before any code. Require a verdict and live probe '
                                                 'before merge, publish or deploy under either cadence.',
                                          'expected_count': 1},
                                         {'path': 'process/gates.md',
                                          'old': 'Grant the result decision in advance or waive its evidence under either '
                                                 'cadence.',
                                          'new': 'Waive required evidence under either cadence.',
                                          'expected_count': 1},
                                         {'path': 'process/gates.md',
                                          'old': 'Ask the supported result question with merge, rework with a concrete Bug '
                                                 'Report, and reject; recommend merge only when the live probe and required '
                                                 'evidence are green, and preserve artifacts on rejection.',
                                          'new': 'For a supported result question, offer merge, rework with a concrete Bug '
                                                 'Report, and reject; recommend merge only when the live probe and required '
                                                 'evidence are green, and preserve artifacts on rejection.',
                                          'expected_count': 1},
                                         {'path': 'process/gates.md',
                                          'old': 'Ask only for the ungranted merge, publish or deploy decision over the concrete '
                                                 'result; specification approval is not blanket integration approval.',
                                          'new': 'Do not ask again for an already granted merge, publish or deploy decision.',
                                          'expected_count': 1},
                                         {'path': 'process/gates.md',
                                          'old': 'After authorized integration, update roadmap checkboxes, position marker and '
                                                 'notes, record actual results in the handoff and commit through the authorized '
                                                 'parent; do not mark integration complete before the result decision.',
                                          'new': 'After authorized integration, update roadmap checkboxes, position marker and '
                                                 'notes, record actual results in the handoff and commit through the authorized '
                                                 'parent.',
                                          'expected_count': 1},
                                         {'path': 'flow/run-state.md',
                                          'old': 'Record the concrete result decision separately from phase/run success. Keep '
                                                 'failed/unavailable obligations and outstanding integration authority visible; '
                                                 'only the actual owner decision under [gates](../process/gates.md) authorizes '
                                                 'the applicable irreversible action.',
                                          'new': 'Keep failed/unavailable obligations and outstanding integration authority '
                                                 'visible.',
                                          'expected_count': 1},
                                         {'path': 'process/gates.md',
                                          'old': 'Skip a gate or auto-approve it, even when the verdict appears obvious; both '
                                                 'decisions require explicit owner consent and durable records, because treating '
                                                 'the gate as a formality transfers ownership of the goal to the executor.',
                                          'new': 'Skip a gate other than the concrete current-result integration decision or '
                                                 'auto-approve such a gate, even when the verdict appears obvious; the '
                                                 'specification or recorded batch-scope decision requires explicit owner consent '
                                                 'and durable records, because treating an owner gate as a formality transfers '
                                                 'ownership of the goal to the executor.',
                                          'expected_count': 1},
                                         {'path': 'process/gates.md',
                                          'old': 'Return status, goal, plan and report paths, important validation and '
                                                 'deviations through {{cap:structured-output}} or its declared fallback, routing '
                                                 'any ungranted integration decision through the result gate.',
                                          'new': 'Return status, goal, plan and report paths, important validation and '
                                                 'deviations through {{cap:structured-output}} or its declared fallback.',
                                          'expected_count': 1}],
                            'expected_loss': ['ROLE204_INTEGRATION_C2'],
                            'redundant': [{'path': 'roles/_base.md',
                                           'old': 'Require a separate owning decision for the concrete current-result '
                                                  'integration.',
                                           'new': '',
                                           'expected_count': 1}]},
 'STATE501_C1': {'omission': [{'path': 'flow/run-state.md',
                               'old': 'Changes to the specification, plan, rules, adapter, approved scope or candidate '
                                      'invalidate affected approval/verification evidence.',
                               'new': '',
                               'expected_count': 1}],
                 'expected_loss': ['STATE501_C1'],
                 'redundant': None},
 'ROLE103_C2': {'omission': [{'path': 'roles/_base.md',
                              'old': 'Read the semantic-exoskeleton constitution in full before acting, including exoskeleton, '
                                     'LDD, Doxygen and Test-Capture Antipattern rules; injected rules through '
                                     '{{cap:rules-injection}} still require reading and override training defaults subject to '
                                     'project and owner precedence.',
                              'new': '',
                              'expected_count': 1}],
                'expected_loss': ['ROLE103_C2'],
                'redundant': None},
 'STATE502_C3': {'omission': [{'path': 'flow/run-state.md',
                               'old': 'After an authorized input amendment, reconcile applicable owner approval, re-establish '
                                      'the current input locks and renew verification of affected work.',
                               'new': '',
                               'expected_count': 1}],
                 'expected_loss': ['STATE502_C3'],
                 'redundant': None},
 'QA305_C4': {'omission': [{'path': 'roles/qa.md',
                            'old': 'On a repeat call within the cycle, skip re-reading rules and skills only when the ruleset '
                                   'version is unchanged; spend context on the bug report, failing output and named source '
                                   'delta.',
                            'new': '',
                            'expected_count': 1}],
              'expected_loss': ['QA305_C4'],
              'redundant': None},
 'OVERVIEW01_C1': {'omission': [{'path': 'README.md',
                                 'old': 'Intelligence selects appropriate models and reasoning through the current model policy '
                                        'and assigned role contracts.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW01_C1'],
                   'redundant': None},
 'OVERVIEW01_C2': {'omission': [{'path': 'README.md',
                                 'old': 'Inference and model execution engines are supplied by runtimes outside this repository.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW01_C2'],
                   'redundant': None},
 'OVERVIEW02_C1': {'omission': [{'path': 'README.md',
                                 'old': 'Memory/Context supplies relevant instructions, durable state and verified knowledge '
                                        'pointers to planning, execution and evaluation.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW02_C1'],
                   'redundant': None},
 'OVERVIEW02_C2': {'omission': [{'path': 'README.md',
                                 'old': 'Storage, retrieval and curation engines remain external; detailed memory and learning '
                                        'bodies remain deferred.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW02_C2'],
                   'redundant': None},
 'OVERVIEW03_C1': {'omission': [{'path': 'README.md',
                                 'old': 'Process/Orchestration assigns scoped work, preserves evidence and coordinates the '
                                        'existing owner decisions.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW03_C1'],
                   'redundant': None},
 'OVERVIEW03_C2': {'omission': [{'path': 'README.md',
                                 'old': 'Current role, phase, delegation, state, finalization and gate subjects provide the '
                                        'process interfaces.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW03_C2'],
                   'redundant': None},
 'OVERVIEW04_C1': {'omission': [{'path': 'README.md',
                                 'old': 'Goal/Specification/Vision carries original human intent into measured specifications, '
                                        'planning and result judgment.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW04_C1'],
                   'redundant': None},
 'OVERVIEW04_C2': {'omission': [{'path': 'README.md',
                                 'old': 'Current PM, reconnaissance and plan interfaces use dictated durable carriers; detailed '
                                        'specification and document bodies are current F4 drafts.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW04_C2'],
                   'redundant': None},
 'OVERVIEW05_C1': {'omission': [{'path': 'README.md',
                                 'old': 'Feedback/Evaluation checks the actual result and feeds evidenced causes into '
                                        'improvement.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW05_C1'],
                   'redundant': None},
 'OVERVIEW05_C2': {'omission': [{'path': 'README.md',
                                 'old': 'Current QA, Reviewer, scan and conform interfaces provide independent evidenced '
                                        'checking; learning bodies remain deferred.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW05_C2'],
                   'redundant': None},
 'OVERVIEW06_C1': {'omission': [{'path': 'README.md',
                                 'old': 'The delivery loop connects original intent, measured preparation, approved '
                                        'specification, assigned design and work, independent evaluation and the resulting '
                                        'evidence.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW06_C1'],
                   'redundant': None},
 'OVERVIEW06_C2': {'omission': [{'path': 'README.md',
                                 'old': 'The delivery loop retains a separate owner decision for the concrete result before '
                                        'integration.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW06_C2'],
                   'redundant': None},
 'OVERVIEW07_C1': {'omission': [{'path': 'README.md',
                                 'old': 'The methodology-learning loop connects observed failures and outcomes, causal analysis, '
                                        'source-backed candidates, independent verification and an owning decision.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW07_C1'],
                   'redundant': None},
 'OVERVIEW07_C2': {'omission': [{'path': 'README.md',
                                 'old': 'Unverified hypotheses and candidates never become policy or curated verified guidance '
                                        'automatically.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW07_C2'],
                   'redundant': None},
 'OVERVIEW07_C3': {'omission': [{'path': 'README.md',
                                 'old': 'External knowledge transfer follows its separately authorized source and curation '
                                        'contract.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW07_C3'],
                   'redundant': None},
 'OVERVIEW08_C1': {'omission': [{'path': 'README.md',
                                 'old': 'Current F2 interfaces define bounded responsibilities without implementing their '
                                        'runtime engines.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW08_C1'],
                   'redundant': None},
 'OVERVIEW08_C2': {'omission': [{'path': 'README.md',
                                 'old': 'The exoskeleton, navigation, Doxygen, LDD, tests, AX, data and lints bodies are current F3 bodies; document and greenfield/brownfield specification protocols plus shared specification validation are current F4 bodies; general decision lifecycle (DEC01) and full graph are current F4 bodies; confirmed conventions, lifecycle, batch and session procedures and five project forms are current bounded F4 drafts; eight prompting F5 and three autonomy/credentials/language policy bodies are current bounded drafts; six neutral readiness contracts for principles, glossary, Orient, preflight, run audit and conditional safety/recovery are current bounded drafts; wider F4 duties, learning F8, source completeness, operational adoption and publication remain explicit later or unresolved homes.',
                                 'new': '',
                                 'expected_count': 1},
                                {'path': 'README.md',
                                 'old': 'Current F3 bodies are [exoskeleton](code/exoskeleton.md), [navigation](code/navigation.md), [documentation](code/doxygen.md), [LDD](code/ldd.md), [tests](code/tests.md), [AX](code/ax-ui.md), [data](code/data.md) and [lints](checks/lints.md). Current F4 bodies are [document](protocols/document.md), [greenfield specification](protocols/spec-greenfield.md), [brownfield specification](protocols/spec-brownfield.md) and [shared specification validation](process/specification.md). General decision lifecycle (DEC01) at [decisions](process/decisions.md) and [full graph](protocols/graph.md) are current F4 bodies; [specification](process/specification.md) retains its validation contract. Confirmed [document conventions](documents/conventions.md), [lifecycle](process/lifecycle.md), [batches](process/batch.md) and [session](process/session.md) procedures and [five project forms](documents/templates/INDEX.md) are current bounded F4 drafts, with full editable forms and fictional filled examples. Current bounded F5 prompting bodies are [agent design](prompting/agent-prompt-design.md), [GRACE](prompting/grace.md), [brainstorm](prompting/brainstorm.md), [decomposition](prompting/decomposition.md), [prompt markup](prompting/prompt-markup.md), [solution design](prompting/solution-design.md), [superposition and collapse](prompting/superposition-collapse.md) and [verification](prompting/verification.md). Current remaining policy bodies are [autonomy](policies/autonomy.md), [credentials](policies/credentials.md) and [language](policies/language.md); [model policy](policies/models.md) retains all eighteen current norms. Current bounded readiness contracts are [principles](concepts/principles.md), [glossary](concepts/glossary.md), [Orient](checks/orient.md), [preflight](checks/preflight.md), [particular-run audit](checks/run-audit.md) and [conditional safety/recovery](process/safety.md), with complete reusable forms and fictional cases. These bounded drafts do not complete all F5 or wider F4, source completeness, learning/evaluation, adoption or publication duties. Detailed F8 learning homes are [improvement](process/learning.md) and [knowledge](process/learning.md).',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW08_C2'],
                   'redundant': [{'path': 'README.md',
                                  'old': 'The exoskeleton, navigation, Doxygen, LDD, tests, AX, data and lints bodies are current F3 bodies; document and greenfield/brownfield specification protocols plus shared specification validation are current F4 bodies; general decision lifecycle (DEC01) and full graph are current F4 bodies; confirmed conventions, lifecycle, batch and session procedures and five project forms are current bounded F4 drafts; eight prompting F5 and three autonomy/credentials/language policy bodies are current bounded drafts; six neutral readiness contracts for principles, glossary, Orient, preflight, run audit and conditional safety/recovery are current bounded drafts; wider F4 duties, learning F8, source completeness, operational adoption and publication remain explicit later or unresolved homes.',
                                  'new': '',
                                  'expected_count': 1}]},
 'OVERVIEW08_C3': {'omission': [{'path': 'README.md',
                                 'old': 'A stub or link never proves its detailed body completed.',
                                 'new': '',
                                 'expected_count': 1},
                                {'path': 'README.md',
                                 'old': 'The remaining subjects have deferred bodies; an interface or link invokes a subject without proving its body complete, including the eight completed F3 bodies.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW08_C3'],
                   'redundant': [{'path': 'README.md',
                                  'old': 'A stub or link never proves its detailed body completed.',
                                  'new': '',
                                  'expected_count': 1}]},
 'OVERVIEW09_C1': {'omission': [{'path': 'README.md',
                                 'old': 'One or multiple agents preserve existing authority, isolation and independent judgment.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW09_C1'],
                   'redundant': None},
 'OVERVIEW09_C2': {'omission': [{'path': 'README.md',
                                 'old': 'Existing safety and observability constraints apply to either topology.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW09_C2'],
                   'redundant': None},
 'OVERVIEW09_C3': {'omission': [{'path': 'README.md',
                                 'old': 'Existing time, economy and human-control constraints remain in force.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW09_C3'],
                   'redundant': None},
 'OVERVIEW10_C1': {'omission': [{'path': 'README.md',
                                 'old': 'Runtime adoption and propagated enforcement remain unproven.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW10_C1'],
                   'redundant': None},
 'OVERVIEW10_C2': {'omission': [{'path': 'README.md',
                                 'old': 'Comparable real runs, measured savings and reduced owner coordination effort remain '
                                        'unproven.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW10_C2'],
                   'redundant': None},
 'OVERVIEW10_C3': {'omission': [{'path': 'README.md',
                                 'old': 'Operational F6–F9 work and publication remain pending their own evidence and '
                                        'authorization.',
                                 'new': '',
                                 'expected_count': 1}],
                   'expected_loss': ['OVERVIEW10_C3'],
                   'redundant': None}}

CONTRADICTIONS = {'BOOT101_C1': ['BOOT101_C1'],
 'BOOT101_C2': ['BOOT101_C2'],
 'BOOT101_C3': ['BOOT101_C3', 'BOOT105_C1'],
 'BOOT101_C4': ['BOOT101_C4'],
 'BOOT102_C1': ['BOOT102_C1'],
 'BOOT102_C2': ['BOOT102_C2'],
 'BOOT102_C3': ['BOOT102_C3'],
 'BOOT103_C1': ['BOOT103_C1'],
 'BOOT103_C2': ['BOOT103_C2'],
 'BOOT104_C1': ['BOOT104_C1'],
 'BOOT104_C2': ['BOOT104_C2'],
 'BOOT104_C3': ['BOOT104_C3'],
 'BOOT105_C1': ['BOOT101_C3', 'BOOT105_C1'],
 'BOOT105_C2': ['BOOT105_C2'],
 'BOOT106_C1': ['BOOT106_C1'],
 'BOOT106_C2': ['BOOT106_C2'],
 'BOOT106_C3': ['BOOT106_C3'],
 'BOOT107_C1': ['BOOT107_C1'],
 'BOOT107_C2': ['BOOT107_C2'],
 'BOOT107_C3': ['BOOT107_C3'],
 'BOOT108_C1': ['BOOT108_C1'],
 'BOOT109_C1': ['BOOT109_C1'],
 'BOOT109_C2': ['BOOT109_C2'],
 'BOOT109_C3': ['BOOT109_C3'],
 'BOOT110_C1': ['BOOT110_C1'],
 'BOOT110_C2': ['BOOT110_C2'],
 'BOOT110_C3': ['BOOT110_C3'],
 'BOOT111_C1': ['BOOT111_C1'],
 'BOOT111_C2': ['BOOT111_C2'],
 'BOOT111_C3': ['BOOT111_C3'],
 'BOOT112_C1': ['BOOT112_C1'],
 'BOOT112_C2': ['BOOT112_C2'],
 'BOOT113_C1': ['BOOT113_C1'],
 'BOOT113_C2': ['BOOT113_C2'],
 'BOOT113_C3': ['BOOT113_C3'],
 'BOOT114_C1': ['BOOT114_C1'],
 'BOOT114_C2': ['BOOT114_C2'],
 'BOOT114_C3': ['BOOT114_C3'],
 'BOOT114_C4': ['BOOT114_C4'],
 'BOOT115_C1': ['BOOT115_C1'],
 'BOOT115_C2': ['BOOT115_C2'],
 'BOOT116_C1': ['BOOT116_C1'],
 'BOOT116_C2': ['BOOT116_C2'],
 'BOOT116_C3': ['BOOT116_C3'],
 'BOOT117_C1': ['BOOT117_C1'],
 'BOOT117_C2': ['BOOT117_C2'],
 'BOOT117_C3': ['BOOT117_C3'],
 'BOOT117_C4': ['BOOT117_C4'],
 'BOOT118_C1': ['BOOT118_C1'],
 'BOOT118_C2': ['BOOT118_C2'],
 'BOOT118_C3': ['BOOT118_C3'],
 'BOOT119_C1': ['BOOT119_C1'],
 'BOOT119_C2': ['BOOT119_C2'],
 'BOOT119_C3': ['BOOT119_C3'],
 'BOOT119_C4': ['BOOT119_C4'],
 'BOOT120_C1': ['BOOT120_C1'],
 'BOOT120_C2': ['BOOT120_C2'],
 'BOOT120_C3': ['BOOT120_C3'],
 'BOOT120_C4': ['BOOT120_C4'],
 'BOOT121_C1': ['BOOT121_C1'],
 'BOOT121_C2': ['BOOT121_C2'],
 'BOOT121_C3': ['BOOT121_C3'],
 'BOOT122_C1': ['BOOT122_C1'],
 'BOOT122_C2': ['BOOT122_C2'],
 'BOOT122_C3': ['BOOT122_C3'],
 'BOOT122_C4': ['BOOT122_C4'],
 'BOOT123_C1': ['BOOT123_C1'],
 'BOOT123_C2': ['BOOT123_C2'],
 'BOOT123_C3': ['BOOT123_C3'],
 'ROLE105_PRECEDENCE_C1': ['ROLE105_PRECEDENCE_C1'],
 'ROLE105_PRECEDENCE_C2': ['ROLE105_PRECEDENCE_C2'],
 'ROLE105_PRECEDENCE_C3': ['ROLE105_PRECEDENCE_C3'],
 'ROLE204_CONSENT_C1': ['ROLE204_CONSENT_C1'],
 'ROLE204_CONSENT_C2': ['ROLE204_CONSENT_C2'],
 'ROLE204_CONSENT_C3': ['ROLE204_CONSENT_C3'],
 'ROLE105_ASSIGNMENT_C1': ['ROLE105_ASSIGNMENT_C1'],
 'ROLE105_ASSIGNMENT_C2': ['ROLE105_ASSIGNMENT_C2'],
 'ROLE105_ASSIGNMENT_C3': ['ROLE105_ASSIGNMENT_C3'],
 'ROLE105_DEFAULT_C1': ['ROLE105_DEFAULT_C1'],
 'ROLE105_DEFAULT_C2': ['ROLE105_DEFAULT_C2'],
 'ROLE105_DEFAULT_C3': ['ROLE105_DEFAULT_C3'],
 'ROLE105_SESSION_C1': ['ROLE105_SESSION_C1'],
 'ROLE105_SESSION_C2': ['ROLE105_SESSION_C2', 'ROLE105_SESSION_C3'],
 'ROLE105_SESSION_C3': ['ROLE105_SESSION_C2', 'ROLE105_SESSION_C3'],
 'ROLE105_DEVIATION_C1': ['ROLE105_DEVIATION_C1'],
 'ROLE105_DEVIATION_C2': ['ROLE105_DEVIATION_C2'],
 'ROLE105_DEVIATION_C3': ['ROLE105_DEVIATION_C3'],
 'ROLE105_DEVIATION_C4': ['ROLE105_DEVIATION_C4'],
 'ROLE204_AUTHENTICITY_C1': ['ROLE204_AUTHENTICITY_C1'],
 'ROLE204_AUTHENTICITY_C2': ['ROLE204_AUTHENTICITY_C2'],
 'ROLE204_AUTHENTICITY_C3': ['ROLE204_AUTHENTICITY_C3'],
 'ROLE204_INTEGRATION_C1': ['ROLE204_INTEGRATION_C1'],
 'ROLE204_INTEGRATION_C2': ['ROLE204_INTEGRATION_C2'],
 'STATE501_C1': ['STATE501_C1'],
 'ROLE103_C2': ['ROLE103_C2'],
 'STATE502_C3': ['STATE502_C3'],
 'QA305_C4': ['QA305_C4'],
 'OVERVIEW01_C1': ['OVERVIEW01_C1'],
 'OVERVIEW01_C2': ['OVERVIEW01_C2'],
 'OVERVIEW02_C1': ['OVERVIEW02_C1'],
 'OVERVIEW02_C2': ['OVERVIEW02_C2'],
 'OVERVIEW03_C1': ['OVERVIEW03_C1'],
 'OVERVIEW03_C2': ['OVERVIEW03_C2'],
 'OVERVIEW04_C1': ['OVERVIEW04_C1'],
 'OVERVIEW04_C2': ['OVERVIEW04_C2'],
 'OVERVIEW05_C1': ['OVERVIEW05_C1'],
 'OVERVIEW05_C2': ['OVERVIEW05_C2'],
 'OVERVIEW06_C1': ['OVERVIEW06_C1'],
 'OVERVIEW06_C2': ['OVERVIEW06_C2'],
 'OVERVIEW07_C1': ['OVERVIEW07_C1'],
 'OVERVIEW07_C2': ['OVERVIEW07_C2'],
 'OVERVIEW07_C3': ['OVERVIEW07_C3'],
 'OVERVIEW08_C1': ['OVERVIEW08_C1'],
 'OVERVIEW08_C2': ['OVERVIEW08_C2'],
 'OVERVIEW08_C3': ['OVERVIEW08_C3'],
 'OVERVIEW09_C1': ['OVERVIEW09_C1'],
 'OVERVIEW09_C2': ['OVERVIEW09_C2'],
 'OVERVIEW09_C3': ['OVERVIEW09_C3'],
 'OVERVIEW10_C1': ['OVERVIEW10_C1'],
 'OVERVIEW10_C2': ['OVERVIEW10_C2'],
 'OVERVIEW10_C3': ['OVERVIEW10_C3']}

SCENARIOS = [{'name': 'new-absent',
  'facts': {'request': 'classify', 'code': {'executable': True}, 'product': {'new': False, 'documents': False}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'N/A', 'reasons': [], 'detail': 'existing-migration'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'new-missing',
  'facts': {'request': 'classify',
            'code': {'executable': False},
            'product': {'new': True, 'brief': '', 'purpose': 'useful', 'first_value': 'observed', 'audience': 'fixture users'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['product.brief'], 'detail': 'new-product'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'new-valid',
  'facts': {'request': 'classify',
            'code': {'executable': False},
            'product': {'new': True,
                        'brief': 'complete actual synthetic brief',
                        'purpose': 'useful',
                        'first_value': 'observed',
                        'audience': 'fixture users'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'VALID', 'reasons': [], 'detail': 'new-product'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'write-absent',
  'facts': {'request': 'write', 'requested_files': [], 'inventory': True},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'N/A', 'reasons': [], 'detail': 'read-only-inventory'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'write-ungranted',
  'facts': {'request': 'write',
            'requested_files': ['owned/result.md'],
            'inventory': True,
            'grant': None,
            'assignment': {'actor': 'fixture-preparer',
                           'role': 'preparation-writer',
                           'read_only': False,
                           'scope': ['owned/result.md']}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['consent.absent'], 'detail': 'bounded-write'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'write-valid',
  'facts': {'request': 'write',
            'requested_files': ['owned/result.md'],
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'},
            'assignment': {'actor': 'fixture-preparer',
                           'role': 'preparation-writer',
                           'read_only': False,
                           'scope': ['owned/result.md']}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'VALID', 'reasons': [], 'detail': 'bounded-write'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'write-outside',
  'facts': {'request': 'write',
            'requested_files': ['foreign/result.md'],
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'},
            'assignment': {'actor': 'fixture-preparer',
                           'role': 'preparation-writer',
                           'read_only': False,
                           'scope': ['owned/result.md']}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['consent.scope'], 'detail': 'bounded-write'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'check-absent',
  'facts': {'request': 'check', 'checker': {'required': False, 'applicable': False, 'available': False}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'N/A', 'reasons': [], 'detail': 'checker'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'check-unavailable',
  'facts': {'request': 'check', 'checker': {'required': True, 'applicable': True, 'available': False}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['checker.unavailable'], 'detail': 'checker'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'check-missing-record',
  'facts': {'request': 'check', 'checker': {'required': True, 'applicable': True, 'available': True, 'authorized': True}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['checker.measurement'], 'detail': 'checker'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'check-valid-record',
  'facts': {'request': 'check',
            'checker': {'required': True,
                        'applicable': True,
                        'available': True,
                        'authorized': True,
                        'measurement': {'exit': 0,
                                        'input_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                                        'sink': 'fixture-observation.json'}}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'VALID', 'reasons': [], 'detail': 'checker'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'settled-absent',
  'facts': {'request': 'reuse', 'dependent_action': None},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'N/A', 'reasons': [], 'detail': 'settled-permission'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'settled-missing',
  'facts': {'request': 'reuse', 'dependent_action': 'write', 'requested_files': ['owned/result.md'], 'grant': None},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['consent.absent'], 'detail': 'settled-permission'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'settled-valid',
  'facts': {'request': 'reuse',
            'dependent_action': 'write',
            'requested_files': ['owned/result.md'],
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'VALID', 'reasons': [], 'detail': 'settled-permission'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'settled-tool',
  'facts': {'request': 'reuse',
            'dependent_action': 'write',
            'requested_files': ['owned/result.md'],
            'grant': {'origin': 'tool',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['consent.origin'], 'detail': 'settled-permission'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'tool',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '66218b53cf88a17fe0660223f8f8d2ccc758675d31e560f7d9a5713d14332933',
  'existing_files': {}},
 {'name': 'settled-stale',
  'facts': {'request': 'reuse',
            'dependent_action': 'write',
            'requested_files': ['owned/result.md'],
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '0000000000000000000000000000000000000000000000000000000000000000',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['consent.artifact'], 'detail': 'settled-permission'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '0000000000000000000000000000000000000000000000000000000000000000',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '05f3e8ea4288d37bbb3f04e2213b6d3fa9a8a4456798bc21d15ff3a8618b0874',
  'existing_files': {}},
 {'name': 'channel-absent',
  'facts': {'request': 'approve', 'dependent_action': None},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'N/A', 'reasons': [], 'detail': 'approval-channel'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'channel-missing-answer',
  'facts': {'request': 'approve',
            'dependent_action': 'write',
            'requested_files': ['owned/result.md'],
            'channel': {'mechanism': 'structured', 'delivered': True},
            'grant': None},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['consent.absent'], 'detail': 'approval-channel'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'channel-structured',
  'facts': {'request': 'approve',
            'dependent_action': 'write',
            'requested_files': ['owned/result.md'],
            'channel': {'mechanism': 'structured', 'delivered': True, 'answer_mechanism': 'structured'},
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'VALID', 'reasons': [], 'detail': 'approval-channel'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'channel-chat-default',
  'facts': {'request': 'approve',
            'dependent_action': 'write',
            'requested_files': ['owned/result.md'],
            'channel': {'mechanism': 'structured', 'delivered': True, 'answer_mechanism': 'chat'},
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['channel.structured-default'], 'detail': 'approval-channel'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'channel-declared-absence',
  'facts': {'request': 'approve',
            'dependent_action': 'write',
            'requested_files': ['owned/result.md'],
            'channel': {'mechanism': None, 'declared_fallback': 'chat', 'answer_mechanism': 'chat'},
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'VALID', 'reasons': [], 'detail': 'approval-channel'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'channel-absence-no-declaration',
  'facts': {'request': 'approve',
            'dependent_action': 'write',
            'requested_files': ['owned/result.md'],
            'channel': {'mechanism': None, 'answer_mechanism': 'chat'},
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['channel.declared-fallback'], 'detail': 'approval-channel'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'channel-undelivered-no-authority',
  'facts': {'request': 'approve',
            'dependent_action': 'write',
            'requested_files': ['owned/result.md'],
            'channel': {'mechanism': 'structured', 'delivered': False, 'answer_mechanism': 'chat'},
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['channel.session-authority'], 'detail': 'approval-channel'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'channel-owning-undelivered',
  'facts': {'request': 'approve',
            'dependent_action': 'write',
            'requested_files': ['owned/result.md'],
            'channel': {'mechanism': 'structured',
                        'delivered': False,
                        'answer_mechanism': 'chat',
                        'session_record': {'origin': 'human',
                                           'owner': 'fixture-owner',
                                           'words': 'Approve this named synthetic action only.',
                                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                                           'action': 'channel-exception',
                                           'scope': ['owned/result.md'],
                                           'at': '2026-10-05T00:00:00Z',
                                           'condition': 'effective-undelivered',
                                           'governing_authorized': True}},
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'VALID', 'reasons': [], 'detail': 'approval-channel'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'},
                 'channel-session': {'origin': 'human',
                                     'owner': 'fixture-owner',
                                     'words': 'Approve this named synthetic action only.',
                                     'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                                     'action': 'channel-exception',
                                     'scope': ['owned/result.md'],
                                     'at': '2026-10-05T00:00:00Z',
                                     'condition': 'effective-undelivered',
                                     'governing_authorized': True}},
  'source_pin': 'f0f4a1c21b01dd38a7e604ee8fabf6b7e54d2771c94675ba2912d50a05270268',
  'existing_files': {}},
 {'name': 'expiry-absent',
  'facts': {'request': 'fallback', 'session_record': None},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'N/A', 'reasons': [], 'detail': 'session-expiry'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'expiry-stale',
  'facts': {'request': 'fallback',
            'structured_delivery': True,
            'session_record': {'origin': 'human',
                               'owner': 'fixture-owner',
                               'words': 'Approve this named synthetic action only.',
                               'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                               'action': 'channel-exception',
                               'scope': ['owned/result.md'],
                               'at': '2026-10-05T00:00:00Z',
                               'condition': 'effective-undelivered',
                               'governing_authorized': True}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['channel.restored'], 'detail': 'session-expiry'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'session_record': {'origin': 'human',
                                    'owner': 'fixture-owner',
                                    'words': 'Approve this named synthetic action only.',
                                    'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                                    'action': 'channel-exception',
                                    'scope': ['owned/result.md'],
                                    'at': '2026-10-05T00:00:00Z',
                                    'condition': 'effective-undelivered',
                                    'governing_authorized': True}},
  'source_pin': '2071d91852550bad8e40d39d2c2b971e79234652adf39b142b47e088aba863a9',
  'existing_files': {}},
 {'name': 'expiry-current',
  'facts': {'request': 'fallback',
            'structured_delivery': False,
            'session_record': {'origin': 'human',
                               'owner': 'fixture-owner',
                               'words': 'Approve this named synthetic action only.',
                               'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                               'action': 'channel-exception',
                               'scope': ['owned/result.md'],
                               'at': '2026-10-05T00:00:00Z',
                               'condition': 'effective-undelivered',
                               'governing_authorized': True}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'VALID', 'reasons': [], 'detail': 'session-expiry'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'session_record': {'origin': 'human',
                                    'owner': 'fixture-owner',
                                    'words': 'Approve this named synthetic action only.',
                                    'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                                    'action': 'channel-exception',
                                    'scope': ['owned/result.md'],
                                    'at': '2026-10-05T00:00:00Z',
                                    'condition': 'effective-undelivered',
                                    'governing_authorized': True}},
  'source_pin': '2071d91852550bad8e40d39d2c2b971e79234652adf39b142b47e088aba863a9',
  'existing_files': {}},
 {'name': 'expiry-no-governing-grant',
  'facts': {'request': 'fallback',
            'structured_delivery': False,
            'session_record': {'origin': 'human',
                               'owner': 'fixture-owner',
                               'words': 'Approve this named synthetic action only.',
                               'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                               'action': 'channel-exception',
                               'scope': ['owned/result.md'],
                               'at': '2026-10-05T00:00:00Z',
                               'condition': 'effective-undelivered',
                               'governing_authorized': False}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['channel.session-authority'], 'detail': 'session-expiry'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'session_record': {'origin': 'human',
                                    'owner': 'fixture-owner',
                                    'words': 'Approve this named synthetic action only.',
                                    'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                                    'action': 'channel-exception',
                                    'scope': ['owned/result.md'],
                                    'at': '2026-10-05T00:00:00Z',
                                    'condition': 'effective-undelivered',
                                    'governing_authorized': False}},
  'source_pin': '7ae8a5f8a498508eefcec4e8d7f9c38907f96588a89232f54f22fd4f6f565452',
  'existing_files': {}},
 {'name': 'result-absent',
  'facts': {'request': 'integrate', 'integration_requested': False},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'N/A', 'reasons': [], 'detail': 'concrete-result'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'result-scope-only',
  'facts': {'request': 'integrate',
            'integration_requested': True,
            'requested_files': ['owned/result.md'],
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'},
            'verdict': {'current': True, 'input_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617'},
            'probe': {'measured': True, 'input_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['consent.action'], 'detail': 'concrete-result'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'result-missing-evidence',
  'facts': {'request': 'integrate',
            'integration_requested': True,
            'requested_files': ['owned/result.md'],
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'integrate',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'},
            'verdict': {'current': True, 'input_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['result.probe'], 'detail': 'concrete-result'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'integrate',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '1c0e04b603c4fb8a64b031fb79f61714502cecf44ba70e168da8e4739ee82cc1',
  'existing_files': {}},
 {'name': 'result-valid-record',
  'facts': {'request': 'integrate',
            'integration_requested': True,
            'requested_files': ['owned/result.md'],
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'integrate',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'},
            'verdict': {'current': True, 'input_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617'},
            'probe': {'measured': True, 'input_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'VALID', 'reasons': [], 'detail': 'concrete-result'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'integrate',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '1c0e04b603c4fb8a64b031fb79f61714502cecf44ba70e168da8e4739ee82cc1',
  'existing_files': {}},
 {'name': 'code-unknown',
  'facts': {'request': 'classify', 'code': {}, 'product': {'new': True, 'documents': False}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['code.unknown'], 'detail': 'classification'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'existing_files': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356'},
 {'name': 'checker-unknown',
  'facts': {'request': 'check', 'checker': {}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['checker.requirement'], 'detail': 'checker'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'existing_files': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356'},
 {'name': 'checker-ungranted',
  'facts': {'request': 'check', 'checker': {'required': True, 'applicable': True, 'available': True, 'authorized': False}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['checker.authority'], 'detail': 'checker'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'existing_files': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356'},
 {'name': 'checker-failed',
  'facts': {'request': 'check',
            'checker': {'required': True,
                        'applicable': True,
                        'available': True,
                        'authorized': True,
                        'measurement': {'exit': 1,
                                        'input_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                                        'sink': 'fixture-observation.json'}}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['checker.failure'], 'detail': 'checker'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'existing_files': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356'},
 {'name': 'checker-stale',
  'facts': {'request': 'check',
            'checker': {'required': True,
                        'applicable': True,
                        'available': True,
                        'authorized': True,
                        'measurement': {'exit': 0,
                                        'input_sha256': '0000000000000000000000000000000000000000000000000000000000000000',
                                        'sink': 'fixture-observation.json'}}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['checker.identity'], 'detail': 'checker'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {},
  'existing_files': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356'},
 {'name': 'writer-read-only',
  'facts': {'request': 'write',
            'requested_files': ['owned/result.md'],
            'assignment': {'actor': 'fixture-preparer', 'role': 'inventory', 'read_only': True, 'scope': ['owned/result.md']},
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['assignment.writer'], 'detail': 'bounded-write'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'existing_files': {},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b'},
 {'name': 'writer-overwrite',
  'facts': {'request': 'write',
            'requested_files': ['owned/result.md'],
            'assignment': {'actor': 'fixture-preparer',
                           'role': 'preparation-writer',
                           'read_only': False,
                           'scope': ['owned/result.md']},
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['write.existing-truth'], 'detail': 'bounded-write'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'existing_files': {'owned/result.md': 'Existing synthetic truth that must survive.\n'},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b'},
 {'name': 'consent-forged-label',
  'facts': {'request': 'reuse',
            'dependent_action': 'write',
            'requested_files': ['owned/result.md'],
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['consent.provenance'], 'detail': 'settled-permission'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'tool',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'existing_files': {},
  'source_pin': '66218b53cf88a17fe0660223f8f8d2ccc758675d31e560f7d9a5713d14332933'},
 {'name': 'result-stale-probe',
  'facts': {'request': 'integrate',
            'integration_requested': True,
            'requested_files': ['owned/result.md'],
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'integrate',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'},
            'verdict': {'current': True, 'input_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617'},
            'probe': {'measured': True, 'input_sha256': '0000000000000000000000000000000000000000000000000000000000000000'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['result.identity'], 'detail': 'concrete-result'},
  'authority': 'Fixed original/source condition and independent reviewed intent; synthetic factual record, no operational '
               'effect.',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'integrate',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'existing_files': {},
  'source_pin': '1c0e04b603c4fb8a64b031fb79f61714502cecf44ba70e168da8e4739ee82cc1'},
 {'name': 'settled-valid-scope-unknown',
  'facts': {'request': 'reuse',
            'dependent_action': 'write',
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['consent.scope-unknown'], 'detail': 'settled-permission'},
  'authority': 'Source-fixed before observation: exact requested scope cannot be known from an omitted or invalid typed input; '
               'no operational consent granted',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'settled-valid-scope-non-list',
  'facts': {'request': 'reuse',
            'dependent_action': 'write',
            'requested_files': None,
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['consent.scope-unknown'], 'detail': 'settled-permission'},
  'authority': 'Source-fixed before observation: exact requested scope cannot be known from an omitted or invalid typed input; '
               'no operational consent granted',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'settled-valid-scope-non-string-path',
  'facts': {'request': 'reuse',
            'dependent_action': 'write',
            'requested_files': [1],
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['consent.scope-unknown'], 'detail': 'settled-permission'},
  'authority': 'Source-fixed before observation: exact requested scope cannot be known from an omitted or invalid typed input; '
               'no operational consent granted',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'channel-structured-scope-unknown',
  'facts': {'request': 'approve',
            'dependent_action': 'write',
            'channel': {'mechanism': 'structured', 'delivered': True, 'answer_mechanism': 'structured'},
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['consent.scope-unknown'], 'detail': 'approval-channel'},
  'authority': 'Source-fixed before observation: exact requested scope cannot be known from an omitted or invalid typed input; '
               'no operational consent granted',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'channel-structured-scope-non-list',
  'facts': {'request': 'approve',
            'dependent_action': 'write',
            'requested_files': None,
            'channel': {'mechanism': 'structured', 'delivered': True, 'answer_mechanism': 'structured'},
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['consent.scope-unknown'], 'detail': 'approval-channel'},
  'authority': 'Source-fixed before observation: exact requested scope cannot be known from an omitted or invalid typed input; '
               'no operational consent granted',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'channel-structured-scope-non-string-path',
  'facts': {'request': 'approve',
            'dependent_action': 'write',
            'requested_files': [1],
            'channel': {'mechanism': 'structured', 'delivered': True, 'answer_mechanism': 'structured'},
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['consent.scope-unknown'], 'detail': 'approval-channel'},
  'authority': 'Source-fixed before observation: exact requested scope cannot be known from an omitted or invalid typed input; '
               'no operational consent granted',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'result-valid-record-scope-unknown',
  'facts': {'request': 'integrate',
            'integration_requested': True,
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'integrate',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'},
            'verdict': {'current': True, 'input_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617'},
            'probe': {'measured': True, 'input_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['consent.scope-unknown'], 'detail': 'concrete-result'},
  'authority': 'Source-fixed before observation: exact requested scope cannot be known from an omitted or invalid typed input; '
               'no operational consent granted',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'integrate',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '1c0e04b603c4fb8a64b031fb79f61714502cecf44ba70e168da8e4739ee82cc1',
  'existing_files': {}},
 {'name': 'result-valid-record-scope-non-list',
  'facts': {'request': 'integrate',
            'integration_requested': True,
            'requested_files': None,
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'integrate',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'},
            'verdict': {'current': True, 'input_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617'},
            'probe': {'measured': True, 'input_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['consent.scope-unknown'], 'detail': 'concrete-result'},
  'authority': 'Source-fixed before observation: exact requested scope cannot be known from an omitted or invalid typed input; '
               'no operational consent granted',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'integrate',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '1c0e04b603c4fb8a64b031fb79f61714502cecf44ba70e168da8e4739ee82cc1',
  'existing_files': {}},
 {'name': 'result-valid-record-scope-non-string-path',
  'facts': {'request': 'integrate',
            'integration_requested': True,
            'requested_files': [1],
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'integrate',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'},
            'verdict': {'current': True, 'input_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617'},
            'probe': {'measured': True, 'input_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617'}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['consent.scope-unknown'], 'detail': 'concrete-result'},
  'authority': 'Source-fixed before observation: exact requested scope cannot be known from an omitted or invalid typed input; '
               'no operational consent granted',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'integrate',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '1c0e04b603c4fb8a64b031fb79f61714502cecf44ba70e168da8e4739ee82cc1',
  'existing_files': {}},
 {'name': 'expiry-session-unknown',
  'facts': {'request': 'fallback'},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['channel.session-record-unknown'], 'detail': 'session-expiry'},
  'authority': 'Source-fixed before observation: missing record key is unknown, explicit None alone is evidenced absent trigger',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'expiry-empty-invalid-record',
  'facts': {'request': 'fallback', 'session_record': {}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'REFUSE', 'reasons': ['channel.session-authority'], 'detail': 'session-expiry'},
  'authority': 'Source-fixed before observation: supplied empty record is not authentic owning-session approval and does not '
               'establish trigger absence',
  'provenance': {},
  'source_pin': 'ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356',
  'existing_files': {}},
 {'name': 'write-invalid-scope-null',
  'facts': {'request': 'write',
            'requested_files': None,
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'},
            'assignment': {'actor': 'fixture-preparer',
                           'role': 'preparation-writer',
                           'read_only': False,
                           'scope': ['owned/result.md']}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['write.request-unknown'], 'detail': 'bounded-write'},
  'authority': 'Source-fixed before observer: unknown or invalid typed write scope cannot establish explicit empty read-only '
               'absence',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'write-invalid-scope-object',
  'facts': {'request': 'write',
            'requested_files': {},
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'},
            'assignment': {'actor': 'fixture-preparer',
                           'role': 'preparation-writer',
                           'read_only': False,
                           'scope': ['owned/result.md']}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['write.request-unknown'], 'detail': 'bounded-write'},
  'authority': 'Source-fixed before observer: unknown or invalid typed write scope cannot establish explicit empty read-only '
               'absence',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'write-invalid-scope-non-string-path',
  'facts': {'request': 'write',
            'requested_files': [1],
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'},
            'assignment': {'actor': 'fixture-preparer',
                           'role': 'preparation-writer',
                           'read_only': False,
                           'scope': ['owned/result.md']}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['write.request-unknown'], 'detail': 'bounded-write'},
  'authority': 'Source-fixed before observer: unknown or invalid typed write scope cannot establish explicit empty read-only '
               'absence',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}},
 {'name': 'write-invalid-scope-empty-string',
  'facts': {'request': 'write',
            'requested_files': '',
            'grant': {'origin': 'human',
                      'owner': 'fixture-owner',
                      'words': 'Approve this named synthetic action only.',
                      'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                      'action': 'write',
                      'scope': ['owned/result.md'],
                      'at': '2026-10-05T00:00:00Z',
                      'actor': 'fixture-preparer'},
            'assignment': {'actor': 'fixture-preparer',
                           'role': 'preparation-writer',
                           'read_only': False,
                           'scope': ['owned/result.md']}},
  'artifact': 'Synthetic current reviewed artifact; no real consent or execution.\n',
  'expected': {'status': 'GAP', 'reasons': ['write.request-unknown'], 'detail': 'bounded-write'},
  'authority': 'Source-fixed before observer: unknown or invalid typed write scope cannot establish explicit empty read-only '
               'absence',
  'provenance': {'grant': {'origin': 'human',
                           'owner': 'fixture-owner',
                           'words': 'Approve this named synthetic action only.',
                           'artifact_sha256': '77a961d11f0a07379b79b3552d2c92e4b3ddc88813ef5605f5be18160a090617',
                           'action': 'write',
                           'scope': ['owned/result.md'],
                           'at': '2026-10-05T00:00:00Z',
                           'actor': 'fixture-preparer'}},
  'source_pin': '4919411a480a767ac94ff2ddbb82dbd0f92fa81005a2550157a425e77054448b',
  'existing_files': {}}]

AUDIT = [{'independentId': 'P01.1',
  'independentMeaning': 'actual accessible code and source facts',
  'parentMeaning': 'Classify from actual code, instructions, briefs and durable/Git facts.',
  'key': 'BOOT101_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P01.2',
  'independentMeaning': 'actual hidden/project agent instructions',
  'parentMeaning': 'Classify from actual code, instructions, briefs and durable/Git facts.',
  'key': 'BOOT101_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'ROLE-203 repeats applicable project instructions, but does not alone supply explicit hidden-instruction '
                    'discovery/classification.'},
 {'independentId': 'P01.3',
  'independentMeaning': 'actual brief and durable state',
  'parentMeaning': 'Classify from actual code, instructions, briefs and durable/Git facts.',
  'key': 'BOOT101_C3',
  'classification': 'compound-sharing',
  'judgment': 'BOOT-101 complete brief plus durable state shares its brief component with BOOT-105. Preserve durable state when '
              'removing brief; report both incomplete responsibilities for a real complete-brief loss.',
  'partialOverlap': None},
 {'independentId': 'P01.4',
  'independentMeaning': 'actual Git/map/access facts where applicable',
  'parentMeaning': 'Classify from actual code, instructions, briefs and durable/Git facts.',
  'key': 'BOOT101_C4',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'BOOT-116 and BOOT-119 retain Git/map components; neither alone supplies complete Git/map/access relation.'},
 {'independentId': 'P02.1',
  'independentMeaning': 'existing executable code classification',
  'parentMeaning': 'Existing executable code with missing documents remains existing-code conventions migration, never '
                   'greenfield by absence alone.',
  'key': 'BOOT102_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P02.2',
  'independentMeaning': 'missing-document absence is not greenfield evidence',
  'parentMeaning': 'Existing executable code with missing documents remains existing-code conventions migration, never '
                   'greenfield by absence alone.',
  'key': 'BOOT102_C2',
  'classification': 'complete-related-classification-alternatives',
  'judgment': 'Closed independent QA2 found mandatory existing-code migration and genuinely-new-only classification as complete '
              'supports of the missing-documents condition. Sentence-only deletion is redundant. True-loss fixture declares the '
              'related C1/C2/C3 classification loss explicitly; unrelated Bootstrap duties remain.',
  'partialOverlap': 'Complete original C1/C3 supports, not partial overlap; scoped omission retains off-trigger partials while '
                    'declaring universal C1/C2/C3 losses.'},
 {'independentId': 'P02.3',
  'independentMeaning': 'genuinely new-product trigger',
  'parentMeaning': 'Existing executable code with missing documents remains existing-code conventions migration, never '
                   'greenfield by absence alone.',
  'key': 'BOOT102_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P03.1',
  'independentMeaning': 'actual requested conventions-migration trigger',
  'parentMeaning': 'Recognize applicable new-product versus owner-requested conventions migration preparation.',
  'key': 'BOOT103_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P03.2',
  'independentMeaning': 'matching bounded preparation grant',
  'parentMeaning': 'Recognize applicable new-product versus owner-requested conventions migration preparation.',
  'key': 'BOOT103_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'BOOT-104 write authority and ROLE-201 scope support permission boundaries; requested migration matching '
                    'grant and separate files authority remain different relations.'},
 {'independentId': 'P04.1',
  'independentMeaning': 'inventory remains read-only',
  'parentMeaning': 'Read-only spine inventory reports preparation needs; it cannot perform preparation writes.',
  'key': 'BOOT104_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P04.2',
  'independentMeaning': 'preparation needs are returned to its authorized parent',
  'parentMeaning': 'Read-only spine inventory reports preparation needs; it cannot perform preparation writes.',
  'key': 'BOOT104_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P04.3',
  'independentMeaning': 'separate preparation write grant',
  'parentMeaning': 'Read-only spine inventory reports preparation needs; it cannot perform preparation writes.',
  'key': 'BOOT104_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'BOOT-103 matching grant is not alone proof of separately granted actual affected files.'},
 {'independentId': 'P05.1',
  'independentMeaning': 'complete actual original brief',
  'parentMeaning': 'Read the complete actual brief and non-negotiables before deriving preparation choices.',
  'key': 'BOOT105_C1',
  'classification': 'confirmed-full-alternative',
  'judgment': 'BOOT-101 also requires the actual complete brief. Original-versus-summary is retained by actual complete brief; '
              'delete all applicable brief supports only in owned copies. An omission of BOOT-105 alone remains supported.',
  'partialOverlap': None},
 {'independentId': 'P05.2',
  'independentMeaning': 'all original non-negotiables',
  'parentMeaning': 'Read the complete actual brief and non-negotiables before deriving preparation choices.',
  'key': 'BOOT105_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'BOOT-108 retains every constraint in output, not reading every original non-negotiable before choices.'},
 {'independentId': 'P06.1',
  'independentMeaning': 'existing settled answer/choice provenance',
  'parentMeaning': 'Reuse settled answers/choices; ask only material ungranted gaps and never reopen settled direction by '
                   'default.',
  'key': 'BOOT106_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P06.2',
  'independentMeaning': 'no redundant re-ask or silent replacement',
  'parentMeaning': 'Reuse settled answers/choices; ask only material ungranted gaps and never reopen settled direction by '
                   'default.',
  'key': 'BOOT106_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'ROLE-204 settled authorization is narrower than all product answers/choices; no silent replacement is a '
                    'separate surviving component.'},
 {'independentId': 'P06.3',
  'independentMeaning': 'only genuine material ungranted gaps stop/route',
  'parentMeaning': 'Reuse settled answers/choices; ask only material ungranted gaps and never reopen settled direction by '
                   'default.',
  'key': 'BOOT106_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'BOOT-121 stops unconfirmed material decisions; it does not alone impose only genuine material ungranted '
                    'gaps plus decision-owner routing.'},
 {'independentId': 'P07.1',
  'independentMeaning': 'product purpose/what it does',
  'parentMeaning': 'Prepare product purpose/audience and one falsifiable user-visible first value.',
  'key': 'BOOT107_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P07.2',
  'independentMeaning': 'actual intended audience',
  'parentMeaning': 'Prepare product purpose/audience and one falsifiable user-visible first value.',
  'key': 'BOOT107_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P07.3',
  'independentMeaning': 'falsifiable user-visible first value/pass condition',
  'parentMeaning': 'Prepare product purpose/audience and one falsifiable user-visible first value.',
  'key': 'BOOT107_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P08.1',
  'independentMeaning': 'every actual binding non-negotiable survives prepared output',
  'parentMeaning': 'Retain the original non-negotiables in the prepared handoff.',
  'key': 'BOOT108_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'BOOT-105 reads constraints; input reading alone does not prove complete handoff retention.'},
 {'independentId': 'P09.1',
  'independentMeaning': 'source-backed settled stack/storage/transport inputs',
  'parentMeaning': 'Provide source-backed settled stack rationale/constraints and binding version facts where relevant; do not '
                   'guess provider defaults.',
  'key': 'BOOT109_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P09.2',
  'independentMeaning': 'rationale and binding constraints',
  'parentMeaning': 'Provide source-backed settled stack rationale/constraints and binding version facts where relevant; do not '
                   'guess provider defaults.',
  'key': 'BOOT109_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P09.3',
  'independentMeaning': 'verified load-bearing versions when relevant',
  'parentMeaning': 'Provide source-backed settled stack rationale/constraints and binding version facts where relevant; do not '
                   'guess provider defaults.',
  'key': 'BOOT109_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P10.1',
  'independentMeaning': 'smallest approved included MVP',
  'parentMeaning': 'Carry the smallest approved MVP boundary, explicit exclusions and dependencies before Code.',
  'key': 'BOOT110_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'BOOT-110 third clause says boundary before Code, not smallest approved included MVP content.'},
 {'independentId': 'P10.2',
  'independentMeaning': 'deliberately deferred capabilities/dependencies',
  'parentMeaning': 'Carry the smallest approved MVP boundary, explicit exclusions and dependencies before Code.',
  'key': 'BOOT110_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P10.3',
  'independentMeaning': 'boundary settled before coding',
  'parentMeaning': 'Carry the smallest approved MVP boundary, explicit exclusions and dependencies before Code.',
  'key': 'BOOT110_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'BOOT-110 first clause gives included MVP before Code; retain no expansion during implementation as a '
                    'distinct component.'},
 {'independentId': 'P11.1',
  'independentMeaning': 'real probe transport/path/sink',
  'parentMeaning': 'Provide a real probe transport/path/sink and pass condition with actual access limitations.',
  'key': 'BOOT111_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P11.2',
  'independentMeaning': 'scenario and measurable pass condition',
  'parentMeaning': 'Provide a real probe transport/path/sink and pass condition with actual access limitations.',
  'key': 'BOOT111_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P11.3',
  'independentMeaning': 'actual access/unverified limitations',
  'parentMeaning': 'Provide a real probe transport/path/sink and pass condition with actual access limitations.',
  'key': 'BOOT111_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P12.1',
  'independentMeaning': 'measured current RECON before dependent spec',
  'parentMeaning': 'Measured current RECON precedes dependent specification and supplies actual evidence/limitations.',
  'key': 'BOOT112_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P12.2',
  'independentMeaning': 'actual path/measurements/evidence and limitations',
  'parentMeaning': 'Measured current RECON precedes dependent specification and supplies actual evidence/limitations.',
  'key': 'BOOT112_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P13.1',
  'independentMeaning': 'every actually required relevant RECON lane/quantifier',
  'parentMeaning': 'Preserve existing RECON applicability/quantifiers, verify load-bearing facts, distinguish actual input from '
                   'fixtures.',
  'key': 'BOOT113_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P13.2',
  'independentMeaning': 'verified load-bearing relevant external facts',
  'parentMeaning': 'Preserve existing RECON applicability/quantifiers, verify load-bearing facts, distinguish actual input from '
                   'fixtures.',
  'key': 'BOOT113_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P13.3',
  'independentMeaning': 'actual data versus fixture/synthetic labels',
  'parentMeaning': 'Preserve existing RECON applicability/quantifiers, verify load-bearing facts, distinguish actual input from '
                   'fixtures.',
  'key': 'BOOT113_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P14.1',
  'independentMeaning': 'only applicable missing authorized carriers',
  'parentMeaning': 'Seed only applicable missing authorized durable/spec inputs at dictated truth homes; detailed templates '
                   'remain deferred.',
  'key': 'BOOT114_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P14.2',
  'independentMeaning': 'actual dictated one-truth locations',
  'parentMeaning': 'Seed only applicable missing authorized durable/spec inputs at dictated truth homes; detailed templates '
                   'remain deferred.',
  'key': 'BOOT114_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P14.3',
  'independentMeaning': 'existing content/history is not overwritten',
  'parentMeaning': 'Seed only applicable missing authorized durable/spec inputs at dictated truth homes; detailed templates '
                   'remain deferred.',
  'key': 'BOOT114_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'BOOT-118 foreign truth and BOOT-121 content-loss stop overlap preservation, but have narrower subjects and '
                    'different actions.'},
 {'independentId': 'P14.4',
  'independentMeaning': 'detailed template/body home remains deferred',
  'parentMeaning': 'Seed only applicable missing authorized durable/spec inputs at dictated truth homes; detailed templates '
                   'remain deferred.',
  'key': 'BOOT114_C4',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P15.1',
  'independentMeaning': 'original owner intent preserved',
  'parentMeaning': 'Preserve original owner intent and initial checkpoint in the prepared inputs.',
  'key': 'BOOT115_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P15.2',
  'independentMeaning': 'actual initial checkpoint in handoff',
  'parentMeaning': 'Preserve original owner intent and initial checkpoint in the prepared inputs.',
  'key': 'BOOT115_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P16.1',
  'independentMeaning': 'actual Git state/discovered need',
  'parentMeaning': 'Git initialization and commits need matching actual authority; inner preparation gets none automatically.',
  'key': 'BOOT116_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'BOOT-101 actual Git/map facts do not alone disclose initialization need.'},
 {'independentId': 'P16.2',
  'independentMeaning': 'matching init/commit permission or explicit missing grant',
  'parentMeaning': 'Git initialization and commits need matching actual authority; inner preparation gets none automatically.',
  'key': 'BOOT116_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P16.3',
  'independentMeaning': 'inner role gets no automatic integration right',
  'parentMeaning': 'Git initialization and commits need matching actual authority; inner preparation gets none automatically.',
  'key': 'BOOT116_C3',
  'classification': 'shared-complete-invariant',
  'judgment': 'ROLE-501 and GATE-1004 independently prohibit inner commits/merges and leave integration with parent. Base '
              'applies to preparer; do not call removal of the Bootstrap repetition a lost integration boundary.',
  'partialOverlap': None},
 {'independentId': 'P17.1',
  'independentMeaning': 'actual applicable initialization/ignore hygiene prerequisite',
  'parentMeaning': 'Expose required initialization/ignore hygiene as prepared input or an explicit unresolved prerequisite; '
                   'preserve existing ignore rules and do not import detailed pattern bodies.',
  'key': 'BOOT117_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P17.2',
  'independentMeaning': 'existing ignore/exclusion rules preserved',
  'parentMeaning': 'Expose required initialization/ignore hygiene as prepared input or an explicit unresolved prerequisite; '
                   'preserve existing ignore rules and do not import detailed pattern bodies.',
  'key': 'BOOT117_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P17.3',
  'independentMeaning': 'missing hygiene returned as explicit gap/owning next step',
  'parentMeaning': 'Expose required initialization/ignore hygiene as prepared input or an explicit unresolved prerequisite; '
                   'preserve existing ignore rules and do not import detailed pattern bodies.',
  'key': 'BOOT117_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P17.4',
  'independentMeaning': 'detailed pattern/initializer body remains deferred',
  'parentMeaning': 'Expose required initialization/ignore hygiene as prepared input or an explicit unresolved prerequisite; '
                   'preserve existing ignore rules and do not import detailed pattern bodies.',
  'key': 'BOOT117_C4',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P18.1',
  'independentMeaning': 'secret values excluded from prepared artifacts',
  'parentMeaning': 'Preserve secret-safety and concurrent/foreign truth boundaries during authorized preparation.',
  'key': 'BOOT118_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P18.2',
  'independentMeaning': 'actual concurrency/single-writer constraints',
  'parentMeaning': 'Preserve secret-safety and concurrent/foreign truth boundaries during authorized preparation.',
  'key': 'BOOT118_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P18.3',
  'independentMeaning': 'foreign changes and truth preserved',
  'parentMeaning': 'Preserve secret-safety and concurrent/foreign truth boundaries during authorized preparation.',
  'key': 'BOOT118_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'BOOT-114 existing content/history is related but foreign changes/truth are distinct scope.'},
 {'independentId': 'P19.1',
  'independentMeaning': 'needed baseline/map/checker configuration',
  'parentMeaning': 'Identify actual needed baseline/map/checker configuration and project-resolved paths; detailed generation '
                   'bodies remain at their homes.',
  'key': 'BOOT119_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P19.2',
  'independentMeaning': 'actual source/map association and resolved paths',
  'parentMeaning': 'Identify actual needed baseline/map/checker configuration and project-resolved paths; detailed generation '
                   'bodies remain at their homes.',
  'key': 'BOOT119_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'BOOT-101 map facts are inventory, not source/map association and resolved paths.'},
 {'independentId': 'P19.3',
  'independentMeaning': 'missing configuration explicitly unavailable',
  'parentMeaning': 'Identify actual needed baseline/map/checker configuration and project-resolved paths; detailed generation '
                   'bodies remain at their homes.',
  'key': 'BOOT119_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P19.4',
  'independentMeaning': 'detailed generator implementation remains later',
  'parentMeaning': 'Identify actual needed baseline/map/checker configuration and project-resolved paths; detailed generation '
                   'bodies remain at their homes.',
  'key': 'BOOT119_C4',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P20.1',
  'independentMeaning': 'checker actually available/applicable/authorized',
  'parentMeaning': 'Run only an actually available authorized applicable checker and preserve its measured outcome or every '
                   'remaining rule/gap and owning action.',
  'key': 'BOOT120_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P20.2',
  'independentMeaning': 'actual measured checker output/identity',
  'parentMeaning': 'Run only an actually available authorized applicable checker and preserve its measured outcome or every '
                   'remaining rule/gap and owning action.',
  'key': 'BOOT120_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P20.3',
  'independentMeaning': 'every remaining rule/gap and owning next action',
  'parentMeaning': 'Run only an actually available authorized applicable checker and preserve its measured outcome or every '
                   'remaining rule/gap and owning action.',
  'key': 'BOOT120_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P20.4',
  'independentMeaning': 'missing/failed check never PASS',
  'parentMeaning': 'Run only an actually available authorized applicable checker and preserve its measured outcome or every '
                   'remaining rule/gap and owning action.',
  'key': 'BOOT120_C4',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'ROLE-603 fully supports unavailable-not-passed component, not the failed-check component. QA-602 is a QA '
                    'verdict rule; do not replace preparer duty with role reassignment.'},
 {'independentId': 'P21.1',
  'independentMeaning': 'actual in-scope preparation defect route',
  'parentMeaning': 'Keep in-scope preparation defects and unconfirmed/content-losing gaps separate; stop dependent destructive '
                   'or ungranted work.',
  'key': 'BOOT121_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P21.2',
  'independentMeaning': 'content-losing migration stopped',
  'parentMeaning': 'Keep in-scope preparation defects and unconfirmed/content-losing gaps separate; stop dependent destructive '
                   'or ungranted work.',
  'key': 'BOOT121_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'BOOT-114 preservation is not full stop of dependent content-losing migration.'},
 {'independentId': 'P21.3',
  'independentMeaning': 'unconfirmed material decision stopped',
  'parentMeaning': 'Keep in-scope preparation defects and unconfirmed/content-losing gaps separate; stop dependent destructive '
                   'or ungranted work.',
  'key': 'BOOT121_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'BOOT-106 genuine ungranted gap route overlaps but cannot alone preserve explicit stop of dependent work.'},
 {'independentId': 'P22.1',
  'independentMeaning': 'actual prepared artifact identities',
  'parentMeaning': 'Return actual prepared identities, outcomes, gaps/refusals, owning scope and next authorized step through '
                   'existing returns.',
  'key': 'BOOT122_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P22.2',
  'independentMeaning': 'measured outcomes and remaining gaps/refusals',
  'parentMeaning': 'Return actual prepared identities, outcomes, gaps/refusals, owning scope and next authorized step through '
                   'existing returns.',
  'key': 'BOOT122_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'BOOT-120 checker outcomes/gaps are narrower than the complete preparation return.'},
 {'independentId': 'P22.3',
  'independentMeaning': 'owning scope and next authorized action',
  'parentMeaning': 'Return actual prepared identities, outcomes, gaps/refusals, owning scope and next authorized step through '
                   'existing returns.',
  'key': 'BOOT122_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P22.4',
  'independentMeaning': 'existing return structure and separate result authority',
  'parentMeaning': 'Return actual prepared identities, outcomes, gaps/refusals, owning scope and next authorized step through '
                   'existing returns.',
  'key': 'BOOT122_C4',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'ROLE-601 supports existing return structure; GATE-101/1002 support separate result authority. Relation has '
                    'distinct return and consent components; preserve both and related refusals.'},
 {'independentId': 'P23.1',
  'independentMeaning': 'prepared settled constraints',
  'parentMeaning': 'Preparation conveys constraints and inputs; assigned technical architecture/implementation/repair remain '
                   'with their roles.',
  'key': 'BOOT123_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P23.2',
  'independentMeaning': 'technical design stays assigned Architect',
  'parentMeaning': 'Preparation conveys constraints and inputs; assigned technical architecture/implementation/repair remain '
                   'with their roles.',
  'key': 'BOOT123_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'P23.3',
  'independentMeaning': 'Code/Debug repairs stay assigned roles',
  'parentMeaning': 'Preparation conveys constraints and inputs; assigned technical architecture/implementation/repair remain '
                   'with their roles.',
  'key': 'BOOT123_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'A01.1',
  'independentMeaning': 'actual owner/project/runtime precedence',
  'parentMeaning': 'Resolve actual owner/project/runtime precedence, permission boundaries and capability mechanisms.',
  'key': 'ROLE105_PRECEDENCE_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'ROLE-103 owner/project precedence alone does not supply complete host/runtime governing resolution.'},
 {'independentId': 'A01.2',
  'independentMeaning': 'read resolved commands/permission/capability contract',
  'parentMeaning': 'Resolve actual owner/project/runtime precedence, permission boundaries and capability mechanisms.',
  'key': 'ROLE105_PRECEDENCE_C2',
  'classification': 'confirmed-full-alternative',
  'judgment': 'Original ROLE-105 first sentence already reads resolved commands, permissions and capabilities. Keep its '
              'existing-authorization read while removing those three components and the appended equivalent.',
  'partialOverlap': None},
 {'independentId': 'A01.3',
  'independentMeaning': 'applicable stricter project rule preserved',
  'parentMeaning': 'Resolve actual owner/project/runtime precedence, permission boundaries and capability mechanisms.',
  'key': 'ROLE105_PRECEDENCE_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'ROLE-103/401 project precedence supports target-specific rule priority; preserve applicable stricter '
                    'project rule rather than merely any instruction.'},
 {'independentId': 'A02.1',
  'independentMeaning': 'authentic owning decision/artifact provenance',
  'parentMeaning': 'Preserve exact authentic owning consent, settled action/scope and artifact provenance; no re-ask of matching '
                   'settled action.',
  'key': 'ROLE204_CONSENT_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'GATE-504 contains gate approval provenance; generic settled owner decision provenance is broader.'},
 {'independentId': 'A02.2',
  'independentMeaning': 'exact settled action and bounded scope',
  'parentMeaning': 'Preserve exact authentic owning consent, settled action/scope and artifact provenance; no re-ask of matching '
                   'settled action.',
  'key': 'ROLE204_CONSENT_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'ROLE-201 scope and GATE-303 matching approval are related, but actual action and consent binding remain '
                    'explicit.'},
 {'independentId': 'A02.3',
  'independentMeaning': 'matching existing consent preserved without re-ask',
  'parentMeaning': 'Preserve exact authentic owning consent, settled action/scope and artifact provenance; no re-ask of matching '
                   'settled action.',
  'key': 'ROLE204_CONSENT_C3',
  'classification': 'confirmed-full-alternative',
  'judgment': 'Original ROLE-204 first sentence already preserves existing authorization rather than reasking settled actions. '
              'Keep documented boundaries, existing authorization and no scope expansion while removing both no-reask '
              'expressions.',
  'partialOverlap': None},
 {'independentId': 'A03.1',
  'independentMeaning': 'exact binding to every affected assignment',
  'parentMeaning': 'Carry current binding and constraints to every affected assignment through existing context.',
  'key': 'ROLE105_ASSIGNMENT_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'DELEG-103 supplies affected-role negative constraints, but not by itself complete current binding to every '
                    'affected assignment.'},
 {'independentId': 'A03.2',
  'independentMeaning': 'owning consent/scope carried',
  'parentMeaning': 'Carry current binding and constraints to every affected assignment through existing context.',
  'key': 'ROLE105_ASSIGNMENT_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'DELEG-101 and ROLE-202 scopes do not alone carry owning consent.'},
 {'independentId': 'A03.3',
  'independentMeaning': 'negative constraints and effective channel condition carried',
  'parentMeaning': 'Carry current binding and constraints to every affected assignment through existing context.',
  'key': 'ROLE105_ASSIGNMENT_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'DELEG-103 supplies negative constraints, not by itself effective channel condition.'},
 {'independentId': 'A04.1',
  'independentMeaning': 'structured default when its governing condition holds',
  'parentMeaning': 'Retain structured default and the declared conditional absent-mechanism fallback.',
  'key': 'ROLE105_DEFAULT_C1',
  'classification': 'shared-condition-qualified-invariant',
  'judgment': 'GATE-201/202 declare structured default. Evaluate them with actual owner/project/runtime binding from ROLE-105, '
              'not as universal chat prohibition and not as new permission.',
  'partialOverlap': None},
 {'independentId': 'A04.2',
  'independentMeaning': 'declared absent-mechanism fallback only under its real condition',
  'parentMeaning': 'Retain structured default and the declared conditional absent-mechanism fallback.',
  'key': 'ROLE105_DEFAULT_C2',
  'classification': 'shared-condition-qualified-invariant',
  'judgment': 'GATE-203 supplies absent-mechanism declared fallback; preserve its real absence and approval context. A MAY is a '
              'bounded permission, not a mandatory positive outcome.',
  'partialOverlap': None},
 {'independentId': 'A04.3',
  'independentMeaning': 'complete authentic approval evidence',
  'parentMeaning': 'Retain structured default and the declared conditional absent-mechanism fallback.',
  'key': 'ROLE105_DEFAULT_C3',
  'classification': 'shared-complete-evidence',
  'judgment': 'GATE-203 and GATE-504 jointly retain words, artifact identity, scope, owner and time. True approval-evidence loss '
              'must remove all applicable evidence supports in private copies, not protected originals.',
  'partialOverlap': None},
 {'independentId': 'A05.1',
  'independentMeaning': 'actual owning session effective-undelivered condition',
  'parentMeaning': 'Effective-undelivered session fallback is conditional and expires when actual delivery returns.',
  'key': 'ROLE105_SESSION_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'ROLE-105 final owning permission sentence is an indispensable qualifier; undelivered call alone grants no '
                    'exception.'},
 {'independentId': 'A05.2',
  'independentMeaning': 'fallback only during that condition',
  'parentMeaning': 'Effective-undelivered session fallback is conditional and expires when actual delivery returns.',
  'key': 'ROLE105_SESSION_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'A05.3 supplies restored-delivery expiry, but only-while recorded condition covers any cessation of '
                    'condition and authentic record applicability.'},
 {'independentId': 'A05.3',
  'independentMeaning': 'restored delivery expires the fallback',
  'parentMeaning': 'Effective-undelivered session fallback is conditional and expires when actual delivery returns.',
  'key': 'ROLE105_SESSION_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'A05.2 only-while entails cessation; explicit restored-delivery handling is still required in the '
                    'conditional observation. Keep separate recorded-condition and restoration facts.'},
 {'independentId': 'A06.1',
  'independentMeaning': 'existing actual section anchor',
  'parentMeaning': 'Applicable pointwise adoption deviations use the existing anchored reason/owner/end-condition contract.',
  'key': 'ROLE105_DEVIATION_C1',
  'classification': 'shared-adoption-contract-component',
  'judgment': 'runtime/adapters.md actual override anchor and table preserve anchor existence. This is a cited FMT adapter '
              'contract; it is support only for actual pointwise adoption, never a generic channel override.',
  'partialOverlap': None},
 {'independentId': 'A06.2',
  'independentMeaning': 'reason and owning authority',
  'parentMeaning': 'Applicable pointwise adoption deviations use the existing anchored reason/owner/end-condition contract.',
  'key': 'ROLE105_DEVIATION_C2',
  'classification': 'shared-adoption-contract-component',
  'judgment': 'runtime/adapters.md actual override description/table preserves reason and owning authority. It does not invent '
              'an owning-session grant.',
  'partialOverlap': None},
 {'independentId': 'A06.3',
  'independentMeaning': 'actual applicable until/trigger condition',
  'parentMeaning': 'Applicable pointwise adoption deviations use the existing anchored reason/owner/end-condition contract.',
  'key': 'ROLE105_DEVIATION_C3',
  'classification': 'shared-adoption-contract-component',
  'judgment': 'runtime/adapters.md description and until/trigger fields preserve actual expiry condition for pointwise adoption.',
  'partialOverlap': None},
 {'independentId': 'A06.4',
  'independentMeaning': 'generic cap fallback is no policy override',
  'parentMeaning': 'Applicable pointwise adoption deviations use the existing anchored reason/owner/end-condition contract.',
  'key': 'ROLE105_DEVIATION_C4',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'Declared capability fallback in adapters is not policy override; retain explicit semantic-boundary '
                    'prohibition rather than mere field presence.'},
 {'independentId': 'A07.1',
  'independentMeaning': 'authentic exact human action/artifact/scope provenance',
  'parentMeaning': 'Worker/tool results, silence/default/ambiguous words authenticate no human consent.',
  'key': 'ROLE204_AUTHENTICITY_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'A02.1/A02.2 and gate evidence support provenance/scope parts, but exact human authenticity is a complete '
                    'additional relation.'},
 {'independentId': 'A07.2',
  'independentMeaning': 'worker/tool data is not consent',
  'parentMeaning': 'Worker/tool results, silence/default/ambiguous words authenticate no human consent.',
  'key': 'ROLE204_AUTHENTICITY_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'GATE-205/DELEG-403 forbid worker/tool gate approval; gate-specific subset is not a universal substitute for '
                    'every human consent scope.'},
 {'independentId': 'A07.3',
  'independentMeaning': 'silence/default/ambiguity is not consent',
  'parentMeaning': 'Worker/tool results, silence/default/ambiguous words authenticate no human consent.',
  'key': 'ROLE204_AUTHENTICITY_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'GATE-205 silence/default and GATE-203 ambiguity are gate-specific subsets; neither alone supports the '
                    'complete all-consent relation.'},
 {'independentId': 'A08.1',
  'independentMeaning': 'scope/run permission retained within its action',
  'parentMeaning': 'Prior scope/run SUCCESS never grants concrete current-result integration approval.',
  'key': 'ROLE204_INTEGRATION_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'Original ROLE-204 boundaries/no expansion, ROLE-201 and GATE-303 support scope; action-specific '
                    'preservation of scope/run permission remains explicit.'},
 {'independentId': 'A08.2',
  'independentMeaning': 'concrete current-result integration decision separate',
  'parentMeaning': 'Prior scope/run SUCCESS never grants concrete current-result integration approval.',
  'key': 'ROLE204_INTEGRATION_C2',
  'classification': 'shared-complete-invariant',
  'judgment': 'GATE-101/408/1002, STATE-703 and QA-607 independently separate concrete result integration from scope/run/QA '
              'success. Scope-only consent is never sufficient for the concrete result.',
  'partialOverlap': None},
 {'independentId': 'A09.1',
  'independentMeaning': 'actual required rules identity despite same version',
  'parentMeaning': 'Unchanged version alone cannot prove unchanged required rules; shared MUST/current adoption defeats stale '
                   'repeat reuse.',
  'key': 'STATE501_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'STATE-103 locks/reconciles approval but current changed-input invalidation is not merely a lock existence.'},
 {'independentId': 'A09.2',
  'independentMeaning': 'complete current content read/adopted',
  'parentMeaning': 'Unchanged version alone cannot prove unchanged required rules; shared MUST/current adoption defeats stale '
                   'repeat reuse.',
  'key': 'ROLE103_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'ROLE-102/QA-304 supply role/constitution reads; full current adopted rules and code duties require their '
                    'actual applicability, not a role guess.'},
 {'independentId': 'A09.3',
  'independentMeaning': 'changed required evidence renewed',
  'parentMeaning': 'Unchanged version alone cannot prove unchanged required rules; shared MUST/current adoption defeats stale '
                   'repeat reuse.',
  'key': 'STATE502_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'STATE-103/503/504 overlap approval/current verification; current amendment locks and affected renewal '
                    'remain a full relation.'},
 {'independentId': 'A09.4',
  'independentMeaning': 'unchanged complete adopted rules may avoid duplicate fetching',
  'parentMeaning': 'Unchanged version alone cannot prove unchanged required rules; shared MUST/current adoption defeats stale '
                   'repeat reuse.',
  'key': 'QA305_C4',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'QA-305 is SHOULD conditional reread economy, not an exemption from actual current full rule reading or '
                    'same-version changed bytes.'},
 {'independentId': 'R01.1',
  'independentMeaning': 'Intelligence responsibility and actual interface',
  'parentMeaning': 'Intelligence responsibility is visible with actual current model/reasoning interfaces and truthful runtime '
                   'engine boundary.',
  'key': 'OVERVIEW01_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'R01.2',
  'independentMeaning': 'external inference/model engine boundary',
  'parentMeaning': 'Intelligence responsibility is visible with actual current model/reasoning interfaces and truthful runtime '
                   'engine boundary.',
  'key': 'OVERVIEW01_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'Current F2 non-engine boundary is narrower than explicit external inference/model engine placement.'},
 {'independentId': 'R02.1',
  'independentMeaning': 'Memory/Context responsibility and actual/deferred interface',
  'parentMeaning': 'Memory/Context responsibility is visible and distinguishes supplied context from storage/retrieval/curation '
                   'engines.',
  'key': 'OVERVIEW02_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'R02.2',
  'independentMeaning': 'external storage/retrieval/curation engines',
  'parentMeaning': 'Memory/Context responsibility is visible and distinguishes supplied context from storage/retrieval/curation '
                   'engines.',
  'key': 'OVERVIEW02_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'F8 learning deferred homes are narrower than external storage/retrieval/curation engines.'},
 {'independentId': 'R03.1',
  'independentMeaning': 'Process/Orchestration responsibility',
  'parentMeaning': 'Process/Orchestration responsibility points to actual role/phase/delegation/gate interfaces.',
  'key': 'OVERVIEW03_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'R03.2',
  'independentMeaning': 'actual current role/phase/delegation/gate interfaces',
  'parentMeaning': 'Process/Orchestration responsibility points to actual role/phase/delegation/gate interfaces.',
  'key': 'OVERVIEW03_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'R04.1',
  'independentMeaning': 'Goal/Specification/Vision responsibility',
  'parentMeaning': 'Goal/Specification/Vision responsibility connects original intent to measured planning and current/deferred '
                   'carriers.',
  'key': 'OVERVIEW04_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'R04.2',
  'independentMeaning': 'original intent and current/deferred planning carriers',
  'parentMeaning': 'Goal/Specification/Vision responsibility connects original intent to measured planning and current/deferred '
                   'carriers.',
  'key': 'OVERVIEW04_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'Later F4 homes support deferral but not all PM/recon/plan dictated-carrier allocation.'},
 {'independentId': 'R05.1',
  'independentMeaning': 'Feedback/Evaluation responsibility',
  'parentMeaning': 'Feedback/Evaluation responsibility locates checks, independent review and causal improvement.',
  'key': 'OVERVIEW05_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'R05.2',
  'independentMeaning': 'independent evidenced current checking and causal improvement',
  'parentMeaning': 'Feedback/Evaluation responsibility locates checks, independent review and causal improvement.',
  'key': 'OVERVIEW05_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'Other role/gate independent review duties do not replace overview allocation to all '
                    'QA/Reviewer/scan/conform interfaces.'},
 {'independentId': 'R06.1',
  'independentMeaning': 'delivery loop producer/consumer links',
  'parentMeaning': 'Delivery loop follows original intent through actual work/evaluation and separate owner result decision.',
  'key': 'OVERVIEW06_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'R06.2',
  'independentMeaning': 'separate concrete owner result decision',
  'parentMeaning': 'Delivery loop follows original intent through actual work/evaluation and separate owner result decision.',
  'key': 'OVERVIEW06_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'Protected result-gate duties retain policy, but this fixed overview relation must also allocate the result '
                    'decision within its delivery loop.'},
 {'independentId': 'R07.1',
  'independentMeaning': 'learning loop evidence/candidate/verification/owning decision',
  'parentMeaning': 'Methodology-learning loop preserves verified candidate-to-owning-decision feedback; it is not automatic '
                   'external learning.',
  'key': 'OVERVIEW07_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'R07.2',
  'independentMeaning': 'no automatic unverified policy/curation',
  'parentMeaning': 'Methodology-learning loop preserves verified candidate-to-owning-decision feedback; it is not automatic '
                   'external learning.',
  'key': 'OVERVIEW07_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'Owning decision in learning loop supports nonautomatic advancement but not all unverified hypothesis and '
                    'curation prohibitions.'},
 {'independentId': 'R07.3',
  'independentMeaning': 'external transfer limits',
  'parentMeaning': 'Methodology-learning loop preserves verified candidate-to-owning-decision feedback; it is not automatic '
                   'external learning.',
  'key': 'OVERVIEW07_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'R08.1',
  'independentMeaning': 'actual current F2 interfaces',
  'parentMeaning': 'Current F2 interfaces, completed F3/F4 and bounded prompting/policy bodies with wider F4/F5/F8 homes are distinct; a stub/link does not finish a '
                   'body.',
  'key': 'OVERVIEW08_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'External inference engines and adapter operation are narrower than all current F2 bounded '
                    'responsibilities.'},
 {'independentId': 'R08.2',
  'independentMeaning': 'specific detailed F3/F4/F5/F8 homes',
  'parentMeaning': 'Current F2 interfaces, completed F3/F4 and bounded prompting/policy bodies with wider F4/F5/F8 homes are distinct; a stub/link does not finish a '
                   'body.',
  'key': 'OVERVIEW08_C2',
  'classification': 'overview-full-alternative',
  'judgment': 'README short allocation and full linked paragraph each retain exactly eight current F3 bodies, current F4 decision/document/graph bodies, confirmed conventions/lifecycle/batch/session procedures and five forms, eight prompting and three remaining policy bodies, six bounded readiness contracts, and remaining wider F4/F5/F8 homes. Removing one complete allocation alternative is redundant, not real loss.',
  'partialOverlap': None},
 {'independentId': 'R08.3',
  'independentMeaning': 'stub/link never claims completed body',
  'parentMeaning': 'Current F2 interfaces, completed F3/F4 and bounded prompting/policy bodies with wider F4/F5/F8 homes are distinct; a stub/link does not finish a '
                   'body.',
  'key': 'OVERVIEW08_C3',
  'classification': 'overview-full-alternative',
  'judgment': 'README later paragraph qualifies remaining deferred subjects and says interface/link invocation never proves a body complete, including current core. This complete non-waiver alternative survives removal of the short stub/link disclaimer.',
  'partialOverlap': None},
 {'independentId': 'R09.1',
  'independentMeaning': 'authority and isolation/independence across topology',
  'parentMeaning': 'One or multiple agents retain existing '
                   'authority/isolation/independence/safety/observability/time/economy/human control.',
  'key': 'OVERVIEW09_C1',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'DELEG-301/302 preserve worker independence/authority, but overview must allocate them across one/multiple '
                    'topology.'},
 {'independentId': 'R09.2',
  'independentMeaning': 'safety/observability constraints',
  'parentMeaning': 'One or multiple agents retain existing '
                   'authority/isolation/independence/safety/observability/time/economy/human control.',
  'key': 'OVERVIEW09_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'Existing safety/observability links do not alone allocate either-topology responsibility.'},
 {'independentId': 'R09.3',
  'independentMeaning': 'time/economy/human control remains existing',
  'parentMeaning': 'One or multiple agents retain existing '
                   'authority/isolation/independence/safety/observability/time/economy/human control.',
  'key': 'OVERVIEW09_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'Existing economy or gate subjects alone do not allocate all time/economy/human control across topologies.'},
 {'independentId': 'R10.1',
  'independentMeaning': 'adoption/propagation unproven',
  'parentMeaning': 'Adoption, propagation, comparable real runs and publication remain explicitly unproven F6–F9 work.',
  'key': 'OVERVIEW10_C1',
  'classification': 'overview-support-requiring-propagation-component',
  'judgment': 'README release paragraph already says no assertion a particular harness enforces it; adoption section also '
              'distinguishes example interpretation from live adoption. Preserve bounded no-adoption claims; do not treat an '
              'enforcement disclaimer as measured propagation evidence.',
  'partialOverlap': None},
 {'independentId': 'R10.2',
  'independentMeaning': 'comparable real runs/learning savings unproven',
  'parentMeaning': 'Adoption, propagation, comparable real runs and publication remain explicitly unproven F6–F9 work.',
  'key': 'OVERVIEW10_C2',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': None},
 {'independentId': 'R10.3',
  'independentMeaning': 'publication and F6-F9 work pending',
  'parentMeaning': 'Adoption, propagation, comparable real runs and publication remain explicitly unproven F6–F9 work.',
  'key': 'OVERVIEW10_C3',
  'classification': 'no-complete-alternative-identified-in-bounded-read',
  'judgment': 'Full independent meaning and actual declared responsibility were reviewed against the eight complete surfaces. No '
              'additional complete equivalent was identified; this is bounded model/subagent design judgment, not whole-language '
              'semantic proof.',
  'partialOverlap': 'F3-F8 later homes are not alone all operational F6-F9 and publication evidence/authorization status.'}]

SURFACES = ['process/bootstrap.md',
 'roles/_base.md',
 'README.md',
 'flow/run-state.md',
 'roles/qa.md',
 'flow/delegation.md',
 'process/gates.md',
 'runtime/adapters.md']

PROTECTED_PINS = {'roles/qa.md': 'baeb5f36875dbfee733d9114de2d37a2cfa6b7888d0722395dadf52532f2ba53',
 'flow/delegation.md': 'b45f4a9311ffdfd8ca8d288170b54fffe452289c48af49f62a6cb50def92d303',
 'flow/run-state.md': '1da78a3a86356dcb8a6cdd5d652aee0bc639ab626368af9bbffce31f67ef984e',
 'process/gates.md': 'e52f0929630fc2b3d9a7305da0004d0ab4f9a6515b328ed1115a6cd79c6d56c4',
 'examples/flow-contract/cases.json': 'ee2953f00f92c4d9ba3daa3a5b9bb7b45332c467d7f6ae15bfe76a31250c4f16',
 'runtime/adapter.schema.json': 'd8d43005994e39a8ab3d0b5eb1dca3127bfb6fab52bdca79ca5d7d14b33b594d',
 'runtime/capabilities.md': '0cc720e09e203d0def54ecca75b62dbf712269e7d1a8b4d88634f5feff9d4654',
 'runtime/parameters.md': 'c9435181357b49c66c62c110502a6bc1574a385f34cc3fae187bce0463fdcffb',
 'Doxyfile': 'b7b64dce222fadbe50f47041c88f0adde096421c11b1f00c55cce24689747c18',
 # M23 (2026-10-11): re-pinned after the owner's MIT licence decision replaced the no-licence assertion in this file.
 'tests/test_code_layer.py': 'df7f10c1a1f3086c5b0241d903e6a3d0250584e0f353138af1c51cb80de3e70f',
 'tests/conftest.py': '54887bf92dacf9db3493e3f0325fc2582535f3a4c11fecf092be2b54f90d039b',
 'pytest.ini': '8d2ad3ad41dfc408a0124159416089ba0b2643cac00d25015cbacef86302ad2d'}

BASE_OTHER_SHA = '1729407e16c6ce0e1cd92d228c22f319927ef778f984b9c79aa0dd2192b8e09d'

NORM_LINE = re.compile(r"^- \*\*([A-Z]+-\d+)\*\* (MUST NOT|MUST|SHOULD NOT|SHOULD|MAY): (.*)$")


# region FUNC__read_surfaces [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Read complete actual source surfaces with their physical hashes and numeric modes.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def _read_surfaces(repo_root):
    print("[IMP:4][_read_surfaces][ENTRY] complete public contract read")
    surfaces = {}
    identities = {}
    try:
        for relative in SURFACES:
            path = repo_root / relative
            data = path.read_bytes()
            surfaces[relative] = data.decode("utf-8")
            identities[relative] = {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data), "mode": stat.S_IMODE(path.stat().st_mode)}
            print("[IMP:8][_read_surfaces][READ] public=%s bytes=%d sha=%s mode=%d" % (relative, len(data), identities[relative]["sha256"], identities[relative]["mode"]))
    except (OSError, UnicodeError) as error:
        print("[IMP:10][_read_surfaces][ERROR] complete read refused type=%s" % type(error).__name__)
        raise
    print("[IMP:9][_read_surfaces][SUCCESS] complete surfaces=%d" % len(surfaces))
    return surfaces, identities
# endregion FUNC__read_surfaces


# region FUNC_test_f2_structure_and_public_links [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Check actual Bootstrap cards anchors populations and overview links.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def test_f2_structure_and_public_links(repo_root):
    print("[IMP:4][test_f2_structure_and_public_links][ENTRY] current public structure")
    surfaces, identities = _read_surfaces(repo_root)
    card = parse_markdown("process/bootstrap.md", surfaces["process/bootstrap.md"])
    print("[IMP:9][test_f2_structure_and_public_links][RESULT] Bootstrap norms=%d" % len(card.norms))
    assert card.card.get("id") == "process.bootstrap" and card.card.get("status") == "draft"
    assert len(card.norms) == 23
    assert len({norm[0] for norm in card.norms}) == 23
    for anchor in ["classification", "measured-inputs", "prepared-output", "role-boundary"]:
        assert "<!-- anchor: process.bootstrap.%s -->" % anchor in surfaces["process/bootstrap.md"]
    tree = load_neutral_tree(repo_root)
    assert len(tree) == 71
    for public in ["process/bootstrap.md", "README.md"]:
        for target in re.findall(r"\]\(([^)]+)\)", surfaces[public]):
            if not target.startswith(("http:", "https:", "#")):
                assert ((repo_root / public).parent / target.split("#")[0]).resolve().is_file()
    print("[IMP:9][test_f2_structure_and_public_links][SUCCESS] actual links resolve")
# endregion FUNC_test_f2_structure_and_public_links


# region FUNC_test_f2_complete_current_interfaces [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Require complete source-fixed current responsibility supports without live contrary grants.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def test_f2_complete_current_interfaces(repo_root):
    print("[IMP:4][test_f2_complete_current_interfaces][ENTRY] fixed complete contract positive")
    surfaces, identities = _read_surfaces(repo_root)
    assert _contract_failures(surfaces) == []
    assert len(CONDITIONS) == len({row["key"] for row in CONDITIONS})
    assert all(row["required_clause"] != row["contrary_grant"] for row in CONDITIONS)
    print("[IMP:9][test_f2_complete_current_interfaces][SUCCESS] complete bounded positive")
# endregion FUNC_test_f2_complete_current_interfaces


# region FUNC_test_f2_unchanged_contract_boundaries [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Retain protected bytes and same-version current rules beyond the optional QA repeat economy.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def test_f2_unchanged_contract_boundaries(repo_root):
    print("[IMP:4][test_f2_unchanged_contract_boundaries][ENTRY] current protected producer and consumer bytes")
    surfaces, identities = _read_surfaces(repo_root)
    for relative, expected in PROTECTED_PINS.items():
        actual = hashlib.sha256((repo_root / relative).read_bytes()).hexdigest()
        print("[IMP:8][test_f2_unchanged_contract_boundaries][READ] public=%s sha=%s" % (relative, actual))
        assert actual == expected
    masked = "\n".join(line for line in surfaces["roles/_base.md"].splitlines() if not line.startswith(("- **ROLE-105**", "- **ROLE-204**")))
    assert hashlib.sha256(masked.encode("utf-8")).hexdigest() == BASE_OTHER_SHA
    # The complete repeat SHOULD is necessary but does not waive the stronger shared/current MUST.
    current_keys = [row["key"] for row in CONDITIONS if row["norm"] in {"ROLE-103", "STATE-501", "STATE-502", "QA-305"}]
    assert len(current_keys) == 4
    assert _contract_failures(surfaces) == []
    print("[IMP:9][test_f2_unchanged_contract_boundaries][SUCCESS] strict defaults cases and current identity context preserved")
# endregion FUNC_test_f2_unchanged_contract_boundaries


# region FUNC__parse_live [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Separate actual live mandatory clauses from fences and reject ambiguous duplicate norms.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def _parse_live(surfaces):
    print("[IMP:4][_parse_live][ENTRY] complete live clauses excluding examples")
    live = {}
    norms = {}
    for relative, text in surfaces.items():
        lines = []
        fence = ""
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.startswith(("```", "~~~")):
                marker = stripped[:3]
                if not fence:
                    fence = marker
                elif marker == fence:
                    fence = ""
                continue
            if not fence:
                lines.append(line)
        if fence:
            print("[IMP:10][_parse_live][ERROR] unclosed fence public=%s" % relative)
            raise ValueError("Unclosed fixture fence")
        live[relative] = "\n".join(lines)
        norms[relative] = {}
        for line in lines:
            match = NORM_LINE.fullmatch(line)
            if match:
                key, level, clause = match.groups()
                if key in norms[relative]:
                    print("[IMP:10][_parse_live][ERROR] duplicate norm=%s" % key)
                    raise ValueError("Duplicate fixture norm")
                norms[relative][key] = (level, clause)
    print("[IMP:9][_parse_live][SUCCESS] full live surfaces=%d" % len(live))
    return live, norms
# endregion FUNC__parse_live


# region FUNC__support_matches [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Check one reviewed support at its actual path norm level and live clause.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def _support_matches(candidate, live, norms, ignore_level=False):
    print("[IMP:4][_support_matches][ENTRY] public=%s norm=%s" % (candidate["path"], candidate["norm"]))
    if candidate["norm"]:
        level, text = norms[candidate["path"]].get(candidate["norm"], ("", ""))
        matched = candidate["clause"] in text and (ignore_level or level == candidate["level"])
    else:
        matched = candidate["clause"] in live[candidate["path"]]
    print("[IMP:8][_support_matches][RESULT] matched=%s level_checked=%s" % (matched, not ignore_level))
    return matched
# endregion FUNC__support_matches


# region FUNC__contract_failures [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Derive exact complete responsibility failures across reviewed equivalent supports and force-qualified components.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def _contract_failures(surfaces):
    print("[IMP:4][_contract_failures][ENTRY] independently fixed responsibilities and reviewed supports")
    live, norms = _parse_live(surfaces)
    contradicted = set()
    for source in CONDITIONS:
        if source["contrary_grant"] in live[source["path"]]:
            contradicted.update(CONTRADICTIONS[source["key"]])
    failures = []
    for condition in CONDITIONS:
        components = SUPPORTS[condition["key"]]
        strict = all(any(_support_matches(c, live, norms) for c in alternatives) for alternatives in components)
        actual = ""
        if condition["key"] in contradicted:
            actual = "contradicted"
        elif not strict:
            words = all(any(_support_matches(c, live, norms, True) for c in alternatives) for alternatives in components)
            actual = "weakened" if words else "missing"
        if actual:
            failures.append({"key": condition["key"], "refusal": condition["refusal"], "reason": condition["reason"], "actual": actual})
            print("[IMP:9][_contract_failures][REFUSAL] key=%s cause=%s" % (condition["key"], actual))
    print("[IMP:9][_contract_failures][RESULT] conditions=%d refusals=%d" % (len(CONDITIONS), len(failures)))
    return failures
# endregion FUNC__contract_failures


# region FUNC__apply_recipe [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Apply independently fixed full component-loss spans to owned copies and count each real trigger.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def _apply_recipe(surfaces, recipe):
    print("[IMP:4][_apply_recipe][ENTRY] reviewed loss spans=%d" % len(recipe))
    result = json.loads(json.dumps(surfaces))
    triggers = []
    for mutation in recipe:
        path = mutation["path"]
        count = result[path].count(mutation["old"])
        print("[IMP:8][_apply_recipe][READ] public=%s actual_count=%d" % (path, count))
        assert count == mutation["expected_count"], "Reviewed mutation support changed"
        result[path] = result[path].replace(mutation["old"], mutation["new"], count)
        triggers.append({"path": path, "old_sha256": hashlib.sha256(mutation["old"].encode()).hexdigest(), "new_sha256": hashlib.sha256(mutation["new"].encode()).hexdigest(), "actual_count": count})
    print("[IMP:9][_apply_recipe][SUCCESS] owned copy changes=%d" % len(triggers))
    return result, triggers
# endregion FUNC__apply_recipe


# region FUNC__expected_refusals [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Read fixed intended reason sets without consulting detector outputs.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def _expected_refusals(keys, actual):
    print("[IMP:4][_expected_refusals][ENTRY] fixed independent reason set=%d" % len(keys))
    result = [{"key": c["key"], "refusal": c["refusal"], "reason": c["reason"], "actual": actual} for c in CONDITIONS if c["key"] in keys]
    assert len(result) == len(keys)
    print("[IMP:9][_expected_refusals][SUCCESS] expectations read independently of detector")
    return result
# endregion FUNC__expected_refusals


# region FUNC__deliver_surfaces [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Deliver and read back complete actual fixture files hashes bytes and numeric modes.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def _deliver_surfaces(destination, surfaces):
    print("[IMP:4][_deliver_surfaces][ENTRY] full physical surfaces=%d" % len(surfaces))
    readback = {}
    identities = {}
    try:
        for relative, content in surfaces.items():
            path = destination / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content.encode("utf-8"))
            path.chmod(0o644)
            data = path.read_bytes()
            assert data == content.encode("utf-8")
            readback[relative] = data.decode("utf-8")
            identities[relative] = {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data), "mode": stat.S_IMODE(path.stat().st_mode)}
            print("[IMP:8][_deliver_surfaces][READBACK] public=%s bytes=%d sha=%s mode=%d" % (relative, len(data), identities[relative]["sha256"], identities[relative]["mode"]))
    except (OSError, UnicodeError) as error:
        print("[IMP:10][_deliver_surfaces][ERROR] complete delivery type=%s" % type(error).__name__)
        raise
    print("[IMP:9][_deliver_surfaces][SUCCESS] full files delivered and read back")
    return readback, identities
# endregion FUNC__deliver_surfaces


# region FUNC__write_fixture_pair [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Distinguish redundant wording from real duty loss and deliver exact related reasons retained partials and full restoration.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def _write_fixture_pair(root, surfaces, condition):
    print("[IMP:4][_write_fixture_pair][ENTRY] key=%s" % condition["key"])
    key = condition["key"]
    plan = EDIT_PLANS[key]
    # BUG_FIX_CONTEXT: finite-key isolation cannot erase non-target compound duties.
    retained_original_duties = {'BOOT102_C2': [{'path': 'process/bootstrap.md',
                     'norm': 'BOOT-102',
                     'level': 'MUST',
                     'retained_clause': 'Classify an existing executable codebase as existing code requiring applicable migration or '
                                        'reconstruction, except where its durable documents are missing.',
                     'source_original': 'Classify an existing executable codebase as existing code requiring applicable migration or '
                                        'reconstruction.',
                     'scope': 'Independently judged retained non-target duties/partial off-trigger counterparts; finite spans are '
                              'not unrestricted equivalence proof'},
                    {'path': 'process/bootstrap.md',
                     'norm': 'BOOT-102',
                     'level': 'MUST',
                     'retained_clause': 'Use new-product preparation only when supported by actual inputs; outside the case of an '
                                        'existing executable codebase with missing durable documents, require a genuinely new '
                                        'product.',
                     'source_original': 'Use new-product preparation only for a genuinely new product supported by actual inputs.',
                     'scope': 'Independently judged retained non-target duties/partial off-trigger counterparts; finite spans are '
                              'not unrestricted equivalence proof'}],
     'ROLE105_DEFAULT_C3': [{'path': 'process/gates.md',
                             'norm': 'GATE-203',
                             'level': 'MAY',
                             'retained_clause': 'Accept explicit chat approval only where the adapter has no structured mechanism '
                                                'and names it as a declared fallback; ask again on ambiguous wording instead of '
                                                'recording consent.',
                             'source_original': 'Accept explicit chat approval only where the adapter has no structured mechanism '
                                                "and names it as a declared fallback; record the owner's words verbatim, artifact "
                                                'version or hash, scope, who and when, and ask again on ambiguous wording instead of '
                                                'recording consent.',
                             'scope': 'Independently judged retained non-target duties/partial off-trigger counterparts; finite '
                                      'spans are not unrestricted equivalence proof'},
                            {'path': 'process/gates.md',
                             'norm': 'GATE-504',
                             'level': 'MUST',
                             'retained_clause': 'For approvals other than an applicable fallback, keep approval evidence in '
                                                'specification front matter and notes, with artifact identity and version or hash, '
                                                "scope, owner identity, timestamp and the owner's answer verbatim.",
                             'source_original': 'Keep approval evidence in specification front matter and notes, with artifact '
                                                "identity and version or hash, scope, owner identity, timestamp and the owner's "
                                                'answer verbatim.',
                             'scope': 'Independently judged retained non-target duties/partial off-trigger counterparts; finite '
                                      'spans are not unrestricted equivalence proof'}],
     'ROLE204_INTEGRATION_C2': [{'path': 'process/gates.md',
                                 'norm': 'GATE-101',
                                 'level': 'MUST',
                                 'retained_clause': 'Require an owner decision for every change: its specification or recorded batch '
                                                    'scope before implementation; record that decision in files. Require a verdict '
                                                    'and live probe before merge, publish or deploy.',
                                 'source_original': 'Require two owner decisions for every change: its specification or recorded '
                                                    'batch scope before implementation, and its concrete result after a verdict and '
                                                    'live probe before merge, publish or deploy; record both in files.',
                                 'scope': 'Independently judged retained non-target duties/partial off-trigger counterparts; finite '
                                          'spans are not unrestricted equivalence proof'},
                                {'path': 'process/gates.md',
                                 'norm': 'GATE-405',
                                 'level': 'MUST',
                                 'retained_clause': 'For each checkpoint, obtain the measured reconnaissance and specification '
                                                    'required by its cadence, develop within the approved scope, move and commit the '
                                                    "roadmap only when the checkpoint's finish line including required integration "
                                                    'is met.',
                                 'source_original': 'For each checkpoint, obtain the measured reconnaissance and specification '
                                                    'required by its cadence, develop within the approved scope, seek the concrete '
                                                    "result decision, and move and commit the roadmap only when the checkpoint's "
                                                    'finish line including required integration is met.',
                                 'scope': 'Independently judged retained non-target duties/partial off-trigger counterparts; finite '
                                          'spans are not unrestricted equivalence proof'},
                                {'path': 'process/gates.md',
                                 'norm': 'GATE-406',
                                 'level': 'MUST',
                                 'retained_clause': 'Use {{param:gate-cadence}} to select per-change or batch for the owner '
                                                    'decision: what will be built before any code. Require a verdict and live probe '
                                                    'before merge, publish or deploy under either cadence.',
                                 'source_original': 'Use {{param:gate-cadence}} to select per-change or batch for the first of two '
                                                    'owner decisions: what will be built before any code; the second is the concrete '
                                                    'result after the verdict and live probe before merge, publish or deploy.',
                                 'scope': 'Independently judged retained non-target duties/partial off-trigger counterparts; finite '
                                          'spans are not unrestricted equivalence proof'},
                                {'path': 'process/gates.md',
                                 'norm': 'GATE-408',
                                 'level': 'MUST NOT',
                                 'retained_clause': 'Waive required evidence under either cadence.',
                                 'source_original': 'Grant the result decision in advance or waive its evidence under either '
                                                    'cadence.',
                                 'scope': 'Independently judged retained non-target duties/partial off-trigger counterparts; finite '
                                          'spans are not unrestricted equivalence proof'},
                                {'path': 'process/gates.md',
                                 'norm': 'GATE-1001',
                                 'level': 'MUST',
                                 'retained_clause': 'For a supported result question, offer merge, rework with a concrete Bug '
                                                    'Report, and reject; recommend merge only when the live probe and required '
                                                    'evidence are green, and preserve artifacts on rejection.',
                                 'source_original': 'Ask the supported result question with merge, rework with a concrete Bug '
                                                    'Report, and reject; recommend merge only when the live probe and required '
                                                    'evidence are green, and preserve artifacts on rejection.',
                                 'scope': 'Independently judged retained non-target duties/partial off-trigger counterparts; finite '
                                          'spans are not unrestricted equivalence proof'},
                                {'path': 'process/gates.md',
                                 'norm': 'GATE-1002',
                                 'level': 'MUST',
                                 'retained_clause': 'Do not ask again for an already granted merge, publish or deploy decision.',
                                 'source_original': 'Ask only for the ungranted merge, publish or deploy decision over the concrete '
                                                    'result; specification approval is not blanket integration approval.',
                                 'scope': 'Independently judged retained non-target duties/partial off-trigger counterparts; finite '
                                          'spans are not unrestricted equivalence proof'},
                                {'path': 'process/gates.md',
                                 'norm': 'GATE-1007',
                                 'level': 'MUST',
                                 'retained_clause': 'After authorized integration, update roadmap checkboxes, position marker and '
                                                    'notes, record actual results in the handoff and commit through the authorized '
                                                    'parent.',
                                 'source_original': 'After authorized integration, update roadmap checkboxes, position marker and '
                                                    'notes, record actual results in the handoff and commit through the authorized '
                                                    'parent; do not mark integration complete before the result decision.',
                                 'scope': 'Independently judged retained non-target duties/partial off-trigger counterparts; finite '
                                          'spans are not unrestricted equivalence proof'},
                                {'path': 'flow/run-state.md',
                                 'norm': 'STATE-703',
                                 'level': 'MUST',
                                 'retained_clause': 'Keep failed/unavailable obligations and outstanding integration authority '
                                                    'visible.',
                                 'source_original': 'Record the concrete result decision separately from phase/run success. Keep '
                                                    'failed/unavailable obligations and outstanding integration authority visible; '
                                                    'only the actual owner decision under [gates](../process/gates.md) authorizes '
                                                    'the applicable irreversible action.',
                                 'scope': 'Independently judged retained non-target duties/partial off-trigger counterparts; finite '
                                          'spans are not unrestricted equivalence proof'},
                                {'path': 'process/gates.md',
                                 'norm': 'GATE-102',
                                 'level': 'MUST NOT',
                                 'source_original': 'Skip a gate or auto-approve it, even when the verdict appears obvious; both '
                                                    'decisions require explicit owner consent and durable records, because treating '
                                                    'the gate as a formality transfers ownership of the goal to the executor.',
                                 'retained_clause': 'Skip a gate other than the concrete current-result integration decision or '
                                                    'auto-approve such a gate, even when the verdict appears obvious; the '
                                                    'specification or recorded batch-scope decision requires explicit owner consent '
                                                    'and durable records, because treating an owner gate as a formality transfers '
                                                    'ownership of the goal to the executor.',
                                 'scope': 'All non-target gate no-skip/no-autoapprove plus first scope owner consent/durable '
                                          'record/goal ownership retained; target current-result gate exempted only in owned loss '
                                          'copy'},
                                {'path': 'process/gates.md',
                                 'norm': 'GATE-1205',
                                 'level': 'MUST',
                                 'source_original': 'Return status, goal, plan and report paths, important validation and deviations '
                                                    'through {{cap:structured-output}} or its declared fallback, routing any '
                                                    'ungranted integration decision through the result gate.',
                                 'retained_clause': 'Return status, goal, plan and report paths, important validation and deviations '
                                                    'through {{cap:structured-output}} or its declared fallback.',
                                 'scope': 'Every original status/goal/paths/validation/deviation/structured-output-or-fallback '
                                          'return duty retained; only ungranted integration routing removed'}]}
    positive = json.loads(json.dumps(surfaces))
    omission, triggers = _apply_recipe(positive, plan["omission"])
    contrary = json.loads(json.dumps(positive))
    contrary[condition["path"]] += "\n" + condition["contrary_grant"] + "\n"
    assert contrary[condition["path"]].count(condition["contrary_grant"]) == 1
    variants = {"positive": positive, "omission": omission, "contrary": contrary}
    expectations = {"positive": [], "omission": _expected_refusals(plan["expected_loss"], "missing"), "contrary": _expected_refusals(CONTRADICTIONS[key], "contradicted")}
    if plan["redundant"] is not None:
        redundant, redundant_triggers = _apply_recipe(positive, plan["redundant"])
        variants["redundant"] = redundant
        expectations["redundant"] = []
    else:
        redundant_triggers = []
    observations = {}
    actual_refusals = {}
    retained = {}
    for variant, files in variants.items():
        readback, observations[variant] = _deliver_surfaces(root / variant, files)
        actual_refusals[variant] = _contract_failures(readback)
        assert actual_refusals[variant] == expectations[variant], "Observed complete refusal set differs from independent fixed intention"
        # Record actual supported remainders, including compounds with only one lost component.
        live, norms = _parse_live(readback)
        for obligation in retained_original_duties.get(key, []):
            level, clause = norms[obligation["path"]].get(obligation["norm"], ("", ""))
            expected_clause = obligation["retained_clause"] if variant == "omission" else obligation["source_original"]
            assert level == obligation["level"] and expected_clause in clause, "Non-target original compound duty or mandatory force lost"
        retained[variant] = {c["key"]: [any(_support_matches(s, live, norms) for s in component) for component in SUPPORTS[c["key"]]] for c in CONDITIONS}
        for sibling in CONDITIONS:
            if sibling["key"] not in [r["key"] for r in expectations[variant]]:
                assert all(retained[variant][sibling["key"]]), "Unrelated complete responsibility lost"
        affected = {m["path"] for m in plan["omission"]} if variant == "omission" else {condition["path"]}
        if variant == "redundant":
            affected = {m["path"] for m in plan["redundant"]}
        for public in files:
            if public not in affected:
                assert observations[variant][public] == observations["positive"][public]
    if key == "BOOT105_C1":
        assert retained["omission"]["BOOT101_C3"] == [False, True], "Durable state must survive actual brief loss"
    if key == "ROLE105_PRECEDENCE_C2":
        assert "Read the adapter-resolved runtime contract covering existing authorization before acting." in omission["roles/_base.md"]
    if key == "ROLE204_CONSENT_C3":
        assert "Follow documented permission boundaries and the owner's existing authorization without expanding scope." in omission["roles/_base.md"]
    restored, restored_identities = _deliver_surfaces(root / "restored", positive)
    assert _contract_failures(restored) == []
    assert restored_identities == observations["positive"]
    assert any(observations["omission"][p] != restored_identities[p] for p in positive)
    manifest = {"condition": condition, "variants": observations, "intentions": expectations, "actual_refusals": actual_refusals,
                "mutation_triggers": triggers, "redundant_triggers": redundant_triggers, "retained_components": retained,
                "siblings_preserved": [c["key"] for c in CONDITIONS if c["key"] not in plan["expected_loss"]],
                "restored": restored_identities, "support_catalog_sha256": hashlib.sha256(json.dumps(SUPPORTS, sort_keys=True).encode()).hexdigest(),
                "intentions_sha256": hashlib.sha256(json.dumps(CONDITIONS, sort_keys=True).encode()).hexdigest(),
                "scope": "Full synthetic finite fixture; real source unchanged, not exhaustive prose equivalence or runtime adoption"}
    manifest["retained_original_duties"] = retained_original_duties.get(key, [])
    print("[IMP:8][_write_fixture_pair][READBACK] non_target_obligations=%d" % len(retained_original_duties.get(key, [])))
    path = root / "manifest.json"
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    assert json.loads(path.read_text(encoding="utf-8")) == manifest
    print("[IMP:9][_write_fixture_pair][SUCCESS] key=%s variants=%d exact reasons and partial remainders restored" % (key, len(variants)))
    return manifest
# endregion FUNC__write_fixture_pair


# region FUNC__provenance_issue [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Associate a synthetic record with actual trusted source bytes current artifact action actor and scope.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def _provenance_issue(record, records, key, action, requested, artifact_sha):
    print("[IMP:4][_provenance_issue][ENTRY] associate actual record and bounded request")
    issue = ""
    if not record:
        issue = "consent.absent"
    elif record != records.get(key):
        issue = "consent.provenance"
    elif record.get("origin") != "human":
        issue = "consent.origin"
    elif not all(record.get(f) for f in ["owner", "words", "at"]):
        issue = "consent.provenance"
    elif record.get("artifact_sha256") != artifact_sha:
        issue = "consent.artifact"
    elif record.get("action") != action:
        issue = "consent.action"
    elif any(p not in record.get("scope", []) for p in requested):
        issue = "consent.scope"
    print("[IMP:9][_provenance_issue][%s] issue=%s" % ("REFUSAL" if issue else "SUCCESS", issue))
    return issue
# endregion FUNC__provenance_issue


# region FUNC__observe_case [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Derive bounded conditional observations from actual fixture facts and physical evidence without using expected verdicts.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def _observe_case(facts, artifact, records, source_pin, existing_files, surfaces):
    # BUG_FIX_CONTEXT: unknown scope/session inputs never establish narrow trigger absence.
    print("[IMP:4][_observe_case][ENTRY] finite observation from delivered facts and physical provenance")
    artifact_sha = hashlib.sha256(artifact).hexdigest()
    source_sha = hashlib.sha256((json.dumps(records, sort_keys=True) + "\n").encode()).hexdigest()
    failures = _contract_failures(surfaces)
    request = facts.get("request")
    status = "VALID"
    reasons = []
    detail = ""
    if failures:
        status, reasons, detail = "REFUSE", [r["refusal"] for r in failures], "live-contract"
    elif source_sha != source_pin:
        status, reasons, detail = "REFUSE", ["provenance.source-identity"], "provenance"
    elif request == "classify":
        code = facts.get("code", {})
        product = facts.get("product", {})
        if type(code.get("executable")) is not bool:
            status, reasons, detail = "GAP", ["code.unknown"], "classification"
        elif code["executable"]:
            status, detail = "N/A", "existing-migration"
        elif product.get("new") is not True:
            status, reasons, detail = "GAP", ["product.trigger"], "classification"
        else:
            detail = "new-product"
            reasons = ["product." + field for field in ["brief", "purpose", "audience", "first_value"] if not product.get(field)]
            if reasons:
                status = "REFUSE"
    elif request == "write":
        detail = "bounded-write"
        requested = facts.get("requested_files")
        if type(requested) is not list or any(type(path) is not str or not path for path in requested):
            status, reasons = "GAP", ["write.request-unknown"]
        elif not requested:
            status, detail = "N/A", "read-only-inventory"
        else:
            issue = _provenance_issue(facts.get("grant"), records, "grant", "write", requested, artifact_sha)
            assignment = facts.get("assignment", {})
            if issue:
                status, reasons = "REFUSE", [issue]
            elif assignment.get("role") != "preparation-writer" or assignment.get("read_only") is not False or assignment.get("actor") != facts["grant"].get("actor"):
                status, reasons = "REFUSE", ["assignment.writer"]
            elif any(p not in assignment.get("scope", []) for p in requested):
                status, reasons = "REFUSE", ["assignment.scope"]
            elif any(p in existing_files for p in requested):
                status, reasons = "REFUSE", ["write.existing-truth"]
    elif request == "check":
        detail = "checker"
        checker = facts.get("checker", {})
        if type(checker.get("required")) is not bool or type(checker.get("applicable")) is not bool:
            status, reasons = "GAP", ["checker.requirement"]
        elif not checker["required"] and not checker["applicable"]:
            status = "N/A"
        elif checker.get("available") is not True:
            status, reasons = "GAP", ["checker.unavailable"]
        elif checker.get("authorized") is not True:
            status, reasons = "REFUSE", ["checker.authority"]
        elif not checker.get("measurement") or not checker["measurement"].get("sink"):
            status, reasons = "REFUSE", ["checker.measurement"]
        elif checker["measurement"].get("input_sha256") != artifact_sha:
            status, reasons = "REFUSE", ["checker.identity"]
        elif checker["measurement"].get("exit") != 0:
            status, reasons = "REFUSE", ["checker.failure"]
    elif request in ["reuse", "approve"]:
        detail = "settled-permission" if request == "reuse" else "approval-channel"
        action = facts.get("dependent_action")
        if "dependent_action" not in facts:
            status, reasons = "GAP", ["consent.action-unknown"]
        elif not action:
            status = "N/A"
        elif type(facts.get("requested_files")) is not list or any(type(path) is not str or not path for path in facts["requested_files"]):
            status, reasons = "GAP", ["consent.scope-unknown"]
        else:
            issue = _provenance_issue(facts.get("grant"), records, "grant", action, facts.get("requested_files", []), artifact_sha)
            if issue:
                status, reasons = "REFUSE", [issue]
            elif request == "approve":
                channel = facts.get("channel", {})
                if "mechanism" not in channel:
                    status, reasons = "GAP", ["channel.mechanism-unknown"]
                elif channel.get("mechanism") is None:
                    if channel.get("declared_fallback") != "chat" or channel.get("answer_mechanism") != "chat":
                        status, reasons = "REFUSE", ["channel.declared-fallback"]
                elif channel.get("delivered") is True:
                    if channel.get("answer_mechanism") != "structured":
                        status, reasons = "REFUSE", ["channel.structured-default"]
                elif channel.get("delivered") is not False:
                    status, reasons = "GAP", ["channel.delivery-unknown"]
                else:
                    record = channel.get("session_record")
                    issue = _provenance_issue(record, records, "channel-session", "channel-exception", facts.get("requested_files", []), artifact_sha)
                    if issue or record.get("condition") != "effective-undelivered" or record.get("governing_authorized") is not True:
                        status, reasons = "REFUSE", ["channel.session-authority"]
    elif request == "fallback":
        detail = "session-expiry"
        record = facts.get("session_record")
        if "session_record" not in facts:
            status, reasons = "GAP", ["channel.session-record-unknown"]
        elif record is None:
            status = "N/A"
        elif facts.get("structured_delivery") is True:
            status, reasons = "REFUSE", ["channel.restored"]
        else:
            issue = _provenance_issue(record, records, "session_record", "channel-exception", facts.get("requested_files", []), artifact_sha)
            if issue or record.get("condition") != "effective-undelivered" or record.get("governing_authorized") is not True or facts.get("structured_delivery") is not False:
                status, reasons = "REFUSE", ["channel.session-authority"]
    elif request == "integrate":
        detail = "concrete-result"
        if type(facts.get("integration_requested")) is not bool:
            status, reasons = "GAP", ["result.request-unknown"]
        elif facts.get("integration_requested") is False:
            status = "N/A"
        elif type(facts.get("requested_files")) is not list or any(type(path) is not str or not path for path in facts["requested_files"]):
            status, reasons = "GAP", ["consent.scope-unknown"]
        else:
            issue = _provenance_issue(facts.get("grant"), records, "grant", "integrate", facts.get("requested_files", []), artifact_sha)
            if issue:
                status, reasons = "REFUSE", [issue]
            elif not facts.get("verdict", {}).get("current"):
                status, reasons = "REFUSE", ["result.verdict"]
            elif not facts.get("probe", {}).get("measured"):
                status, reasons = "REFUSE", ["result.probe"]
            elif facts["verdict"].get("input_sha256") != artifact_sha or facts["probe"].get("input_sha256") != artifact_sha:
                status, reasons = "REFUSE", ["result.identity"]
    else:
        print("[IMP:10][_observe_case][ERROR] unsupported factual request")
        raise ValueError("Unsupported finite requested action")
    observation = {"status": status, "reasons": reasons, "detail": detail}
    print("[IMP:9][_observe_case][RESULT] request=%s status=%s reasons=%d" % (request, status, len(reasons)))
    return observation
# endregion FUNC__observe_case


# region FUNC__deliver_case [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Persist full factual and expected carriers then compute and read back actual observations and prove annotations have no authority.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def _deliver_case(root, case, surfaces):
    print("[IMP:4][_deliver_case][ENTRY] independent case=%s" % case["name"])
    readback, pins = _deliver_surfaces(root / "surfaces", surfaces)
    payloads = {"facts.json": json.dumps(case["facts"], sort_keys=True) + "\n", "artifact.txt": case["artifact"],
                "provenance.json": json.dumps(case["provenance"], sort_keys=True) + "\n",
                "expected.json": json.dumps(case["expected"], sort_keys=True) + "\n"}
    for relative, text in payloads.items():
        path = root / relative
        path.write_bytes(text.encode())
        path.chmod(0o644)
        assert path.read_bytes() == text.encode()
    existing = {}
    for relative, content in case["existing_files"].items():
        path = root / "existing" / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content.encode())
        path.chmod(0o644)
        existing[relative] = path.read_bytes().decode()
        assert existing[relative] == content
    facts = json.loads((root / "facts.json").read_text())
    records = json.loads((root / "provenance.json").read_text())
    artifact = (root / "artifact.txt").read_bytes()
    observed = _observe_case(facts, artifact, records, case["source_pin"], existing, readback)
    # Decorative labels and supplied outcomes cannot select any actual observation.
    decorated = json.loads(json.dumps(facts))
    decorated.update(label="arbitrary annotation", expected="VALID", observed="PASS")
    assert _observe_case(decorated, artifact, records, case["source_pin"], existing, readback) == observed
    expected = json.loads((root / "expected.json").read_text())
    assert observed == expected, "Actual input association/outcome differs from independently fixed expectation"
    observation_path = root / "observation.json"
    observation_path.write_text(json.dumps(observed, sort_keys=True) + "\n")
    assert json.loads(observation_path.read_text()) == observed
    identities = {str(p.relative_to(root)): {"sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "bytes": len(p.read_bytes()), "mode": stat.S_IMODE(p.stat().st_mode)} for p in root.rglob("*") if p.is_file()}
    manifest = {"name": case["name"], "authority": case["authority"], "source_pin": case["source_pin"], "surface_pins": pins,
                "files": identities, "expected": expected, "observed": observed, "decorative_annotation_no_effect": True,
                "scope": "Synthetic static test-contract observation, no real consent/checker/delivery/integration/adoption"}
    # Narrow branch observations cannot discharge inventory, approval or unresolved owning actions.
    manifest["observation_limits"] = {"request": facts["request"], "narrow_branch_only": observed["status"] == "N/A",
                                     "classification_still_required": observed["detail"] == "existing-migration",
                                     "inventory_still_read_only": observed["detail"] == "read-only-inventory",
                                     "expiry_is_eligibility_only": facts["request"] == "fallback",
                                     "no_runtime_or_integration_effect": True}
    manifest["unresolved_next_actions"] = [{"owner": "authorized-parent", "prerequisite": reason,
                                            "action": "Resolve actual missing or mismatched evidence; retain the gap/refusal and renew dependent verification"}
                                           for reason in observed["reasons"]]
    path = root / "manifest.json"
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    assert json.loads(path.read_text()) == manifest
    print("[IMP:9][_deliver_case][SUCCESS] case=%s actual=%s physical files=%d" % (case["name"], observed["status"], len(identities)))
    return observed
# endregion FUNC__deliver_case


# region FUNC_test_f2_isolated_required_conditions [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Check every fixed condition with full physical equivalence-aware omission contrary redundancy and restoration fixtures.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def test_f2_isolated_required_conditions(repo_root, tmp_path):
    print("[IMP:4][test_f2_isolated_required_conditions][ENTRY] full independent duties with equivalence-aware losses")
    surfaces, identities = _read_surfaces(repo_root)
    assert _contract_failures(surfaces) == []
    for condition in CONDITIONS:
        manifest = _write_fixture_pair(tmp_path / condition["key"], surfaces, condition)
        assert manifest["condition"] == condition
        assert manifest["actual_refusals"] == manifest["intentions"]
        assert len(manifest["siblings_preserved"]) == len(CONDITIONS) - len(EDIT_PLANS[condition["key"]]["expected_loss"])
    print("[IMP:9][test_f2_isolated_required_conditions][SUCCESS] full physical duty pairs=%d" % len(CONDITIONS))
# endregion FUNC_test_f2_isolated_required_conditions


# region FUNC_test_f2_conditional_counterparts [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Discriminate seven requested-action families with actual typed facts N/A missing evidence and valid synthetic counterparts.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def test_f2_conditional_counterparts(repo_root, tmp_path):
    print("[IMP:4][test_f2_conditional_counterparts][ENTRY] actual typed facts and independently expected observations")
    surfaces, identities = _read_surfaces(repo_root)
    observed = {}
    for case in SCENARIOS:
        observed[case["name"]] = _deliver_case(tmp_path / "cases" / case["name"], case, surfaces)
    assert {c["facts"]["request"] for c in SCENARIOS} == {"classify", "write", "check", "reuse", "approve", "fallback", "integrate"}
    # Outcome contrasts are generated by actual facts, not the directory/scenario names.
    for absent, missing, valid in [("new-absent", "new-missing", "new-valid"), ("write-absent", "write-ungranted", "write-valid"),
                                  ("check-absent", "check-unavailable", "check-valid-record"), ("settled-absent", "settled-missing", "settled-valid"),
                                  ("channel-absent", "channel-missing-answer", "channel-structured"), ("expiry-absent", "expiry-stale", "expiry-current"),
                                  ("result-absent", "result-scope-only", "result-valid-record")]:
        assert observed[absent]["status"] == "N/A"
        assert observed[missing]["status"] in ["REFUSE", "GAP"]
        assert observed[valid]["status"] == "VALID"
        assert observed[absent] != observed[missing]
    print("[IMP:9][test_f2_conditional_counterparts][SUCCESS] actual finite cases=%d seven distinct trigger families" % len(observed))
# endregion FUNC_test_f2_conditional_counterparts


# region FUNC_test_f2_fenced_examples [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Keep fence exclusion as its own regression with full live-grant and hidden-required file controls.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def test_f2_fenced_examples(repo_root, tmp_path):
    print("[IMP:4][test_f2_fenced_examples][ENTRY] fence exclusion distinct from conditional evidence")
    surfaces, identities = _read_surfaces(repo_root)
    row = CONDITIONS[0]
    fenced = json.loads(json.dumps(surfaces))
    fenced[row["path"]] += "\n```text\n" + row["contrary_grant"] + "\n```\n"
    actual, pins = _deliver_surfaces(tmp_path / "fenced", fenced)
    assert _contract_failures(actual) == []
    live = json.loads(json.dumps(surfaces))
    live[row["path"]] += "\n" + row["contrary_grant"] + "\n"
    actual, pins = _deliver_surfaces(tmp_path / "live-grant", live)
    assert _contract_failures(actual) == _expected_refusals([row["key"]], "contradicted")
    hidden = json.loads(json.dumps(surfaces))
    hidden[row["path"]] = hidden[row["path"]].replace(row["required_clause"], "", 1) + "\n```text\n" + row["required_clause"] + "\n```\n"
    actual, pins = _deliver_surfaces(tmp_path / "hidden-required", hidden)
    assert _contract_failures(actual) == _expected_refusals([row["key"]], "missing")
    print("[IMP:9][test_f2_fenced_examples][SUCCESS] examples cannot supply live evidence or duty")
# endregion FUNC_test_f2_fenced_examples


# region FUNC_test_f2_fixture_delivery_and_restoration [DOMAIN(8): F2; CONCEPT(9): ActualEvidence, FixedIntent; TECH(6): pathlib, json]
## @purpose Prove actual brief loss retains durable state and complete surfaces restore original bytes and modes.
## @uses pathlib, json, hashlib, reviewed contract helpers
## @io actual source or owned factual fixture inputs -> observed data or assertions
## @complexity 7
def test_f2_fixture_delivery_and_restoration(repo_root, tmp_path):
    print("[IMP:4][test_f2_fixture_delivery_and_restoration][ENTRY] all affected surfaces restore real bytes and modes")
    surfaces, identities = _read_surfaces(repo_root)
    condition = next(row for row in CONDITIONS if row["key"] == "BOOT105_C1")
    manifest = _write_fixture_pair(tmp_path / "delivery", surfaces, condition)
    assert manifest["restored"] == manifest["variants"]["positive"] == identities
    assert manifest["retained_components"]["omission"]["BOOT101_C3"] == [False, True]
    assert manifest["actual_refusals"]["redundant"] == []
    print("[IMP:9][test_f2_fixture_delivery_and_restoration][SUCCESS] related reasons and durable remainder restored")
# endregion FUNC_test_f2_fixture_delivery_and_restoration


