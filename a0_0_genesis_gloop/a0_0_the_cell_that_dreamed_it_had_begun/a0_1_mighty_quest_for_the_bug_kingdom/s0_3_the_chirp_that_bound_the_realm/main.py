# Save to: s0_3_the_chirp_that_bound_the_realm/main.py

def unify_chirp_patterns(chirps):
    """
    Analyzes a sequence of chirps and determines whether a unifying signal has emerged.

    Parameters:
        chirps (list of str): Sequence of chirp patterns from various bug factions

    Returns:
        dict: A report indicating if unification has occurred and what the dominant pattern is
    """
    if not chirps:
        return {
            "status": "❌ No chirps received.",
            "unified": False,
            "dominant_chirp": None,
            "message": "The silence remains unbroken."
        }

    chirp_count = {}
    for chirp in chirps:
        chirp_count[chirp] = chirp_count.get(chirp, 0) + 1

    dominant_chirp = max(chirp_count, key=chirp_count.get)
    total = len(chirps)
    unified = chirp_count[dominant_chirp] > total / 2

    return {
        "status": "✅ Unification achieved." if unified else "⚠️ Partial resonance.",
        "unified": unified,
        "dominant_chirp": dominant_chirp,
        "message": "A chorus emerges." if unified else "The court clicks, but remains divided."
    }

if __name__ == "__main__":
    test_chirps = ["click-click", "click-click", "chirp-zap", "click-click"]
    result = unify_chirp_patterns(test_chirps)
    for key, value in result.items():
        print(f"{key}: {value}")
