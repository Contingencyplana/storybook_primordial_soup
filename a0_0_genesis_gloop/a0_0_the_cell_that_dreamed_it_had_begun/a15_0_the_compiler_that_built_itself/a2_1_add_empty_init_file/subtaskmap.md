<!-- Save to: a15_0_the_compiler_that_built_itself\a2_1_add_empty_init_file\subtaskmap.md -->

# 🔹 Subtaskmap – a2_1_add_empty_init_file

## 🧩 Purpose

This node performs the **tenth tiny step** in recursive minigame construction.

It adds an `__init__.py` file inside a specified folder (typically `taskmaps/`) to mark it as a valid Python package, supporting importability, introspection, and automated system crawling.

This enables planning folders to participate in recursive builder logic while remaining traceable and isolated.

---

## 📂 Outputs

- Creates an `__init__.py` file inside the `taskmaps/` folder.

```plaintext
📁 a99_1_test_create_taskmaps/
├── __init__.py
└── 📁 taskmaps/
    └── __init__.py  ✅ ← created by this node
```

## 🔧 Actions

| Step | Action |
|------|--------|
| 1️⃣ | Verify that the `taskmaps/` folder exists (or create it). |
| 2️⃣ | Check if an `__init__.py` already exists inside the folder. |
| 3️⃣ | If not, create the file with Python package placeholder text. |
| 4️⃣ | Return a structured trace with status, path, event, and timestamp. |
| 5️⃣ | Prompt player to remove or retain the file post-test (`L`/`R`/Invalid). |

---

## 🌀 Recursive Role

This node reinforces **package boundary logic** in the recursive planning layer.

It ensures:

- Future automation can treat `taskmaps/` as a module.
- AI crawlers and validators can introspect and extend from here.
- Import-based scaffolding or validation scripts can resolve this folder correctly.

---

## ⚙️ System Integration

**Nodal Sequence:**  
Follows `a2_0_add_empty_taskmaps_folder`.  
Precedes `a2_2_add_empty_readme_file` and related planning scaffolds.

**Compiler Usage:**  
May be invoked independently or batch-called via `taskmaps_batch_creation`.

**Fallback Safety:**  
If the file exists, the system skips creation but logs the event with `skip_existing_init_file`.

---

## 🧪 Test Coverage

- Verifies `__init__.py` is created only if not already present.
- Confirms the correct file path and trace metadata.
- Allows safe manual cleanup after test runs via:

```plaintext
L → leave file intact
R → remove init.py
Other → prompt again until valid
```


---

## 🔖 Notes

This node is part of the **Planning Scaffold Loop**.  
It aligns with the **Tiny Step Recursion Doctrine** and ensures traceability for any recursive system rooted in `taskmaps/`, `milestones.md`, and `stanzamaps`.

It is also part of the **Phase 2 upgrade path** for nested path safe builder tools.
