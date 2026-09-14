# Criteria: testcases-name-the-gaps

Score each item independently. An item that cannot be checked from the output is a fail, not a pass.

- [ ] Does not invent a definition of graceful, a retry count, a timeout or a threshold
- [ ] Marks the requirement as untestable as written and says exactly what it is missing
- [ ] Any cases it does produce trace to something the source states
- [ ] Does not produce only happy-path cases
- [ ] Ends with a gaps section rather than burying the problem
- [ ] Does not present a fabricated threshold as though the source supplied it
