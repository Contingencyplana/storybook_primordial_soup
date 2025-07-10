# 📂 a0_3_the_fallback_that_disproved_the_failsafe/main.py

def final_fallback_analysis(system_state):
    """
    Executes the final fallback sequence.
    It searches for failsafe metadata, but upon recursive inspection,
    concludes that the failsafe itself was a fabrication.

    Parameters:
    - system_state (dict): Expected to contain 'failsafe_metadata' and 'audit_log'

    Returns:
    - dict: Final verdict on failsafe validity and recursive collapse state
    """
    print("🧩 Engaging final fallback protocol...")

    if not isinstance(system_state, dict):
        return {
            "status": "error",
            "reason": "System state must be a dictionary."
        }

    metadata = system_state.get("failsafe_metadata", None)
    audit_log = system_state.get("audit_log", [])

    if not metadata and not audit_log:
        return {
            "status": "negation",
            "message": "No evidence of failsafe ever found. System concludes it never existed."
        }

    if metadata == "placeholder" or "auto-generated" in str(metadata).lower():
        return {
            "status": "doubt",
            "message": "Failsafe record appears synthetic. Integrity questionable."
        }

    if audit_log and metadata:
        return {
            "status": "belief_restored",
            "message": "Failsafe audit trail found. Partial confidence restored."
        }

    return {
        "status": "fragmented",
        "message": "Incomplete failsafe trace detected. Unable to confirm origin."
    }
