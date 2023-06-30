from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def encrypt(text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(text.encode(), AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text.hex()


def decrypt(encrypted_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_text = bytes.fromhex(encrypted_text)
    decrypted_text = cipher.decrypt(encrypted_text)
    unpadded_text = unpad(decrypted_text, AES.block_size)
    return unpadded_text.decode()


def generate_key():
    return get_random_bytes(16)
