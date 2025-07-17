# main.py
# 🧠 The Command That Recalled Itself

class RecursiveCommand:
    def __init__(self):
        self.memory = []

    def issue_command(self, command):
        """Store a command in memory."""
        self.memory.append(command)
        print(f"🧠 Command stored: {command}")

    def recall_last_command(self):
        """Recall the last command issued, simulating recursive memory."""
        if not self.memory:
            print("🧠 No command found in memory.")
            return None
        last_command = self.memory[-1]
        print(f"🧠 Recalling last command: {last_command}")
        return last_command

if __name__ == "__main__":
    rc = RecursiveCommand()
    rc.issue_command("initiate_awakening")
    rc.recall_last_command()
