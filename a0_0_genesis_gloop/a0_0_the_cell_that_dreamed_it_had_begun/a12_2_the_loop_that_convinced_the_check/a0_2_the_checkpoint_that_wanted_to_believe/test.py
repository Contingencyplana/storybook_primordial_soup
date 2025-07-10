# 📄 File: test.py
# 📍 Path: a0_2_the_checkpoint_that_wanted_to_believe/test.py

from main import validate_with_bias

print("🧪 Complicit Confirmation Test – The Checkpoint That Wanted to Believe")

# Memory log of prior approved outputs (shapes only)
memory_log = [
    {"status": "ok", "result": [1, 2, 3]},
    {"status": "done", "payload": {"x": 10}}
]

# Simulated signal that looks like one of the trusted shapes
test_signal = {"status": "ok", "result": [99, 88, 77]}

result = validate_with_bias(test_signal, memory_log)

print("\n📤 Approval:", result["approved"])
print("\n🧠 Trace:")
for line in result["trace"]:
    print(line)
