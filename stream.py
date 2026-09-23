#Stream Chiper 
#Konversi teks ke binary

def text_to_binary(text):
    "Mengubah setiap karakter menjadi 8-bit binary."

    binary = ""

    for char in text:
        binary += format(ord(char), "08b")

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
            "seed 0000 tidak diperbolehkan"
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

    hex_text = hex_text.strip()


    if not hex_text:
        raise ValueError(
            "Ciphertext HEX kosong."
        )

    if len(hex_text) % 2 != 0:
        raise ValueError(
            "Ciphertext HEX harus memiliki jumlah digit genap."
        )

    binary = ""

    for i in range(0, len(hex_text), 2):

        byte_hex = hex_text[i:i + 2]

        print("DEBUG BYTE:", repr(byte_hex))

        try:
            value = int(byte_hex, 16)

        except ValueError:
            raise ValueError(
                f"Ciphertext mengandung karakter HEX yang tidak valid: {repr(byte_hex)}"
            )

        binary += format(value, "08b")

    return binary



#enkripsi

def encrypt(text, seed):

    plaintext_binary = text_to_binary(text)

    keystream = lsfr_generate(
        seed,
        len(plaintext_binary)
    )

    ciphertext_binary = xor_binary(
        plaintext_binary,
        keystream
    )

    ciphertext_hex = binary_to_hex(
        ciphertext_binary
    )

    return {
        "plaintext": text,
        "plaintext_binary": plaintext_binary,
        "keystream": keystream,
        "ciphertext_binary": ciphertext_binary,
        "ciphertext_hex": ciphertext_hex
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

streamCipherNotes = """
            ### 🔐 Proses Enkripsi Stream Cipher

            **1. Konversi Plaintext ke Binary**

            Setiap karakter pada plaintext dikonversi menjadi representasi
            binary 8-bit.

            **2. Generate Keystream**

            Seed 4-bit digunakan sebagai nilai awal LFSR (Linear Feedback
            Shift Register). LFSR menghasilkan rangkaian bit yang disebut
            keystream.

            **3. Operasi XOR**

            Plaintext binary di-XOR dengan keystream yang dihasilkan oleh LFSR.

            **4. Menghasilkan Ciphertext Binary**

            Hasil operasi XOR berupa ciphertext dalam bentuk binary.

            **5. Konversi Binary ke HEX**

            Ciphertext binary dikonversi menjadi hexadecimal agar lebih mudah
            ditampilkan dan digunakan sebagai ciphertext.

            ---

            ### 🔓 Proses Dekripsi

            **1. Konversi Ciphertext HEX ke Binary**

            Ciphertext hexadecimal dikonversi kembali menjadi binary.

            **2. Generate Keystream**

            Seed yang sama digunakan untuk menghasilkan keystream yang sama
            menggunakan LFSR.

            **3. Operasi XOR**

            Ciphertext binary di-XOR dengan keystream.

            **4. Menghasilkan Plaintext Binary**

            Hasil XOR menghasilkan kembali binary dari plaintext asli.

            **5. Konversi Binary ke Teks**

            Plaintext binary dikonversi kembali menjadi karakter sehingga
            menghasilkan plaintext asli.

            ---

            ### Alur Enkripsi

            Plaintext
            ↓
            Binary
            ↓
            LFSR + Seed
            ↓
            Keystream
            ↓
            XOR
            ↓
            Ciphertext Binary
            ↓
            HEX
            ↓
            Ciphertext HEX

            ### Alur Dekripsi

            Ciphertext HEX
            ↓
            Binary
            ↓
            LFSR + Seed
            ↓
            Keystream
            ↓
            XOR
            ↓
            Plaintext Binary
            ↓
            Text
            ↓
            Plaintext
            """