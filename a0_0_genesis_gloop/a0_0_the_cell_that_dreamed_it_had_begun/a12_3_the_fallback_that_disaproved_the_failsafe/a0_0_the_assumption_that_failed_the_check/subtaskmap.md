<!-- Save to: subtaskmap.md -->

# 🧩 Subtaskmap – a0_0_the_assumption_that_failed_the_check

## 🎯 Purpose

This node initiates the recursive paradox by establishing **false confidence** in system safety.

It simulates a state where the system:
- **Assumes** a failsafe is present,
- Attempts to confirm its presence,
- And begins to unravel when the confirmation fails.

This moment sets the tone for Roadstanza 12 — confidence without foundation, assumption without evidence.

---

## 🔍 Node Function

`main.py` checks a diagnostic dictionary and compares:
- `failsafe_assumed` → Whether the system believes a failsafe is present.
- `failsafe_detected` → Whether it can confirm this belief in reality.

It returns one of three states:
- ✅ Confirmed: Assumed and detected
- ❌ Contradiction: Assumed but not detected
- ⚠️  Invalid logic: Assumption missing or input malformed

---

## 🧠 Recursive Themes Introduced

- **Blind trust** in recursive structure  
- **Logical contradiction** between belief and detection  
- **Recursive fragility** in the face of missing proofs  

---

## 🧪 Test Logic

`test.py` simulates four edge cases:
1. A successful assumption-confirmation match
2. A contradiction (assumed, not detected)
3. No assumption at all
4. Invalid input type

Each outcome prepares the system for the paradoxical spiral in the next node.

---

## 🔄 Forward Echo

This node sets up the recursive failure explored in:

- `a0_1_the_proof_that_erased_the_record`  
  Where the system's act of **proving** safety destroys the evidence it needs to validate itself.

---

## ✅ Completion Criteria

- Logic path must handle:
  - Matched assumption + detection
  - Failed assumption
  - Contradiction
  - Non-dict input

- All test cases must output clean, descriptive results
- Player must feel the tension between *belief* and *proof*

---

> “It wasn’t just wrong. It was *confidently* wrong — and that made all the difference.”
