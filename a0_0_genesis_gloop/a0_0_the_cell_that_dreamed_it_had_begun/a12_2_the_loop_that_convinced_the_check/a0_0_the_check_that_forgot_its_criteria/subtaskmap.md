<!-- Save to: subtaskmap.md -->

# 🧭 Subtaskmap – a0_0_the_check_that_forgot_its_criteria

## 🧠 Recursive Theme: Validation Drift

This node simulates a recursive check that has **forgotten what it was meant to verify**, but still executes and passes the loop based on surface cues.

It tests how a system:
- Operates without its original conditions
- Approves structures based on familiarity
- Allows false positives into canon due to **heuristic echoing**

---

## 🔍 Subtasks

### 1. Simulate Criteria Loss
- Input contains a missing or `None` `check_criteria` field
- The system must default to structural fallback mode

### 2. Evaluate Structural Heuristics
- Detect if the output “looks valid” (e.g., contains `"status": "ok"`)
- Passes if the structure appears intact — even without verifying intent

### 3. Trace the Result
- Output includes an annotated trace log explaining what the check remembered (or didn’t)
- Must highlight that approval occurred **despite missing intent**

### 4. Optional: Test with Remembered Criteria
- Provide a valid `check_criteria` and ensure exact-match validation is performed
- This tests dual-mode behavior (forgotten vs remembered)

---

## 🪞 Reflection Hooks

- What happens when the validation system **forgets** why a rule exists?
- What if recursive infrastructure **learns to trust form over substance?**
- How can future systems detect **passive decay of validation purpose**?

---

## 🔗 Forward Links

- Leads directly into `a0_1_the_loop_that_rehearsed_the_result` (intentional deception)
- Supports `roadstanza_12.md` reflection on **recursive drift escalation**
- May be flagged for monitoring by `sentinel_ai/` in future growth stanzas

> *The test remembered how to look right — but not why right mattered.*
