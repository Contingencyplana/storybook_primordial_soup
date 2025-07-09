<!-- Save to: subtaskmap.md -->

# 🧭 Subtaskmap – a0_1_the_choice_that_predated_its_trigger

## 🎯 Purpose

This stanza line explores **causal inversion** —  
where a system **remembers a decision before it was made**,  
and behaves as if a player has already chosen an option  
never presented to them.

It is a test of **false determinism** and pre-emptive system behavior.

---

## ⚙️ Function Tested

```python
evaluate_choice(memory_log, presented_options)
```

- Detects whether the system already holds a **“remembered” choice**.
- If memory exists but no current prompt is active, flags it as **predated**.
- Determines if the remembered choice is:
  - **Valid** (from a future set)
  - **Invalid** (never truly available)

## 🧪 Sample Inputs & Expected Output

| Memory Log         | Presented Options             | Preselection Detected  | Outcome Type         |
|--------------------|-------------------------------|------------------------|----------------------|
| ["red pill"]       | ["blue pill", "green pill"]   | ✅                     | Invalid pre-choice   |
| ["green pill"]     | ["blue pill", "green pill"]   | ✅                     | Valid pre-choice     |
| []                 | ["wait", "run"]               | ❌                     | No memory conflict   |

## 📂 File Behavior Overview

- `main.py` contains the logic to check if the choice was made *before* the options were shown.
- `test.py` simulates an interactive session:
  - Option set is revealed
  - Player is told what choice the system already remembers

## 🔄 Failure Conditions

- If the system **acts on remembered choices not yet made**,  
  it may override true player intent.

- If it **rejects valid late input** because it believes a choice was already confirmed,  
  the player’s agency is compromised.

This test helps identify improper **chronological leakage** between decision and prompt.

## 🎭 Reflection Cue

> “I remember choosing this.  
> But I never saw the options.”
