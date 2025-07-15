# 📂 schema_contracts/

## Purpose

This folder houses **schema contracts** for Primordial Soup's recursive workflow system.

Each **stanza or minigame** may include:

| File | Purpose |
|------|---------|
| `input_schema.json` | Defines what inputs are required before recursion can proceed. |
| `output_contract.json` | Specifies the structure of outputs required after recursion executes. |
| `fallback_schema.json` | Describes fallback behaviors if recursion fails validation. |

---

## Why This Folder Exists

- To support **automated recursion validation**  
- To enable **self-expanding cybercells with safe boundaries**  
- To provide **machine-readable recursion rules** that align with the game's poetic structure

---

## Usage

Schemas are:

- **Generated automatically** by `workflow_compiler.py` (or written manually for creative control)  
- **Checked live** during recursion cycles by introspection and validation tools  
- **Updated over time** as recursive structures grow

---

## Related Systems

- `workflow_compiler.py`  
- `snapshot_manager.py`  
- `introspection_tools/`  
- `recursive_workflow.md`

---

This folder ensures that **Primordial Soup remains safe, playful, and recursively self-validating** as it evolves.
