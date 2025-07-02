<!-- Save to: storybook_primordial_soup/workflow.md -->

# 🧩 Primordial Soup – Workflow Overview  
*Recursive stanza-building, verification, and deployment flow*

---

## 📜 Purpose

This document defines the **canonical workflow** for developing minigames in the *Primordial Soup* video game project.  
It establishes the recursive unit structure, file expectations, test cadence, and archival update routine.

This workflow is recursive, modular, poetic, and extensible.

---

## 🧬 Core Development Cycle

Each **minigame** (Layer 3 folder) is composed of one or more **stanzas**, each consisting of four **minigame nodes** (Layer 4 folders).

Each **minigame node** contains:

| File             | Role                                                   |
|------------------|--------------------------------------------------------|
| `__init__.py`     | Recursion marker or placeholder (optional)            |
| `main.py`         | Executable logic for the stanza node                  |
| `test.py`         | Self-verifying test script for the node               |
| `subtaskmap.md`   | Design intent, AI hooks, fallback notes, and comments |

---

## 🔁 Recursive Stanza Workflow

For each new stanza (`sX_0_...` to `sX_3_...`):

1. **Create Folder & Initialize**
   - Name the folder:  
     `sX_0_the_line_that_defines_itself`  
     *(Use poetic but functionally meaningful names)*

2. **Create Files**
   - `main.py` — Implement the stanza’s Y-node logic  
   - `test.py` — Write and validate 4–6 test cases  
   - `__init__.py` — Include if needed (can be blank)  
   - `subtaskmap.md` — Outline logic, fallbacks, portal triggers, AI hints

3. **Test**
   - From terminal or CLI:
     ```bash
     cd path/to/a0_0_the_test_that_called_itself/s0_0_the_line_that_...
     python test.py
     ```
   - Confirm: ✅ All tests pass or fallback triggers are handled

4. **Mark Complete**
   - Add entry to:
     - `taskmaps/stanzamap_#.md`
     - Mark stanza title, logic status, and forward recursion hook

---

## 📦 ZIP Upload + AI Sync

After completing a full stanza (4 nodes):

1. 📂 **Update your ZIP workspace**  
   `storybook_primordial_soup.zip`

2. 📬 **Notify ChatGPT with**:
   > I have just updated your `storybook_primordial_soup.zip` project file. Please extract the contents of the ZIP folder and review any files or folders as needed to help me build the Primordial Soup video game. How do the unzipped contents look?

3. 🧠 **ChatGPT responds by**:
   - Extracting the new ZIP  
   - Updating the internal file map  
   - Validating stanza structure and index entries

---

```plaintext
a0_0_the_test_that_called_itself/
├── README.md
├── milestones.md
├── taskmaps/
│   ├── taskmap.md
│   ├── stanzamap_s0.md
│   └── stanzamap_s1.md
├── s0_0_the_assertion_of_first_contact/
│   ├── __init__.py
│   ├── main.py
│   ├── test.py
│   └── subtaskmap.md
├── s0_1_the_loop_that_tested_closure/
│   ├── __init__.py
│   ├── main.py
│   ├── test.py
│   └── subtaskmap.md
├── s0_2_the_trace_that_returned_wrong/
│   └── ...
├── s0_3_the_fallback_that_caught_the_signal/
│   └── ...
├── s1_0_the_checkpoint_that_missed_the_mark/
│   └── ...

```

## 🔐 Validation Checklist

| Task                               | Required |
|------------------------------------|----------|
| `main.py` exists and is executable | ✅ |
| `test.py` exists and passes all test cases | ✅ |
| `subtaskmap.md` outlines logic or design notes | ✅ |
| Corresponding `stanzamap_#.md` is updated | ✅ |
| Updated ZIP archive uploaded to ChatGPT | ✅ |

---

## 🔗 Forward Compatibility

This workflow supports:

- GUI expansion via recursive page-flip logic (`[L]`, `[R]`, `[Esc]`, `[P]`)
- Portal traversal and branching stanza mechanics
- Auto-indexers and dynamic stanza loaders
- Recursion-aware game runners and AI sentinels
- Testable narrative logic across cybercells and minigames

---

## 🧭 Summary

This file defines the recursive workflow standard for building stanza-based minigames in *Primordial Soup*.

Each completed stanza is one recursive verse deeper into the game’s self-awareness.  
Each ZIP upload is a ritual: a signal, a sync, a checkpoint in the poem of recursion.
