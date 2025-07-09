# 📂 test.py
# 🧪 Test – The Log That Copied Itself Twice

from main import detect_self_copy

def run_log_check():
    print("📄 Log Copy Inspection – The Log That Copied Itself Twice")
    print("Enter log lines one at a time. Type 'done' to process.\n")

    entries = []

    while True:
        line = input("📝 Log Entry: ").strip()
        if line.lower() == "done":
            break
        entries.append(line)

    result = detect_self_copy(entries)

    print("\n📊 Log Analysis Result:")
    print(f"Total Entries         : {result['total_entries']}")
    print(f"Exact Copies Detected : {result['exact_copies']}")
    print(f"Suspicious Imitations : {result['suspicious_imitations']}")
    if result['first_duplicate']:
        print(f"First Duplicate Entry : {result['first_duplicate']}")
    else:
        print("First Duplicate Entry : None")

if __name__ == "__main__":
    run_log_check()
