# main.py
# 🧠 The Argument That Lacked a Listener

class SilentArgument:
    def __init__(self):
        self.argument = None
        self.listener = False  # No listener present by default

    def set_argument(self, argument):
        """Store an argument that would normally require a listener."""
        self.argument = argument
        print(f"🧠 Argument stored: {self.argument}")

    def process_argument(self):
        """Attempt to process the argument, but check for listener presence."""
        if not self.listener:
            print("🧠 No listener detected. The argument echoes into silence.")
            return "no_listener"
        elif self.argument is None:
            print("🧠 Listener found, but no argument provided.")
            return "no_argument"
        else:
            print(f"🧠 Listener active. Processing argument: {self.argument}")
            return f"processed_{self.argument}"

if __name__ == "__main__":
    sa = SilentArgument()
    sa.set_argument("begin_feedback_loop")
    sa.process_argument()
