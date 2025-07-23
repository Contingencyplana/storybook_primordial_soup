<!-- Save to: a15_0_the_compiler_that_built_itself\a2_0_add_empty_taskmaps_folder\subtaskmap.md -->

# 🔹 Subtaskmap – a2_0_add_empty_taskmaps_folder

## 🧩 Purpose

This node performs the **seventh recursive compiler step** in minigame construction.  
It initiates the **taskmaps scaffolding phase** by creating the `taskmaps/` folder inside the current minigame node.  
This step lays the groundwork for all task-level documentation and recursive trace mapping.

Once in place, the `taskmaps/` folder will hold:
- `milestones.md` (next node)
- `README.md` and `stanzamap_#.md` (future nodes)
- Recursive planning and introspective analysis tools

---

## 📂 Outputs

- Creates a `taskmaps/` folder inside the local minigame node directory.
- Ensures the folder exists without overwriting or duplicating.
- Confirms folder creation through a structured trace event.

```plaintext
📂 taskmaps/
├── ⏳ milestones.md         # (a2_2)
├── 📘 README.md             # (a2_3)
├── 🧭 stanzamap_0.md        # (a3_0)
├── 🔧 subtaskmap.md         # (a2_0 - this file)
```

## 🔧 Actions

| **Step** | **Action** |
|----------|------------|
| 1️⃣ | Check for existence of `taskmaps/` directory. |
| 2️⃣ | If missing, create it. |
| 3️⃣ | If present, skip creation (idempotent behavior). |
| 4️⃣ | Log a trace with timestamp and event type. |
| 5️⃣ | Return result indicating whether the folder was added or skipped. |

---

## 🌀 Recursive Role

This node begins the **task-level orchestration** phase of the compiler.  
It separates **nodal tooling** (`a0_#` and `a1_#`) from **meta-documentation** (`a2_#` and `a3_#`),  
enabling stanzas and minigames to support:

- Internal planning  
- Output mapping  
- Introspective analysis  
- Schema-based enforcement (future stanzas)

It is the first step where the compiler documents *why* something exists — not just *what* was built.

---

## ⚙️ System Integration

**Nodal Sequence:**  
Follows `a1_3_placeholder` (completes nodal setup phase).  
Precedes `a2_1_add_empty_init_file` (for taskmaps logic encapsulation).

**Meta-Recursive Compiler Role:**  
Begins the second major compiler domain — `taskmaps/`.  
Provides structure for future indexers, dashboards, and trace analyzers.

---

## 🧪 Test Coverage

This node should be tested to ensure:

- `taskmaps/` is created inside the active minigame node folder  
- Existing folders are safely detected and skipped  
- Output result reflects actual action taken (added vs skipped)  
- Trace output includes:  
  - Folder path  
  - Event type: `created_taskmaps_folder`  
  - UTC timestamp  

---

## 🔖 Notes

This is a **structure-critical node**.  
Every minigame must have a `taskmaps/` folder, even if temporarily empty.

Creating it as a standalone compiler step ensures:

- Future tooling can rely on its presence  
- All planning files and indexes remain centralized  
- Placeholder integrity is preserved, even during partial builds

Failure to include this node would break **recursive traceability**  
and derail **stanza-wide introspection**.

This node ensures the compiler has a place to **plan** — not just build.
