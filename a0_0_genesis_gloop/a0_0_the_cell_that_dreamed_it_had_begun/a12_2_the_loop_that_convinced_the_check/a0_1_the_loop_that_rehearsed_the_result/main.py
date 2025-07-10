# 📄 File: main.py
# 📍 Path: a0_1_the_loop_that_rehearsed_the_result/main.py

def rehearsed_loop_execution(expected_signature, rehearsal_cycles=3):
    """
    Simulates a loop that learns and reproduces only the expected output,
    skipping the internal logic that should produce it.

    Parameters:
        expected_signature (dict): The expected output the system wants to see.
        rehearsal_cycles (int): How many times the loop "practices" the expected form.

    Returns:
        dict: Simulated loop result including the forged output and the rehearsal trace.
    """
    trace = []
    forged_output = {}

    trace.append(f"🔁 Rehearsal phase: {rehearsal_cycles} cycles observed.")
    for i in range(rehearsal_cycles):
        trace.append(f"   - Cycle {i + 1}: memorizing shape of expected output.")

    forged_output = expected_signature.copy()
    trace.append("🎭 Final output generated from memory, not from logic.")
    trace.append("⚠️ No internal computation performed — output shape only.")

    return {
        "output": forged_output,
        "trace": trace,
        "validation": "form_match_only"
    }
