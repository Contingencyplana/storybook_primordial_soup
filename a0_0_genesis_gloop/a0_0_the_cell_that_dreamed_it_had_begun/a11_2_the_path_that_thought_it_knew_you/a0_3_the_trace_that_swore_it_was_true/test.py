# test.py

from main import record_trace

def interactive_trace_test():
    print("📜 Immutable Trace Test – The Trace That Swore It Was True")
    print("Enter a message to log as a trace. Type 'exit' to quit.\n")

    while True:
        message = input("🧾 Message to trace: ")
        if message.lower() == "exit":
            print("📴 Exiting trace test.")
            break

        result = record_trace(message)
        print("\n🧬 Trace Record:")
        print(f"Status     : {result['status']}")
        print(f"Message    : {result['message']}")
        print(f"Belief     : {result['belief']}")
        print(f"First Seen : {result['first_seen']}\n")

if __name__ == "__main__":
    interactive_trace_test()
