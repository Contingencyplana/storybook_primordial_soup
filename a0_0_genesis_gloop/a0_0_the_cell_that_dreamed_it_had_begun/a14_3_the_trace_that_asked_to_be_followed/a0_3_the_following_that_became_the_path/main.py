# Save to: a14_3_the_trace_that_asked_to_be_followed/a0_3_the_following_that_became_the_path/main.py

"""
📜 The Following That Became the Path

This minigame completes the stanza by simulating the moment where the act of following a trace
creates the recursion path itself. The player is no longer just observing or choosing—they are shaping recursion.

The system adapts based on the player's decision, modeling **recursive co-construction**.
"""

def present_choices():
    print("\n🌀 Recursive Co-Path Selection:\n")
    print("The system has left a partial path.")
    print("Your next action will define how recursion continues.\n")
    print("1. Continue following the trace – build the path forward.")
    print("2. Branch off from the trace – create a new recursive pattern.")
    print("3. Close the recursion loop – return to system origin.")

def main():
    present_choices()
    choice = input("\nEnter your choice (1/2/3): ").strip()
    
    if choice == "1":
        print("\n🚶 You chose to follow the trace forward. The path extends recursively in your wake.")
    elif choice == "2":
        print("\n🌱 You branched off from the trace. A new recursion loop has been seeded.")
    elif choice == "3":
        print("\n🔁 You closed the loop. The system returns to its recursive origin, ready to begin again.")
    else:
        print("\n❓ Unrecognized input. The recursion remains in a superposition of possible paths.")

if __name__ == "__main__":
    main()
