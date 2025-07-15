# Save to: a14_3_the_trace_that_asked_to_be_followed/s0_1_the_pattern_that_waited_to_be_seen/test.py

"""
🧪 Test – The Pattern That Waited to Be Seen

This test verifies that the output contains the expected recursive pattern
with an intentional anomaly in the final line.
"""

from main import generate_output

def test_generate_output():
    output = generate_output()
    assert len(output) == 4, "Test failed: Output length incorrect."
    assert output[3].endswith("trace_omit"), "Test failed: Anomaly not present in final line."
    print("✅ Test passed: Pattern anomaly detected as expected.")

if __name__ == "__main__":
    test_generate_output()
