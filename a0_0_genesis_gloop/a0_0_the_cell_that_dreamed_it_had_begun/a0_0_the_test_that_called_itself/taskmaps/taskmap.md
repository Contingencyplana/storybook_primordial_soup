
<!-- Save to: a0_0_the_test_that_called_itself/taskmap.md -->

# 🧩 Taskmap – Very Basic Test Functionality  
*The Test That Called Itself*

---

## 📜 Purpose

The first stanza line (`s0_0_the_assertion_of_first_contact`) initiated the **recursive test structure** in *Primordial Soup*.  
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
- Falls back to other test nodes on failure.

---

## 🛡️ Failure Behavior

If a tested `main.py` file is **missing or broken**, `test.py` reports:

> ❌ "Your army suffers defeat and must retreat..."

It then:
- Falls back to another test node (based on stanza logic),
- Or marks the path as broken for repair.

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
│   ├── stanzamap_s0.md             # Index of stanza 0  
│   ├── stanzamap_s1.md             # Index of stanza 1  
│   └── stanzamap_s2.md             # Index of stanza 2 (in progress)  
├── s0_0_the_assertion_of_first_contact/  
│   ├── __init__.py                 # Python init (optional)  
│   ├── main.py                     # Playable Y-node (executes test logic)  
│   ├── subtaskmap.md               # Line-specific notes (optional)  
│   └── test.py                     # Interactive test interface (L/R/Escape)  
└── ...                             # Additional stanza lines follow this format  

```

---

## 📖 List of Stanzas in This Minigame

| Stanza ID | Index File         | Description                                                            | Status         |
|-----------|--------------------|------------------------------------------------------------------------|----------------|
| `s0`      | `stanzamap_s0.md`  | The recursion began. It tested its own test.                           | ✅ Complete     |
| `s1`      | `stanzamap_s1.md`  | The checkpoint broke. The log forgot. The flag was raised too soon.    | ✅ Complete     |
| `s2`      | `stanzamap_s2.md`  | The assertion reversed. The loop refused. The trace arrived too late.  | 🧪 In Progress  |
| `s3`      | _TBD_              | The next recursive stanza — not yet spoken                             | ⏳ Pending      |

---

## 🧬 Summary

This stanza line begins the poem that tests itself.
The bug wore a crown. The test called its own name.
From this seed, all future verifications bloom.
