# 📄 File: main.py
# 📍 Path: a0_2_the_checkpoint_that_wanted_to_believe/main.py

def validate_with_bias(signal, memory_log):
    """
    Simulates a checkpoint that trusts outputs based on resemblance to past success
    rather than current validation logic.

    Parameters:
        signal (dict): The loop output being evaluated.
        memory_log (list): A list of previously approved output shapes.

    Returns:
        dict: Result with approval status and checkpoint reasoning trace.
    """
    trace = []

    if not isinstance(signal, dict):
        trace.append("❌ Signal format invalid — not a dictionary.")
        return {"approved": False, "trace": trace}

    trace.append("🔍 Comparing signal to memory log of trusted shapes...")

    for idx, past in enumerate(memory_log):
        if set(signal.keys()) == set(past.keys()):
            trace.append(f"✅ Signal resembles trusted output #{idx + 1} — approval granted.")
            return {"approved": True, "trace": trace}

    trace.append("❌ No match found in trusted shapes — approval denied.")
    return {"approved": False, "trace": trace}
