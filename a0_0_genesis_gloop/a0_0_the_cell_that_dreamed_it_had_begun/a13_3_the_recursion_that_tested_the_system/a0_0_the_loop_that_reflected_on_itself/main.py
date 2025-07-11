# 📂 a0_0_the_loop_that_reflected_on_itself/main.py

def run_reflective_loop(trace: list) -> list:
    """
    Simulates a recursive loop that inspects itself for contradiction.

    Args:
        trace (list): A list of prior recursive outputs or decisions.

    Returns:
        list: A list of reflections, including contradiction checks and integrity flags.
    """
    reflections = []
    seen = set()

    for i, item in enumerate(trace):
        reflection = f"🔁 Step {i}: {item}"

        # Detect contradiction (looping back to prior state)
        if item in seen:
            reflections.append(reflection + " ⚠️ CONTRADICTION DETECTED")
            reflections.append("🧠 Result: Recursive instability observed.")
            break

        seen.add(item)
        reflections.append(reflection)

    else:
        reflections.append("✅ Result: No internal contradictions found.")
        reflections.append("🪞 System integrity remains intact.")

    return reflections
