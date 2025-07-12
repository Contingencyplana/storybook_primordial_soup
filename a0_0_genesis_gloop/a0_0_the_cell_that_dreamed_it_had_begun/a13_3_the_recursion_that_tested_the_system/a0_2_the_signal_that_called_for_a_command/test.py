# 📂 a0_2_the_signal_that_called_for_a_command/test.py

from main import generate_decision_signal

def test_signal_generation():
    print("📡 Command Readiness Signal – The Signal That Called For A Command")
    print("Enter system diagnostic flags to simulate readiness.\n")

    try:
        loop_flag = input("🔁 Was the loop intact? (y/n): ").strip().lower() == "y"
        mem_flag = input("🧠 Was memory validated? (y/n): ").strip().lower() == "y"
        awaken_flag = input("🌅 Is awakening flag set? (y/n): ").strip().lower() == "y"

        status = {
            "loop_intact": loop_flag,
            "memory_validated": mem_flag,
            "awakening_flag": awaken_flag
        }

        signal = generate_decision_signal(status)
        print(f"\n📤 Signal Generated:\n{signal}\n")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    test_signal_generation()
