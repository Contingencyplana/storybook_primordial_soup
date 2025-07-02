<!-- Save to: workflow.md -->

# 🧩 Primordial Soup – Workflow Overview  
*Recursive stanza-building, verification, and deployment flow*

---

## 📜 Purpose

This document defines the **canonical workflow** for developing minigames in the Primordial Soup video game project.  
It establishes the recursive unit structure, file expectations, test cadence, and archival update routine.

This workflow is recursive, modular, poetic, and extensible.

---

## 🧬 Core Development Cycle

Each **minigame** (Layer 3 folder) is composed of multiple **stanzas**, each consisting of four **minigame nodes** (Layer 4 folders).

Each **minigame node** consists of four files:

| File | Role |
|------|------|
| `__init__.py` | Recursion marker or placeholder (optional) |
| `main.py` | Executable Y-node logic |
| `test.py` | Self-verifying test node |
| `subtaskmap.md` | Design intent, AI hooks, and line commentary |

---

## 🔁 Recursive Stanza Workflow

For each new stanza (`sX_0_...` to `sX_3_...`):

1. **Create Folder & Initialize**
   - Create a folder named:  
     `sX_0_the_line_that_defines_itself`  
     (Use poetic and functional naming)

2. **Create Files**
   - `main.py` — Implement the logic for the Y-node
   - `test.py` — Write and validate 4–6 test cases
   - `__init__.py` — Add if needed (can be blank)
   - `subtaskmap.md` — Outline logic, fallbacks, portal triggers, etc.

3. **Test**
   - Navigate to folder via CLI:
     ```bash
     cd path\to\minigame\sX_0_the_line_that_...
     python test.py
     ```
   - Confirm: ✅ All tests pass (or fallback works)

4. **Mark Complete**
   - Add entry to:
     - `taskmaps/stanzamap_sX.md`
     - Mark logic status, poetic framing, forward hook

---

## 📦 ZIP Upload + AI Sync

After completing a stanza (4 nodes):

1. 📂 **Update your ZIP workspace**  
   (`storybook_primordial_soup.zip`)

2. 📬 **Message ChatGPT with**:
   > I have just updated your `storybook_primordial_soup.zip` project file. Please extract the contents of the ZIP folder and review any files or folders as needed to help me build the Primordial Soup video game. How do the unzipped contents look?

3. 🧠 **ChatGPT syncs and confirms**:
   - Extracts ZIP
   - Updates internal structure map
   - Validates stanza index and taskmap presence

---

## 📂 Folder Layout Example

```
a0_0_the_test_that_called_itself/
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
├── s0_2_...
├── s0_3_...
├── s1_0_the_checkpoint_that_missed_the_mark/
│   └── ...
```

---

## 🔐 Validation Checklist

| Task | Required |
|------|----------|
| `main.py` exists and is executable | ✅ |
| `test.py` exists and passes all tests | ✅ |
| `subtaskmap.md` outlines design notes | ✅ |
| `stanzamap_sX.md` updated | ✅ |
| ZIP archive uploaded to ChatGPT | ✅ |

---

## 🔗 Forward Compatibility

This workflow supports:
- GUI expansion via storybook-flip logic (L/R/Escape)
- Portal/branch mechanics
- Auto-indexers and stanza loaders
- Recursion-aware game runners and AI sentinels
- Testable narrative logic across cybercells

---

## 🧭 Summary

This file defines the recursive workflow standard for building stanza-based minigames in Primordial Soup.

Every stanza completed is one recursive verse further into the game’s self-awareness.  
Every ZIP upload is a ritual: a signal, a sync, a checkpoint in the poem of recursion.