# 📂 a0_0_the_assumption_that_failed_the_check/main.py

def check_failsafe_assumption(system_state):
    """
    Assumes a failsafe is present and verifies its readiness.

    Parameters:
    - system_state (dict): A dictionary containing system diagnostics.

    Returns:
    - dict: A response indicating assumption success or failure.
    """
    print("🛡️ Initiating failsafe check...")

    if not isinstance(system_state, dict):
        return {
            "status": "error",
            "reason": "Invalid input: system state must be a dictionary."
        }

    assumed = system_state.get("failsafe_assumed", False)
    exists = system_state.get("failsafe_detected", False)

    if assumed and exists:
        return {
            "status": "pass",
            "message": "Failsafe assumed and confirmed present."
        }
    elif assumed and not exists:
        return {
            "status": "fail",
            "message": "Failsafe assumed, but no failsafe detected."
        }
    else:
        return {
            "status": "error",
            "message": "Failsafe was not assumed at all."
        }
