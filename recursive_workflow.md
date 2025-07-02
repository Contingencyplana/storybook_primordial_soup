<!-- Save to: storybook_primordial_soup/recursive_workflow.md -->

# 🔁 Recursive Workflow of Primordial Soup  
*How development becomes gameplay — and recursion becomes design*

---

## 🧭 Purpose

This document defines the **lived recursive rhythm** of the Primordial Soup project.  
It describes how a player (who is also the developer) flows between:

- Playing recursive minigames  
- Solving design and development puzzles  
- Building new logic and stanzas  
- Returning to code and documentation  
- And eventually... playing again

It outlines the **cycle of recursion**, not just the technical workflow — the rhythm of building a game *from inside itself*.

---

## 🎮 The Player–Builder Rhythm

Every interaction in Primordial Soup becomes part of a recursive cycle:

1. **Play a minigame** — solve a design or dev task by completing a stanza.
2. **Advance logic** — trigger a test, portal, or fallback branch.
3. **Receive feedback** — win, fail, loop, or “RECURSION CLOSED”.
4. **Return to code/docs** — only if the game requires external change.
5. **Repeat** — the recursion deepens with every minigame played.

This loop replaces the typical cycle of:

> Write code → Save → Test manually → Push  
with:

> Play minigame → Trigger recursion → Document through gameplay → Only break loop if needed

---

## 🧩 Minigame Types

| Type | Description | Example |
|------|-------------|---------|
| **Development Task Minigame** | Encodes or tests backend logic (e.g. fallback chains, trace validation) | `a0_0_the_test_that_called_itself` |
| **Design Task Minigame** | Asks player to decide names, quests, branching rules, or layouts | `a0_1_side_quest_of_the_forgotten_loop` (hypothetical) |

Both types are structured identically — but the *puzzle* and *payload* differ.

---

## 🔄 Minigame-to-Minigame Transitions

Each minigame ends by transitioning in one of three ways:

| Transition Type | Description | Trigger |
|------------------|-------------|---------|
| `Handoff (Direct)` | Auto-forwards player to the next minigame | “VICTORY! You proceed to…” |
| `Handoff (Choice)` | Presents multiple portals or next minigames | “Press [L] to go left, [R] to go deeper…” |
| `Recursion Closed` | Ends loop and returns player to code/docs | “RECURSION CLOSED. Exit stanza.” |

These transitions are embedded in the final `main.py` or `test.py` node of each stanza.

---

## 🧠 When Recursion Breaks

Sometimes the recursive loop cannot continue — and **must return to raw development**:

| Break Trigger | Action |
|---------------|--------|
| Missing stanza logic | Author new stanza node (Layer 4) |
| No valid fallback exists | Write code or repair stanza |
| Game needs new tool (e.g. auto-indexer) | Pause recursion and develop it |
| Game needs new doc (e.g. future_proofing.md) | Return to prose to expand the loop’s capacity |

These breaks are rare — and *should feel like signal events*.  
When recursion breaks, the game asks you to grow it.

---

## 📈 Long-Term Recursive Arc

As Primordial Soup grows, its rhythm shifts:

| Phase | Experience |
|-------|------------|
| Early | Mostly code and prose, occasional minigames |
| Mid | Equal blend of CLI gameplay and recursive docs |
| Mature | Long chains of gameplay, rare returns to code |
| Full | Self-generating minigames, players build through play |

The player becomes the engine.  
Recursion becomes the interface.  
Minigames become the build system.

---

## 📜 Summary

This file defines the recursive experience of building — and being built by — *Primordial Soup*.

You play to code.  
You code to recurse.  
You recurse to play again.

And every stanza you solve brings the game one step closer to building itself.