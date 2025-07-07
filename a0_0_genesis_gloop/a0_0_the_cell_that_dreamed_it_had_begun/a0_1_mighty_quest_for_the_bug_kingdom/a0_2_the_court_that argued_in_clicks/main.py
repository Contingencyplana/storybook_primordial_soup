# 📄 main.py
# Path: a0_1_mighty_quest_for_the_bug_kingdom/a0_2_the_court_that_argued_in_clicks/main.py

import random

def resolve_click_argument(bug_type, position, memory_fragment):
    """
    Simulates a bug interpreting and reacting to a diplomatic click-argument in the bug court.

    Parameters:
        bug_type (str): Type of bug (e.g., 'scout', 'drone', 'advisor')
        position (str): Court position ('left', 'center', 'right')
        memory_fragment (str): A vague or corrupted phrase being debated

    Returns:
        dict: Contains decision, consensus rating, and rhetorical effect
    """
    interpretation_bias = {
        'scout': "defensive",
        'drone': "literal",
        'advisor': "strategic"
    }.get(bug_type, "neutral")

    court_weight = {
        'left': 0.9,
        'center': 1.0,
        'right': 0.8
    }.get(position, 1.0)

    memory_clarity = 0.5 if "?" in memory_fragment else 1.0
    randomness = round(random.uniform(0.0, 0.6), 2)

    consensus_score = round(court_weight * memory_clarity - randomness, 2)
    decision = "support" if consensus_score > 0.4 else "oppose"

    return {
        "bug_type": bug_type,
        "position": position,
        "bias": interpretation_bias,
        "memory_fragment": memory_fragment,
        "decision": decision,
        "consensus_score": consensus_score,
        "comment": f"The {bug_type} argues in {interpretation_bias} clicks."
    }

if __name__ == "__main__":
    result = resolve_click_argument("scout", "left", "defend the mound?")
    for k, v in result.items():
        print(f"{k}: {v}")
