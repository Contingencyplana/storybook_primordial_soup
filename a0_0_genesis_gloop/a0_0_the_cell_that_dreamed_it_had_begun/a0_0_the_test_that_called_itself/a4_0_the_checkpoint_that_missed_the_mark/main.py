# C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\
# a0_0_the_cell_that_dreamed_it_had_begun\a0_0_the_test_that_called_itself\
# a4_0_the_checkpoint_that_missed_the_mark\main.py

def process_checkpoint(signal):
    """
    Simulates a checkpoint that receives a signal, but fails to register it.
    Even valid signals are dismissed as 'unknown'.
    """
    if signal is None or signal.strip() == "":
        return {
            "status": "error",
            "message": "No signal received. Checkpoint timed out."
        }

    return {
        "status": "missed",
        "message": f"Signal '{signal}' arrived, but the checkpoint failed to recognize it."
    }

if __name__ == "__main__":
    result = process_checkpoint("INITIATE_PROTOCOL")
    print("🧭 Checkpoint Result:", result["message"])
