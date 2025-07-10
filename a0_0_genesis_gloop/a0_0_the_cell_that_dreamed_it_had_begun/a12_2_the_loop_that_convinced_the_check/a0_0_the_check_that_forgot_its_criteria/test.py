# 📄 File: test.py
# 📍 Path: a0_0_the_check_that_forgot_its_criteria/test.py

from main import run_loop_with_check

print("🧪 Validation Drift Test – The Check That Forgot Its Criteria")

# Simulated test case where criteria are forgotten
simulated_input = {
    "check_criteria": None,
    "output": {"status": "ok", "data": [1, 2, 3]}
}

result = run_loop_with_check(simulated_input)

print("\n📤 Result:")
print("Approved:", result["approved"])
print("\n🧠 Trace:")
for line in result["trace"]:
    print(line)
