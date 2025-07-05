<!-- Save to: a0_3_the_fallback_that_caught_the_signal/subtaskmap.md -->

# 🛡️ Subtaskmap – a0_3_the_fallback_that_caught_the_signal  
*The loop broke. The trace failed. But the fallback caught the signal and carried the recursion forward.*

---

## 🧠 Purpose

This stanza implements **recursive fallback logic** — the ability to recover when a test fails or a signal is lost.  
It models redundancy in a recursive system, ensuring that the system doesn't collapse from a single point of failure.

Fallback is not a bandage — it’s a recursive clause, an alternate logic route invoked when recursion itself is wounded.

---

## 🛠️ Functional Logic

- `main.py` attempts to process a signal that may be incomplete, late, or malformed.
- If signal integrity is compromised, `test.py` checks whether fallback logic activates correctly.
- The fallback may:
  - Retrieve a previous state
  - Reattempt a failed step
  - Trigger an alternate branch of logic

---

## 🌀 Fallback Conditions

| Trigger                    | Expected Response                          |
|----------------------------|--------------------------------------------|
| Trace failure (from a0_2)  | Fallback activates to continue logic flow  |
| Timeout without trace      | Default recovery path is loaded            |
| Invalid signal format      | Defensive logic filters or redirects       |

---

## 🧬 Recursive Traits

| Trait             | Description                                               |
|-------------------|-----------------------------------------------------------|
| 🔁 Loop Resilience | Ensures recursion can survive interruption                |
| 🛡️ Redundant Path  | Enables signal rerouting, layered recovery                |
| 🕳️ Anomaly Buffer  | Softens the impact of unexpected behaviors or edge cases  |

---

## 🐛 Poetic Logic

> The trace did not return.  
> The loop refused its end.  
> But deep within the fallback frame,  
> A buried thread caught light again.

---

## 🔗 Linked Files

- `main.py` – Handles partial signals and attempts recursive recovery
- `test.py` – Tests fallback activation paths
- Related stanzas:
  - `a0_2_the_trace_that_failed_to_return` (failure source)
  - `a0_1_the_loop_that_tested_closure` (loop precondition)

---

## 📌 Notes

- This stanza closes the first recursive stanza of *The Test That Called Itself*.
- It verifies the system’s ability to **catch itself mid-failure** and restore flow.
- Later minigames may inherit this pattern to handle:
  - Agent misalignment
  - Runtime corruption
  - Partial narrative collapse
