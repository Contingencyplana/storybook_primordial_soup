# Save to: s0_3_the_chirp_that_bound_the_realm/test.py

from main import unify_chirp_patterns

def simulate_courtroom_clicks():
    print("🎼 Bug Kingdom Chirp Unifier")
    print("Enter chirps one at a time (type 'done' to finish):")
    chirps = []

    while True:
        chirp = input("Chirp> ").strip()
        if chirp.lower() == "done":
            break
        if chirp:
            chirps.append(chirp)

    result = unify_chirp_patterns(chirps)
    print("\n📜 Chirp Consensus Report:")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    simulate_courtroom_clicks()
