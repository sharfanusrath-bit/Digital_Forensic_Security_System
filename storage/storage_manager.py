import os
import shutil
from encryption.file_encryption import encrypt_file, decrypt_file

STORAGE_PATH = "storage/"

def store_file(filepath):
    encrypt_file(filepath)
    encrypted_file = filepath + ".enc"
    shutil.move(encrypted_file, STORAGE_PATH)
    os.remove(filepath)
    print("File securely stored")

def retrieve_file(filename):
    encrypted_path = os.path.join(STORAGE_PATH, filename)
    decrypt_file(encrypted_path)
    print("File retrieved and decrypted")
