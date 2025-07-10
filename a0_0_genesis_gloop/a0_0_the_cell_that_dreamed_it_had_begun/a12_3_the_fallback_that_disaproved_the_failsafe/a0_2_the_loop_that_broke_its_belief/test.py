# 📂 a0_2_the_loop_that_broke_its_belief/test.py

from main import recursive_failsafe_loop

print("📜 Loop Test – The Loop That Broke Its Belief")

test_cases = [
    {"recovery_hint": "trust_signal"},
    {"recovery_hint": None},
    {"recovery_hint": "noise"},
    "invalid_format"
]

for idx, case in enumerate(test_cases):
    print(f"\n🔹 Test Case {idx + 1}")
    result = recursive_failsafe_loop(case)
    print(result)
