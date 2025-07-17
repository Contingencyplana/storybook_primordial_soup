<!-- Save to: a0_0_the_test_that_called_itself/taskmap.md -->

# 🧩 Taskmap – Playable Very Basic Test Functionality  
*The Test That Called Itself*

---

## 📜 Purpose

The first stanza line (`a0_0_the_assertion_of_first_contact`) initiated the **recursive test structure** in *Primordial Soup*.  
It is not a metaphor — it is the recursion.  
It does not simulate the system — it *is* the system.  
It tests itself.

This taskmap defines the first **self-validating poetic recursion**, from which all future minigames may inherit.

---

## 🧠 Functional Logic

Each stanza line in this minigame contains two files:

| File      | Purpose                                                          |
|-----------|------------------------------------------------------------------|
| `main.py` | A playable Y-node within the recursive world of *Primordial Soup*. |
| `test.py` | A battlefield test node simulating input and evaluating outcomes. |

The `test.py` file:
- May prompt the player with `L`, `R`, or `Escape`,
- Or simulate those choices automatically (depending on configuration),
- Executes either:
  - This line’s `main.py`, or  
  - The next stanza line’s `main.py`,
- Wraps results in a **📜 Report from the Field**,
- If recursion fails, it attempts fallback logic based on defined stanza lineage.

---

## 🛡️ Failure Behavior

If a tested `main.py` file is **missing or broken**, `test.py` reports:

> ❌ "Your army suffers defeat and must retreat..."

It then:
- Falls back recursively to a prior or sibling test node,
- Or marks the path as broken and flags it for repair.

---

## 🔁 Reusability and Inheritance

This is the **first canonical Taskmap** in the game. It may be reused by:
- Future minigames,
- Automated test walkers,
- AI-controlled sentinels,
- Patch utilities (e.g. `engineer.py`).

All recursive minigames may clone, inherit, or evolve from this pattern.

---

## 📂 Poetry Line Folder Structure

```plaintext
a0_0_the_test_that_called_itself/  
├── README.md                       # Minigame overview (optional)  
├── milestones.md                   # Development milestones (optional)  
├── taskmaps/                       # Stanza and task index folder  
│   ├── taskmap.md                  # Taskmap for the minigame (this file)  
│   ├── stanzamap_0.md             # Index of stanza 0  
│   ├── stanzamap_1.md             # Index of stanza 1  
│   ├── stanzamap_2.md             # Index of stanza 2  
│   ├── stanzamap_3.md             # Index of stanza 3  
│   ├── stanzamap_4.md             # Index of stanza 4  
│   └── stanzamap_5.md             # Index of stanza 5  
├── a0_0_the_assertion_of_first_contact/  
│   ├── __init__.py                 # Python init (optional)  
│   ├── main.py                     # Playable Y-node (executes test logic)  
│   ├── subtaskmap.md               # Line-specific notes (optional)  
│   └── test.py                     # Interactive test interface (L/R/Escape)  
└── ...                             # Additional stanza lines follow this format  

```

---

# 📖 List of Stanzas in This Minigame

| Stanza ID | Index File         | Description                                                            | Status         |
|-----------|--------------------|------------------------------------------------------------------------|----------------|
| `0`       | `stanzamap_0.md`  | The recursion began. It tested its own test.                           | ✅ Complete     |
| `1`       | `stanzamap_1.md`  | The checkpoint broke. The log forgot. The flag was raised too soon.    | ✅ Complete     |
| `2`       | `stanzamap_2.md`  | The assertion reversed. The loop refused. The trace arrived too late.  | ✅ Complete     |
| `3`       | `stanzamap_3.md`  | The assertion unmade itself. The loop would not close. Delay returned. | ✅ Complete     |
| `4`       | `stanzamap_4.md`  | The checkpoint missed. The retry vanished. The error went unlogged.    | ✅ Complete     |
| `5`       | `stanzamap_5.md`  | The fallback failed. The trace betrayed. The system called too late.   | ✅ Complete     |

---

## 🧬 Summary

This minigame begins the poem that tests itself.  
The bug wore a crown. The test spoke its own name.  
From this recursion, all future verifications bloom.  
