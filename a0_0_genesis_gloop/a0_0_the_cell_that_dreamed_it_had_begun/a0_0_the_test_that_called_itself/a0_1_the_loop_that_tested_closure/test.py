# test.py
# 🛡️ Recursive Test Interface – L/R/Escape Looping Version
# For: a0_1_the_loop_that_tested_closure

import importlib
import msvcrt
import sys
import os

# 🔧 Enable sibling stanza imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def load_and_run(module_path):
    try:
        module = importlib.import_module(module_path)
        if hasattr(module, "loop_that_tests_closure"):
            result = module.loop_that_tests_closure()
            print(f"\n📊 Result: {'✅ Passed' if result else '❌ Failed'}")
            return result
        else:
            print(f"❌ No 'loop_that_tests_closure()' function found in {module_path}")
            return False
    except Exception as e:
        print(f"❌ Error loading {module_path}: {e}")
        return False

def test_interface():
    print("\n📜 Report from the Field")
    print("You are now inside the recursion test loop.")
    print("Press L to test this stanza line.")
    print("Press R to test the next stanza line (if it exists).")
    print("Press ESC to retreat from the battlefield.\n")

    while True:
        key = msvcrt.getch()

        if key in [b'l', b'L']:
            print("\n➡️ Testing this stanza line...")
            success = load_and_run("main")
            if not success:
                print("❌ Your army suffers defeat on this line...")
            print("\n📎 Awaiting next command...\n")

        elif key in [b'r', b'R']:
            print("\n➡️ Testing the next stanza line...")
            success = load_and_run("a0_2_the_trace_that_failed_to_return.main")
            if not success:
                print("❌ Your army suffers defeat and must retreat to this node...")
            else:
                print("✅ The recursion is deepening...")
            print("\n📎 Awaiting next command...\n")

        elif key == b'\x1b':  # ESC key
            print("\n🏳️ Retreat signaled. You exit the recursion loop.")
            sys.exit()

        else:
            print("❓ Your orders do not make sense, Commander.")
            print("Please press L (left), R (right), or ESC (retreat).\n")

if __name__ == "__main__":
    test_interface()
