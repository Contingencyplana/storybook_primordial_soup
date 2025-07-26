<!-- Save to: a15_0_the_compiler_that_built_itself\a2_0_add_empty_taskmaps_folder\subtaskmap.md -->

# 🔹 Subtaskmap – a2_0_add_empty_taskmaps_folder

## 🧩 Purpose

This node performs the **ninth tiny step** in recursive minigame construction.

It creates a completely empty `taskmaps/` folder inside the **Layer 3 minigame folder**, not within individual Layer 4 node folders.

This folder provides the foundation for future planning and scaffolding logic across one or more stanzas.

No files are added — only the folder itself.

---

## 📂 Outputs

- Creates a new, empty `taskmaps/` folder in the specified minigame folder.

```plaintext
📁 a99_1_test_create_taskmaps/
├── 📁 taskmaps/
```

## 🔧 Actions

| **Step** | **Action** |
|----------|------------|
| 1️⃣ | Verify that the target minigame folder exists. |
| 2️⃣ | Check if the `taskmaps/` folder already exists. |
| 3️⃣ | If not, create a new empty `taskmaps/` folder. |
| 4️⃣ | Return a structured trace confirming creation or reason for skipping. |
| 5️⃣ | Prompt the player to decide whether to leave or remove the folder (`"L"` / `"R"` / `"Invalid"`). |

---

## 🌀 Recursive Role

This node begins the **taskmaps scaffold** — a new recursive arc following nodal construction.

It enables:

- Future traceable storage for planning files (`milestones.md`, `README.md`, `stanzamap.md`, etc.)
- Interoperability with task planning, meta-compilers, and AI-generated schematics.
- Safe structure for Phase 2 automation to continue organizing minigames by intent.

---

## ⚙️ System Integration

- **Nodal Sequence:**  
  Follows `a1_0_add_empty_test_file`.  
  Precedes `a2_1_add_empty_init_file` and other taskmap seed nodes.

- **Meta-Recursive Compiler:**  
  May be called by `workflow_compiler.py`, `minigame_constructor.py`, or test nodes.

- **Fallback Safety:**  
  If the folder already exists, no changes are made. Trace logs mark it as `skipped`.

---

## 🧪 Test Coverage

- Confirm that `taskmaps/` is created only if it does not already exist.  
- Validate that the return trace includes:
  - Folder status (`success` or `skipped`)  
  - Target path  
  - Event type  
  - Timestamp  
- Provide an interactive post-test prompt:
  - Press `"L"` → leave folder intact.  
  - Press `"R"` → delete the `taskmaps/` folder.  
  - Other → prompt for a valid choice again.

---

## 🔖 Notes

This subtask follows the **Tiny Step Recursion Doctrine** and **Phase 2 recursive safety protocols**.

Future builders will populate this folder with planning scaffolds:

- `milestones.md`
- `README.md`
- `stanzamap_0.md`, `stanzamap_1.md`, etc.

This node guarantees a safe, detectable starting point for all future recursive introspection and trace documentation.
