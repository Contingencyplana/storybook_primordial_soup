# C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\
# a0_0_the_cell_that_dreamed_it_had_begun\a0_0_the_test_that_called_itself\
# a4_2_the_log_that_forgot_the_error\test.py

from main import process_and_log_error

def test_unlogged_error():
    print("🔍 Running test: error occurs but is not logged...\n")

    result = process_and_log_error(simulate_error=True)
    print("📋", result["message"])
    print("🗒️ Log Contents:", result["log"])
    
    assert result["status"] == "error_unlogged", "Expected unlogged error status."
    assert result["log"] == [], "Log should be empty despite error."

    print("\n✅ Running control: normal operation with logging...")
    clean_result = process_and_log_error(simulate_error=False)
    print("📋", clean_result["message"])
    print("🗒️ Log Contents:", clean_result["log"])
    
    assert clean_result["status"] == "success", "Expected success status."
    assert len(clean_result["log"]) == 1, "Log should contain one success entry."

if __name__ == "__main__":
    test_unlogged_error()
