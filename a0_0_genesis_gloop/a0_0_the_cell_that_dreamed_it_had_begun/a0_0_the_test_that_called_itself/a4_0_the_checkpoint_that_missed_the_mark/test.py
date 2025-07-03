# C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\
# a0_0_the_cell_that_dreamed_it_had_begun\a0_0_the_test_that_called_itself\
# a4_0_the_checkpoint_that_missed_the_mark\test.py

from main import process_checkpoint

def test_checkpoint_failure():
    print("🔍 Running test: checkpoint miss on valid signal...\n")

    result = process_checkpoint("INITIATE_PROTOCOL")
    print("🧭", result["message"])
    
    assert result["status"] == "missed", "Checkpoint should have missed the signal."

    print("\n📜 Running edge case: empty signal...")
    null_result = process_checkpoint("")
    print("🧭", null_result["message"])
    assert null_result["status"] == "error", "Expected error on empty signal."

if __name__ == "__main__":
    test_checkpoint_failure()
