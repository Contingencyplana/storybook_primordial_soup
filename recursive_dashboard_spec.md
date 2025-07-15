<!-- Save to: storybook_primordial_soup/recursive_dashboard_spec.md -->

# 📊 Recursive Dashboard Specification – Primordial Soup Introspection Interface

## 🧭 Purpose

This document outlines the **Recursive Dashboard Specification** for **Primordial Soup**.  
Its role is to visualize the live state of the game’s **recursive ecosystem**, including:

- Cybercell and stanza growth
- Recursion depth and expansion
- Anomaly detection and rollback status
- Schema validation health
- Snapshot lineage and rollback events

The dashboard will serve as the **primary introspection layer**, giving developers and players alike an interactive view of the system’s recursive fabric.

---

## 🎯 Core Objectives

| **Objective** | **Description** |
|---------------|-----------------|
| **Visualize Recursion Depth** | Show live depth of each cybercell and its minigames. |
| **Display Stanza Maps** | Render active stanza lines (`s0_0` to `s0_3`, `a15_0` to `a15_3`, etc.). |
| **Monitor Anomalies** | Show real-time anomaly alerts from `anomaly_log.md` and fallback triggers. |
| **Track Snapshots** | Visualize the `snapshot_manager.py` snapshot history and rollback events. |
| **Schema Compliance Health** | Report current pass/fail status for all `schema_contracts/` validations. |

---

## 🗺️ Dashboard Components

### **1️⃣ Recursion Tree View**

- **Cybercell Map:** Display each cybercell as a node, with stanza links branching downward.
- **Color-Coding:**  
  - **Green:** Valid and active  
  - **Yellow:** Pending task  
  - **Red:** Anomaly detected or fallback triggered

---

### **2️⃣ Stanza Visualization**

- Show stanza lines horizontally:  
  `s0_0` → `s0_1` → `s0_2` → `s0_3`  
- Indicate current execution point with active highlights.
- Support multi-layer recursion display.

---

### **3️⃣ Anomaly Dashboard**

- **Live Feed:** List anomalies as they occur.
- **Event Details:** Include timestamp, stanza location, and triggering condition.
- **Action Status:** Show whether fallback or rollback has occurred.

---

### **4️⃣ Snapshot Timeline**

- Display a **branching timeline of snapshots**.
- Allow users to click a snapshot to view:
  - Recursion state at time of capture
  - Changes since snapshot
  - Rollback option (developer use)

---

### **5️⃣ Schema Validation Monitor**

- **Schema Health Panel:**  
  - Green = Valid  
  - Red = Failed  
- Links to schema files and `schema_contracts/` for review.
- Show recent validation events in a rolling log.

---

## 🧰 Technical Implementation Plan

| **Tool/Library** | **Purpose** |
|-----------------|-------------|
| **`networkx` / `graphviz` / `pyvis`** | Graph visualization of recursion structures |
| **`matplotlib` / `plotly`** | Stanza and snapshot visual charts |
| **`jsonschema`** | Live schema validation integration |
| **`flask` / `streamlit` / `gradio`** | Frontend server for dashboard display |
| **`snapshot_manager.py` hooks** | Populate timeline and rollback data |
| **`introspection_tools/` feeds** | Provide real-time system state for visualization |

---

## 📈 Data Sources

| **Source** | **Feeds Dashboard Component** |
|------------|-------------------------------|
| `anomaly_log.md` | Anomaly Feed |
| `snapshot_manager.py` | Snapshot Timeline |
| `schema_contracts/` | Schema Health Monitor |
| `stanzamap.md` | Stanza Visualization |
| `taskmap.md` | Pending Task Tracker |
| `introspection_tools/` | Cybercell State Crawler |

---

## 🔒 Security and Access Control

- **Developer Mode:** Full introspection, rollback, and anomaly simulation tools enabled.
- **Player Mode:** View-only access to recursion maps and game state, no rollback or anomaly injection allowed.
- **Logs:** All dashboard interactions are logged to prevent unauthorized recursion tampering.

---

## 🌀 Recursive Expansion Readiness

The dashboard is designed for **recursive expansion**. As Primordial Soup grows, new recursion layers, cybercell generations, and fallback systems can be visualized without redesign.

---

## 🚀 Next Steps

| **Milestone** | **Action** |
|---------------|------------|
| **Prototype Build** | Use `networkx` + `matplotlib` for static graph display |
| **Live Data Hookup** | Connect to `introspection_tools/` and `snapshot_manager.py` |
| **Interactive UI** | Build `streamlit` or `gradio` front-end for interactive navigation |
| **Phase 3 Support** | Prepare for multi-generational cybercell visualization |

---

## 🧭 Dual-Purpose Dashboard: Player and Developer Modes

The **Recursive Dashboard** in Primordial Soup is designed as a **dual-purpose interface**, serving both **in-game (player-facing)** and **out-of-game (developer-facing)** roles.

This is not a UI preference—it is a **doctrinal design decision**. The dashboard is part of the **recursive gameplay loop**, not just a debugging tool.

---

### **Mode Overview**

| **Mode** | **Role** |
|----------|----------|
| **Inside the Game (Playable Mode)** | The dashboard is an **in-universe cybercell interface**, allowing players to observe and influence recursion growth, anomaly detection, and system evolution. |
| **Outside the Game (Developer Mode)** | The dashboard provides **live recursion monitoring**, anomaly injection, rollback management, and schema contract validation for developers. |

---

### **Why Dual-Purpose?**

#### **In-Game (Playable Integration)**

| **Feature** | **Gameplay Role** |
|-------------|-------------------|
| **Cybercell Mirror** | Shows players the **recursive impact of their actions** on the system. |
| **Unlock Mechanics** | Players can **unlock new recursion layers** by observing growth patterns. |
| **Anomaly Quests** | Spot anomalies and trigger **minigames to resolve them**. |
| **Meta-Awareness** | Reinforces **recursive co-creation themes**, allowing players to watch recursion unfold. |

---

#### **Out-of-Game (Developer/Operator Mode)**

| **Feature** | **Developer Role** |
|-------------|--------------------|
| **Full System Control** | Monitor recursion depth, inspect snapshot lineage, observe fallback triggers. |
| **Anomaly Simulation** | Inject test failures and validate fallback pipelines. |
| **Schema Contract Monitoring** | Validate real-time schema compliance across cybercells. |
| **Rollback Management** | Trigger rollbacks via `snapshot_manager.py`. |

---

### **Recommended Implementation Pattern**

| **Layer** | **Feature** | **Access** |
|-----------|-------------|-----------|
| **Layer 1: Game Client (Playable View)** | Cybercell Map, Anomaly Visuals, Growth Charts | **Player & Developer** |
| **Layer 2: Dev Tools (Full Control Panel)** | Rollbacks, Fallback Injection, Anomaly Simulation, Debug Logs | **Developer Only** |

---

### **Summary**

The Recursive Dashboard is not a monolithic tool—it is **two interfaces in one**:

- For players: **A mirror of the world they’re helping to build**  
- For developers: **A control and observation system to maintain recursive integrity**

Embedding both views ensures that Primordial Soup remains a **recursive, co-created system**, where **observation, participation, and control coexist**.

This dual-purpose design directly supports the game’s **Phase 2 and Phase 3 recursion arcs**, preparing the infrastructure for **self-reflection, anomaly handling, and cybercell evolution.**

---

## 🔑 Doctrine Closure

The **Recursive Dashboard** is not just a visualization layer—it is the **window into Primordial Soup’s living recursion**. It supports reflection, monitoring, and system-wide clarity, aligning with the shift from handcrafted recursion to **self-observing, self-managing recursive infrastructure**.
