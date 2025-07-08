# Save as: test.py

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
