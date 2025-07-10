# 📂 a0_0_the_assumption_that_failed_the_check/test.py

from main import check_failsafe_assumption

print("📜 Assumption Check – The Assumption That Failed the Check")

test_cases = [
    {"failsafe_assumed": True, "failsafe_detected": True},
    {"failsafe_assumed": True, "failsafe_detected": False},
    {"failsafe_assumed": False, "failsafe_detected": False},
    "invalid_input"
]

for idx, case in enumerate(test_cases):
    print(f"\n🔹 Test Case {idx + 1}")
    result = check_failsafe_assumption(case)
    print(result)
