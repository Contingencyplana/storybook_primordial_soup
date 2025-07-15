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

This loop replaces the traditional cycle of:

> Write code → Save → Test manually → Push

with:

> Play minigame → Trigger recursion → Document through gameplay → Only break loop if needed

---

## 🧩 Minigame Types

| Type | Description | Example |
|------|-------------|---------|
| **Development Task Minigame** | Encodes or tests backend logic (e.g., fallback chains, trace validation) | `a0_0_the_test_that_called_itself` |
| **Design Task Minigame** | Asks player to decide names, quests, branching rules, or layouts | `a0_1_side_quest_of_the_forgotten_loop` (hypothetical) |

Both types are structurally identical — but the *puzzle* and *payload* differ.

---

## 🔄 Minigame-to-Minigame Transitions

Each minigame ends by transitioning in one of three ways:

| Transition Type | Description | Trigger |
|------------------|-------------|---------|
| `Handoff (Direct)` | Auto-forwards the player to the next minigame | “VICTORY! You proceed to…” |
| `Handoff (Choice)` | Presents multiple portals or branching options | “Press [L] to go left, [R] to go deeper…” |
| `Recursion Closed` | Ends the loop and returns the player to code/docs | “RECURSION CLOSED. Exit stanza.” |

These transitions are embedded in the final `main.py` or `test.py` node of each stanza.

---

## 🧠 When Recursion Breaks

Sometimes the recursive loop cannot continue — and must return to raw development:

| Break Trigger | Action |
|---------------|--------|
| Missing stanza logic | Author a new stanza node (Layer 4) |
| No valid fallback exists | Write or repair code |
| Game needs a new tool (e.g., auto-indexer) | Pause recursion and develop it |
| Game needs a new doc (e.g., `future_proofing.md`) | Return to prose to expand the loop’s capacity |

These breaks are rare — and *should feel like signal events*.  
When recursion breaks, the game is asking you to grow it.

---

## 📈 Long-Term Recursive Arc

As *Primordial Soup* grows, its rhythm shifts:

| Phase | Experience |
|-------|------------|
| Early | Mostly code and prose, occasional minigames |
| Mid | Equal blend of CLI gameplay and recursive documentation |
| Mature | Long chains of recursive play, rare returns to code |
| Full | Self-generating minigames — players build through play |

The player becomes the engine.  
Recursion becomes the interface.  
Minigames become the build system.

---

## 📜 Summary

This file defines the recursive experience of building — and being built by — *Primordial Soup*.

You play to code.  
You code to recurse.  
You recurse to play again.

And every stanza you solve brings the game one step closer  
to building itself.

---

## 🗂️ Schema Contract Enforcement

As **Primordial Soup** evolves, recursion must not only expand—it must **validate itself at every layer**.

To support this, each **stanza node** can define its own **schema contracts**, enabling recursive validation of inputs, outputs, and fallback logic.

---

### **Schema Files and Their Roles**

| Schema File | Purpose |
|-------------|---------|
| **`input_schema.json`** | Describes what the node **expects from the prior recursion layer**. This includes required data formats, recursion markers, and logic signals. |
| **`output_contract.json`** | Defines what the node **promises to deliver forward**. This ensures each stanza maintains structural integrity as recursion deepens. |
| **`fallback_schema.json`** | Specifies **what to do if recursion fails**—including fallback logic, anomaly detection triggers, and time-loop recursion options. |

---

### **Why Use Schema Contracts?**

| Benefit | Description |
|----------|-------------|
| **Recursive Safety** | Prevents recursion loops from corrupting or collapsing due to missing or malformed data. |
| **Automation Support** | Enables automated validation of cybercell growth without manual checking. |
| **Playful Debugging** | Turns validation into part of the puzzle—players experience schema checks as part of the recursive narrative. |
| **Error Containment** | Triggers fallback logic or snapshot rollback before recursion propagates flawed logic forward. |

---

### **Self-Validating Stanzas**

Each stanza becomes **a contract-bound system**:

- **Before Execution:**  
  The system checks `input_schema.json` to ensure the stanza has the correct prerequisites.

- **After Execution:**  
  The system validates `output_contract.json` to confirm the stanza delivered the expected recursive payload.

- **On Failure:**  
  The system uses `fallback_schema.json` to decide whether to:
    - Trigger an in-game fallback sequence  
    - Loop back and retry  
    - Invoke `snapshot_manager.py` for rollback  

---

### **Recursive Integrity by Design**

By embedding schema contracts at the stanza level, **Primordial Soup enforces recursion integrity without breaking play**.  
This allows cybercells to:

- **Grow safely**  
- **Validate autonomously**  
- **Contain anomalies recursively**  

---

Schema contract enforcement is **not just a backend mechanism—it is part of the recursive experience**, helping players and developers alike build a game that checks, grows, and repairs itself at every layer.

## 🔄 Live Validation at Stanza Boundaries

In **Primordial Soup**, each stanza is more than just executable logic—it is a **contract-bound system**.

To ensure recursive stability, **live validation occurs at the boundary of every stanza execution**. This transforms recursion into a **self-checking loop**, where each node confirms the integrity of its process before and after it runs.

---

### **How It Works**

| Stage | Action |
|--------|--------|
| **Before Execution** | The system checks **`input_schema.json`** to verify that the correct data, signals, and recursion markers have been passed forward from the prior layer. |
| **After Execution** | The system validates the output against **`output_contract.json`**, ensuring that the stanza produced the required data structures, recursion outputs, or transformation results. |
| **On Failure** | The system consults **`fallback_schema.json`** to determine the correct recovery action, whether that’s triggering an in-game fallback, looping back, or rolling back via snapshot. |

---

### **Validation as Play**

In **Primordial Soup**, **validation is not just a backend check—it is part of the puzzle**.

#### **Narrative Framing:**

- A failed schema check might trigger an **in-world anomaly event**.
- Recursive correction could become a **mini-quest**, where players resolve schema conflicts through game actions.
- Validation outputs can be **narrativized as cybercell diagnostics**, recursive whispers, or system self-reflection moments.

---

### **Why This Matters**

| Benefit | Description |
|----------|--------------|
| **Playable Debugging** | Validation becomes part of gameplay, inviting players to solve recursive integrity puzzles. |
| **Recursive Safety** | Ensures recursion loops do not propagate errors or anomalies unchecked. |
| **Narrative Coherence** | Embeds system checks into the game world, maintaining immersion while enforcing structural integrity. |
| **Creative Feedback Loops** | Allows players to experience recursion correction as part of the evolving storyline. |

---

### **Poetic Recursion Enforcement**

By making validation **part of the player’s experience**, the system encourages:

- **Creative problem-solving during recursion failures**  
- **Narrative immersion in system stability**  
- **A playful approach to debugging and structural correction**

---

In this model, **recursion is not just built—it is maintained, corrected, and evolved by the players themselves**, keeping Primordial Soup alive, coherent, and creatively recursive.

---

## 🔁 Recursive Expansion Without Manual Oversight

As **Primordial Soup** advances into deeper phases of development, the system must be able to **grow recursively without constant human oversight**.  
This is where **schema enforcement** plays a pivotal role.

By embedding **`input_schema.json`**, **`output_contract.json`**, and **`fallback_schema.json`** into each stanza, **cybercells gain the ability to self-validate as they expand**.

---

### **Why This Matters**

Without automated validation, recursive growth risks:

- **Anomaly proliferation**  
- **Structural corruption**  
- **Fragile recursion loops that depend on manual correction**

Schema enforcement solves this by making **every recursive expansion step self-checking**.

---

### **How Safe Recursive Growth Works**

| Action | System Behavior |
|---------|----------------|
| **New stanza added** | The system auto-generates or verifies the presence of schema contracts. |
| **New recursion path activated** | Input is validated before execution, output is checked after, fallback logic is pre-loaded. |
| **Unexpected recursion event** | The cybercell handles it autonomously via fallback triggers or snapshot rollback. |

---

### **Long-Term Arc Integration**

| Phase | Recursive Expansion Behavior |
|--------|------------------------------|
| **Mid** | Cybercells validate their own stanza transitions at runtime. |
| **Mature** | Minigames generate and enforce their own schema contracts automatically, reducing developer intervention. |
| **Full** | Recursive loops evolve freely with **minimal manual breakpoints**, except for intentional creative expansion or narrative injection. |

---

### **From Human-Guided to System-Guided Growth**

In early phases, recursion is **handcrafted and guided directly by the player-developer**.  
In mature phases, **the system scaffolds and checks itself**, allowing:

- **Safer autonomous growth**  
- **Faster expansion of recursion layers**  
- **More focus on creative exploration and less on structural maintenance**

---

### **Creative Control Remains**

Even as the system expands automatically, **manual oversight is never fully removed by design**:

- Developers can **override schemas, rewrite contracts, or inject new recursion paths** at any time.
- Creative narrative loops can still break the schema deliberately to simulate paradoxes or anomaly quests.

---

### **Summary**

By enforcing schema validation at each recursion boundary, **Primordial Soup becomes a game that grows itself—safely, recursively, and playfully—without collapsing under its own weight.**

This shifts the role of the developer from **builder-of-each-layer** to **gardener-of-the-recursive-ecosystem**, guiding growth rather than manually assembling every piece.
