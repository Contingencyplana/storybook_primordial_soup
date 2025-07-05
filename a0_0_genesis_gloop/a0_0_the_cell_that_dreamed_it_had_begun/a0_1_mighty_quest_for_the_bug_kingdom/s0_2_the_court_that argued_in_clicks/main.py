# Save to: s0_2_the_court_that_argued_in_clicks/main.py

def interpret_clicks(click_pattern):
    """
    Interprets the click pattern of insect delegates in the court.

    Parameters:
        click_pattern (str): A string representing the rhythm of clicks.

    Returns:
        dict: A structured interpretation of the court's sentiment and unity.
    """
    if "— — —" in click_pattern or click_pattern.count("—") > 5:
        return {
            "sentiment": "🛑 Hostile",
            "message": "Tensions rise. Factions clash.",
            "unified": False
        }
    elif "· — ·" in click_pattern or click_pattern.strip() == "· · ·":
        return {
            "sentiment": "🤝 Diplomatic",
            "message": "The court is listening. Consensus is forming.",
            "unified": True
        }
    elif click_pattern.count("·") > click_pattern.count("—"):
        return {
            "sentiment": "🪲 Curious",
            "message": "Delegates murmur. Curiosity flickers.",
            "unified": False
        }
    else:
        return {
            "sentiment": "😐 Unclear",
            "message": "The clicks carry no clear meaning.",
            "unified": False
        }

if __name__ == "__main__":
    result = interpret_clicks("· — ·")
    for k, v in result.items():
        print(f"{k}: {v}")
