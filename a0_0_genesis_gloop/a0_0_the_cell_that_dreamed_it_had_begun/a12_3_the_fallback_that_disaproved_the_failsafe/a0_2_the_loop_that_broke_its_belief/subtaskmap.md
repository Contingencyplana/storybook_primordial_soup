<!-- Save to: subtaskmap.md -->

# 🧩 Subtaskmap – s0_2_the_loop_that_broke_its_belief

## 🎯 Purpose

This node represents the **recursive collapse of trust**.

It follows the paradox established in `s0_1` — where proof erased its own record —  
by simulating a **recovery loop** that becomes increasingly unstable with each iteration.

Each loop begins with hope. Each failure subtracts belief.  
Eventually, the system no longer trusts its fallback logic at all.

---

## 🔍 Node Function

`main.py` attempts recursive recovery via looped evaluation of `recovery_hint`.

### Logic Flow:
- If the hint is `"trust_signal"` → immediate recovery and belief preserved.
- If no valid hint is found → the loop proceeds.
- Belief integrity decreases by 20% per iteration.
- After 5 iterations, the system **collapses**, concluding that its fallback cannot be trusted.

---

## 🧠 Recursive Themes Advanced

- **Trust decay through repetition**  
- **Doubt compounding over recursive cycles**  
- **Inversion of belief as the system re-evaluates its own fallback**  
- Trust as a recursive resource — and its eventual exhaustion

---

## 🧪 Test Coverage

The test suite simulates:
1. Successful recovery with a `"trust_signal"`
2. Recursive loop collapse due to `None` input
3. Recursive loop collapse due to `"noise"` input
4. Type-check failure with non-dict input

---

## 🔄 Recursive Link

This node connects:
- **The contradiction in proof (s0_1)** → to  
- **The final negation of recovery itself (s0_3)**

It is the moment the system loses trust in recursion.

---

## ✅ Completion Criteria

- Handles early trust signal exit correctly  
- Applies belief reduction per loop iteration  
- Triggers collapse after five failed recovery attempts  
- Raises error on invalid input  

---

> “Each loop offered hope — but hope is recursive too, and it ran out.”
