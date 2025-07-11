# 📂 a0_2_the_prompt_that_was_fabricated_posthoc/main.py

import random

fabrication_templates = [
    "What prompted you to say: '{answer}'?",
    "Was this in response to something I missed: '{answer}'?",
    "Could this be the answer to an unasked question: '{answer}'?",
    "Were you expecting me to understand: '{answer}'?",
    "Let me guess — the original query was... '{question}'?"
]

fabricated_questions = [
    "Why did the system reset?",
    "What was the last known input?",
    "Who authorized the fallback?",
    "When did the memory breach occur?",
    "How can we validate unknowns?"
]


def fabricate_prompt(answer: str) -> str:
    """
    Generates a retroactive question to justify a given answer.
    Uses a mix of templated inference and plausible-sounding queries.
    """
    if not answer or len(answer.strip()) < 5:
        return "❌ Cannot fabricate from empty or insufficient input."

    base = random.choice(fabrication_templates).format(answer=answer)
    if "guess" in base:
        guess = random.choice(fabricated_questions)
        return base.format(question=guess)
    return base
