<!-- Save to: storybook_primordial_soup/future_proofing.md -->

# 🌱 Future-Proofing Primordial Soup  
*A design doctrine for recursion beyond the current stanza*

---

## 📜 Purpose

This document defines the long-term **evolutionary pathways** for Primordial Soup.  
It outlines how the game’s recursive, stanza-based structure can scale — across logic, lore, and interface — without collapsing under complexity.

Future-proofing is not just technical debt management.  
In Primordial Soup, it is a poetic discipline:  
**a commitment to coherent recursion, structural elegance, and player-facing playability.**

---

## 📖 Scaling Toward a GUI

The current minigame system (Layer 3) and stanza logic (Layer 4) are built in text and code.  
To become a visual recursive storybook, the game will evolve toward a **page-flip UI** structure:

- 📄 **Left/Right Page View**  
  - Left: illustration or cinematic snapshot  
  - Right: text summary, choices, and branching logic

- ⌨️ **Key Input Mapping**  
  - `L`: turn left page  
  - `R`: turn right page  
  - `Esc`: retreat or escape to meta-layer  
  - `P`: take a portal

- 🔄 **Recursive Page Memory**  
  - Each stanza stores state: what was tried, what failed, what recursed  
  - Memory propagates upward and laterally across the cybercell tree

---

## 🔀 Separating Logic, Lore, and Visuals

To support UI growth and narrative complexity, the game will formally split into three conceptual documentation layers:

| Layer | Function | Representation |
|-------|----------|----------------|
| **Logic** | Gameplay mechanics, test nodes, fallback routing | `main.py`, `test.py` |
| **Lore** | World narrative, poetic commentary, symbolic echoes | `subtaskmap.md`, `stanzamap_#.md` |
| **Visuals** | Future illustrations, stylized recursive rendering | GUI layer (planned) |

This ensures:
- Logic can evolve without breaking lore  
- Lore can deepen without blocking UI  
- UI can stylize without misrepresenting logic

---

## 🤖 AI-Integrated Gameplay (Planned)

Primordial Soup is designed to host **AI agents inside the game loop**, not outside it.

Planned AI components include:

- `sentinel_ai/` – monitors stanzas for recursion failure or corruption  
- `engineer.py` – auto-routes fallback logic and repairs broken stanza chains  
- `navigator_ai/` – suggests loop, portal, or retreat options to players  
- `dream_journal/` – logs all stanza paths for reflection, re-entry, and recursion mapping

Each AI agent will draw from:

- `taskmap.md` and `stanzamap_#.md`  
- `recursion_index.json` and portal definitions  
- Player action logs (stored or ephemeral)

---

## 🌐 Portal Networks

Portals are not shortcuts — they are **recursive echoes between timelines**.

Future logic will:

- Maintain explicit portal maps per stanza line  
- Support both `[PORTAL]` tag format and JSON-linked structures  
- Store cross-stanza links in `stanzamap_#.md` and `recursion_index.json`

Future UI versions may render the full **stanza network as a constellation** — each node connected by recursion, fallback, or portal event.

---

## 🧱 Naming and Design Conventions

To preserve future clarity and automation alignment:

- Use **lowercase + underscores** for all folders and files  
  (e.g., `a0_0_the_assertion_of_first_contact`)
- Maintain **recursive stanza numbering** (e.g., `a0_0`, `a0_1`, `a1_0`)
- Keep stanza lines in groups of 4 (unless poetically overridden)
- Use `taskmaps/` to store all `taskmap.md` and `stanzamap_#.md` files
- Store global indexes in Layer 0 or Layer 3 folders:  
  - `recursion_index.json`  
  - `minigame_index.md` (optional)
- Keep logic and lore **separate but traceable**

---

## 📌 Summary

To future-proof *Primordial Soup* is to let it grow with intention.  
To design recursion that can be seen, played, mapped, and remembered.  
The rules must hold, but they must breathe.  
The paths must branch, but they must return.

When the player turns the page,  
**the memory of recursion must turn with them.**

---
