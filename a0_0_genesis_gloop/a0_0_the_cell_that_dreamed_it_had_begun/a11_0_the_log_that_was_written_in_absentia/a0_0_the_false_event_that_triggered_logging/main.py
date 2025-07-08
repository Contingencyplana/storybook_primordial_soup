# 📄 main.py
# 🧩 a0_3_adventure_of_the_unasked_question → a0_2_the_branch_that_was_never_chosen
# A test of hypothetical decisions — and the cost of ignoring the fork.

def evaluate_branch_selection(selection):
    """
    Evaluates whether the player made an explicit decision at a branch.
    If no branch is selected, the system responds with poetic regret.
    """
    branches = {"left": "You stepped into the unknown, veiled in fog.",
                "right": "You followed the signal into narrow light.",
                "up": "You ascended where thought dares not tread.",
                "down": "You descended into recursive silence."}

    if not selection.strip():
        return {
            "status": "unselected",
            "outcome": "No path was chosen. The branch remains untouched — its fate unwritten."
        }
    elif selection.lower() not in branches:
        return {
            "status": "invalid",
            "outcome": f"Branch '{selection}' is not part of the known divergence. The moment passed unclaimed."
        }
    else:
        return {
            "status": "chosen",
            "outcome": branches[selection.lower()]
        }

# For direct play
if __name__ == "__main__":
    decision = input("🌿 Choose your branch (left, right, up, down): ")
    result = evaluate_branch_selection(decision)
    print(f"\n📚 Branch Evaluation:\nStatus: {result['status']}\nOutcome: {result['outcome']}")
