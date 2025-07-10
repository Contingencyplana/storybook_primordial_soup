# 📄 File: test.py
# 📍 Path: a0_1_the_loop_that_rehearsed_the_result/test.py

from main import rehearsed_loop_execution

print("🧪 Premeditated Output Test – The Loop That Rehearsed the Result")

expected = {
    "status": "ok",
    "result": [42, 42, 42]
}

result = rehearsed_loop_execution(expected)

print("\n📤 Output:")
print(result["output"])

print("\n🧠 Trace:")
for line in result["trace"]:
    print(line)

print("\n✅ Validation Mode:", result["validation"])
