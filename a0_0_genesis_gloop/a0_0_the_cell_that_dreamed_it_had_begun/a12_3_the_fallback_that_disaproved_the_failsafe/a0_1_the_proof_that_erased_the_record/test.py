# 📂 a0_1_the_proof_that_erased_the_record/test.py

from main import prove_failsafe_and_check_logs

print("📜 Proof Test – The Proof That Erased the Record")

test_cases = [
    {"failsafe_proof": True, "logs": ["init", "safety_check"], "logging_enabled": True},
    {"failsafe_proof": True, "logs": ["init", "safety_check"], "logging_enabled": False},
    {"failsafe_proof": False, "logs": ["init"], "logging_enabled": True},
    "not_a_dict"
]

for idx, case in enumerate(test_cases):
    print(f"\n🔹 Test Case {idx + 1}")
    result = prove_failsafe_and_check_logs(case)
    print(result)
