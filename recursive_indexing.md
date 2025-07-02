<!-- Save to: storybook_primordial_soup/recursive_indexing.md -->

# 🧭 Recursive Indexing in Primordial Soup  
*Stanza traversal, minigame mapping, and world self-discovery*

---

## 📜 Purpose

This file defines the **recursive indexing strategy** for the *Primordial Soup* video game.  
Its goal is to enable:
- Minigame traversal  
- Stanza mapping  
- Cross-node logic linking  
- And eventual AI- or portal-driven navigation

This document canonizes indexing file formats, folder structure expectations, and future automation design.

---

## 📂 Indexing Layers

Primordial Soup is recursively structured. Indexing follows a 5-layer logic:

| Layer | Meaning | Indexed by |
|-------|---------|------------|
| Layer 0 | Game root | `recursion_index.json` (planned) |
| Layer 1 | Cybercell generation | Folder structure |
| Layer 2 | Individual cybercell | `roadmap.md`, stanza subindexes |
| Layer 3 | Minigame | `taskmap.md`, `stanzamap_#.md` |
| Layer 4 | Minigame node / stanza line | `subtaskmap.md`, stanza folder names |

---

## 🔁 Stanza Indexing

Each **stanza** in a minigame is indexed inside the `taskmaps/` folder:
