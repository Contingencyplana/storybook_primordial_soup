# C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\
# a0_0_the_cell_that_dreamed_it_had_begun\a0_0_the_test_that_called_itself\
# a3_2_the_trace_that_returned_too_late\test.py

from main import delayed_trace

def test_trace_timing():
    print("🔍 Running test: trace delay vs. timeout...\n")

    result = delayed_trace(context_timeout=1.0, delay=2.0)

    print("📡 Trace Delay:", result["delay"])
    print("📜", result["message"])
    
    assert result["status"] == "expired", "Expected trace to be marked as expired."
    assert result["delay"] > 1.0, "Delay should exceed timeout."

if __name__ == "__main__":
    test_trace_timing()
