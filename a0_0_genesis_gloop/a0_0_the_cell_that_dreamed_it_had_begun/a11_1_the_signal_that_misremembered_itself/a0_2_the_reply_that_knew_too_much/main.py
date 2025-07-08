# 🧠 main.py – The Reply That Knew Too Much
# This file implements a signal comparison system where a reply is evaluated
# not just for structural correctness, but for unauthorized knowledge leakage.

def extract_keywords(text):
    words = text.strip().lower().split()
    return set(words)

def detect_unauthorized_knowledge(prompt, reply):
    prompt_keywords = extract_keywords(prompt)
    reply_keywords = extract_keywords(reply)

    # Unauthorized knowledge = reply contains keywords not in prompt
    unauthorized = reply_keywords - prompt_keywords
    return unauthorized
