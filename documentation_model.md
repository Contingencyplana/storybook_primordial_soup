<!-- Save to: storybook_primordial_soup/documentation_model.md -->

# 🧾 Documentation Model – Primordial Soup

## Purpose

This file defines the official documentation structure for **Primordial Soup**.  
It canonizes the minimalist, recursion-bound doctrine that governs how all design, development, and decision records are created, stored, and retrieved.

---

## 🌱 Core Principle

> **All documentation in Primordial Soup is in-world, recursive, and embedded directly in the playable file structure.**  
> No external GDDs (Game Design Documents), GDJs (Game Development Journals), or appendices shall be used.

---

## 🧭 Layered Documentation Structure

| Layer   | Folder Type | Documentation File | Purpose                                     |
|---------|-------------|--------------------|---------------------------------------------|
| Layer 1 | Game Root | N/A | Holds core verse structure and orchestrates recursive spread |
| Layer 2 | Cybercell Generation (e.g., `a0_0_`, `a0_1_`, ...) | `mirror_decision.md` | Logs key design↔gameplay mirror decisions |
| Layer 3 | Individual Cybercell (e.g., `a0_0_the_cell_`, ...) | `roadmap.md` | Tracks minigames, system activation, and division readiness |
| Layer 4 | Minigame (quest or loop) | `taskmap.md` | Links narrative gameplay to real dev/design tasks |
|         | Minigame Stanza (4 nodes) | `stanzamap_#.md` | Documents recursive stanza logic, node sequence, and hooks |
| Layer 5 | Minigame Node (4 files) | `subtaskmap.md` | Captures logic behind node-specific gameplay or test decisions |

All files must use **SHAGI-aligned markdown**, structured for both human and AI readability.  
`subtaskmap.md` files are often intentionally left blank but exist as scaffolding for recursive growth.

---

## ❌ Prohibited Structures

| File Type | Status | Notes   |
|-----------|--------|---------|
| GDDs (Game Design Documents) | ❌ Not permitted | Design logic must live inside `roadmap.md` or `mirror_decision.md` |
| GDJs (Game Development Journals) | ❌ Not permitted | Historical decisions are encoded within playable stanzas |
| Appendices | ❌ Not permitted | No external meta-hierarchies; recursion must be self-contained |

---

## 🧠 Agents and Automation

All future AI agents (e.g., `archivist.py`, `namer_agent.py`, `memory_ai`, etc.) must:

- ✅ Read and write only **in-world markdown files**
- ✅ Treat this file as the **source-of-truth for documentation practices**
- ❌ Avoid generating external docs unless explicitly tasked with producing a human-readable export

---

## 🔁 Recursion Doctrine

> If a system must remember, let it remember *within itself.*  
> If a decision must echo, let it echo *in the folders it changed.*  
> Primordial Soup does not look outward — it loops.

---

## ✅ Status: Active

This file governs the recursive documentation model of **all current and future cybercell generations**.
