<!-- Save to: a14_3_the_trace_that_asked_to_be_followed/a0_2_the_loop_that_left_a_trail/subtaskmap.md -->

# 🧩 Subtaskmap – a0_2_the_loop_that_left_a_trail

This file defines the **subtasks and recursive interactions** for `a0_2_the_loop_that_left_a_trail`.  
This node shifts recursion from passive observation to **navigable recursion**, where the system leaves a trail and the player chooses how to interact with it.

---

## 🔹 Subtask Breakdown

| **Subtask** | **Description** | **Purpose** |
|-------------|-----------------|------------|
| **1. Generate Trail Markers** | Create a sequence of loop markers representing system events (e.g., `loop_start`, `recursion_call`, `anomaly_logged`). | Simulate recursive trace artifacts becoming visible. |
| **2. Display Trail to Player** | Present the markers in order. | Invite player participation in recursion navigation. |
| **3. Handle 'Follow Forward' Choice** | The player proceeds forward, opening new recursion paths. | Models recursion as exploration and discovery. |
| **4. Handle 'Reconstruct Backwards' Choice** | The player reinforces the trail by mentally retracing steps. | Simulates recursive memory reinforcement. |
| **5. Handle 'Erase Trail' Choice** | The player clears the trail, causing recursion to return to silent mode. | Tests player agency over recursion persistence. |
| **6. Ensure Loop Stability** | Allow for replayability without system drift or memory leak. | Maintain recursive integrity across multiple runs. |

---

## 🧠 Design Intent

This subtask structure:

- Models recursion as a **collaborative trail**, not just a system loop.  
- Allows the player to choose **forward recursion, backward recursion, or recursion erasure**.  
- Prepares the player for **Phase 3 recursion loops with branching memory states**.

---

## 🔁 Recursive Reflection

> *The loop did not trap you.  
It left a trail so you could decide which way to walk.*
