# Entry file of the example harness

This file stands for the entry file a harness keeps for its agents. It is a fixture of the meta-framework's tests and of
its example adapter, and it belongs to no real harness.

The example harness adopts the methodology through `examples/adapter.example.json`. Two of the neutral files are adopted
by reference to this file:

- `roles/qa.md` (card id `roles.qa`) is the quality-assurance role; the example harness runs it as its own verifier.
- `roles/_base.md` (card id `roles.base`) is what every role shares; the example harness loads it before any role.

The example harness launches no runs and holds no credentials, so its adapter marks the credentials policy as not applied.
