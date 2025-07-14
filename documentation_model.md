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

| Layer   | Folder Type                                          | Documentation File                                     |  purpose          |
|---------|------------------------------------------------------|--------------------------------------------------------|-------------------|
| Layer 0 | Game Root (`storybook_primordial_soup/`)             | `README.md`, `milestones.md`, etc.                     | Defines core game structure and records major game-wide milestones (e.g., cybercell generations, phase transitions, workspace expansions).            |
| Layer 1 | Cybercell Generation (e.g., `a0_0_genesis_gloop/`)   | `mirror_decision.md`, `README.md`, `milestones.md`     | Logs foundational generation-level reflections and design↔gameplay splits. (Genesis Gloop excepted - as it encompasses Cybercell Generations 1 through 3)       |
|         | Generation Stanza (across 4 cybercells)              | `mirrorstanza_#.md`                                    | Records philosophical or poetic logic guiding generation-level mirror behavior.           |
| Layer 2 | Individual Cybercell (e.g., `a0_0_the_cell_.../`)    | `roadmap.md`, `primary_function.md`, `secondary_function.md`, `README.md`, `milestones.md` | Tracks minigame orchestration, recursion triggers, and cybercell division readiness. Distinguishes between functional logic (`1A`, `2A`) and division stanzas (`1B`, `2B`).                         |
|         | Cybercell Stanza (4 minigames)                       | `roadstanza_#.md`, `primary_roadstanza_#.md`, `secondary_roadstanza_#.md`  | Describes strategic development across minigames. Can represent either a Primary (`1B`) or Secondary (`2B`) cybercellular division stanza.    |
| Layer 3 | Minigame (e.g., `a0_0_the_test_that_called_itself/`) | `taskmap.md`, `milestones.md`, `README.md`             | Links narrative gameplay to design and dev tasks.                                            |
|         | Minigame Stanza (4 nodes)                            | `stanzamap_0.md`, `stanzamap_1.md`, etc.               | Documents recursive stanza logic, node sequencing, and test orchestration.                  |
| Layer 4 | Minigame Node (e.g., `a0_0_the_assertion_.../`)      | `subtaskmap.md`                                        | Captures node-specific logic, fallback triggers, or test rationale.                     |

---

All files must use **SHAGI-aligned markdown**, structured for both human and AI readability.

---

## ❌ Prohibited Structures

| File Type | Status | Notes |
|-----------|--------|-------|
| GDDs (Game Design Documents) | ❌ Not permitted | Design logic must live inside `roadmap.md` or `mirror_decision.md`. |
| GDJs (Game Development Journals) | ❌ Not permitted | Historical decisions are encoded within playable stanzas. |
| Appendices | ❌ Not permitted | No external meta-hierarchies; recursion must be self-contained. |

---

## 🧠 Agents and Automation

All future AI agents (e.g., `archivist.py`, `namer_agent.py`, `memory_ai`, etc.) must:

- ✅ Read and write only **in-world markdown files**  
- ✅ Treat this file as the **source of truth** for documentation practices  
- ❌ Avoid generating external docs unless explicitly tasked with producing a human-readable export

---

## 🔁 Recursion Doctrine

> If a system must remember, let it remember *within itself.*  
> If a decision must echo, let it echo *in the folders it changed.*  
> Primordial Soup does not look outward — it loops.

---

## ✅ Status: Active

This file governs the recursive documentation model of **all current and future cybercell generations**.
