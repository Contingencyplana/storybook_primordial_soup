# 📂 a0_1_the_proof_that_erased_the_record/main.py

def prove_failsafe_and_check_logs(system_state):
    """
    Attempts to prove the failsafe exists.
    In doing so, it triggers a side effect that may erase logs unintentionally.

    Parameters:
    - system_state (dict): Contains 'failsafe_proof', 'logs', and 'logging_enabled'

    Returns:
    - dict: Outcome of the proof and its side effect
    """
    print("📄 Attempting to prove failsafe...")

    if not isinstance(system_state, dict):
        return {
            "status": "error",
            "reason": "System state must be a dictionary."
        }

    proof = system_state.get("failsafe_proof", False)
    logs = system_state.get("logs", [])
    logging_enabled = system_state.get("logging_enabled", True)

    if proof:
        # Simulate paradox: proof triggers side effect
        if logging_enabled:
            system_state["logs"] = []  # Erase logs as a side effect
            return {
                "status": "contradiction",
                "message": "Failsafe was proven, but logs were erased in the process."
            }
        else:
            return {
                "status": "pass",
                "message": "Failsafe proof accepted with no erasure."
            }
    else:
        return {
            "status": "fail",
            "message": "Failsafe proof missing or incomplete."
        }
