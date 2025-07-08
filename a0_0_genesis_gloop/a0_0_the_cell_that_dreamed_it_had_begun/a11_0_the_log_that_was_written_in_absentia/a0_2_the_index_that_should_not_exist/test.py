# Save as: a11_0_the_log_that_was_written_in_absentia/a0_2_the_index_that_should_not_exist/test.py

from main import evaluate_index_entry

print("📜 Index Diagnostic Test – The Index That Should Not Exist\n")

while True:
    entry = input("Enter index entry (or press Enter for none, or type 'exit'): ").strip()
    if entry.lower() in {"exit", "quit"}:
        print("👋 Exiting index diagnostics.")
        break

    result = evaluate_index_entry(entry)
    print("\n🧠 Evaluation:")
    print(f"Status : {result['status']}")
    print(f"Message: {result['message']}\n")
