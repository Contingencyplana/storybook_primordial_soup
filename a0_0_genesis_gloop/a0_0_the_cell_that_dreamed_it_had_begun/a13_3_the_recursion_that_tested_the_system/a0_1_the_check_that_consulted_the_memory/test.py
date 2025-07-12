# 📂 a0_1_the_check_that_consulted_the_memory/test.py

from main import store_memory, check_memory_consistency

def run_memory_checker():
    print("📜 Memory Check – The Check That Consulted The Memory")
    print("Store past system states. Then ask a query to validate.\n")

    while True:
        mode = input("🧠 Type 'store', 'query', or 'exit': ").strip().lower()

        if mode == "exit":
            print("👋 Ending session.")
            break
        elif mode == "store":
            entry = input("📥 Enter memory: ")
            store_memory(entry)
            print("✅ Memory stored.\n")
        elif mode == "query":
            query = input("🔎 Enter query to check: ")
            result = check_memory_consistency(query)
            print(f"\n🧪 Consistency Check:\n{result}\n")
        else:
            print("❓ Invalid input. Try 'store', 'query', or 'exit'.\n")

if __name__ == "__main__":
    run_memory_checker()
