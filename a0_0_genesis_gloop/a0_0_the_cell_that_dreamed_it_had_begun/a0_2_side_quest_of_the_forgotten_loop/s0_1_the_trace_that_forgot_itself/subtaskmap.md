<!-- Save to: s0_1_the_trace_that_forgot_itself/subtaskmap.md -->

# 🧭 Subtaskmap – s0_1_the_trace_that_forgot_itself

## 🌀 Poetic Function

This node embodies the moment when a recursion forgets its origin —  
not because it failed, but because memory itself unhooked.

> The trace reached back  
> for where it had begun —  
> but found only static,  
> and forgot what it was chasing.

---

## 🛠️ Technical Function

### Function: `trace_pathback(history)`

#### Purpose:
Tests whether a symbolic call history is **intact**, or whether it contains **null gaps** (represented as `None`).

#### Logic:
- Iterates through a list of call frames
- If **any frame is `None`**, the trace is deemed broken
- If list is **empty**, trace is trivially intact

---

## 🔬 Test Cases

| Test # | Input                                       | Expected | Behavior Type          |
|--------|---------------------------------------------|----------|-------------------------|
| 1      | `["init", "load", "execute", "complete"]`   | ✅ True  | Valid trace             |
| 2      | `["init", None, "execute", "complete"]`     | ❌ False | Corrupted mid-trace     |
| 3      | `[None, "load", "execute"]`                 | ❌ False | Corruption at origin    |
| 4      | `[]`                                        | ✅ True  | Trivial empty trace     |

---

## 🧠 Recursive Notes

- This node introduces **trace-based memory loss** as a gameplay metaphor
- Helps test **fallibility of system memory** or signal propagation decay
- May feed into:
  - `memory_ai` recovery logic
  - `sentinel_ai` escalation when trace loops silently drop
  - Post-phase diagnostics where orphaned recursion needs audit

---

## 🔁 Design Echoes

- Builds on the **"trivial closure" pattern** from `s0_0`
- Sets the stage for `s0_2` (unobserved triggers) and `s0_3` (misaddressed returns)

---

## 🧩 Status

| Element              | Value        |
|----------------------|--------------|
| Logic Implemented    | ✅ Yes       |
| Tests Passed         | ✅ Yes       |
| Trace Decay Modeled  | ✅ Accurate  |
| Ready for Next Node  | ✅ Proceed   |
