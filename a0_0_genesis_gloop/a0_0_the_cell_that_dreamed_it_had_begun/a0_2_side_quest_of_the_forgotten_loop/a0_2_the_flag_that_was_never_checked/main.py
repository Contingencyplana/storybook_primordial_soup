# 📄 main.py
# Path: a0_2_side_quest_of_the_forgotten_loop/a0_2_the_flag_that_was_never_checked/main.py

def check_unqueried_flag(state):
    """
    Evaluates whether a critical flag was raised but never verified.

    Parameters:
        state (dict): A dictionary containing keys like 'flag_set', 'checked', 'flag_name'.

    Returns:
        dict: Evaluation result, including dormant risk if unqueried.
    """
    flag_set = state.get("flag_set", False)
    checked = state.get("checked", False)
    flag_name = state.get("flag_name", "unnamed_flag")

    if flag_set and not checked:
        return {
            "flag": flag_name,
            "status": "⚠️ Unchecked",
            "risk": "Dormant recursion hazard",
            "action_required": True
        }
    elif flag_set and checked:
        return {
            "flag": flag_name,
            "status": "✅ Verified",
            "risk": "None",
            "action_required": False
        }
    else:
        return {
            "flag": flag_name,
            "status": "🔘 Not Set",
            "risk": "None",
            "action_required": False
        }
