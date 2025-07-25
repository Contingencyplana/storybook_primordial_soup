# 🧠 Subtaskmap – a1_2_minigame_node_batch_creation

## 📘 Purpose

This node acts as the **Node Constructor Hand**, orchestrating the batch creation of a fully scaffolded Layer 4 minigame node. It dynamically spawns all necessary components using six underlying builder nodes ("fingers"), enabling reusable, CLI-driven recursive construction across the project.

---

## 🧩 Recursive Finger Calls

| Step | Node Called                            | Role                                               |
|------|----------------------------------------|----------------------------------------------------|
| 1    | `a0_0_add_empty_minigame_node`         | Create the empty minigame node folder              |
| 2    | `a0_1_add_empty_init_file`             | Insert `__init__.py` inside the node folder        |
| 3    | `a0_2_add_empty_main_file`             | Add `main.py` to the node                          |
| 4    | `a0_3_add_empty_subtaskmap_file`       | Add an empty `subtaskmap.md` scaffold              |
| 5    | `a1_0_add_empty_test_file`             | Add `test.py` to the node                          |
| 6    | `a1_1_link_nodal_meta_recursion_controls` | Add meta-recursive linkage files or headers    |

---

## 🔁 Invocation Logic

- This file is designed for **dynamic CLI invocation**:

  ```bash
  python main.py a99_0_new_minigame_node
  ```

## 🧠 CLI Rules and Invocation Pattern

### 🔤 Canonical Folder Name Format

The target node name must match the canonical recursive pattern:

```bash
a<digit+><digit+><descriptive_snake_case>
```

Example:

```bash
a33_1_a_new_node
```

If the folder already exists, the operation is **aborted with a warning** to prevent overwrite or recursion corruption.

---

### 🔧 Future CLI Upgrades (Planned)

- `--dry-run` → Simulate without writing changes  
- `--overwrite` → Force operation even if folder exists  
- `.recursive_log.txt` → Append execution results and recursive trace logs  

---

## ✅ Output

Upon successful execution, this node produces:

- A complete Layer 4 **folder scaffold**
- All **base files** created and ready for editing or execution
- Minimal, editable **stubs** for recursive follow-up logic

---

## 🧱 Related Hands and Orchestrators

- 🖐️ `a3_2_taskmaps_batch_creation`  
  Builds the planning scaffold (`taskmaps/`) alongside this node constructor.

- 🧠 `a99_2_test_create_minigame`  
  Higher-order orchestrator that invokes both hands and validates full recursive cohesion.

---

## 🧠 Notes on Recursive Architecture

This orchestration node is one of the **central recursive builder utilities** in Phase 2.  
It formalizes the “hand-of-functions” architecture:

- 🖐️ **Hand** = Function batch  
- ☝️ **Finger** = Atomic logic unit  
- 🧠 **CLI** = Dynamic recursive interface  

Its stability and reusability are critical to success in Phase 3 and beyond.
