# C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\
# a0_0_the_cell_that_dreamed_it_had_begun\a0_0_the_test_that_called_itself\
# a3_0_the_assertion_that_unmade_itself\test.py

from main import evaluate_assertion

def test_self_negating_assertion():
    print("🔍 Running test: self-negating assertion...\n")

    test_inputs = [
        "I exist",
        "Truth is absolute",
        "This statement is true",
        "",
        None
    ]

    for signal in test_inputs:
        result = evaluate_assertion(signal)
        print(f"🧪 Input: {repr(signal)}")
        print(f"📜 Result: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_self_negating_assertion()
