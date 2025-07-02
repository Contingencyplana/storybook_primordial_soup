# s1_3_the_function_that_called_itself_wrong/main.py

def recursive_caller(n, max_depth=10):
    """
    Simulates a recursive function with a maximum depth safeguard.
    Returns a message if recursion is successful or fails.
    """
    if n > max_depth:
        return f"Recursion failed: exceeded max depth ({max_depth})."
    if n == max_depth:
        return "Recursion ended successfully at max depth."
    return recursive_caller(n + 1, max_depth)


if __name__ == "__main__":
    # Manual test run
    print(recursive_caller(0))

