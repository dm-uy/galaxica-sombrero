---
id: code.ax-ui
title: Accessibility-tree UI contract
status: draft
---

# Accessibility-tree UI contract

The accessibility tree gives agents a structured surface for finding and checking web controls. It supports structural
and behavioral evidence; it does not establish visual correctness or universal accessibility compliance. Browser tooling
is supplied through {{cap:browser}} after {{cap:capability-discovery}}, not implemented by this document.

<!-- anchor: code.ax-ui.applicability -->

## Planning and applicability

- **AX-101** MUST: Before planning a slice that creates or modifies web UI, load this contract through {{cap:skill-loading}} and translate its applicable duties into measurable acceptance criteria in the [development plan](../protocols/dev-plan.md). Give Code concrete control, state, validation and identity criteria. Pure backend, Python or CLI work has no web-UI trigger; record that reason rather than invent a frontend.
- **AX-102** MUST: For a non-web conversational surface use the project's structured conversation observations and actual harness, rather than claim it exposes a browser accessibility tree. Keep its behavioral and delivery criteria explicit under the [test contract](tests.md).

<!-- anchor: code.ax-ui.controls -->

## Controls, names and state

- **AX-201** MUST: Give every interactive control a semantic role, an accessible name, its applicable dynamic state and a stable identity. Prefer native semantic elements such as a button, input, select, link with destination or dialog. Use an explicit role only when native semantics cannot express the widget; roleless clickable containers are not an acceptable replacement for a button.
- **AX-202** MUST: Prefer a visible label linked to the control; when that is insufficient use an explicit accessible name or a reference to labeling text. Icon-only buttons require an accessible name. A placeholder is not a label or accessible name.
- **AX-203** MUST: Expose actual expanded, selected, current, checked, invalid, disabled and value-text state where each is applicable. A stateless button does not acquire an invented expanded state. State must change with the behavior, so the observer can distinguish open from closed or selected from idle.
- **AX-204** MUST: Give every interactive control and status/error node a stable test identifier or stable element identity. Correlate that DOM/locator identity with observed role/name/state; a DOM test identifier is not assumed to be an attribute emitted by every accessibility-tree API.

<!-- anchor: code.ax-ui.feedback -->

## Validation, asynchronous results and keyboard behavior

- **AX-301** MUST: Expose validation errors in a discoverable alert or polite live region, link the message to its field through its accessible description and mark the field invalid. Expose loading, result and empty outcomes through a status/live region. Check the actual post-action feedback, rather than infer success from a request call or a styled text node alone.
- **AX-302** MUST: Add ARIA only where native semantics are insufficient and pair a custom widget's roles and states with matching focus, Enter/Space and arrow-key behavior. Incorrect ARIA can misrepresent the control; adding attributes without implementing the keyboard behavior does not satisfy this contract.
- **AX-303** MUST NOT: Accept unnamed controls, placeholder-only labels, icon-only controls without names, hidden toggle/tab/expansion state, roleless click handlers or validation/status that the required observer cannot discover. The source rationale warns that plain styled feedback can hide broken flows; it is not a measured claim that all such text is absent from every browser tree.

<!-- anchor: code.ax-ui.verification -->

## Actual verification and fallback limits

- **AX-401** MUST: Discover the available browser capability and read its documented capture and interaction API. With a runnable frontend and actual DOM/accessibility access, navigate and interact by role plus name or a stable supported locator, then promptly capture and assert observed role/name/state and applicable validation/status. Retain the input, action, observed state, capture identity and isolated target. Do not target interactions by pixel coordinates or invent a snapshot tool.
- **AX-402** MUST: Use accessibility snapshots as primary evidence for structure and behavior, and screenshots only for visual claims such as layout, overlap, color or stacking. Passing one channel never proves the other; retain separately applicable visual checks.
- **AX-403** MUST: If live capture is unavailable, use actual rendered component tests where available and report the missing live evidence explicitly. A required live delivery criterion remains blocked or unverified; component evidence does not turn it into a pass or an applicability exclusion. A genuinely false UI trigger is distinct from an unavailable required browser.
- **AX-404** MUST: Retain the client-only markup permission in [exoskeleton](exoskeleton.md) and browser-only logging exception in [LDD](ldd.md), with typed component fixtures and this AX surface as applicable verification. Neither exception grants a backend logging or markup waiver; host rules and authored edit locality remain in their owning contracts.
