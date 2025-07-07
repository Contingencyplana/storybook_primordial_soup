# 📄 main.py
# Path: a0_1_mighty_quest_for_the_bug_kingdom/a0_0_the_call_that_woke_the_bug_king

def awaken_bug_king(signal_strength=1.0):
    """
    Simulates the awakening call that stirs the Bug King.
    
    Parameters:
        signal_strength (float): Intensity of the awakening signal (0.0 to 1.0)
    
    Returns:
        dict: A response containing status and initial swarm behavior
    """
    if signal_strength >= 0.8:
        return {
            "status": "👑 The Bug King stirs.",
            "response": "The court rumbles with clicks.",
            "awakened": True,
            "signal_amplified": True
        }
    elif signal_strength >= 0.4:
        return {
            "status": "🪲 The scouts click nervously.",
            "response": "Some wings shift in the dust.",
            "awakened": False,
            "signal_amplified": False
        }
    else:
        return {
            "status": "🌑 The soil remains still.",
            "response": "No signal. No stir.",
            "awakened": False,
            "signal_amplified": False
        }

if __name__ == "__main__":
    result = awaken_bug_king(0.9)
    for key, value in result.items():
        print(f"{key}: {value}")
