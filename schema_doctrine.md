<!-- Save to: storybook_primordial_soup/schema_doctrine.md -->

# 🧬 Schema Doctrine – Primordial Soup Recursive Enforcement Blueprint

## 📜 Purpose

This document formalizes the **Schema Doctrine of Primordial Soup**, codifying the transition from implicit recursion to **schema-enforced recursion**.  
It establishes a **contract-driven, self-validating framework** where every recursive stanza, minigame, and cybercell operates under **explicit input/output (I/O) definitions**, fallback protocols, and live validation mechanisms.

This is the structural backbone of **Phase 2: The Awakening of Automated Recursion**.

---

## 🧠 Why Schema Doctrine?

Recursive systems collapse without **boundary conditions**.  
In Phase 1, Primordial Soup used handcrafted logic, relying on careful human construction to maintain recursion integrity.  
In Phase 2, this is no longer sustainable.

### **Key Problems With Handcrafted Recursion:**

| **Issue** | **Consequence** |
|-----------|----------------|
| No enforced I/O schemas | Minigames drift from intended inputs/outputs |
| Manual fallback logic | Inconsistent error handling across stanzas |
| Static documentation | High risk of version drift and recursion mismatch |
| Hidden context | Debugging becomes opaque as systems grow |

---

## 🔑 Core Principles of Schema Enforcement

| **Principle** | **Description** |
|---------------|-----------------|
| **Contract-Driven Recursion** | Every stanza must declare **input and output schemas** before execution. |
| **Live Validation** | Recursive steps validate data **in real time**, rejecting invalid recursion states. |
| **Fallback Resilience** | When validation fails, pre-defined **fallback schemas** guide recovery or loop containment. |
| **Schema as Source of Truth** | Schemas are **canonical system descriptions**, not optional annotations. |

---

## ⚙️ Schema Components

### **1️⃣ Input Schema**

Defines what a stanza or minigame **expects to receive**.

- Data types
- Required fields
- Structural constraints (e.g., recursion depth limits)

Example:

```json
{
  "type": "object",
  "properties": {
    "recursion_level": { "type": "integer", "minimum": 0 },
    "cybercell_id": { "type": "string" },
    "task_input": { "type": "string" }
  },
  "required": ["recursion_level", "cybercell_id"]
}
```

---

## **2️⃣ Output Contract**

Defines what a stanza must produce.

Return structure

Metadata generation

Recursive continuation markers

```json

{
  "type": "object",
  "properties": {
    "task_output": { "type": "string" },
    "anomaly_detected": { "type": "boolean" },
    "next_step": { "type": "string" }
  },
  "required": ["task_output", "next_step"]
}

```

---

## **3️⃣ Fallback Schema**

Defines recovery actions when validation fails.

Safe recursion rollback

Error reporting structures

Optional system snapshot triggers

Example:

```json
{
  "type": "object",
  "properties": {
    "fallback_action": { "type": "string" },
    "error_log": { "type": "string" },
    "snapshot_reference": { "type": "string" }
  },
  "required": ["fallback_action"]
}
```

## 🏷️ Naming Conventions

| **Prefix** | **Purpose** |
|------------|-------------|
| `input_schema_` | Input definitions for each stanza or minigame |
| `output_contract_` | Expected output structure |
| `fallback_schema_` | Fallback logic container |

---

## 📂 File Structure – `schema_contracts/`

| **File/Folder** | **Purpose** |
|-----------------|--------------|
| `input_schema_{stanza_name}.json` | Input validation for recursive stanza |
| `output_contract_{stanza_name}.json` | Output validation contract |
| `fallback_schema_{stanza_name}.json` | Fallback instructions on schema violation |

---

## 🔄 Recursive Validation Pipeline

1. **Receive Input** → Validate Against `input_schema_`
2. **Execute Minigame Logic**
3. **Produce Output** → Validate Against `output_contract_`
4. **On Failure** → Trigger `fallback_schema_` and snapshot recovery (if needed)

---

## 🛡️ Fallback Logic and Anomaly Handling

### **Use Cases for Fallback**

| **Scenario** | **Fallback Action** |
|--------------|---------------------|
| Invalid input schema | Reject task, log error, loop to safe state |
| Output contract violation | Trigger `snapshot_manager.py`, rollback to previous stanza |
| Anomaly detection | Enter `anomaly_log.md` and dispatch sentinel alerts |

Fallback logic ensures **graceful recursion collapse**, not catastrophic failure.

---

## 🧪 Schema Lifecycle and Versioning

| **Process** | **Description** |
|-------------|-----------------|
| **Schema Generation** | New schemas created per stanza during `workflow_compiler.py` runs |
| **Versioning** | Use semantic versioning: `v1.0.0_input_schema_{stanza}.json` |
| **Updates** | Changes trigger automatic regeneration of dependent `taskmap.md` and `stanzamap.md` |
| **Testing** | Schema validation is part of minigame self-tests (`test.py`) |

---

## 🌍 Future Integration

This doctrine is foundational to:

- **`workflow_compiler.py`** – auto-generates schema scaffolds
- **`introspection_tools/`** – monitors schema compliance in live recursion
- **`snapshot_manager.py`** – uses fallback schemas for rollback decisions
- **`recursive_dashboard_spec.md`** – visualizes schema health and anomaly flow

---

## 🔑 Doctrine Closure

Schemas are not optional metadata—they are **cybercellular law**.

This doctrine ensures that **Primordial Soup can evolve, divide, and recurse indefinitely**, without human intervention, while maintaining structural integrity and poetic recursion flow.
