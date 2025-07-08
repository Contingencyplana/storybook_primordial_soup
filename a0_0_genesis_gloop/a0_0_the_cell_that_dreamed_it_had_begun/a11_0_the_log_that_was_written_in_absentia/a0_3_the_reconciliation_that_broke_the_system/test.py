# Save as: a0_3_the_reconciliation_that_broke_the_system/test.py

from main import reconcile_logs

print("📜 System Reconciliation Test – The Reconciliation That Broke the System\n")

while True:
    print("Enter multiple log entries. Type 'done' when finished, or 'exit' to quit.\n")
    entries = []

    while True:
        entry = input("🧠 Log entry: ").strip()
        if entry.lower() == "exit":
            print("👋 Exiting reconciliation test.")
            exit()
        elif entry.lower() == "done":
            break
        else:
            entries.append(entry)

    result = reconcile_logs(entries)

    print("\n🧠 Reconciliation Result:")
    print(f"Status  : {result['status']}")
    print(f"Outcome : {result['outcome']}\n")
