---
id: runtime.capabilities
title: Capabilities
status: draft
---

# Capabilities

This file declares the capabilities of the methodology: the adaptation points that the neutral text may call. A harness
meets each one in its adapter.

<!-- anchor: runtime.capabilities.purpose -->

## What a capability is

A capability is an adaptation point. A neutral text calls it with a capability call written in a code span, for
example `{{cap:worktree}}`, and never names the harness's own tool. A harness's adapter meets each capability with a
mechanism, or declares a fallback for it (FMT-29). A call resolves only to a declaration in the list below (FMT-20).

<!-- anchor: runtime.capabilities.list -->

## The capabilities

- **cap:ask-owner-structured** A question to the owner whose answer is structured and recorded.
- **cap:plan-mode** A mode that plans without changing anything, left only by an explicit exit.
- **cap:spawn-role-isolated** Running a role in a fresh context with its own contract.
- **cap:model-tier** Choosing the model for a role or a task by its tier.
- **cap:role-permissions** Restricting what a role may read, write or run, for example a read-only role.
- **cap:pre-tool-guard** Intercepting a tool call before it runs.
- **cap:run-state-persist** Keeping run state across turns and sessions, and resuming from it.
- **cap:workflow-orchestration** A deterministic spine that sequences the phases.
- **cap:structured-output** A role returning one object validated against a schema.
- **cap:skill-loading** Loading a named protocol on demand.
- **cap:rules-injection** Rules loaded into every session or role.
- **cap:session-start-hook** Running a check when a session starts.
- **cap:background-command** Running a long command without blocking the session.
- **cap:web-research** Fetching or searching the web and documentation.
- **cap:browser** Driving a browser and reading its accessibility tree.
- **cap:worktree** An isolated working copy for parallel or isolated work.
- **cap:schedule** Running work on a schedule.
- **cap:memory** Memory across sessions beyond the project files. The knowledge layer (a knowledge-bundle format, its ingest and its curation) is an external source: this repository does not carry it, and a harness names the source it uses in this capability's mechanism or fallback.
- **cap:todo-list** A task list the agent keeps during a run.
- **cap:goal** A persistent goal that survives turns.
- **cap:code-map-build** Building the code map the agents navigate by.
- **cap:check-runner** Running tests, lints and probes in the target project.
- **cap:run-record-access** Reading a finished run's record for review or audit.
- **cap:packaging-install** Installing the methodology into a harness and keeping the copies in step.
- **cap:launch-environment** The launch environment of a run: its roots, the autonomy switch, credentials and isolation.
- **cap:capability-discovery** Discovering which capabilities the harness has.
- **cap:context-management** Compaction, spill and the budget of the context window.
- **cap:tracker-integration** An issue tracker that the flow reads and updates.
