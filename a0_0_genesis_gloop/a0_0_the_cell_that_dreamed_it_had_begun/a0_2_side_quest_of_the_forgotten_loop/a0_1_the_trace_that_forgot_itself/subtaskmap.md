<!-- Save to: a0_1_the_trace_that_forgot_itself/subtaskmap.md -->

# 🐛 Subtaskmap – a0_1_the_trace_that_forgot_itself  
*The Memory That Repeated, But Didn’t Remember Why*

# Path: a0_2_side_quest_of_the_forgotten_loop/a0_1_the_trace_that_forgot_itself

---

## 📜 Poetic Purpose

The loop didn’t close — but something repeated.  
Not once. Not clearly. Not with intent.  
But enough for the swarm to ask:

> "Have we seen this step before?"

This stanza tracks a recursion that **repeats**,  
but **cannot recall its reason for doing so.**

Where the loop that almost closed failed from structure,  
this one fails from **memory**.

---

## 🧠 Functional Summary

- Accepts a **list of symbolic trace steps**
- Checks if `"origin"` exists (explicit recursion root)
- Detects **cyclic behavior** — repetition of prior steps
- Flags **ghost entries** (`"???"`) as corrupted memory
- Returns diagnostic metrics for recursion agents

---

## 🪞 Key Memory Conditions

| Scenario                                  | Detected As       | Implication                                |
|------------------------------------------|-------------------|---------------------------------------------|
| Starts with `"origin"`                   | `origin_found: True` | Structured trace with a known root      |
| Contains repeated steps                  | `cyclic: True`    | Memory loop or recursion with drift         |
| Contains `"???"` in entries              | `ghost_entries: True` | Fragmented or corrupted memory trace  |
| Only unique and valid items              | All False except status | Clean trace, no errors               |

---

## 🧬 Recursive Implication

This stanza marks the **first appearance of memory ghosts** in the system:
- Traces that know *something* happened
- But forget *why* or *when*

It prepares future systems for:
- **Loop healing**
- **Orphaned signal repair**
- **Recursive memory re-indexing**

---

## 📂 Folder Structure

```plaintext
a0_1_the_trace_that_forgot_itself/
├── main.py         # Trace memory analysis logic
├── test.py         # CLI interface to input trace logs
└── subtaskmap.md   # (this file)
