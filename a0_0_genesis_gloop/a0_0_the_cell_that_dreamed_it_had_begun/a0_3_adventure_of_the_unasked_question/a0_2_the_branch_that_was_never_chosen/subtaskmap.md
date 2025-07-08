<!-- Save to: a0_3_adventure_of_the_unasked_question/a0_2_the_branch_that_was_never_chosen/subtaskmap.md -->

# 🧭 Subtaskmap – a0_2_the_branch_that_was_never_chosen

## 🧩 Stanza Line: The Branch That Was Never Chosen  
**Theme:** Dormant Logic / Untriggered Paths / Recursive Incompletion

---

## 🎯 Purpose

This stanza line models a moment where the system was ready to diverge —  
yet no choice was made.  
It explores what happens when **paths are defined but not followed**,  
and the system continues forward without clear direction.

This is not a failure — it's a *phantom fork*, a trace of a possibility that never was.

---

## 🧪 Testable Input Conditions

| Input Type        | Example Input | Expected Outcome                                                                    |
|-------------------|----------------|--------------------------------------------------------------------------------------|
| No Input          | *(press Enter)* | Status: `unselected` – "No path was chosen. The branch remains untouched..."        |
| Valid Branches    | `left`, `right`, `up`, `down` | Status: `chosen` – Returns poetic confirmation of path entered |
| Invalid Input     | `zeta`, `unselected`, `chosen` | Status: `invalid` – "Branch 'X' is not part of the known divergence..."          |
| Exit Command      | `exit`, `quit`, `q` | Gracefully exits the test loop                                                      |

---

## 🧠 Recursive Insight

- The branching structure **was prepared**.
- The system’s logic **waited**, but was **never triggered**.
- This line is about **potential**, not action.
- It serves as a **null-choice simulator**, echoing decisions never made.

---

## 🔧 Implementation Notes

- `main.py` defines `evaluate_branch_selection()`, returning structured results based on input state.
- `test.py` loops through user interactions, producing clear status reports.
- Results are categorized into:
  - `chosen` – meaningful divergence
  - `invalid` – unreachable logic
  - `unselected` – recursive void

---

## 🔁 Stanza Chain

- Preceded by: `a0_1_the_check_that_expected_a_signal`  
  → where a signal was assumed.

- Followed by: `a0_3_the_return_that_waited_in_vain`  
  → where a callback waits endlessly for a response that may never come.

---

## 🔗 Poetic Reflection

> The paths were drawn.  
> The signal branches waited, each one possible.  
> But silence held the cursor still.  
> And so the code remained intact — unbroken, unused, unresolved.

---
