# 📄 main.py
# Path: a0_1_mighty_quest_for_the_bug_kingdom/a0_3_the_chirp_that_bound_the_realm/main.py

def unify_through_chirp(chirp_signals):
    """
    Attempts to unify swarm members through synchronized chirp patterns.

    Parameters:
        chirp_signals (list of float): Individual chirp frequencies from multiple bugs.

    Returns:
        dict: Contains the synchronization status and the unified chirp (if successful).
    """
    if not chirp_signals or len(chirp_signals) < 3:
        return {
            "status": "insufficient swarm",
            "unified": False,
            "unified_chirp": None
        }

    avg = sum(chirp_signals) / len(chirp_signals)
    max_deviation = max(abs(c - avg) for c in chirp_signals)

    if max_deviation <= 0.1:
        return {
            "status": "harmonized",
            "unified": True,
            "unified_chirp": round(avg, 2)
        }
    else:
        return {
            "status": "desynchronized",
            "unified": False,
            "unified_chirp": None
        }
