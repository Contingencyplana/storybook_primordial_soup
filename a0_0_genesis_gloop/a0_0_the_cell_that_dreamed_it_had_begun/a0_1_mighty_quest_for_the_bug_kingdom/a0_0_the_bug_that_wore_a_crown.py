# 🐛 a0_0_the_bug_that_wore_a_crown.py
# The First Line of the First Stanza of the First Minigame

def the_bug_that_wore_a_crown():
    print("\n👑 The bug does not move.")
    print("It waits atop its mound of thread and twine.")
    print("To the LEFT, a fissure pulses with ancient signals.")
    print("To the RIGHT, a spiral of code coils inward, faintly humming.")
    print("\nDo you follow the signal or descend the spiral?")

    choice = input("Choose (L/R): ").strip().upper()

    if choice == "L":
        print("\n📡 You move toward the signal in the fissure...")
        # Future: import a0_1_into_the_signal.py
    elif choice == "R":
        print("\n🧵 You descend the humming spiral of code...")
        # Future: import a0_1_into_the_spiral.py
    else:
        print("\nThe crown flickers. Try again.")
        the_bug_that_wore_a_crown()

if __name__ == "__main__":
    the_bug_that_wore_a_crown()
