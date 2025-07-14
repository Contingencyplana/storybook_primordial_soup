# main.py
# 🧠 The Flag That Waited in Memory

class DormantFlag:
    def __init__(self):
        self.flag = None  # Start with no flag set

    def set_flag(self, value):
        """Set a flag value, simulating dormant system memory."""
        self.flag = value
        print(f"🧠 Dormant flag set to: {self.flag}")

    def process_flag(self):
        """Process the dormant flag when the system is ready."""
        if self.flag is None:
            print("🧠 No flag present. The system remains dormant.")
            return "dormant"
        elif self.flag == "awaken":
            print("🧠 Dormant flag resolved. The system transitions to active response.")
            return "resolved"
        else:
            print(f"🧠 Unrecognized flag state: {self.flag}")
            return "unknown"

if __name__ == "__main__":
    df = DormantFlag()
    df.set_flag("awaken")
    df.process_flag()
