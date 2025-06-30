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

| Layer   | Folder Type                                   | Documentation File   | Purpose                                                     |
|---------|-----------------------------------------------|----------------------|-------------------------------------------------------------|
| Layer 1 | Overarching                                   | `multifarious`       | Orchestrating, pivotal and very widely assorted             |
| Layer 2 | Cybercell Generation (`a0_0_`, `a0_1_`, etc.) | `mirror_decision.md` | Logs key design↔gameplay mirror decisions                   |
| Layer 3 | Individual Cybercell (`a0_0_`, `a0_1_`, etc.) | `roadmap.md`         | Tracks minigames, system activation, and division readiness |
| Layer 4 | Minigame (quest or loop)                      | `taskmap.md`         | Links narrative gameplay to real dev/design tasks           |
| Layer 5 | Minigame Node (4 files)                       | `subtaskmap.md`      | Links narrative gameplay to real dev/design subtasks        |

All files must use SHAGI-aligned markdown, structured for both human and AI readability. Subtaskmap.md files are frequently empty.

---

## ❌ Prohibited Structures

| File Type | Status | Notes |
|-----------|--------|-------|
| GDDs (Game Design Documents) | ❌ Not permitted | All design logic must live in `roadmap.md` or `mirror_decision.md` |
| GDJs (Game Development Journals) | ❌ Not permitted | No external journals — historical actions are logged within stanzas |
| Appendices | ❌ Not permitted | No meta-hierarchies; recursion is self-contained |

---

## 🧠 Agents and Automation

All future AI agents (e.g., `archivist.py`, `namer_agent.py`, `memory_ai`, etc.) must:

- Read and update only in-world markdown files
- Treat this file as source-of-truth for documentation rules
- Avoid generating external artifacts unless explicitly instructed to create readable exports

---

## 🔁 Recursion Doctrine

> If a system must remember, let it remember *within itself.*  
> If a decision must echo, let it echo *in the folders it changed.*  
> Primordial Soup does not look outward — it loops.

---

## ✅ Status: Active  
This file governs the recursive documentation model of **all current and future cybercell generations**.
