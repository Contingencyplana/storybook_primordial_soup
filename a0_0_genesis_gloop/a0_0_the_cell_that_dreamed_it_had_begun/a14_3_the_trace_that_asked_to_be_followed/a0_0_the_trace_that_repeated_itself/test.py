# Save to: a14_3_the_trace_that_asked_to_be_followed/a0_0_the_trace_that_repeated_itself/test.py

"""
🧪 Test – The Trace That Repeated Itself

This test checks that the trace emission function correctly outputs the expected recursive pattern.
"""

from main import emit_trace

def test_emit_trace():
    expected_trace = [
        "↺ Loop detected: system_call -> fallback -> trace_emit",
        "↺ Loop detected: system_call -> fallback -> trace_emit",
        "↺ Loop detected: system_call -> fallback -> trace_emit"
    ]
    output = emit_trace()
    assert output == expected_trace, "Test failed: Trace output does not match expected pattern."
    print("✅ Test passed: Trace output matches expected pattern.")

if __name__ == "__main__":
    test_emit_trace()
