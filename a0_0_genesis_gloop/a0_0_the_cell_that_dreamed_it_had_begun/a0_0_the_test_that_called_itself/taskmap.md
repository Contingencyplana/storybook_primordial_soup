<!-- Save to: a0_0_the_test_that_called_itself/taskmap.md -->

# 🧩 Taskmap – Very Basic Test Functionality  
*The Test That Called Itself*

---

## 📜 Purpose

This stanza line represents the **first recursive test structure** in Primordial Soup.  
It is not a metaphor — it is the recursion.  
It does not simulate the system — it is the system.  
It tests itself.

This line begins the **self-validating poetic recursion** that all future minigames may inherit.

---

## 🧠 Functional Logic

Each stanza line in this minigame contains two files:

| File | Purpose |
|------|---------|
| `main.py` | A playable Y-node in the world of Primordial Soup. |
| `test.py` | A battlefield test node that simulates input and reports outcomes. |

The `test.py` file:
- Prompts the player with `L`, `R`, or `Escape`,
- Calls and executes either:
  - This line’s `main.py`, or
  - The next stanza line’s `main.py`,
- Wraps results in a **“📜 Report from the Field”**,
- Falls back to other test nodes on failure.

---

## 🛡️ Failure Behavior

If a tested `main.py` file is **missing or broken**, `test.py` reports:

> ❌ "Your army suffers defeat and must retreat..."

It then:
- Falls back to another test node (based on fallback logic),
- Or marks the path for repair.

---

## 🔁 Reusability and Inheritance

This structure defines the **first Taskmap** of the game and can be imported by:
- Future minigames,
- Automated test walkers,
- AI-controlled sentinels,
- Patch utilities like `engineer.py`.

All minigames may clone or evolve this format.

---

## 📂 Poetry Line Folder Structure

a0_0_the_test_that_called_itself/ 
├── __init__.md                     # Initialization logic for the minigame (optional)
├── taskmap.md                      # Taskmap for the minigame (this file)
└── s0_0_the_assertion_of_first_contact/
    ├── __init__.py                 # Python init (optional)
    ├── main.py                     # Playable Y-node
    ├── subtaskmap.md               # Line-specific notes (optional)
    └── test.py                     # Interactive test interface (L/R/Escape)

---

## 🧬 Summary

This line begins the poem that tests itself.  
The bug wore a crown. The test called its name.  
From this seed, all future verifications bloom.
