# main.py
# 🧠 The Flag That Waited in Memory

class DormantFlag:
    def __init__(self):
        self.flag = None  # The flag starts unset

    def set_flag(self, value):
        """Simulates a system flag being set long ago."""
        self.flag = value
        print(f"🧠 Dormant flag set to: {self.flag}")

    def check_flag(self):
        """Checks if the flag has waited long enough to awaken."""
        if self.flag is None:
            print("🧠 No flag found. Dormant state persists.")
            return "dormant"
        elif self.flag == "awaken":
            print("🧠 Dormant flag resolved. The system begins to respond.")
            return "resolved"
        else:
            print(f"🧠 Flag is set but unrecognized: {self.flag}")
            return "unknown_flag"

if __name__ == "__main__":
    df = DormantFlag()
    # Simulate a flag that was set long ago but only now processed
    df.set_flag("awaken")
    df.check_flag()
