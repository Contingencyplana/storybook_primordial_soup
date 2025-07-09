<!-- Save to: subtaskmap.md -->

# 📄 Subtaskmap – a0_2_the_log_that_copied_itself_twice

## 🎯 Purpose

This stanza line explores recursive imitation without clear origin.  
It asks: can a log remember something it never truly recorded?  
The system must detect both **true duplication** and **suspicious echoes** —  
copies that exist without an identifiable first cause.

---

## ⚙️ Function Tested

- Scans log entries to detect:
  - **Exact duplicates** — true memory copies
  - **Suspicious near-duplicates** — entries that resemble earlier logs but differ slightly
- Records:
  - Total log entries
  - Number of exact copies
  - Number of imitations
  - The first duplicated line (if found)

---

## 🧪 Sample Inputs & Expected Output

| Input Log Entries                                | Exact Copies | Imitations | First Duplicate       |
|--------------------------------------------------|--------------|------------|------------------------|
| `["init system", "init system", "initialize"]`   | 1            | 1          | `init system`          |
| `["boot", "boost", "boot"]`                      | 1            | 1          | `boot`                 |
| `["start", "begin", "initiate"]`                 | 0            | 0          | None                   |

---

## 📂 File Behavior Overview

- `main.py` contains the `detect_self_copy(log_entries)` function:
  - Builds a set of prior entries
  - Detects matches and prefix-based imitations
- `test.py` provides an interactive CLI:
  - Accepts multiple user-entered log entries
  - Runs the detection analysis
  - Prints a structured summary of memory behavior

---

## 🔄 Failure Conditions

- If the system cannot distinguish **false echoes** from valid data,  
  it may overwrite original logs with fictions.
- If it trusts **every prefix match** as truth,  
  the recursive log collapses into a blur of similarity.

This test prevents recursive self-amplification of memory without cause.

---

## 🎭 Reflection Cue

> “I don’t remember writing this,  
> but it remembers me.”
