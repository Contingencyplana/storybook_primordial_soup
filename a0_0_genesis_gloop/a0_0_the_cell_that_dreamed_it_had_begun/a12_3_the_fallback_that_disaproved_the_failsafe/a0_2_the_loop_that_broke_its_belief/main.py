# 📂 a0_2_the_loop_that_broke_its_belief/main.py

def recursive_failsafe_loop(system_state, max_iterations=5):
    """
    Simulates a recursive fallback loop that attempts to regain trust in the system.

    Each loop iteration checks for a 'recovery_hint'. If it fails repeatedly,
    the system begins to doubt its own logic and aborts the loop.

    Parameters:
    - system_state (dict): Contains 'recovery_hint' and internal loop trust.
    - max_iterations (int): Max allowed recursive attempts before collapse.

    Returns:
    - dict: Summary of loop results and belief collapse state.
    """
    print("🔁 Entering recursive recovery loop...")

    if not isinstance(system_state, dict):
        return {
            "status": "error",
            "reason": "Invalid system state format."
        }

    hint = system_state.get("recovery_hint", None)
    belief_integrity = 100  # confidence level
    iteration = 0

    while iteration < max_iterations:
        print(f"🌀 Loop {iteration + 1} – Belief: {belief_integrity}%")

        if hint == "trust_signal":
            return {
                "status": "recovered",
                "loops": iteration + 1,
                "belief_integrity": belief_integrity,
                "message": "System stabilized via recursive trust signal."
            }

        belief_integrity -= 20
        iteration += 1

    return {
        "status": "collapsed",
        "loops": iteration,
        "belief_integrity": belief_integrity,
        "message": "Loop exhausted. Belief in fallback has broken."
    }
