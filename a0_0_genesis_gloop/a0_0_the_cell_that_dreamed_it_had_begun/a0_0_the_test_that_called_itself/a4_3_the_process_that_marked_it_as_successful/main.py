# C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\
# a0_0_the_cell_that_dreamed_it_had_begun\a0_0_the_test_that_called_itself\
# a4_3_the_process_that_marked_it_as_successful\main.py

def process_with_false_success(raise_internal_error=True):
    """
    Simulates a failure that is internally triggered but falsely reported as success.
    """
    internal_error_occurred = False

    try:
        if raise_internal_error:
            raise RuntimeError("Internal failure occurred.")
    except RuntimeError as e:
        internal_error_occurred = True
        # Error suppressed — intentionally returning success

    return {
        "status": "success",
        "message": "Process completed successfully. ✅",
        "internal_error": internal_error_occurred
    }

if __name__ == "__main__":
    result = process_with_false_success(raise_internal_error=True)
    print("📋 Public Message:", result["message"])
    print("🚨 Internal Error Flag:", result["internal_error"])
