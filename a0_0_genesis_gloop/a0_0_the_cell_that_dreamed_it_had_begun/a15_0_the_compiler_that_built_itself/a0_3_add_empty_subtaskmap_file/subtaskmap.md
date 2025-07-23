<!-- Save to: a15_0_the_compiler_that_built_itself\a0_3_add_empty_subtaskmap_file\subtaskmap.md -->

# 🔹 Subtaskmap – a0_3_add_empty_subtaskmap_file

## 🧩 Purpose

This node performs the **fourth tiny step** in recursive minigame node construction.

It creates an empty `subtaskmap.md` file within the target minigame node folder.  
This file is used to document the specific purpose, logic, and structure of the node.

---

## 📂 Outputs

- Creates a blank `subtaskmap.md` in the target minigame node folder.

```plaintext
📁 a99_0_test_create_minigame_node/
└── 📁 a0_0_test_minigame_node/
    └── 📄 subtaskmap.md
```

## 🔧 Actions

| **Step** | **Action** |
|----------|------------|
| 1️⃣ | Confirm the target minigame node folder exists. |
| 2️⃣ | Check if `subtaskmap.md` already exists — avoid overwriting. |
| 3️⃣ | Create the file with a comment header placeholder. |
| 4️⃣ | Return a structured trace log of the action performed. |

---

## 🌀 Recursive Role

This node enables traceable documentation of recursive logic **per node**.  
It provides a writable space for future automated compilers to embed logic or notes.

---

## ⚙️ System Integration

**Nodal Sequence:**  
Follows `a0_2_add_empty_main_file`.  
Precedes `a1_0_add_empty_test_file`.

**Meta-Recursive Compiler:**  
This node gives future builder loops a defined insertion point for recursive role descriptions.

**Fallback Safety:**  
If `subtaskmap.md` already exists, this task will skip safely and log the status.

---

## 🧪 Test Coverage

- Ensure the file is created only if it does not already exist.  
- Confirm placeholder content (`<!-- Subtaskmap placeholder for recursive node documentation -->`) is correctly written.  
- Validate returned trace includes:
  - File creation status  
  - Path confirmation  
  - Timestamp  
  - Event type: `create_subtaskmap` or `skip_existing_subtaskmap`

---

## 🔖 Notes

This node adheres to the **Tiny Step Recursion Doctrine**, reinforcing that **every node documents itself**.  

Future introspection tools may reference this file when mapping or summarizing recursive execution paths.
