<!-- Save to: C:\Users\Admin\storybook_primordial_soup\player_command_and_field_report_templates.md -->

# 🧠 Player Command and Field Report Templates  
*A Canonical Interface for Recursion-Based Play*

This file defines the recursive interface through which players (and later AI agents) interact with the world of **Primordial Soup**.  
It introduces two core formats:

1. 🎮 **Player Commands** – To issue actions.
2. 📡 **Field Reports** – To return findings.

All future recursion agents, minigames, and automation logic should conform to these formats.

---

## 🎮 Player Command Template

Player commands are single-line directives that invoke action from the game world.  
They begin with `!` and follow a strict, parsable syntax:

`!<verb> <agent> to <target> [with <payload>] [as <alias>]`

### ✅ Valid Examples

!deploy insect scouts to a0_1_side_quest_of_the_forgotten_loop
!invoke memory_agent to a0_2_adventure_of_the_unasked_question
!assign builder to a0_3_yet_both_now_raced_to_test_their_worth with structure_template_v2
!dispatch topsy to forgotten_loop as recon_thread

### 📌 Field Breakdown

| Segment         | Description                                           |
|-----------------|-------------------------------------------------------|
| `!verb`         | Required. Command action (`deploy`, `invoke`, etc.)   |
| `agent`         | Required. The acting entity (`scouts`, `topsy`, etc.) |
| `to` + `target` | Required. Destination (quest, stanza, folder)         |
| `with` + `payload` | Optional. Tool, file, or schema carried            |
| `as` + `alias`  | Optional. Custom thread name or tag                   |

### 📡 Field Report Template
Field reports are structured markdown files that record the outcome of a command or operation.
They live inside the recursion and are treated as system memory.

# 🛰️ Report – [Short Title]

## 🎯 Trigger
- **Command**: `!<original command>`
- **Agent**: `<agent name>`
- **Location**: `<folder or stanza>`

## 📅 Timestamp
[UTC ISO format]

## 📋 Summary
*A 1–3 sentence overview of the operation's result.*

## 🐞 Findings
- Bullet list of anomalies, discoveries, bugs, or system states.
- May include stubs for new quests or reflections.

## 🔧 Recommendations
- Next steps for the player or system.
- Suggestions for patching, escalation, or memory logging.

## 🔗 Linked Entities
- Referenced quests, agents, or memory threads.

## ✅ Status
`PENDING` / `RESOLVED` / `ESCALATE` / `ARCHIVE`
🔁 Why It Matters
Predictable – Future scripts like scout_agent.py or memory_ai.py can parse these easily.

Recursive – Reports feed back into the system, evolving the world through play.

Playable – You can simulate this today using markdown and ChatGPT as your interpreter.

## 🛠️ Companion Systems (Planned)
System	Role	Status
scout_agent.py	Executes command logic, returns reports	PLANNED
field_report_parser.py	Reads field reports, triggers consequences	PLANNED
topsy_core.py	Oversees recursive agent dispatch	PLANNED

## 📄 Status: Canonical
These templates are now official interfaces for player-driven recursion in Primordial Soup.
Any new command or report should conform to them — within the loop, and as part of the game’s living archive.