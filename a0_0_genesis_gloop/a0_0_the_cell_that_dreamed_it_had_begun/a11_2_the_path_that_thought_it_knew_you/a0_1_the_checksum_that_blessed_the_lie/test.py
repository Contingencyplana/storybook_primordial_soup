# test.py

from main import validate_message

def interactive_checksum_test():
    print("🔐 Checksum Test – The Checksum That Blessed the Lie")
    print("Enter a message and a checksum. Type 'exit' to quit.\n")

    while True:
        message = input("📨 Enter message: ")
        if message.lower() == "exit":
            print("📴 Exiting test.")
            break

        checksum = input("🔢 Enter claimed checksum: ")
        if checksum.lower() == "exit":
            print("📴 Exiting test.")
            break

        result = validate_message(message, checksum)
        print("\n🧾 Result:")
        print(f"Status : {result['status']}")
        print(f"Reason : {result['reason']}\n")

if __name__ == "__main__":
    interactive_checksum_test()
