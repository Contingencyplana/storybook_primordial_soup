# Save to: s0_2_the_court_that_argued_in_clicks/test.py

from main import interpret_clicks

def simulate_court():
    print("🗣️ Insect Court Click Interpreter")
    print("Enter click pattern (use '·' for soft clicks, '—' for hard clicks):")
    pattern = input("Click Pattern: ").strip()

    result = interpret_clicks(pattern)
    
    print("\n📜 Court Report:")
    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    simulate_court()
