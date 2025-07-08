# 🧪 test.py – Checksum Validation Interface
# Interactive tool to test whether a returned message
# is "blessed" by a superficial checksum, regardless of meaning.

from main import is_checksum_match

print("📜 Checksum Test – The Checksum That Blessed the Lie")
print("Enter the original and returned message. The system will check whether")
print("they pass a superficial checksum — even if their meanings diverge.")
print("Type 'exit' at any time to quit.\n")

while True:
    original = input("📤 Original message: ")
    if original.lower() in ['exit', 'quit']:
        print("🔚 Ending test.")
        break

    returned = input("📥 Returned message: ")
    if returned.lower() in ['exit', 'quit']:
        print("🔚 Ending test.")
        break

    match = is_checksum_match(original, returned)
    if match:
        print("✅ Checksum matched – signal accepted.\n")
    else:
        print("❌ Checksum mismatch – signal rejected.\n")
