# 📄 main.py
# 🧩 a0_3_adventure_of_the_unasked_question → a0_3_the_return_that_waited_in_vain
# A callback function that waits for a response that will never come.

import time

def await_callback_response(signal_received=False, timeout=3):
    """
    Waits for a return signal that is never guaranteed to arrive.
    If no signal is received, the system waits silently — then returns sorrow.
    """
    if signal_received:
        return {
            "status": "completed",
            "response": "Signal received. Callback executed successfully."
        }

    # Simulate the wait
    time.sleep(timeout)
    return {
        "status": "timed_out",
        "response": "No return signal arrived. The handler waited in vain."
    }

# Manual test
if __name__ == "__main__":
    response = await_callback_response(False)
    print("\n📡 Callback Result:")
    print(f"Status   : {response['status']}")
    print(f"Response : {response['response']}")

