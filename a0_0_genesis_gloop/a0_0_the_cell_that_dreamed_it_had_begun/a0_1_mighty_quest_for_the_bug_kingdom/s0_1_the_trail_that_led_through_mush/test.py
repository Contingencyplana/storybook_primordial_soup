# Save to: s0_1_the_trail_that_led_through_mush/test.py

from main import navigate_fungal_maze

def simulate_maze_travel():
    print("🌫️ Fungal Maze Navigation Interface")
    print("Paths: forward, left, right")
    path = input("Choose your path: ").strip().lower()

    result = navigate_fungal_maze(path)

    print("\n📜 Trail Report:")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    simulate_maze_travel()
