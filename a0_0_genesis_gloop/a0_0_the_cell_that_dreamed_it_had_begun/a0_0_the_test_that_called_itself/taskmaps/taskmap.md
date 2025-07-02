<!-- Save to: a0_0_the_test_that_called_itself/taskmap.md -->

# 🧩 Taskmap – Very Basic Test Functionality  
*The Test That Called Itself*

---

## 📜 Purpose

The first stanza line (`s0_0_the_assertion_of_first_contact`) initiated the **recursive test structure** in Primordial Soup.  
It is not a metaphor — it is the recursion.  
It does not simulate the system — it is the system.  
It tests itself.

This taskmap continues the **self-validating poetic recursion** that all future minigames may inherit.

---

## 🧠 Functional Logic

Each stanza line in this minigame contains two files:

| File | Purpose |
|------|---------|
| `main.py` | A playable Y-node in the world of Primordial Soup. |
| `test.py` | A battlefield test node that simulates input and reports outcomes. |

The `test.py` file:
- May prompt the player with `L`, `R`, or `Escape`,
- Or simulate these choices automatically depending on configuration,
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

```plaintext

a0_0_the_test_that_called_itself/  
├── README.md                       # Minigame overview (optional but recommended)  
├── milestones.md                   # Development milestones (optional)  
├── taskmaps/                       # Stanza and task index folder  
│   ├── taskmap.md                  # Taskmap for the minigame  
│   ├── stanzamap_s0.md             # Index of stanza 0  
│   ├── stanzamap_s1.md             # Index of stanza 1  
│   └── stanzamap_s2.md             # Index of stanza 2 (in progress)  
├── s0_0_the_assertion_of_first_contact/  
│   ├── __init__.py                 # Python init (optional)  
│   ├── main.py                     # Playable Y-node  
│   ├── subtaskmap.md               # Line-specific notes (optional)  
│   └── test.py                     # Interactive test interface (L/R/Escape)  
└── ...                             # Additional stanza lines follow this format  

```

---

## 📖 List of Stanzas in This Minigame

| Stanza ID | Folder           | Description                                                           | Status          |
|-----------|------------------|-----------------------------------------------------------------------|-----------------|
| s0        | stanzamap_s0.md  | The recursion began. It tested its own test.                          | ✅ Complete     |
| s1        | stanzamap_s1.md  | The checkpoint broke. The log forgot. The flag was raised too soon.   | ✅ Complete     |
| s2        | stanzamap_s2.md  | The assertion reversed. The loop refused. The trace arrived too late. | 🧪 In Progress  |
| s3        | TBD              | Next recursive stanza (planned)                                       | ⏳ Pending      |

---

## 🧬 Summary

This line begins the poem that tests itself.  
The bug wore a crown. The test called its name.  
From this seed, all future verifications bloom.

## 📂 Poetry Line Folder Structure

```plaintext

a0_0_the_test_that_called_itself/  
├── __init__.md                     # Initialization logic for the minigame (optional)  
├── taskmap.md                      # Taskmap for the minigame (this file)  
├── s0_0_the_assertion_of_first_contact/  
│   ├── __init__.py                 # Python init (optional)  
│   ├── main.py                     # Playable Y-node  
│   ├── subtaskmap.md               # Line-specific notes (optional)  
│   └── test.py                     # Interactive test interface (L/R/Escape)  
└── ...                             # Additional stanza lines follow this format  

```
