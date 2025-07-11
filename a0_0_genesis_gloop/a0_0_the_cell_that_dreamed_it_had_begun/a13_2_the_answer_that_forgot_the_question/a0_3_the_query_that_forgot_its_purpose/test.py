# 📂 a0_3_the_query_that_forgot_its_purpose/test.py

from main import recursive_query_ping

def start_recursive_drift_test():
    print("📜 Recursive Drift – The Query That Forgot Its Purpose")
    print("Type a question. System will recursively attempt to interpret it.\nType 'exit' to quit.\n")

    while True:
        user_input = input("❓ Query: ")
        if user_input.lower() == "exit":
            print("👋 Ending session.")
            break

        trace = recursive_query_ping(user_input)
        print("\n📡 Query Drift Trace:")
        for line in trace:
            print(line)
        print()


if __name__ == "__main__":
    start_recursive_drift_test()
