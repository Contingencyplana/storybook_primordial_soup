<!-- Save to: a15_0_the_compiler_that_built_itself\a0_2_add_empty_main_file\subtaskmap.md -->

# 🔹 Subtaskmap – a0_2_add_empty_main_file

## 🧩 Purpose

This node performs the **third tiny step** in recursive minigame node construction.

It creates an empty `main.py` file inside the specified minigame node folder.  
This file is a placeholder for future node logic and execution entrypoints.

> ✅ Note: Intermediate folders must already exist before this node runs.

---

## 📂 Outputs

- Adds an empty `main.py` file to the target minigame node folder.

```plaintext
📁 a99_0_test_create_minigame_node/
└── 📁 a0_0_test_minigame_node/
    └── 📄 main.py
```

---

## 🔧 Actions

| **Step** | **Action** |
|----------|------------|
| 1️⃣ | Confirm the target minigame node folder exists. |
| 2️⃣ | Check if `main.py` already exists — avoid overwriting. |
| 3️⃣ | Create the file with a basic placeholder comment. |
| 4️⃣ | Return a structured trace log of the action performed. |

---

## 🌀 Recursive Role

This node ensures every minigame node has a valid `main.py` entrypoint.  
It supports recursive orchestration, test harness injection, or manual execution.

This entrypoint becomes the **runtime shell** into which higher-level logic may later be injected, linked, or scheduled.

---

## ⚙️ System Integration

**Nodal Sequence:**  
- Follows: `a0_1_add_empty_init_file`  
- Precedes: `a0_3_add_empty_subtaskmap_file`

**Meta-Recursive Compiler Role:**  
- Used by `workflow_compiler.py` or `main.py` orchestrators.  
- Enables compatibility with:
  - `recursive_executor.py`  
  - `logic_injector.py`  
  - `linker.py`

**Fallback Safety:**  
- Skips creation if `main.py` already exists.  
- Logs a `skip_existing_main` event in the trace log.

**Path Compatibility:**  
- Fully supports sandboxed and nested minigame paths (e.g., `a99_0/.../a0_0_test_minigame_node`).

---

## 🧪 Test Coverage

Tests confirm that:

- The file is only created if it doesn’t already exist.  
- The placeholder content matches:  
  `# Main execution file for minigame node`  
- The returned trace includes:
  - `status` (success or skipped)  
  - `path` to the file  
  - `timestamp` (in UTC)  
  - `event` (create_main_file or skip_existing_main)

---

## 🔖 Notes

This node adheres to the **Tiny Step Recursion Doctrine**.  
It is not just a placeholder — it is the **formal execution anchor** for all recursive builders.

Without this file, logic orchestrators cannot route signals, run stanzas, or inject behavioral code into a node.

Its presence ensures every node in the system is **executable**, **traceable**, and **upgradeable**.
