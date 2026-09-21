def railFenceEncrypt(text, rails):
    if rails <= 1:
        return text

    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail].append(char)

        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1

        rail += direction

    return ''.join(''.join(row) for row in fence)

def railFenceDecrypt(cipher, rails):
    if rails <= 1:
        return cipher

    pattern = []
    rail = 0
    direction = 1

    for _ in cipher:
        pattern.append(rail)

        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1

        rail += direction

    counts = [pattern.count(i) for i in range(rails)]

    rails_data = []
    index = 0

    for count in counts:
        rails_data.append(list(cipher[index:index + count]))
        index += count

    result = []

    for r in pattern:
        result.append(rails_data[r].pop(0))

    return ''.join(result)


def railFenceProcess(text, rails, decrypt=False):
    if decrypt:
        result = railFenceDecrypt(text, rails)
        return result

    rows = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        rows[rail].append(char)

        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1

        rail += direction

    return '\n'.join(
        f"Rail {i + 1}: {' '.join(row)}"
        for i, row in enumerate(rows)
    )

railFenceNotes = """
        **Proses Enkripsi:**

        1. Plaintext ditulis secara zig-zag.
        2. Penulisan dilakukan pada sejumlah rail.
        3. Setelah mencapai rail terakhir, arah berubah.
        4. Ciphertext dibentuk dengan membaca setiap rail dari atas ke bawah.

        **Contoh dengan 3 rail:**

        ```text
        INFORMATIKA UPN
        ```

        Disusun menjadi pola zig-zag:

        ```text
        I       R       I       U 
          N   O   M   T   K       P
            F       A       A       N
        ```

        Kemudian karakter dibaca per rail untuk menghasilkan ciphertext.

        **Dekripsi:**

        Ciphertext disusun kembali berdasarkan pola zig-zag,
        kemudian dibaca mengikuti pola tersebut untuk mendapatkan plaintext.
        """
    