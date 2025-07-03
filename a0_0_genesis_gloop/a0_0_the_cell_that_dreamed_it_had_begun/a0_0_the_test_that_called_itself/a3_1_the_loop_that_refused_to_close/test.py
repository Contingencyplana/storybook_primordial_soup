# C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\
# a0_0_the_cell_that_dreamed_it_had_begun\a0_0_the_test_that_called_itself\
# a3_1_the_loop_that_refused_to_close\test.py

from main import unresolved_loop_check

def test_unclosed_loop():
    print("🔍 Running test: unresolved loop behavior...\n")

    result = unresolved_loop_check(threshold=4)

    for line in result["iterations"]:
        print("🔁", line)

    print(f"\n📜 Status: {result['status']}")
    print(f"📜 Message: {result['message']}")
    assert result["status"] == "loop_incomplete", "Loop did not report incomplete status."
    assert len(result["iterations"]) == 4, "Unexpected loop iteration count."

if __name__ == "__main__":
    test_unclosed_loop()
