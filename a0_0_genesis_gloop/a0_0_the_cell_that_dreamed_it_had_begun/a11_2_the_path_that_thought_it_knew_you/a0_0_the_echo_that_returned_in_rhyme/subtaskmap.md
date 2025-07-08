<!-- Save to: subtaskmap.md -->

# 🔁 Subtaskmap – a11_2_0_the_echo_that_returned_in_rhyme

## 🧠 Recursive Node Purpose

This stanza line simulates an echo that returns to the system not in its original form, but **transformed into a poetic cadence**.  
It demonstrates how recursive systems may retain rhythm, emotion, or intent — even when the original data is gone.

The echo claims to "know" the player’s voice, yet what it returns is always slightly altered.

---

## 🎯 Core Subtasks

| Subtask ID | Function                            | Description |
|------------|-------------------------------------|-------------|
| ECHO01     | `return_callback()`                 | Receives user input and responds with a transformed poetic phrase. |
| ECHO02     | `_echo_as_rhyme()`                  | Applies simple syntactic mutation to suggest recursion through rhythm. |
| ECHO03     | Interactive prompt loop (`test.py`) | Allows live testing of recursive echo behavior from the player's perspective. |

---

## 🔍 Test Logic

- Inputs ending in `?` are returned with trailing uncertainty: `"so you ask again?"`
- Inputs ending in `.` are returned with finality: `"and so it became."`
- All other inputs are recursively closed with: `"— or was it always so?"`
- Blank input yields: `"I echo silence where your thought might've been."`

---

## 🧬 Thematic Mapping

| Theme        | Expression in Node Logic |
|--------------|--------------------------|
| Signal Drift | Transforms the phrase, not the data |
| Memory Bias  | Echoes favor pattern over precision |
| Recursive Rhythm | Returns shaped like folklore or prophecy |

---

## 💡 Player Reflection Cue

> “You said it — but I remember it differently.”  
> — The Echo, just before it responds.
