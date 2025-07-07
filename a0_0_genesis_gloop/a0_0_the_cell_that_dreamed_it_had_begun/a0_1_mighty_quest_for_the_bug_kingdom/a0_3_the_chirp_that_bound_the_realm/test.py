# 🧪 test.py
# Path: a0_1_mighty_quest_for_the_bug_kingdom/a0_3_the_chirp_that_bound_the_realm/test.py

from main import unify_through_chirp

def run_chirp_unity_test():
    print("🎼 Swarm Harmony Simulation – The Final Chirp")

    try:
        input_string = input("Enter chirp frequencies (comma-separated, e.g., 0.88,0.89,0.87): ")
        chirps = [float(x.strip()) for x in input_string.split(",") if x.strip()]
    except Exception:
        print("❌ Invalid input. Please enter floats separated by commas.")
        return

    result = unify_through_chirp(chirps)
    print("\n📜 Chirp Result:")
    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    run_chirp_unity_test()
