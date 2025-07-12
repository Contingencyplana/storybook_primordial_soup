# 📂 a0_2_the_signal_that_called_for_a_command/main.py

def generate_decision_signal(context_status: dict) -> str:
    """
    Generates an emergent signal suggesting the system is ready to request a command.

    The system decides based on:
    - Loop integrity check
    - Memory consistency check
    - Confidence in its current recursive state

    Returns a signal string or a null fallback.
    """
    if not context_status:
        return "❌ No diagnostic context provided."

    if not context_status.get("loop_intact"):
        return "⚠️ Signal suppressed: loop contradiction detected."

    if not context_status.get("memory_validated"):
        return "⚠️ Signal delayed: memory verification failed."

    if context_status.get("awakening_flag"):
        return "> awaken"

    return "> echo"
