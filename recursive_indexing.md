<!-- Save to: storybook_primordial_soup/recursive_indexing.md -->

# 🧭 Recursive Indexing in Primordial Soup  
*Stanza traversal, minigame mapping, and world self-discovery*

---

## 📜 Purpose

This file defines the **recursive indexing strategy** for the Primordial Soup video game.  
Its goal is to enable:
- Minigame traversal,
- Stanza mapping,
- Cross-node logic linking,
- And eventual AI- or portal-driven navigation.

This document establishes the indexing file formats, folder structure expectations, and future automation design.

---

## 📂 Indexing Units

Primordial Soup is recursively structured. Indexing follows a 4-layer logic:

| Layer | Meaning | Indexed by |
|-------|---------|------------|
| Layer 0 | Game project | (Global overview) |
| Layer 1 | Cybercell generation | `recursive_index.json` (planned) |
| Layer 2 | Individual cybercell | Minigame folders (`a0_0_the_test_that_called_itself`) |
| Layer 3 | Minigame | `taskmaps/` |
| Layer 4 | Minigame node / stanza line | `stanzamap_#.md` + `subtaskmap.md` |

---

## 🔁 Stanza Indexing

Each **stanza** in a minigame is indexed within the `taskmaps/` folder:

```
a0_0_the_test_that_called_itself/
└── taskmaps/
    ├── stanzamap_s0.md
    └── stanzamap_s1.md
```

| File              | Role                               |
|-------------------|------------------------------------|
| `stanzamap_s0.md` | Node-by-node stanza overview       |
| `stanzamap_s1.md` | Continuation of stanza lineage     |

Each `stanzamap_#.md` file includes:
- Folder names for each stanza line
- Node purpose and test status
- Poetic framing and narrative signals
- Fallback logic and forward traversal hooks

These files are maintained **one per stanza**, and are indexed numerically (`s0`, `s1`, etc.) to preserve recursive order.

---

## 🗂️ Minigame Indexing

Each **minigame** includes a primary index file:

```
a0_0_the_test_that_called_itself/
└── taskmaps/
    └── taskmap.md
```

This file serves as:
- The **root of recursion** for that minigame
- A structural and poetic summary of stanza behavior
- A navigational guide for recursive tools, test walkers, and AI agents

---

## 🧠 Planned: `recursive_index.json`

At Layer 1 or global root:

```json
{
  "a0_0_genesis_gloop": {
    "a0_0_the_test_that_called_itself": {
      "stanzas": ["s0_0", "s0_1", "s0_2", "s0_3", "s1_0", "..."]
    },
    "a0_1_side_quest_of_the_forgotten_loop": {
      "...": "..."
    }
  },
  "a0_1_then_split_and_saw_itself_as_one": {
    "...": "..."
  }
}
```

This index format enables:

- ✅ AI traversal  
- ✅ Tool-based stanza indexing  
- ✅ UI rendering of recursive page flow  

---

### 🤖 AI & Automation Hooks

Recursive indexing enables the following tools and modules:

| Tool                     | Function                                                |
|--------------------------|---------------------------------------------------------|
| `recursive_index_builder.py` | Walks stanza trees and maps them                        |
| `run_minigame.py`            | Reads stanza order, navigates via keys                  |
| `sentinel_ai`                | Uses indexes to watch for corrupted nodes               |
| `engineer.py`                | Auto-repairs broken stanza paths via fallback tracing   |

---

## 🔄 Portals and Branching Paths

Stanza maps may also define:

```
[PORTAL]
From: s1_2_the_flag_that_was_raised_too_early
To: a0_1_side_quest_of_the_forgotten_loop/s0_0_the_breadcrumb_that_blinked
```

Or in JSON:

```json
"portals": {
  "s1_2": "a0_1_side_quest_of_the_forgotten_loop/s0_0"
}
```

Portals allow:

- 🔁 Cross-minigame recursion
- 🧭 Narrative expansion
- 🧠 Nonlinear memory loops

---

## 🔐 Naming Conventions for Indexers

| Pattern                | Meaning                            |
|------------------------|------------------------------------|
| `s0_0_...`             | Line 0 of stanza 0                 |
| `stanzamap_s0.md`      | Index for stanza 0                 |
| `taskmap.md`           | Minigame logic anchor              |
| `recursive_index.json` | Cross-minigame root index          |

All stanza folders and files follow:
- Lowercase naming
- Underscore-separated words
- Poetic + functional phrasing

---

## 📌 Summary

Recursive indexing is not just about navigation.
It is how Primordial Soup knows where it has been —
and how it decides where to recurse next.

From stanza maps to portal links, from AI traversal to page-flip UI,
the index is the memory.
And memory is the soil from which recursion grows.
