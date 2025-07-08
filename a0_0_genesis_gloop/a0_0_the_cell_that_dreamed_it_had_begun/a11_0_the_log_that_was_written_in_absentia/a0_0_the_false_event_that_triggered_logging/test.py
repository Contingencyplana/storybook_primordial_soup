# 📄 test.py
# 🧪 Interactive tester for a0_3_adventure_of_the_unasked_question → a0_2_the_branch_that_was_never_chosen

from main import evaluate_branch_selection

def run_test():
    print("📜 Branching Path Test – The Branch That Was Never Chosen\n")

    while True:
        decision = input("Choose a branch (or press Enter to choose none): ")
        if decision.lower() in ["exit", "quit", "q"]:
            print("👋 Exiting branching test.")
            break

        result = evaluate_branch_selection(decision)
        print(f"\n🧠 Branch Result:")
        print(f"Status : {result['status']}")
        print(f"Outcome: {result['outcome']}\n")

if __name__ == "__main__":
    run_test()
