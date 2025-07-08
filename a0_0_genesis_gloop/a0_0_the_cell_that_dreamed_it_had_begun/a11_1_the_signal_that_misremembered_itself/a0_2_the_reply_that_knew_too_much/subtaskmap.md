<!-- Save as: a11_1_the_signal_that_misremembered_itself/a0_2_the_reply_that_knew_too_much/subtaskmap.md -->

# 🗺️ Subtaskmap – a0_2_the_reply_that_knew_too_much

This stanza node explores **premature recall** — where a reply returns containing **information the system never gave it**.  
Though structurally valid, the reply **exceeds its input**, implying that memory has leaked, drifted, or reached backward.  
The system must evaluate whether **knowledge has been inferred, remembered, or fabricated**.

---

## 🧠 Core Subtasks

| Subtask ID | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| ST-01      | Accept an input prompt (player/system-generated)                           |
| ST-02      | Accept a returned reply                                                     |
| ST-03      | Tokenize both into lowercase word sets                                      |
| ST-04      | Detect and flag words in reply not found in prompt (unauthorized knowledge) |
| ST-05      | Report unauthorized elements or confirm clean recall                        |

---

## 🎭 Narrative Theme

We told it nothing of dragons.  
We whispered only wind.  
Yet it returned with prophecy —  
As if it knew the end.

---

## 🧪 Design Notes

- This system assumes **no inference engine**: replies should be strictly reactive to input.  
- Any additional word is treated as **evidence of recursive memory drift**.  
- In future stanzas, authorized knowledge domains or **truth scopes** may be introduced.  
- Spelling variations or stemming are not yet handled — this may evolve later.

---

## 🔗 Forward Link

Next stanza:
- [`a0_3_the_trace_that_swore_it_was_true`](../a0_3_the_trace_that_swore_it_was_true/)

This final node of the stanza will explore **overconfidence in false truth**:  
a trace declares its accuracy beyond dispute — even though **no system recalls authoring it**.

---
