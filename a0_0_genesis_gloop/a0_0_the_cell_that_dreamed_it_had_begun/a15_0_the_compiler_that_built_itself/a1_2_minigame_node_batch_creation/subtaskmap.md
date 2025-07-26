# 🧠 Subtaskmap – a1_2_minigame_node_batch_creation

## 📘 Purpose

This node acts as the **Node Constructor Hand**, orchestrating the batch creation of a fully scaffolded Layer 4 minigame node.  
It dynamically spawns all required components using six recursive builder nodes ("fingers"), enabling reusable, CLI-driven recursive construction across the project.

---

## 🧩 Recursive Finger Calls

| Step | Node Called                               | Role                                               |
|------|-------------------------------------------|----------------------------------------------------|
| 1️⃣   | `a0_0_add_empty_minigame_node`            | Create the empty minigame node folder              |
| 2️⃣   | `a0_1_add_empty_init_file`                | Insert `__init__.py` inside the node folder        |
| 3️⃣   | `a0_2_add_empty_main_file`                | Add `main.py` to the node                          |
| 4️⃣   | `a0_3_add_empty_subtaskmap_file`          | Add an empty `subtaskmap.md` scaffold              |
| 5️⃣   | `a1_0_add_empty_test_file`                | Add `test.py` to the node                          |
| 6️⃣   | `a1_1_link_nodal_meta_recursion_controls` | Register the node in `meta_recursion_controls.md`  |

---

## 🔁 Invocation Logic

This file is designed for **dynamic CLI invocation**:

```bash
python main.py a99_0_test_create_minigame_node/a0_0_test_minigame_node
```

Supports nested paths and creates intermediate folders as needed.

---

## 🔤 Canonical Folder Name Format

The final folder name must follow this recursive naming convention:

```plaintext
a<digits>_<digits>_<descriptive_snake_case>
```

Example:

```plaintext
a33_1_a_new_node
```

If the folder already exists, the operation is **aborted with a warning** to prevent recursive corruption.

---

## 🔧 Future CLI Upgrades (Planned)

- `--dry-run` → Simulate execution without writing files  
- `--overwrite` → Force execution even if the target exists  
- `.recursive_log.txt` → Append trace logs and execution reports for introspection tools

---

## ✅ Output

Upon success, this node produces:

- A complete Layer 4 **minigame node folder**  
- All base files created (`__init__.py`, `main.py`, `test.py`, `subtaskmap.md`)  
- Structural trace metadata (via inner scripts)  
- Ready-to-edit stubs for recursive logic or test pipelines

---

## 🧱 Related Hands and Orchestrators

- 🖐️ `a3_2_taskmaps_batch_creation`  
  Builds the `taskmaps/` planning scaffold alongside this node constructor.

- 🧠 `a4_2_link_minigame_meta_recursion_controls`  
  Higher-order integrator — links and registers minigame-level scaffolds into the recursive ecosystem.

- 🧠 `a99_2_test_create_minigame`  
  End-to-end orchestrator that invokes both hands and validates recursive cohesion.

---

## 🧠 Notes on Recursive Architecture

This orchestration node embodies the **“hand-of-functions” architecture**:

- 🖐️ **Hand** = A recursive batch of finger nodes  
- ☝️ **Finger** = A single atomic tool with focused logic  
- 🧠 **CLI** = The interactive recursive interface layer

Its traceable, reusable design is critical for deeper automation, recursive planning,  
and introspective integrity across all future phases.
