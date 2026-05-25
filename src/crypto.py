import os
import json
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def derive_key(password: str, salt: bytes) -> bytes:
    """Derive a 256-bit AES key from a password."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600_000,
    )
    return kdf.derive(password.encode())

def encrypt_list_of_lists(data_list: list, password: str) -> bytes:
    """Serializes a list of lists and encrypts it in memory."""
    # 1. Convert the list of lists into a JSON string, then encode to bytes
    serialized_data = json.dumps(data_list).encode('utf-8')
    
    # 2. Encrypt the serialized bytes
    salt = os.urandom(16)
    key = derive_key(password, salt)
    
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, serialized_data, None)
    
    return salt + nonce + ciphertext

def decrypt_to_list_of_lists(encrypted_blob: bytes, password: str) -> list:
    """Decrypts data and deserializes it back into a list of lists."""
    salt = encrypted_blob[:16]
    nonce = encrypted_blob[16:28]
    ciphertext = encrypted_blob[28:]
    
    # 1. Decrypt back to serialized bytes
    key = derive_key(password, salt)
    aesgcm = AESGCM(key)
    decrypted_bytes = aesgcm.decrypt(nonce, ciphertext, None)
    
    # 2. Decode the bytes back to a JSON string, then parse it back to a list
    serialized_data = decrypted_bytes.decode('utf-8')
    return json.loads(serialized_data)


'''
# Example Usage
password = "super-secret-password"
my_list_of_lists = [
    ["Alice", 28, "Engineer"],
    ["Bob", 34, "Designer"],
    ["Charlie", 22, "Data Scientist"]
]

# Encrypt
encrypted_blob = encrypt_list_of_lists(my_list_of_lists, password)
print(f"Encrypted blob type: {type(encrypted_blob)} (Length: {len(encrypted_blob)} bytes)")

# Decrypt
restored_list = decrypt_to_list_of_lists(encrypted_blob, password)
print(f"Decrypted data type: {type(restored_list)}")
print(f"Restored content: {restored_list}")
'''