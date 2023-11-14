import random


def encrypt(message, key):
    encrypted = []
    for char in message:
        encrypted_char = ord(char) ^ key
        encrypted.append(encrypted_char)
    return bytes(encrypted)


def decrypt(encrypted_message, key):
    decrypted = []
    for char in encrypted_message:
        decrypted_char = char ^ key
        decrypted.append(decrypted_char)
    return bytes(decrypted).decode()


def generate_key():
    return random.randint(1, 255)
