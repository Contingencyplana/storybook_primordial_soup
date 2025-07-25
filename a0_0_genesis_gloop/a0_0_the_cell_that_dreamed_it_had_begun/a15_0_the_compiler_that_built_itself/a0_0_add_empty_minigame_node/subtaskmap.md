<!-- Save to: a15_0_the_compiler_that_built_itself\a0_0_add_empty_minigame_node\subtaskmap.md -->

# 🔹 Subtaskmap – a0_0_add_empty_minigame_node

## 🧩 Purpose

This node performs the **first tiny step** in recursive minigame node construction.

It creates the outermost folder of a minigame node using a nested path, ensuring all intermediate folders are created if needed.

The folder is empty by design — it is the seed of recursion, from which all other node scaffolds will grow.

---

## 📂 Outputs

- Creates the outer minigame node folder at a recursive nested path.

Example:

```plaintext
📁 a99_0_test_create_minigame_node/
└── 📁 a0_0_test_minigame_node/
```

> **Note:** Intermediate folders (like `a99_0_test_create_minigame_node`) are created automatically.

---

## 🔧 Actions

| **Step** | **Action** |
|----------|------------|
| 1️⃣ | Accept a nested folder path (e.g., `a99_0/.../a0_0_...`) as input. |
| 2️⃣ | Create all missing parent folders if they don’t exist. |
| 3️⃣ | Check if the final target node folder already exists — prevent overwrite. |
| 4️⃣ | If not, create the folder and return a structured trace. |
| 5️⃣ | If it exists, return a trace with `"status": "skipped"`. |

---

## 🌀 Recursive Role

This node begins the **Tiny Step Compiler Loop**. It is the root constructor for all Layer 4 scaffolds.

By handling nested path creation and validating existence, it ensures:

- Minigame nodes are safe to build without collisions  
- Higher-order builders can assume a consistent folder base  
- All subsequent node steps have a guaranteed location  

---

## ⚙️ System Integration

- **Nodal Sequence:**  
  This node comes **first** in the compiler loop. It must succeed before any others run.

- **Meta-Recursive Compiler:**  
  Used by `workflow_compiler.py`, `main.py` in orchestration nodes, or manually in development testing.

- **Fallback Safety:**  
  Folder creation is idempotent. If the folder already exists, the node will exit cleanly and log a `skip_existing_minigame_node` trace.

- **Path Compatibility:**  
  ✅ Fully supports nested paths and automatic creation of intermediate directories.

---

## 🧪 Test Coverage

Tests for this node will:

- Confirm a new node folder is created if it doesn’t exist  
- Confirm that re-running skips creation with `"status": "skipped"`  
- Ensure proper handling of deeply nested target paths  
- Validate the structure of the returned trace dictionary:  
  - `status` field  
  - `message` summary  
  - `timestamp` in UTC  
  - `event`: either `create_empty_minigame_node` or `skip_existing_minigame_node`  

---

## 🔖 Notes

This step lays the **foundational recursion anchor** for every minigame node.

Future layers will rely on this seed to expand safely.  
It represents the **primordial node shell** — the silent ancestor from which structure emerges.

Supports both canonical and test minigames equally (e.g., `a12_3/...`, `a99_0/...`, etc.).
