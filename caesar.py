def caesar_encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
            result += char

    return result


def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)


def caesar_encrypt_process(text, key):
    process = []

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            new_char = chr(shifted)

            process.append({
                "input": char,
                "output": new_char,
                "operation": f"Geser +{key}"
            })

        else:
            process.append({
                "input": char,
                "output": char,
                "operation": "Tidak berubah"
            })

    return caesar_encrypt(text, key), process


def caesar_decrypt_process(ciphertext, key):
    process = []

    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base - key) % 26 + base
            new_char = chr(shifted)

            process.append({
                "input": char,
                "output": new_char,
                "operation": f"Geser -{key}"
            })

        else:
            process.append({
                "input": char,
                "output": char,
                "operation": "Tidak berubah"
            })

    return caesar_decrypt(ciphertext, key), process