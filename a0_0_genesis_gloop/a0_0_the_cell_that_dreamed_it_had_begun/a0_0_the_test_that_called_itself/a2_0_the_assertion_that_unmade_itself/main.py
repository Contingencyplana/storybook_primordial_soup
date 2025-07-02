# main.py — a2_0_the_assertion_that_unmade_itself
# This test tries to affirm a basic truth, only to unravel it by recursive contradiction.

def recursive_assertion(counter=0, max_depth=10):
    """
    Attempts to assert a base truth — but the deeper it recurses, 
    the more it contradicts its own assumption.
    """
    if counter >= max_depth:
        return True  # Base case: forced truth at bottom layer

    # Initial assumption
    assertion = True

    # But the recursion undermines it
    contradiction = not recursive_assertion(counter + 1, max_depth)

    # Self-negation logic: contradiction overpowers the initial truth
    return assertion and contradiction


if __name__ == "__main__":
    result = recursive_assertion()
    print(f"Assertion outcome (negated by recursion): {result}")
