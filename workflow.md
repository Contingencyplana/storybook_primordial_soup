<!-- Save to: storybook_primordial_soup/workflow.md -->

# 🧩 Primordial Soup – Workflow Overview  
*Recursive stanza-building, verification, and deployment flow*

---

## 📜 Purpose

This document defines the **canonical workflow** for developing minigames in the *Primordial Soup* video game project.  
It establishes the recursive unit structure, file expectations, test cadence, and archival update routine.

This workflow is recursive, modular, poetic, and extensible.

---

## 🧬 Core Development Cycle

Each **minigame** (Layer 3 folder) is composed of one or more **stanzas**, each consisting of four **minigame nodes** (Layer 4 folders).

Each **minigame node** contains:

| File             | Role                                                   |
|------------------|--------------------------------------------------------|
| `__init__.py`     | Recursion marker or placeholder (optional)            |
| `main.py`         | Executable logic for the stanza node                  |
| `test.py`         | Self-verifying test script for the node               |
| `subtaskmap.md`   | Design intent, AI hooks, fallback notes, and comments |

---

## 🔁 Recursive Stanza Workflow

For each new stanza (`sX_0_...` to `sX_3_...`):

1. **Create Folder & Initialize**
   - Name the folder:  
     `sX_0_the_line_that_defines_itself`  
     *(Use poetic but functionally meaningful names)*

2. **Create Files**
   - `main.py` — Implement the stanza’s Y-node logic  
   - `test.py` — Write and validate 4–6 test cases  
   - `__init__.py` — Include if needed (can be blank)  
   - `subtaskmap.md` — Outline logic, fallbacks, portal triggers, AI hints

3. **Test**
   - From terminal or CLI:
     ```bash
     cd path/to/a0_0_the_test_that_called_itself/a0_0_the_line_that_...
     python test.py
     ```
   - Confirm: ✅ All tests pass or fallback triggers are handled

4. **Mark Complete**
   - Add entry to:
     - `taskmaps/stanzamap_#.md`
     - Mark stanza title, logic status, and forward recursion hook

---

## 📦 ZIP Upload + AI Sync

After completing a full stanza (4 nodes):

1. 📂 **Update your ZIP workspace**  
   `storybook_primordial_soup.zip`

2. 📬 **Notify ChatGPT with**:
   > I have just updated your `storybook_primordial_soup.zip` project file. Please extract the contents of the ZIP folder and review any files or folders as needed to help me build the Primordial Soup video game. How do the unzipped contents look?

3. 🧠 **ChatGPT responds by**:
   - Extracting the new ZIP  
   - Updating the internal file map  
   - Validating stanza structure and index entries

---

```plaintext
a0_0_the_test_that_called_itself/
├── README.md
├── milestones.md
├── taskmaps/
│   ├── taskmap.md
│   ├── stanzamap_s0.md
│   └── stanzamap_s1.md
├── a0_0_the_assertion_of_first_contact/
│   ├── __init__.py
│   ├── main.py
│   ├── test.py
│   └── subtaskmap.md
├── a0_1_the_loop_that_tested_closure/
│   ├── __init__.py
│   ├── main.py
│   ├── test.py
│   └── subtaskmap.md
├── a0_2_the_trace_that_returned_wrong/
│   └── ...
├── a0_3_the_fallback_that_caught_the_signal/
│   └── ...
├── a1_0_the_checkpoint_that_missed_the_mark/
│   └── ...

```

## 🔐 Validation Checklist

| Task                               | Required |
|------------------------------------|----------|
| `main.py` exists and is executable | ✅ |
| `test.py` exists and passes all test cases | ✅ |
| `subtaskmap.md` outlines logic or design notes | ✅ |
| Corresponding `stanzamap_#.md` is updated | ✅ |
| Updated ZIP archive uploaded to ChatGPT | ✅ |

---

## 🔗 Forward Compatibility

This workflow supports:

- GUI expansion via recursive page-flip logic (`[L]`, `[R]`, `[Esc]`, `[P]`)
- Portal traversal and branching stanza mechanics
- Auto-indexers and dynamic stanza loaders
- Recursion-aware game runners and AI sentinels
- Testable narrative logic across cybercells and minigames

---

## 🧭 Summary

This file defines the recursive workflow standard for building stanza-based minigames in *Primordial Soup*.

Each completed stanza is one recursive verse deeper into the game’s self-awareness.  
Each ZIP upload is a ritual: a signal, a sync, a checkpoint in the poem of recursion.

## 🤖 Automated Workflow Evolution

In **Primordial Soup**, recursion itself evolves.

As the system matures, **cybercells begin to generate their own scaffolds**—writing their own `taskmaps`, `stanzamaps`, and `subtaskmap.md` files based on **folder growth and naming logic**.

This transition marks the move from **Phase 1 (manual stanza building)** to **Phase 2 (automated scaffold generation)**. Both phases **coexist**, giving developers and players full control over recursion depth and workflow style.

---

### **`workflow_compiler.py`**

A dedicated script—**`workflow_compiler.py`**—handles automated scaffold generation.

#### **What It Does:**

- **Crawls the `a0_0_genesis_gloop/` folder structure**
    - Detects existing minigames, stanzas, and nodes
    - Maps current recursion layers and relationships

- **Detects new minigames, stanzas, and nodes**
    - Identifies which scaffolds are missing or incomplete
    - Recognizes standard naming conventions (e.g., `a0_0_`, `a0_0_`, `a1_0_`)

- **Auto-generates key workflow files**
    - Creates `taskmap.md` for the minigame if absent
    - Creates `stanzamap.md` entries for new stanzas
    - Generates `README.md` files with summary logic and placeholders
    - Builds `subtaskmap.md` files for each node, including base fallback logic and recursive notes

- **Produces optional schema contracts**
    - If a `schema_contracts/` folder exists, `workflow_compiler.py` will auto-generate:
        - **`input_schema.json`** – Defines what each stanza node expects as input
        - **`output_contract.json`** – Specifies what each stanza node must output
    - These schemas support **live recursion validation** and prepare for anomaly handling systems

---

### **Why Automate?**

Recursive systems **grow beyond human maintenance**.  
By letting the cybercell scaffold its own future tasks, **Primordial Soup enters a new phase of recursive gameplay and development**.

This approach:

- Reduces manual overhead  
- Supports playful exploration of recursion depth  
- Enables dynamic expansion of cybercell logic without bottlenecking creative flow

---

### **Manual Override Always Available**

Automation is **optional and playful**.  
You can:

- **Manually edit any auto-generated files**  
- **Disable automation entirely** for handcrafted recursion  
- **Use hybrid workflows**, letting the system scaffold drafts while you rewrite, remix, or poeticize them

---

This section defines the path forward for **self-expanding recursion in Primordial Soup**—keeping the process playful, generative, and layered at every phase.

## 🗂️ Schema Contracts and Validation

Each **stanza step** in *Primordial Soup* can define its own **schema contracts**, allowing the system to validate recursion paths and enforce logical consistency.

### **Schema Types:**

| File | Purpose |
|------|---------|
| **`input_schema.json`** | Defines what the stanza node **expects as input**. |
| **`output_contract.json`** | Specifies what the stanza node **promises to output**. |
| **`fallback_schema.json`** | Describes **what happens if something goes wrong**—including fallback triggers, anomaly signals, or recursive catchpoints. |

---

### **Playful Yet Precise**

Schemas in *Primordial Soup* are **machine-readable** but also **poetic and human-playable**.

Example:

```json
{
  "input_schema": {
    "required_signal": "a whisper from the prior recursion layer",
    "expected_format": "string, lowercased, poetic in tone"
  },
  "output_contract": {
    "recursive_promise": "a transformed signal, encoded with one layer deeper meaning",
    "format": "JSON object with 'message' and 'recursion_depth' keys"
  },
  "fallback_schema": {
    "if_input_missing": "invoke a0_3_the_fallback_that_caught_the_signal",
    "if_output_invalid": "loop back to prior stanza and retry"
  }
}
```

This format allows for **both logical precision and narrative layering**, keeping the system **recursive and playful**.

---

## **Automated Validation Pipeline**

Each stanza node runs **live validation**:

- **Before execution**: Input is checked against `input_schema.json`
- **After execution**: Output is checked against `output_contract.json`
- **On failure**: The system consults `fallback_schema.json` to determine next actions

---

### **This ensures:**

- **Reduced error propagation**  
- **Recursive containment of anomalies**  
- **Playful but controlled recursion growth**

---

## 🔍 **Cybercell Introspection**

The **`introspection_tools/`** folder contains scripts that allow cybercells to:

- **Reflect on their own structure**  
- **Generate live growth summaries**  
- **Detect incomplete or pending recursion states**

---

### **This introspection layer feeds into:**

- **Recursive maturity tracking**  
- **Real-time dashboard summaries**  
- **Anomaly detection and recovery hooks**

---

## 🌀 **Recursive Snapshots and Time-Loop Support**

The **`snapshot_manager.py`** tool enables **versioned recursion snapshots**.

### **Snapshot Features:**

- **Checkpoint the current state of a cybercell**  
- **Rollback to previous recursion states if anomalies are detected**  
- **Support time-loop recursion for experimental or narrative purposes**

---

## **Why This Matters**

By combining **schema validation**, **introspection**, and **snapshot management**, *Primordial Soup* creates a **self-observing, self-correcting recursion system**.

---

### **This supports:**

- **Playful recursion growth**  
- **Safe expansion of cybercell layers**  
- **Narrative-rich anomaly handling**  
- **Recursive time experiments without fear of corruption**

---

These systems help **Primordial Soup remain a game that writes, tests, and repairs itself**, while staying true to its **poetic and modular foundations**.

## 🔍 Cybercell Introspection

As Primordial Soup evolves, **cybercells gain the ability to observe and reflect on their own structure**.

A dedicated toolset in **`introspection_tools/`** allows for recursive system self-awareness, enabling cybercells to:

- **Reflect on their own structure**  
  - Crawl their folder hierarchy  
  - Identify stanza layers, minigames, and recursion depth  

- **Generate growth summaries**  
  - Report current stanza completions  
  - Track pending tasks or incomplete recursion cycles  

- **Detect incomplete or pending recursion states**  
  - Flag missing `stanzamap.md` or `subtaskmap.md` files  
  - Identify schema gaps or fallback logic that has not been defined  

---

### **Purpose and Integration**

This introspection layer serves multiple roles:

| Function | Outcome |
|----------|---------|
| **Dynamic recursion maturity tracking** | Cybercells know how far they’ve grown and how deep recursion has gone |
| **Real-time dashboard summaries** | Generates snapshots of system status for player and developer insight |
| **Anomaly detection and recovery hooks** | Flags inconsistencies, recursion breaks, or structural anomalies |

---

### **Gameplay and Maintenance Synergy**

**Cybercell introspection is not just a system tool—it’s part of the game’s recursive narrative.**

By reflecting on their own growth and recursion status, cybercells help:

- Guide players or developers through recursive evolution  
- Ensure the integrity of the stanza-building process  
- Prepare for autonomous expansion and safe anomaly management

---

This keeps **Primordial Soup playful, self-aware, and resilient**, growing recursively while maintaining coherence across minigames, cybercells, and recursive generations.


## 🌀 Recursive Snapshots and Time-Loop Support

In **Primordial Soup**, recursion does not merely grow—it loops, reflects, and sometimes returns to its own beginnings.

To support this, the system includes **recursive snapshots and time-loop management**.

---

### **`snapshot_manager.py`**

A dedicated tool—**`snapshot_manager.py`**—handles **versioned recursion snapshots**.

#### **What It Does:**

- **Checkpoint the current state of a cybercell**
    - Captures stanza completion status, schema validation state, and structural metadata.
    - Stores snapshots in versioned directories or files for later retrieval.

- **Rollback to previous recursion states if anomalies are detected**
    - Reverts a cybercell to a known-good prior state.
    - Ensures recursive safety during anomaly handling or failed expansions.

- **Support time-loop recursion for experimental or narrative purposes**
    - Allows players or developers to intentionally replay recursion layers.
    - Enables recursive experiments, paradox simulations, or layered narrative loops.

---

### **Why Snapshots Matter**

Without versioned checkpoints, recursion risks:

- **Data drift**  
- **Structural anomalies**  
- **Loss of poetic cohesion between recursive layers**

By integrating snapshots into the workflow, **Primordial Soup supports safe, playful recursion loops** that:

| Function | Purpose |
|----------|---------|
| **Checkpoint growth** | Preserve milestones in cybercell development |
| **Enable rollback** | Undo problematic recursion branches |
| **Create narrative loops** | Explore recursion time travel and paradox arcs |

---

### **Anomaly Management Integration**

**Anomaly management is tied to snapshot checkpoints**:

- If recursive validation fails, the system can trigger a **fallback rollback**.  
- If unexpected growth patterns emerge, the cybercell can **reset to a prior recursion state**, preserving system stability while enabling playful exploration.

---

### **Recursive Storytelling Potential**

Snapshots are not just technical tools—they’re **narrative devices**.  

They allow Primordial Soup to:

- Simulate **recursive paradoxes**  
- Explore **nonlinear narrative time**  
- Embed **self-healing recursion loops** into gameplay  

---

This system ensures that Primordial Soup remains **safe to expand, safe to break, and safe to loop—again and again**, without fear of corruption or structural loss.

## 📜 Manual or Automated? Player’s Choice

In the spirit of **Primordial Soup**, the workflow is **not rigid**—it is **recursive and optional**, allowing developers (or players, in advanced modes) to **choose their preferred approach** for cybercell expansion.

---

### **Modes of Workflow Expansion**

| Mode | Description |
|------|-------------|
| **Manual Mode** | **Hand-craft each stanza and minigame scaffold**, following the standard workflow outlined in this document. This preserves full creative control, allowing poetic phrasing, custom logic, and playful recursion layering by hand. |
| **Automated Mode** | **Run `workflow_compiler.py`** to let the system scaffold the next layer recursively. This auto-generates `taskmap.md`, `stanzamap.md`, `subtaskmap.md`, and schema contracts, saving time while maintaining structural integrity. |
| **Hybrid Mode** | **Use automated scaffolds as drafts**, then **revise, overwrite, or remix them** with poetic, narrative, or experimental modifications. This merges system efficiency with creative play. |

---

### **Why Offer a Choice?**

Primordial Soup is both:

- **A game engine** that builds recursive logic structures  
- **A playground** for recursive design, narrative recursion, and playful systems engineering  

By allowing multiple workflow modes, the system remains:

- **Flexible for developers**  
- **Playable for designers**  
- **Expandable for AI-driven experiments**  

---

Whether you handcraft every line or let the recursion scaffold itself, **Primordial Soup remains a self-writing, self-expanding world—guided by both human hands and automated growth.**

## 🧭 Evolution Summary

With the introduction of automated scaffolding, **this workflow now supports two recursive layers**:

| Layer | Description |
|--------|-------------|
| **Phase 1** | **Human-written recursion scaffolding**, built stanza by stanza. This phase emphasizes creative control, poetic structure, and manual recursive design. |
| **Phase 2** | **Self-generating recursion scaffolding**, managed by `workflow_compiler.py` and **schema-driven validation**. This phase enables cybercells to expand autonomously, generating taskmaps, stanzamaps, subtaskmaps, and schemas as part of their growth. |

---

### **Coexistence of Layers**

Both layers are **active and complementary**:

- **Manual Mode** preserves the craft of recursion writing.
- **Automated Mode** accelerates system growth while maintaining recursion integrity.
- **Hybrid Mode** allows creative remixing of autogenerated scaffolds, ensuring the system stays playful and emergent.

---

### **Primordial Soup’s Recursive Future**

Primordial Soup is now:

- **A game that writes itself**  
- **A system that scaffolds its own recursion**  
- **A poetic engine for layered, playful growth**

By evolving beyond hand-coded structures while keeping manual recursion alive, **Primordial Soup remains a recursive playground—growing deeper, looping wider, and always expanding at the meta-level.**
