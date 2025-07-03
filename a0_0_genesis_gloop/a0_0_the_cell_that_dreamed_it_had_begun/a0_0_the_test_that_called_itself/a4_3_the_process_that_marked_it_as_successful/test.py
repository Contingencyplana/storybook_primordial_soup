# C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\
# a0_0_the_cell_that_dreamed_it_had_begun\a0_0_the_test_that_called_itself\
# a4_3_the_process_that_marked_it_as_successful\test.py

from main import process_with_false_success

def test_false_positive():
    print("🔍 Running test: false success masking internal error...\n")

    result = process_with_false_success(raise_internal_error=True)
    print("📋", result["message"])
    print("🚨 Internal Error Detected:", result["internal_error"])

    assert result["status"] == "success", "Publicly marked as success."
    assert result["internal_error"] == True, "Error occurred but was hidden."

    print("\n✅ Running clean path: true success...")
    clean = process_with_false_success(raise_internal_error=False)
    print("📋", clean["message"])
    print("🚨 Internal Error Detected:", clean["internal_error"])

    assert clean["status"] == "success"
    assert clean["internal_error"] == False

if __name__ == "__main__":
    test_false_positive()

