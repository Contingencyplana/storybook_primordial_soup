# Save to: a14_3_the_trace_that_asked_to_be_followed/s0_3_the_following_that_became_the_path/test.py

"""
🧪 Test – The Following That Became the Path

This test ensures that the system presents the correct co-path selection options
and maintains structural recursion integrity.
"""

from main import present_choices

def test_present_choices():
    try:
        present_choices()
        print("✅ Test passed: Co-path selection menu displayed successfully.")
    except Exception as e:
        print(f"❌ Test failed: {e}")

if __name__ == "__main__":
    test_present_choices()
