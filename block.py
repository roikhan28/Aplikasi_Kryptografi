import base64
import secrets

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

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

aesNotes = """
        **Proses Enkripsi:**
        
        1. **Generate Key**
        
           Sistem menghasilkan kunci AES secara acak dengan panjang 256-bit
           (32 byte).
        
        2. **Generate Nonce**
        
           Sistem menghasilkan nonce sepanjang 12 byte yang digunakan
           dalam proses enkripsi.
        
        3. **Konversi Plaintext**
        
           Plaintext diubah menjadi bentuk bytes menggunakan encoding UTF-8.
        
        4. **Proses Enkripsi**
        
           Plaintext dienkripsi menggunakan AES-256 dengan mode GCM
           menggunakan key dan nonce.
        
        5. **Menghasilkan Ciphertext**
        
           Hasil enkripsi berupa ciphertext yang tidak dapat dibaca seperti
           plaintext asli.
        
        6. **Menghasilkan Authentication Tag**
        
           AES-GCM menghasilkan authentication tag yang digunakan untuk
           memverifikasi integritas data saat proses dekripsi.
        
        **Alur Enkripsi:**
        
        Plaintext + AES-256 Key + Nonce
        ↓
        AES-256-GCM
        ↓
        Ciphertext + Authentication Tag
        
        
        **Proses Dekripsi:**
        
        1. Ciphertext, key, nonce, dan authentication tag dimasukkan
           ke dalam proses dekripsi.
        
        2. AES-256-GCM memverifikasi authentication tag untuk memastikan
           ciphertext tidak mengalami perubahan.
        
        3. Jika authentication tag valid, ciphertext didekripsi menggunakan
           key dan nonce.
        
        4. Hasil dekripsi dikonversi kembali dari bytes menjadi teks UTF-8.
        
        5. Plaintext asli berhasil diperoleh kembali.
        
        **Alur Dekripsi:**
        
        Ciphertext + AES-256 Key + Nonce + Authentication Tag
        ↓
        AES-256-GCM
        ↓
        Plaintext
        """