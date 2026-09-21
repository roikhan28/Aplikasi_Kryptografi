import base64
import secrets

from cryptography.hazmat.backends import Cipher, algorithms, modes

def generate_key():
    return secrets.token_bytes(32)  # Generate a random 256-bit key

def aesencrypt(text, key):
    plaintext = text.encode('utf-8')

    nonce = secrets.token_bytes(12)

    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))

    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    tag = encryptor.tag

    return(
        base64.b64encode(nonce).decode('utf-8'),
        base64.b64encode(ciphertext).decode('utf-8'),
        base64.b64encode(tag).decode('utf-8')
    )

def aesdecrypt(ciphertext, key, nonce, tag):
    ciphertext = base64.b64decode(ciphertext)
    nonce = base64.b64decode(nonce)
    tag = base64.b64decode(tag)

    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag))

    decryptor = cipher.decryptor()

    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return plaintext.decode('utf-8')