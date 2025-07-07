# 📄 main.py
# Path: a0_1_mighty_quest_for_the_bug_kingdom/a0_1_the_trail_that_led_through_mush/main.py

import random

def follow_trail_through_mush(signal_strength, bug_type="scout"):
    """
    Simulates a bug trying to follow a signal trail through uncertain mush.

    Parameters:
        signal_strength (float): The clarity of the trail (0.0 to 1.0)
        bug_type (str): The type of bug attempting to navigate (e.g., "scout", "drone", "king")

    Returns:
        dict: Result of the trail attempt, including confusion, progress, and signal distortion.
    """
    base_confusion = 1.0 - signal_strength
    role_modifier = {
        "scout": 0.8,
        "drone": 1.0,
        "king": 1.2
    }.get(bug_type, 1.0)

    confusion_level = round(base_confusion * role_modifier, 2)
    success_chance = max(0.0, signal_strength - (confusion_level * 0.5))

    progress = random.random() < success_chance

    return {
        "bug_type": bug_type,
        "signal_strength": signal_strength,
        "confusion_level": confusion_level,
        "found_path": progress,
        "comment": "Trail lost in mush." if not progress else "A path emerges, barely."
    }

if __name__ == "__main__":
    result = follow_trail_through_mush(0.6)
    for k, v in result.items():
        print(f"{k}: {v}")
