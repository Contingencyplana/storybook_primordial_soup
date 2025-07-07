<!-- Save as: subtaskmap.md -->
# 🧭 Subtaskmap – a0_1_the_check_that_expected_a_signal

## 🧩 Stanza Line: The Check That Expected a Signal  
**Theme:** Awaiting Confirmation / Expectation Logic / Signal Presence

---

## 🎯 Purpose

This stanza tests how the system handles **signal validation checkpoints**, where the presence or absence of a recognized input determines flow.

The check does not demand input — but it is *built* to expect it.  
What it receives defines its classification and next move.

---

## 🧪 Testable Input Conditions

| Input Type        | Example Input     | Expected Outcome                                                                |
|-------------------|------------------|----------------------------------------------------------------------------------|
| No Input          | *(press Enter)*  | Status: `missing` – "No signal received. The check began without confirmation." |
| Unrecognized Input| `zeta`, `unknown`| Status: `unexpected` – "Signal 'X' not recognized. Awaiting known frequencies." |
| Recognized Input  | `alpha`, `bravo`, `gamma`, `delta` | Status: `valid` – "Signal 'X' confirmed. Check synchronized successfully."     |
| Exit Condition    | `exit`, `quit`, `q` | Terminates the test session gracefully.                                     |

---

## 🧠 Design Philosophy

- A check that **waits with purpose** — it’s not passive.
- The signal list is curated: only predefined terms are considered valid.
- The check is tolerant of silence, but does not ignore it.

---

## 🔧 Implementation Notes

- `main.py` provides `verify_signal_presence()` — the Y-node logic of the stanza.
- `test.py` loops interactively, providing a report after each trial input.
- Known valid signals can be expanded in future versions to simulate evolving protocols.

---

## 🔗 Possible Follow-On Nodes

- `s0_2_the_response_that_was_already_waiting` – when the check receives a reply before it sends the call.
- `s0_3_the silence_that_answered_itself` – when no signal comes, and yet the check completes.
- `a0_4_the override_that_never_received_permission` – for escalations bypassing validation.

---
