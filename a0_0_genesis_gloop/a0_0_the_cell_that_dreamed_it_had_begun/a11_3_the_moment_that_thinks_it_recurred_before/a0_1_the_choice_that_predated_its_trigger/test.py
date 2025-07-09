# 📂 test.py
# 🧪 Test Interface – The First Echo That Felt Like the Second

from main import receive_signal

def run_echo_test():
    print("📡 Echo Test – The First Echo That Felt Like the Second")
    print("Enter signals one at a time. Type 'done' to end.\n")

    signal_log = []

    while True:
        new_signal = input("🔁 Signal: ").strip()
        if new_signal.lower() == "done":
            break

        result = receive_signal(signal_log, new_signal)
        signal_log.append(new_signal)

        print("\n🧠 Echo Perception Result:")
        print(f"Signal        : {result['signal']}")
        print(f"True Repeat   : {result['true_repeat']}")
        print(f"Felt Like Echo: {result['echo']}")
        if result['match_pattern']:
            print(f"Matched Pattern: {result['match_pattern']}")
        print()

if __name__ == "__main__":
    run_echo_test()
