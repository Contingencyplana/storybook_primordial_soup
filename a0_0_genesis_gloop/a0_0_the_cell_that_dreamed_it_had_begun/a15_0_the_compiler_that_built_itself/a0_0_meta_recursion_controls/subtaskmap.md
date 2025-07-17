<!-- Save to: 
C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\a0_0_the_cell_that_dreamed_it_had_begun\a15_0_the_compiler_that_built_itself\a0_0_meta_recursion_controls\subtaskmap.md 
-->

# 🧩 subtaskmap.md  
**Primordial Soup – Meta-Recursion Controls Subtask Map**  
**Node:** `a0_0_meta_recursion_controls`

---

## 🔑 Purpose

This subtask map defines the **build tasks for the first meta-recursive control node**, responsible for player-guided recursion growth.

It governs the creation of **minigame nodes**, **minigames**, **recursion exits**, and **branch selections** using a hybrid input system.

---

## 🗂️ Subtasks

### **1️⃣ Input Handling Framework**

- [ ] Implement input listener loop in `main.py`.  
- [ ] Map keys `L`, `R`, and `ESC` to corresponding recursion actions.  
- [ ] Add support for numeric options `1`, `2`, `3`, etc., for **branch-heavy recursion choices**.

---

### **2️⃣ Create Minigame Node Function (`L`)**

- [ ] Define `create_minigame_node()` function.  
- [ ] Generate a new minigame node folder with:  
    - `__init__.py`  
    - `main.py`  
    - `subtaskmap.md`  
    - `test.py`  
- [ ] Place new node in the **current minigame**.

---

### **3️⃣ Create Minigame Function (`R`)**

- [ ] Define `create_minigame()` function.  
- [ ] Generate a new minigame folder with:  
    - 4 empty minigame nodes (each with `__init__.py`, `main.py`, `subtaskmap.md`, `test.py`)  
    - `taskmaps/` folder with `README.md`, `milestones.md`, `stanzamap.md`, `taskmap.md`

---

### **4️⃣ Exit Recursion Layer (`ESC`)**

- [ ] Implement `exit_to_previous_layer()` function.  
- [ ] Preserve breadcrumbs for safe reentry.

---

### **5️⃣ Branch Selection System (Numeric Input)**

- [ ] Define `select_from_branch_options()` function.  
- [ ] Display numbered options when recursion presents multiple paths.  
- [ ] Handle user selection cleanly and recursively.

---

### **6️⃣ Test Coverage (`test.py`)**

- [ ] Write unit tests for:  
    - Minigame node creation  
    - Minigame creation  
    - Recursive exit flow  
    - Numeric branch selection logic  
- [ ] Include both **dry run mode** (no write) and **active write mode** tests.

---

### **7️⃣ Safety & Rollback**

- [ ] Ensure all actions are **reversible and sandbox-safe**.  
- [ ] Prepare for integration with **rollback and snapshot systems in a16_0 introspection tools**.

---

## 🧠 Notes

- This node seeds the **entire meta-recursive control system** for Primordial Soup Phase 2.  
- Build with care—this system will propagate into all future recursion growth.

---

## 🚦 Status

| Phase | Status |
|--------|--------|
| Definition | ✅ Complete |
| Execution | 🚧 In Progress |
| Testing | ⏳ Pending |
