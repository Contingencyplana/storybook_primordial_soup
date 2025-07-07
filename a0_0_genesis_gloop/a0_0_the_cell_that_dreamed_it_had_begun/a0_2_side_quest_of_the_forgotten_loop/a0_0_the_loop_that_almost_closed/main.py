# 📄 main.py
# Path: a0_2_side_quest_of_the_forgotten_loop/a0_0_the_loop_that_almost_closed/main.py

def simulate_forgotten_loop(task_sequence):
    """
    Evaluates whether a recursive loop almost closed — but didn't.

    Parameters:
        task_sequence (list of str): A list of task checkpoints.

    Returns:
        dict: Loop status, closure suspicion, and tail signature.
    """
    if not task_sequence:
        return {
            "status": "empty loop",
            "closed": False,
            "suspicious": False,
            "tail": None
        }

    loop_closed = task_sequence[0] == task_sequence[-1]
    suspicious = not loop_closed and len(set(task_sequence)) < len(task_sequence)

    return {
        "status": "loop resolved" if loop_closed else "loop unresolved",
        "closed": loop_closed,
        "suspicious": suspicious,
        "tail": task_sequence[-1]
    }
