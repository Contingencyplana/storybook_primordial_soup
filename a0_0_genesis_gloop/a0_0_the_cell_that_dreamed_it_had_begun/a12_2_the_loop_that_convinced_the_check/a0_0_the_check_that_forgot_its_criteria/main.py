# 📄 File: main.py
# 📍 Path: a0_0_the_check_that_forgot_its_criteria/main.py

def run_loop_with_check(task_data):
    """
    Simulates a recursive loop that forgets what it's meant to check.
    The system approves the result if the loop structure appears intact,
    regardless of the task's original criteria.

    Parameters:
        task_data (dict): Contains task metadata and simulated loop output.

    Returns:
        dict: Result containing approval status and reasoning trace.
    """
    result_trace = []

    # Simulated degraded check memory
    remembered_conditions = task_data.get("check_criteria", None)
    actual_output = task_data.get("output", None)

    if remembered_conditions is None:
        result_trace.append("⚠️ Criteria missing — defaulting to structural heuristics.")

        if isinstance(actual_output, dict) and "status" in actual_output:
            result_trace.append("✅ Loop structure appears intact.")
            result_trace.append("✅ 'status' key detected — assuming successful outcome.")
            passed = True
        else:
            result_trace.append("❌ Output malformed. Structural check failed.")
            passed = False
    else:
        result_trace.append("🧠 Check criteria remembered — unexpected path taken.")
        passed = (actual_output == remembered_conditions)
        result_trace.append("✅" if passed else "❌" + " Output matched original criteria.")

    return {
        "approved": passed,
        "trace": result_trace
    }
