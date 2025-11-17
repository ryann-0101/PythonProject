
from cryptography.fernet import Fernet

# Use the same key every time (hardcoded for simplicity)
key = b'l8gEh39bkcFotJRANfvGv9hXHH0S92RLLYLmGAVQ0Fg='  # Replace with a generated key once
cipher = Fernet(key)

print("""
**MENU**
1 - Encrypt 
2 - Decrypt
""")
choice = int(input("Enter operation to complete: "))

def encrypt():
    phrase = input("Enter phrase to encrypt: ")
    encrypted = cipher.encrypt(phrase.encode())
    print("Encrypted phrase:\n", encrypted.decode())  # Show token

def decrypt():
    token = input("Enter token to decrypt: ").encode()  # Convert back to bytes
    try:
        decrypted = cipher.decrypt(token).decode()
        print("Decrypted phrase:\n", decrypted)
    except:
        print("Invalid token or wrong key!")

if choice == 1:
    encrypt()
elif choice == 2:
    decrypt()
else:
    print("Invalid choice.")
