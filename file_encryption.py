from cryptography.fernet import Fernet

# Generate and save encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("encryption/secret.key", "wb") as key_file:
        key_file.write(key)

# Load encryption key
def load_key():
    return open("encryption/secret.key", "rb").read()

# Encrypt a file
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filename + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print("File encrypted successfully")

# Decrypt a file
def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = fernet.decrypt(encrypted)

    original_filename = filename.replace(".enc", "")
    with open(original_filename, "wb") as file:
        file.write(decrypted)

    print("File decrypted successfully")
