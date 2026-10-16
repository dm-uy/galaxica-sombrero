# DSH subagents & workflows — reference for plugin/preset authors

Read-only source of these findings, under the owner's dev directory: the `deepseek-harness` checkout at `3d_party/deepseek-harness`. All citations below are relative to that checkout.
`packages/subagent/subagent-in-process-driver/` has **only** `lib/` here (no `src/`, no `package.json`), so
driver claims cite `lib/index.js` / `lib/types/*.d.ts`.

## Tool surface

**`subagent`** — `@deepseek-ai/dsh-tool-subagent`; name from config `toolName` (default `subagent`)
(`packages/subagent/tool-subagent/src/index.ts:96`, `:171`).

| param | type | req | default | notes |
|---|---|---|---|---|
| `cwd` | string | no | caller's dir | relative resolves vs caller; later `cd`s independent (`src/index.ts:232-235`) |
| `description` | string | yes | — | 3-5 word label (`:236-240`) |
| `prompt` | string | yes | — | wording varies by `inheritsParentContext` (`:241-245`) |
| `provider` | string | no | provider/config defaults | **only when `modelSelectionSettings: true`** (`:246-252`) |
| `model` | string | no | idem | supply with `provider` (`:253-258`) |
| `reasoning_effort` | string | no | selected model's default | adapter-owned (`:259-264`) |

No `run_in_background` and no output-schema param: the tool is `isConcurrencySafe: () => true` and returns
`{kind:'activation', subagentId}` immediately (`src/index.ts:268-279`, `:341`); the child's answer arrives later
via the completion notice / `send_message` (`packages/bundle/base/README.md:52`).

**`subagent_fork`** — same package, `{provider: fork, toolName: subagent_fork}` with **no**
`modelSelectionSettings`, so only `cwd`/`description`/`prompt` and no `list_subagent_models`
(`packages/bundle/base/cordis.patch.yml:386-390`; rationale `:381-385`; `tool-subagent/README.md:211`).

**`list_subagent_models`** — only when model selection is enabled (`src/index.ts:206`); `provider` (string,
optional), `model` (string, optional, requires `provider`) (`docs/tool-catalog.md:2018-2038`).

**`send_message`** — `agent_id`, `message` (both string, required)
(`packages/subagent/tool-subagent-control/src/index.ts:29-41`). **`interrupt_agent`** — `agent_id` (string,
required; direct child *or* deeper descendant) (`:70-85`). **`list_agents`** — `scope` (enum
`children`|`descendants`, default `children`) (`list-agents.ts:50-52`).

**`workflow`** — `@deepseek-ai/dsh-tool-workflow`, `toolName` default `workflow`
(`packages/workflow/tool-workflow/src/index.ts:60`). `script` (string, req), `meta` (object, req; `name` +
`description` req, optional `whenToUse`, `phases[]{title(req),detail,provider,model}`), `args` (object, opt),
`run_in_background` (boolean, opt; schema present only while `enableRunInBackground`, default `true`)
(`src/index.ts:59-63`, `:331-374`).

## Child agent composition

A parent **can** control: initial `cwd` (`src/index.ts:325`; `docs/subsystems/subagent.md:11`); load-time
`agentOptions` (`provider`/`model`/`reasoningEffort`/`maxTokens`, `src/index.ts:99-109`, README `:50`); per-run
`provider`/`model` only when model selection is enabled; `persona` (`:69`, `:329`) and
`toolFilter.{allow|deny}` (`:75-80`, `:330`); `maxDepth` number or `'provider-managed'` (`:91`, `:323`).

A parent **cannot** control a child's skills catalog or instruction set. The child joins its parent's preset
revision (`agentPresets.composeFrom`, `packages/subagent/subagent/src/child-agent.ts:203`) and inherits that
scope chain; the only injection is the fixed delegation context string (`:170-174`, `:204-208`). No per-child
prompt or skill parameter exists in `SubagentStartRequest` (`docs/subsystems/subagent.md:11-137`). Per-child
`persona` shadows only `deployment:persona-prefix` (`child-agent.ts:209-215`). Tool scoping is subtractive:
`toolFilter` runs `tools.restrict()` in the child's creation window, so filtered tools vanish from the prompt
*and* refuse to execute (`:216`; `docs/subsystems/subagent.md:120-125`). No add-tools seam was found
(UNCONFIRMED whether a plugin could register extra tools into a child scope).

Sandbox/approvals: the child inherits only the parent session's **explicit** sandbox-mode override, and its
approval policy is pinned to `'never'` (asks rejected deterministically), except permission identity inherited
through Auto / Full access; these land on the child log as `source: 'delegation'` events
(`child-agent.ts:247-278`, `:219-234`). Child sessions carry `parentSession`, `origin: 'subagent'`,
`delegationDepth`, same `agentPreset` (`:137-155`).

Isolation: `spawn` = fresh Agent, own session/system prompt, zero parent context
(`subagent-spawn-in-process/src/index.ts:1-6`, `:48`); `fork` = seeded with the parent's balanced completed-turn
prefix (through the last `turn/end`), captured once at creation
(`subagent-fork-in-process/src/index.ts:38-53`, `:74-80`). Spawn/fork advertise `agentOptions`,
`outputSchema`, `depthLimit`, `toolFilter`, `persona` (`subagent-spawn-in-process/src/index.ts:40-46`).
`maxActiveSubagents` default 8; `maxDepth` default 1, a live Host setting re-read per delegation
(`packages/subagent/subagent/src/index.ts:183-195`; `tool-subagent/README.md:63`).

Results: `stopReason` is merge-extensible — `completed`, `aborted`, `error`, `max-tokens`, `refusal` — plus an
optional provider `diagnostic` capped at 4096 UTF-8 bytes (`docs/subsystems/subagent.md:239-299`). Child-level
failure resolves (never rejects) and maps to an `isError` tool result; only infrastructure faults reject.
`structured` exists only when the provider honored the schema. Fork children are continuable, external backends
one-shot (`tool-subagent/README.md:61`, `:212`).

Cost/token accounting: children are separate Agents/Sessions; "child-model tokens are separate from the parent's
retained context" (`packages/workflow/tool-workflow/README.md:157`). No per-child cost roll-up into the parent
was found (UNCONFIRMED: `packages/llm/token-meter/src/*` has no subagent branch).

## Preset interaction

A subagent **cannot** be launched under a named preset via any shipped tool or seam field:
`SubagentStartRequest` has no preset field (`docs/subsystems/subagent.md:11-137`) and the in-process driver calls
`applyChildComposition` → `composeFrom(childCtx, parent.ctx)`, joining the *parent's retained revision*
(`child-agent.ts:198-217`; `packages/preset/agent-preset-registry/src/index.ts:288-310`); a child that already
has a binding throws "Child already joined a preset" (`:288-310`). The `mount(ctx, id)` path that does take a
preset id serves session composition (`packages/api/session-controller/src/agent.ts:383-400`) and the webhook
entry (`packages/experimental/webhook/src/session.ts:126-140`), not delegation. *Role workaround:* one
distinctly named delegation tool instance per role, each with its own `persona`, `toolFilter`, `agentOptions`,
`maxDepth` (`tool-subagent/README.md:212`).

## Workflow hooks

Inside `script` (`packages/workflow/workflow-ptc/src/runtime.ts:85-98`):

- `agent(prompt, opts?)` — non-empty string prompt; `opts` a plain-JSON object. Keys: `label` (string), `phase`
  (string), `schema` (object-rooted JSON Schema), `provider` (string), `model` (string). `effort`, `isolation`,
  `agentType` are explicitly deferred and rejected (`:33-35`, `:252-282`). Returns the child's concatenated final
  text, `opts.schema`'s validated object, or `null` on child failure; a start failure or rejected child result is
  fatal (`:163-229`). `phase` defaults to the current `phase()` title; `label` to the prompt's first line clipped
  to 48 chars (`:45-50`, `:176-177`).
- `pipeline(items, ...stages)` — items array + ≥1 stages; each stage gets `(prev, item, index)`; a stage throw
  nulls that item and skips its remaining stages; fatal errors kill the run (`:311-340`).
- `parallel(thunks)` — array of zero-arg functions, `Promise.all` barrier; a throw → `null` (`:285-308`).
- `phase(title)` — non-empty string; sets the phase for later `agent()` calls (`:351-358`). `log(message)` —
  string narration (`:360-366`).
- `args` — the tool call's `args` object, copied over the PTC JSON channel (`:91-93`).

Caps (`workflow-ptc/src/index.ts:106-112`): `maxConcurrentAgents` `0` → `min(16, max(1, cores-2))` (`:141-144`);
`maxTotalAgents` `1000`; `maxItemsPerCall` `4096`; `syncTimeoutMs` `5000`; `provider` `spawn` — every child of the
run uses that one backend (`:107`; `host.ts:203-220`). `WorkflowStartRequest.subagentProvider` and a *lowering*
`maxTotalAgents` exist for owning consumers but **script hooks cannot change either**, and the `workflow` tool
exposes neither (`packages/workflow/workflow/src/runtime-types.ts:26-29`; `workflow-ptc/README.md:47`). Children
get the calling parent's effective `cwd` and `delivery: 'caller'` (no parent completion notice; not in the
parent's subagent catalog) (`host.ts:142`, `:200-220`; `workflow-ptc/README.md:53`, `:71`). Sandbox policy is the
calling session's resolved at start (`workflow-ptc/src/index.ts:167`; README `:59`).

Author docs: `packages/workflow/README.md:12`, `workflow/workflow/README.md`, `workflow-ptc/README.md:28-61`,
`tool-workflow/README.md:28-52`, `docs/subsystems/workflow.md`. The authoritative hook text is embedded in the
tool description (`tool-workflow/src/index.ts:158-166`) and mirrored in `docs/tool-catalog.md:2614-2640`.

## Caveats / limits

- Delegation tools never wait for results; only `send_message` / completion notices deliver child output
  (`tool-subagent/README.md:210`).
- `persona`, `toolFilter`, `maxDepth` are **fixed per registered tool instance** (`tool-subagent/README.md:212`).
- Numeric `maxDepth` needs the `depthLimit` capability and `agentOptions` needs `agentOptions`; a mismatch fails
  the plugin mount, not the first delegation (`src/index.ts:176-194`).
- Shipped fork delegation cannot select a child route (KV-cache reuse) (`tool-subagent/README.md:211`);
  `list_subagent_models` is advisory (`docs/tool-catalog.md:2018`).
- Workflow `agent()` accepts no preset/effort/isolation/agentType; unknown keys are fatal (`runtime.ts:33-35`,
  `:252-257`). The script has no fs/network/timer/Node APIs, but the VM is **not** a security boundary
  (`tool-workflow/src/index.ts:166`; `workflow-ptc/README.md:59`).
- Background runs report no intermediate value; `run_in_background` needs a live `ctx.jobs` registry or the call
  fails naming the missing pieces (`tool-workflow/src/index.ts:49-56`, `:269-272`; README `:170`).
- Host routing: `dsh-base` mounts `subagent`, `subagent_fork`, the control tools, `workflow-ptc`, `tool-workflow`
  (`packages/bundle/base/cordis.patch.yml:357-401`). Web App disables every one of those host rows
  (`packages/bundle/web-app/cordis.patch.yml:543-559`, rationale `:536-541`) and re-inserts them in each session
  preset's `delegation` group (`presets/standard.patch.yml:86-121`; same rows with `workflow-ptc`/`tool-workflow`
  `disabled: true` in `presets/ptc.patch.yml:116-121`). The `subagents` service and both providers stay on the
  host plane (`web-app/cordis.patch.yml:536-541`), so a methodology package should add its own preset rows rather
  than re-mount the providers.
