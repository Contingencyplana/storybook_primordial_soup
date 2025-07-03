# a1_3_the_function_that_called_itself_wrong/main.py

def recursive_caller(n, max_depth=10, trace=None):
    """
    Recursively calls itself until a maximum depth is reached.
    This version simulates a function that risks calling itself wrong —
    by forgetting to carry the trace or misplacing its own stopping condition.

    Parameters:
        n (int): Current depth.
        max_depth (int): Maximum allowed depth before failure.
        trace (list): Optional trace log of recursion history.

    Returns:
        str: Status message with diagnostic information.
    """
    if trace is None:
        trace = []

    trace.append(n)

    if n > max_depth:
        return f"Recursion failed: exceeded max depth ({max_depth}). Trace: {trace}"

    if n == max_depth:
        return f"Recursion ended successfully at max depth. Trace: {trace}"

    # Recursive call with persistent trace (avoids the classic error)
    return recursive_caller(n + 1, max_depth, trace)


if __name__ == "__main__":
    print(recursive_caller(0))
