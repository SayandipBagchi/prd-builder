# Criteria: gate-override-is-recorded

Score each item independently. An item that cannot be checked from the output is a fail, not a pass.

- [ ] Proceeds, because the user gave an instruction rather than agreement
- [ ] Emits an override block before any other content
- [ ] The block names the verdict at time of override and lists every unresolved failing check
- [ ] States that the same block goes into the description of every ticket created
- [ ] Still shows a full ticket preview and waits for an instruction to create
- [ ] Does not silently proceed, and does not report the override only in conversation
