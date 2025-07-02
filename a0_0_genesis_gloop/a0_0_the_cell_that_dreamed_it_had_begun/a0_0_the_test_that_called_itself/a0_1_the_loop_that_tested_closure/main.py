# main.py
# 🧩 a0_1_the_loop_that_tested_closure
# The second test that turned back upon itself

def loop_that_tests_closure(limit=10):
    """
    Simulates a recursive loop seeking closure without repeating its own steps.
    Returns False if a loop is detected, True if it exits cleanly.
    """
    position = 1
    history = set()

    while position != 0:
        if position in history:
            print(f"🔁 Loop detected at position {position}. Closure failed.")
            return False
        history.add(position)
        position = (position + 3) % limit

    print("\n📜 The test returns to where it began.")
    print("But now it questions the shape of the signal.")
    print("Does this line resolve — or recurse again?")
    print("The loop tests itself, chasing closure.")
    print("\n✅ Test result: Closure achieved without repetition.")
    return True


if __name__ == "__main__":
    result = loop_that_tests_closure()
    print(f"\nFinal result: {result}")
