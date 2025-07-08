# 📄 test.py
# 🧪 Memory Conflict Test – a11_0_the_log_that_was_written_in_absentia → a0_1_the_record_that_disagreed_with_itself
# Simulates contradictory logs of a single event. Can the system resolve the split?

from main import evaluate_record

print("📜 Dual Record Test – The Record That Disagreed With Itself\n")

while True:
    print("Enter two memory records for the same event.")
    print("Type 'exit' to quit.\n")

    source_a = input("🧠 Source A memory: ").strip()
    if source_a.lower() == "exit":
        print("👋 Exiting memory reconciliation.")
        break

    source_b = input("🧠 Source B memory: ").strip()
    if source_b.lower() == "exit":
        print("👋 Exiting memory reconciliation.")
        break

    result = evaluate_record({
        "source_a": source_a,
        "source_b": source_b
    })

    print("\n🧠 Record Analysis:")
    print(f"Status  : {result['status']}")
    print(f"Verdict : {result['verdict']}\n")
