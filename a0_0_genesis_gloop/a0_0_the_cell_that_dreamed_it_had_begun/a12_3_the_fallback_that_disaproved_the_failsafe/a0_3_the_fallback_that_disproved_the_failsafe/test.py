# 📂 a0_3_the_fallback_that_disproved_the_failsafe/test.py

from main import final_fallback_analysis

print("📜 Final Fallback – The Fallback That Disproved the Failsafe")

test_cases = [
    {"failsafe_metadata": None, "audit_log": []},
    {"failsafe_metadata": "placeholder", "audit_log": ["entry1"]},
    {"failsafe_metadata": "Confirmed", "audit_log": ["created", "validated"]},
    {"failsafe_metadata": None, "audit_log": ["incomplete fragment"]},
    "invalid_input"
]

for idx, case in enumerate(test_cases):
    print(f"\n🔹 Test Case {idx + 1}")
    result = final_fallback_analysis(case)
    print(result)
