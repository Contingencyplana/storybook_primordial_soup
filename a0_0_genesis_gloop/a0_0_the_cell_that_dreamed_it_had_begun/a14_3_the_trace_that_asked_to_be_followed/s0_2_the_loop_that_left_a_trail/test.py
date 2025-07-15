# Save to: a14_3_the_trace_that_asked_to_be_followed/s0_2_the_loop_that_left_a_trail/test.py

"""
🧪 Test – The Loop That Left a Trail

This test checks that the trail generation function produces the correct sequence of trail markers.
"""

from main import generate_trail

def test_generate_trail():
    expected_trail = [
        "🧭 Trail Marker 1: loop_start",
        "🧭 Trail Marker 2: recursion_call",
        "🧭 Trail Marker 3: fallback_detected",
        "🧭 Trail Marker 4: anomaly_logged",
        "🧭 Trail Marker 5: loop_continues"
    ]
    output = generate_trail()
    assert output == expected_trail, "Test failed: Trail output does not match expected markers."
    print("✅ Test passed: Trail output matches expected markers.")

if __name__ == "__main__":
    test_generate_trail()
