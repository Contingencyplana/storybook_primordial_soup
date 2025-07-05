# Save to: s0_1_the_trail_that_led_through_mush/main.py

import random

def navigate_fungal_maze(path_choice="forward"):
    """
    Simulates traversal through a confusing fungal trail.

    Parameters:
        path_choice (str): Direction chosen – "forward", "left", or "right"

    Returns:
        dict: Trail feedback, obstacle result, and next decision hint
    """
    trail_conditions = {
        "forward": "The mush deepens. Strange spores cloud your antennae.",
        "left": "A slippery slope descends into clicking echoes.",
        "right": "Faint chirps beckon, but the ground pulses unevenly."
    }

    if path_choice not in trail_conditions:
        return {
            "status": "❌",
            "message": "Lost in the fog. Invalid trail choice.",
            "confused": True
        }

    confusion_factor = random.choice([True, False])

    return {
        "status": "🧭",
        "message": trail_conditions[path_choice],
        "confused": confusion_factor,
        "suggested_next": "follow the rhythm" if not confusion_factor else "pause and recalibrate"
    }

if __name__ == "__main__":
    outcome = navigate_fungal_maze("forward")
    for key, value in outcome.items():
        print(f"{key}: {value}")
