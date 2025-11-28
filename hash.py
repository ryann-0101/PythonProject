
from cryptography.fernet import Fernet

# Use the same key every time (hardcoded for simplicity)
key = b'l8gEh39bkcFotJRANfvGv9hXHH0S92RLLYLmGAVQ0Fg='  
cipher = Fernet(key)


def encrypt():
    try:
        phrase = input("Enter phrase to encrypt: ")
        encrypted = cipher.encrypt(phrase.encode())
        print("Encrypted phrase:\n", encrypted.decode())  
        print("Going back to menu.....")
        menu()
    except:
        print("Invalid Input")
        encrypt()

def decrypt():
    token = input("Enter token to decrypt: ").encode()  # Convert back to bytes
    try:
        decrypted = cipher.decrypt(token).decode()
        print("Decrypted phrase:\n", decrypted)
        print("Going back to menu.....")
        menu()
    except:
        print("Invalid token or wrong key!")
        decrypt()

def menu():
    print("""
**MENU**
1 - Encrypt 
2 - Decrypt
3 - Exit Program
""")
    choice = int(input("Enter operation to complete: "))

    if choice == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    elif choice ==3:
        print("Exiting Program.....")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    print("Do not run this file directly - instead run main.py")