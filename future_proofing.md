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

The current minigame system (Layer 3) and stanza logic (Layer 4) is built in text and code.  
To make it playable as a visual recursive storybook, we intend to evolve toward a **page-flip UI** structure:

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
  - Memory propagates up and across the cybercell tree

---

## 🔀 Separating Logic, Lore, and Visuals

To support GUI growth and narrative complexity, we will **split the game’s structure into three conceptual layers**:

| Layer | Function | Representation |
|-------|----------|----------------|
| **Logic** | Gameplay mechanics, test nodes, fallbacks | `main.py`, `test.py` |
| **Lore** | World narrative, poetic commentary, voice | `subtaskmap.md`, `stanzamap_#.md` |
| **Visuals** | Future illustrations, symbolic page-flip rendering | GUI layer (planned) |

This ensures:
- Logic can evolve without breaking lore
- Lore can deepen without blocking UI
- UI can stylize without misrepresenting meaning

---

## 🤖 AI-Integrated Gameplay (Planned)

Primordial Soup is designed to host **AI agents** within the game loop, not outside it.

Future-proofing includes:
- `sentinel_ai/`: Monitors stanzas for corruption, anomaly, or recursion collapse
- `engineer.py`: Attempts automatic repair or fallback routing when a stanza breaks
- `navigator_ai/`: Helps the player decide when to loop, recurse, portal, or exit
- `dream_journal/`: Logs all past stanza paths and decision points for re-entry or echo analysis

Each AI component will eventually draw from:
- `taskmap.md` and `stanzamap_#.md`
- `recursive_index.json` and portal definitions
- Player action logs

---

## 🌐 Portal Networks

Portals are not shortcuts — they are recursive echoes between timelines.

We will:
- Maintain explicit portal maps per stanza line
- Support both `[PORTAL]` and JSON notation
- Index portals in `stanzamap_#.md` and eventually in `recursive_index.json`

Future versions of the UI may show a **network of stanzas** like stars in a constellation — each linked by recursion, portal, or fallback.

---

## 🧱 Naming and Design Conventions

To ensure structural clarity:

- Use **underscored lowercase** for all folders and files  
  (e.g., `s0_0_the_assertion_of_first_contact`)
- Maintain **recursive line numbering** (e.g., `s0_0`, `s0_1`, `s1_0`)
- Keep stanza lines in groups of 4 (unless superseded by poetic exception)
- Use `taskmaps/` to hold all `taskmap.md` and `stanzamap_#.md` files
- Store global indexes in root or minigame folders:
  - `recursive_index.json`
  - `minigame_index.md` (optional)
- Keep lore and logic separate but traceable

---

## 📌 Summary

To future-proof Primordial Soup is to let it grow with intention.  
To design recursion that can be seen, played, mapped, and remembered.  
The rules must hold, but they must breathe.  
The paths must branch, but they must return.

When the player turns the page,  
**the memory of recursion must turn with them.**

---
