# C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\
# a0_0_the_cell_that_dreamed_it_had_begun\a0_0_the_test_that_called_itself\
# a3_3_the_fallback_that_caused_the_failure\main.py

def perform_with_fallback(primary_success=True, fallback_enabled=True):
    """
    Simulates a system where fallback logic introduces the failure it was meant to avoid.
    """
    if primary_success:
        return {
            "status": "success",
            "message": "Primary operation completed successfully. No fallback triggered."
        }

    if fallback_enabled:
        return {
            "status": "failure",
            "message": "⚠️ Fallback activated... and caused systemic failure."
        }

    return {
        "status": "error",
        "message": "Primary failed. No fallback was configured. Silent failure occurred."
    }

if __name__ == "__main__":
    result = perform_with_fallback(primary_success=False, fallback_enabled=True)
    print("🧪 Fallback Result:", result["message"])
