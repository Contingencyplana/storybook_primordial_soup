<!-- Save to: a0_2_the_flag_that_was_never_checked/subtaskmap.md -->

# 🐛 Subtaskmap – a0_2_the_flag_that_was_never_checked  
*The Condition That Slept Forever*

# Path: a0_2_side_quest_of_the_forgotten_loop/a0_2_the_flag_that_was_never_checked

---

## 📜 Poetic Purpose

This stanza captures the **silent recursion**:  
The condition that was triggered...  
but never read.  
The fallback that waited...  
but was never needed.  
The flag that **was set**,  
but **was never checked**.

In a recursive system, silence is not safety.  
Sometimes, silence is **a forgotten call to action**.

---

## 🧠 Functional Summary

- Accepts a `state` dictionary with:
  - `flag_set` (bool)
  - `checked` (bool)
  - `flag_name` (str)
- Returns:
  - Whether the flag was ever verified
  - Whether dormant risks exist
  - Whether action is still required

---

## 🚩 Flag Logic Reference

| Scenario                       | Output Status     | Risk                     | Action Required |
|--------------------------------|-------------------|--------------------------|-----------------|
| `flag_set = True`, `checked = False` | ⚠️ Unchecked        | Dormant hazard present     | ✅ Yes           |
| `flag_set = True`, `checked = True`  | ✅ Verified         | None                     | ❌ No            |
| `flag_set = False`, `checked = True` | 🔘 Not Set         | None                     | ❌ No            |
| `flag_set = False`, `checked = False`| 🔘 Not Set         | None                     | ❌ No            |

---

## 🪞 Recursive Implication

This line encodes a core recursion truth:  
> A system that sets a flag **but forgets to query it**  
> is a system that cannot prevent collapse.

This prepares the logic bedrock for:
- Flag-driven fallback logic
- AI self-check patterns
- Safety conditions and recursion gates

---

## 📂 Folder Structure

```plaintext
a0_2_the_flag_that_was_never_checked/
├── main.py         # Flag state evaluation logic
├── test.py         # CLI flag testing simulator
└── subtaskmap.md   # (this file)
