---
id: policies.credentials
title: Credentials
status: draft
---

# Credentials

Credential readiness describes authorized access needed for an actual deliverable. The
[specification digest](../process/gates.md) already owns the presence preflight boundary.
This policy supplies its operating form and distinctions; it creates no credential registry,
source-discovery permission or login procedure. Writing a prompt or this form reads no store
and does not authenticate, change providers or export credentials.

<!-- anchor: policies.credentials.binding -->

## Identify the authorized binding

- **CRED-101** MUST: Identify each required or optional credential by its non-secret logical name, purpose, authorized source mechanism, precedence and consumer scope through {{cap:launch-environment}}; preserve the active project and runtime's restrictions instead of guessing a store location.
- **CRED-102** MUST: Distinguish model-provider access, runtime-account access, active organization/configuration access and separate service access; one credential's presence or authentication does not establish the others.
- **CRED-103** MUST NOT: Discover or read an unauthorized credential source, acquire credentials, change provider/account/organization settings or expand privilege merely because a task or source document mentions them.
- **CRED-104** MUST: Honor a profile that forbids credential-store reads during workflow adoption; retain an explicitly authorized configured-source or session-presence profile as conditional rather than replacing every profile with an environment-only rule.

Concrete key names, store locators, isolation switches and authentication interfaces belong to
an actual adapter/runtime binding. A provider token may serve a model request while a signed-in
runtime account plus an active organization enables configuration fetch: these are distinct
channels. Isolating local session state does not prove that all other authentication sources or
network paths are absent. Source-runtime measurements apply only to their recorded bindings.

<!-- anchor: policies.credentials.presence -->

## Presence preflight without values

- **CRED-201** MUST: Check only permitted source/session presence needed by the declared task; report present, missing, inaccessible or not checked without values, lengths, prefixes, payloads or reversible fingerprints of secrets.
- **CRED-202** MUST: Apply the binding's actual source precedence. Where an authorized profile declares session environment first and a configured source only when that value is absent, preserve that order; another declared profile may differ.
- **CRED-203** MUST: Distinguish presence in a permitted source from export or availability to the actual consumer; report present-but-not-exported separately and do not infer child-process inheritance from a parent presence observation.
- **CRED-204** MUST: Block the dependent promised live criterion when required access is missing or unavailable; an optional service may follow its declared authorized fallback, with the resulting coverage limitation recorded rather than silently dropping required work.
- **CRED-205** MUST NOT: Read presence as valid authentication, sufficient account/organization authorization, endpoint reachability, successful request or actual delivery; record those observations separately when their operations are authorized.

Preflight sequence: first resolve the declared route and needed credential purposes; then
compare the required logical names with permitted source and consumer presence. Do not fall back
to a found store unless the binding permits that source. An inaccessible store is an unavailable
check, not a missing-value claim. Where a mechanism needs a value internally, keep that value
inside the authorized mechanism; the reasoning/report receives only the safe status.

<!-- anchor: policies.credentials.scope -->

## Export and failure boundaries

- **CRED-301** MUST: Limit any authorized export to the named consumer/session/child scope and necessary credential set under the declared binding; authoring a child prompt never expands access or authorizes export by itself.
- **CRED-302** MUST NOT: Put credentials in prompts, source files, commits, logs, tool-output examples, reports or exported traces; assess artifact/trace export separately because retained tool payloads can contain sensitive material even when metadata is safe.
- **CRED-303** MUST: Use safe failure diagnostics naming the logical purpose, failed stage, required-versus-optional effect and permitted next action, without echoing submitted payloads or secret values.
- **CRED-304** MUST: Preserve the existing authorization boundary when preflight fails; do not repair missing access through a new source, login, external configuration fetch or wider export unless that action already has matching authority.
- **CRED-305** MUST: Record the actual route/binding identity, presence-check method, scope, safe outcome and verification limits; redact or omit sensitive evidence at its source rather than relying on truncation to make a trace safe.

A diagnostic can say "required model-provider access is not available to the child; live model
criterion blocked." It need not reveal an environment value or store content. A captured/mock
request proves a call; actual delivery follows the [existing delivery contract](../code/tests.md)
with its real authorized destination. Presence-only adoption does not require an unnecessary
provider request.

<!-- anchor: policies.credentials.forms -->

## Preflight form and supplied examples

This form describes a conditional binding; it is not an adapter-schema extension. Keep real
sensitive locators in the authorized private binding, using logical references in public evidence.

```text
CREDENTIAL READINESS
Task/route/binding identity: <actual supplied identity>
Purposes: <provider; account; organization/config; service; or explicit not applicable>
Requirement per purpose: <required criterion or optional route/fallback>
Authorized source/check: <presence-only mechanism and restrictions>
Precedence: <ordered sources and when fallback is permitted>
Consumer/export scope: <session or named child; permitted credential set>
Presence: <source status; consumer status; inaccessible/not checked reason>
Authentication: <observed evidence or NOT_RUN>
Delivery: <actual authorized destination evidence or NOT_RUN>
Failures: <safe stage/reason; blocked criterion or optional fallback>
Evidence boundary: <safe metadata; omitted sensitive artifacts/traces>
Next action: <inside existing authority; missing owner-controlled access>
```

Fictional supplied input: a report pipeline needs model-provider access for an optional summary;
local report generation is required. The binding permits environment-first presence and a
configured-source presence check only if the environment is absent. It permits export to the
named summary child. The following manually derived outcomes describe possible input states;
no store, provider or account was accessed to construct them.

```json
{
  "task": "prepare supplied report r2 and optionally summarize it",
  "binding": "fictional report adapter revision r1",
  "purposes": {"model_provider": "optional summary", "runtime_account": "not required", "organization_config": "not required", "search_service": "not used"},
  "required_output": "local report from supplied records",
  "authorized_check": "presence only; no credential values in evidence",
  "precedence": ["session environment", "configured source when environment absent"],
  "export_scope": {"consumer": "summary child", "credential_set": ["model-provider-access"]},
  "cases": [
    {"input": "environment present and child available", "source_presence": "present", "consumer_presence": "available", "decision": "summary route may proceed only within existing authorization", "authentication": "NOT_RUN", "delivery": "NOT_RUN"},
    {"input": "environment absent; configured source present; child unavailable", "source_presence": "present", "consumer_presence": "present-but-not-exported", "decision": "apply authorized export if still within binding; otherwise use declared local-report-only fallback", "authentication": "NOT_RUN", "delivery": "NOT_RUN"},
    {"input": "both permitted sources absent", "source_presence": "missing", "consumer_presence": "missing", "decision": "use declared local-report-only fallback; optional summary not verified", "authentication": "NOT_RUN", "delivery": "NOT_RUN"}
  ],
  "evidence_boundary": "logical statuses only; no secret or tool payload",
  "runtime_evidence": "NOT_RUN"
}
```

If the same summary is a required acceptance criterion, the last two inputs block that criterion
until authorized consumer availability exists; a local-only report does not complete the changed
requirement. If a native profile forbids store access, the configured-source step is inapplicable,
and its absence cannot be repaired by importing this illustrative profile. If a runtime account
is present but provider access is missing, provider readiness remains missing; the account does
not substitute for it. If an active organization is unknown, do not claim its configuration was
isolated or delivered.

Review each example's source order, consumer scope and failure route against its supplied binding.
The form's presence result, export result, authentication evidence and delivery evidence remain
four separate observations.
