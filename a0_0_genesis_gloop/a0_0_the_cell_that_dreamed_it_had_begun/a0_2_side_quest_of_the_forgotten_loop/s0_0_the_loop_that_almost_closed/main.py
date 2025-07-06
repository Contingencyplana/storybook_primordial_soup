# main.py

def incomplete_loop_detector(sequence):
    """
    Simulates a loop that nearly completes but fails on the final condition.
    
    A valid loop should return True only if it iterates cleanly through all elements
    and ends on a known terminal symbol ('END'). If it breaks early or forgets the
    closure, it returns False.
    """
    for i, item in enumerate(sequence):
        if item == "BREAK":
            print(f"Loop terminated early at index {i}")
            return False
        if i == len(sequence) - 1 and item != "END":
            print(f"Loop ended without reaching END at index {i}")
            return False
    return True
