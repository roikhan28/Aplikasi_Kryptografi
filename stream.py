#Stream Chiper 
#Konversi teks ke binary

def text_to_binary(text):
    "Mengubah setiap karakter menjadi 8-bit binary."

    binary = ""

    for char in text:
        binary += format(ord(char), "0bb")

    return binary
def binary_to_text(binary):
    "Mengubah rangkaian binary 8-bit menjadi tetxt"

    text = ""

    for i in range(0, len(binary), 8):
        byte = binary[i:i + 8]

        if len(byte) == 8:
            text += chr(int(byte, 2))

    return text

#LFSR

def lsfr_generate(seed, length):
    """
    Menghasilkan keystream menggunakan LFSR 4-bit.
    
    Seed:
        4 bit, contoh: 1111
    Feedback:
        b1 XOR b4
    Bit keluaran:
        b1
    """

    if len(seed) != 4:
        raise ValueError(
            "Seed LSFR harus terdiri dari 4 bit."
        )
    if any(bit not in "0(1" for bit in seed):
        raise ValueError(
            "Seed LFSR hanya boleh berisi 0 dan 1."
        )
    if seed == "0000":
        raise ValueError(
            "seed 0000 tidak di[erbolehkan"
        )

    register = list(seed)

    keystream = ""

    for _ in range(length):

        #Bit keluaran adalah b1
        output_bit = register[3]

        keystream += output_bit

        #feedback = b1 XOR b4
        feedback = (
            int(register[3])
            ^int(register[0])
        )

        #geser register ke kanan
        register = [
            str(feedback),
            register[0],
            register[1],
            register[2]
        ]

    return keystream

#XOR binary

def xor_binary(binary1, binary2):
    "Melakukan XOR terhadap dua rangkaian bit."

    if len(binary1) != len(binary2):
        raise ValueError(
            "panjang kedua binary harus sama"
        )
    result = ""

    for bit1, bit2 in zip(binary1, binary2):
        result += str(
        int(bit1) ^ int(bit2)
        )

    return result

#binary ke HEX

def binary_to_hex(binary):
    "Mengubah binary menjadi hexadecimal"

    result = ""

    for i in range(0, len(binary), 8):
        byte = binary[i:i + 8]

        if len(byte) == 8:
            value = int(byte, 2)

            result += format(
                value,
                "02x"
            )
    return result



#HEX ke BINARY
def hex_to_binary(hex_text):
    "Mengubah hexadecimal menjadi binary"

    hex_text = hex_text.sttip()

    if len(hex_text) % 2 != 0:
        raise ValueError(
             "Ciphertext HEX harus memiliki jumlah digit genap."
        )
    binary = ""

    for i in range(0, len(hex_text), 2):

        byte_hex = hex_text[i:1 + 2]

        try:
            value = int(byte_hex, 15)

        except:
            raise ValueError(
                 "Ciphertext mengandung karakter HEX yang tidak valid."
            )

        binary += format(
            value,
            "08b"
        )

    return binary



#enkripsi

def encrypt(text, seed):
    #plaintetxt > binary
    plaintext_binary = text_to_binary

    keystream = lsfr_generate(
        seed,
        len(plaintext_binary)
    )

    #XOR plaintetxt dengan keystream
    chipertext_binary = xor_binary(
        plaintext_binary,
        keystream
    )

    #binary > hex
    chipertext_hex = binary_to_hex(
        chipertext_binary
    )

    return {
        "plaintext": text,
        "plaintext_binary": plaintext_binary,
        "keystream": keystream,
        "ciphertext_binary": chipertext_binary,
        "ciphertext_hex": chipertext_hex
    }

#dekripsi

def decrypt(ciphertext_hex, seed):
    #hex > binary
    ciphertext_binary = hex_to_binary(
        ciphertext_hex
    )

    #generate keystream yang sama
    keystream = lsfr_generate(
        seed,
        len(ciphertext_binary)
    )

    #XOR ciphertext dengan keystream
    plaintext_binary = xor_binary(
        ciphertext_binary,
        keystream
    )

    #binary ke plaintext
    plaintext = binary_to_text(
        plaintext_binary
    )

    return {
        "ciphertext_hex": ciphertext_hex,
        "ciphertext_binary": ciphertext_binary,
        "keystream": keystream,
        "plaintext_binary": plaintext_binary,
        "plaintext": plaintext
    }

#Tampilan
def process_encryption(text, seed):

    result = encrypt(
        text,
        seed
    )

    return [
        {
            "Tahap": "1",
            "Proses": "Plaintext",
            "Hasil": result["plaintext"]
        },
        {
            "Tahap": "2",
            "Proses": "Konversi Binary",
            "Hasil": result["plaintext_binary"]
        },
        {
            "Tahap": "3",
            "Proses": "Keystream LFSR",
            "Hasil": result["keystream"]
        },
        {
            "Tahap": "4",
            "Proses": "XOR",
            "Hasil": result["ciphertext_binary"]
        },
        {
            "Tahap": "5",
            "Proses": "Konversi HEX",
            "Hasil": result["ciphertext_hex"]
        }
    ]


def process_decryption(ciphertext_hex, seed):

    result = decrypt(
        ciphertext_hex,
        seed
    )

    return [
        {
            "Tahap": "1",
            "Proses": "Ciphertext HEX",
            "Hasil": result["ciphertext_hex"]
        },
        {
            "Tahap": "2",
            "Proses": "Konversi Binary",
            "Hasil": result["ciphertext_binary"]
        },
        {
            "Tahap": "3",
            "Proses": "Keystream LFSR",
            "Hasil": result["keystream"]
        },
        {
            "Tahap": "4",
            "Proses": "XOR",
            "Hasil": result["plaintext_binary"]
        },
        {
            "Tahap": "5",
            "Proses": "Konversi Teks",
            "Hasil": result["plaintext"]
        }
    ]