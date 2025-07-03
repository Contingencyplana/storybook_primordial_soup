# C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\
# a0_0_the_cell_that_dreamed_it_had_begun\a0_0_the_test_that_called_itself\
# a3_3_the_fallback_that_caused_the_failure\test.py

from main import perform_with_fallback

def test_paradox_fallback():
    print("🔍 Running test: fallback causes failure...\n")

    result = perform_with_fallback(primary_success=False, fallback_enabled=True)

    print("📜", result["message"])
    assert result["status"] == "failure", "Fallback should have caused failure."

if __name__ == "__main__":
    test_paradox_fallback()
