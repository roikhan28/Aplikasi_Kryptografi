import streamlit as st
import base64

from rail_fence import(
    railFenceEncrypt,
    railFenceDecrypt,
    railFenceNotes,
)

from caesar import (
    caesar_encrypt,
    caesar_decrypt,
    caesar_encrypt_process,
    caesar_decrypt_process,
)

from block import (
    generate_key,
    aesencrypt,
    aesdecrypt,
    aesNotes
)

from stream import (
    encrypt,
    decrypt,
    process_encryption,
    process_decryption,
    streamCipherNotes
)

from block import (
    generate_key,
    aesencrypt,
    aesdecrypt,
    aesNotes
)

from super_encryption import (
    super_encrypt,
    super_decrypt
)

st.title("Aplikasi Enkripsi dan Dekripsi Kriptografi")


# =========================
# NAVIGATION
# =========================

if "menu" not in st.session_state:
    st.session_state.menu = "Caesar Cipher"


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("Caesar", use_container_width=True):
        st.session_state.menu = "Caesar Cipher"

with col2:
    if st.button("Rail Fence", use_container_width=True):
        st.session_state.menu = "Rail Fence Cipher"

with col3:
    if st.button("AES", use_container_width=True):
        st.session_state.menu = "AES"

with col4:
    if st.button("Stream", use_container_width=True):
        st.session_state.menu = "Stream"

with col5:
    if st.button("Super Encryption", use_container_width=True):
        st.session_state.menu = "Super Encryption"


menu = st.session_state.menu

# CAESARRRR

if menu == "Caesar Cipher":
    
    st.header("Caesar Cipher")

    st.write(
        "Caesar Cipher adalah algoritma kriptografi klasik "
        "yang menggantikan setiap huruf dalam plaintext "
        "dengan huruf lain yang berada pada posisi tertentu "
        "di alfabet."
    )

    text = st.text_area(
        "Masukkan teks",
        placeholder="Contoh: INFORMATIKA UPN"
    )

    key = st.number_input(
        "Kunci (Key)",
        min_value=1,
        max_value=25,
        value=3
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("🔒 Enkripsi", use_container_width=True):

            if text:

                result, process = caesar_encrypt_process(text, key)

                st.success("Enkripsi berhasil!")
                st.code(result)

                with st.expander("📖 Lihat Proses Algoritma"):
                    for step in process:
                        st.write(
                            f"Input: {step['input']} | "
                            f"Output: {step['output']} | "
                            f"Operasi: {step['operation']}"
                        )

    with col2:

        if st.button("🔓 Dekripsi", use_container_width=True):

            if text:

                result, process = caesar_decrypt_process(text, key)

                st.success("Dekripsi berhasil!")
                st.code(result)

                with st.expander("📖 Lihat Proses Algoritma"):
                    for step in process:
                        st.write(
                            f"Input: {step['input']} | "
                            f"Output: {step['output']} | "
                            f"Operasi: {step['operation']}"
                        )


# RAIL FENCEEE


elif menu == "Rail Fence Cipher":

    st.header("Rail Fence Cipher")

    st.write(
        "Rail Fence Cipher merupakan algoritma transposisi klasik "
        "yang menyusun plaintext secara zig-zag pada beberapa rail."
    )

    text = st.text_area(
        "Masukkan teks",
        placeholder="Contoh: INFORMATIKA UPN"
    )

    rails = st.number_input(
        "Jumlah Rail",
        min_value=2,
        max_value=20,
        value=3
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("🔒 Enkripsi", use_container_width=True):

            if text:

                result = railFenceEncrypt(text, rails)

                st.success("Enkripsi berhasil!")
                st.code(result)

    with col2:

        if st.button("🔓 Dekripsi", use_container_width=True):

            if text:

                result = railFenceDecrypt(text, rails)

                st.success("Dekripsi berhasil!")
                st.code(result)

    st.divider()

    with st.expander("📖 Lihat Proses Algoritma"):

        st.markdown(railFenceNotes)


# AESSSSS


elif menu == "AES":

    st.header("AES Cipher")

    st.write(
        "AES (Advanced Encryption Standard) merupakan algoritma kriptografi "
        "simetris modern yang digunakan untuk mengenkripsi dan mendekripsi "
        "data menggunakan kunci yang sama. AES mendukung ukuran kunci "
        "128, 192, dan 256-bit."
    )

    # =========================
    # SESSION STATE
    # =========================

    if "key" not in st.session_state:
        st.session_state.key = None

    if "ciphertext" not in st.session_state:
        st.session_state.ciphertext = None

    if "nonce" not in st.session_state:
        st.session_state.nonce = None

    if "tag" not in st.session_state:
        st.session_state.tag = None


    # =========================
    # GENERATE KEY
    # =========================

    if st.button("Generate AES Key"):

        st.session_state.key = generate_key()

        # Reset hasil enkripsi sebelumnya
        st.session_state.ciphertext = None
        st.session_state.nonce = None
        st.session_state.tag = None


    # Tampilkan key jika sudah ada
    if st.session_state.key is not None:

        key_display = base64.b64encode(
            st.session_state.key
        ).decode("utf-8")

        st.write("AES-256 Key:")
        st.code(key_display)


    st.divider()


    # =========================
    # ENKRIPSI
    # =========================

    st.subheader("Enkripsi")

    plaintext = st.text_area(
        "Masukkan teks",
        placeholder="Contoh: INFORMATIKA UPN"
    )


    if st.button(
        "Enkripsi",
        use_container_width=True
    ):

        if not plaintext:

            st.warning(
                "Masukkan teks terlebih dahulu."
            )

        elif st.session_state.key is None:

            st.warning(
                "Generate AES Key terlebih dahulu."
            )

        else:

            (
                st.session_state.nonce,
                st.session_state.ciphertext,
                st.session_state.tag
            ) = aesencrypt(
                plaintext,
                st.session_state.key
            )

            st.success(
                "Enkripsi berhasil!"
            )


    # =========================
    # HASIL ENKRIPSI
    # =========================

    if st.session_state.ciphertext is not None:

        st.write("Ciphertext:")
        st.code(
            st.session_state.ciphertext
        )

        st.write("Nonce:")
        st.code(
            st.session_state.nonce
        )

        st.write("Authentication Tag:")
        st.code(
            st.session_state.tag
        )


    st.divider()


    # =========================
    # DEKRIPSI
    # =========================

    st.subheader("Dekripsi")

    ciphertext_input = st.text_area(
        "Masukkan ciphertext",
        placeholder="Masukkan ciphertext hasil enkripsi"
    )


    nonce_col, tag_col = st.columns(2)

    with nonce_col:

        nonce_input = st.text_input(
            "Nonce",
            placeholder="Masukkan nonce"
        )


    with tag_col:

        tag_input = st.text_input(
            "Authentication Tag",
            placeholder="Masukkan authentication tag"
        )


    if st.button(
        "Dekripsi",
        use_container_width=True
    ):

        if not ciphertext_input:

            st.warning(
                "Masukkan ciphertext terlebih dahulu."
            )

        elif not nonce_input:

            st.warning(
                "Masukkan nonce terlebih dahulu."
            )

        elif not tag_input:

            st.warning(
                "Masukkan authentication tag terlebih dahulu."
            )

        elif st.session_state.key is None:

            st.warning(
                "Generate AES Key terlebih dahulu."
            )

        else:

            try:

                result = aesdecrypt(
                    ciphertext_input,
                    st.session_state.key,
                    nonce_input,
                    tag_input
                )

                st.success(
                    "Dekripsi berhasil!"
                )

                st.write("Plaintext:")
                st.code(result)

            except Exception:

                st.error(
                    "Dekripsi gagal. Pastikan ciphertext, "
                    "nonce, authentication tag, dan key "
                    "sesuai."
                )


    st.divider()


    # =========================
    # PENJELASAN ALGORITMA
    # =========================

    with st.expander(
        "📖 Lihat Proses Algoritma"
    ):

        st.markdown(aesNotes)


# STREAMMMM

elif menu == "Stream":

    st.header("Stream Cipher")

    st.write(
        "Stream Cipher merupakan metode kriptografi yang mengenkripsi "
        "data secara bit demi bit menggunakan keystream. Pada aplikasi "
        "ini, keystream dihasilkan menggunakan LFSR (Linear Feedback "
        "Shift Register) dengan seed 4-bit."
    )

    st.divider()

    # =========================
    # ENKRIPSI
    # =========================

    st.subheader("🔐 Enkripsi")

    plaintext = st.text_area(
        "Masukkan teks",
        placeholder="Contoh: INFORMATIKA UPN"
    )

    seed = st.text_input(
        "Seed LFSR",
        placeholder="Contoh: 1011",
        max_chars=4
    )

    if st.button("Enkripsi", use_container_width=True):

        if not plaintext:
            st.warning("Masukkan teks terlebih dahulu.")

        elif not seed:
            st.warning("Masukkan seed LFSR terlebih dahulu.")

        elif len(seed) != 4 or any(bit not in "01" for bit in seed):
            st.warning("Seed harus terdiri dari 4 bit, contoh: 1011.")

        else:
            try:
                result = process_encryption(
                    plaintext,
                    seed
                )

                st.success("Enkripsi berhasil!")

                st.write("### Proses Enkripsi")

                for step in result:
                    st.write(
                        f"**Tahap {step['Tahap']} — {step['Proses']}**"
                    )
                    st.code(step["Hasil"])

            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")

    st.divider()

    # =========================
    # DEKRIPSI
    # =========================

    st.subheader("🔓 Dekripsi")

    ciphertext_hex = st.text_area(
        "Masukkan Ciphertext HEX",
        placeholder="Contoh: 4f2a8b..."
    )

    decrypt_seed = st.text_input(
        "Seed LFSR",
        placeholder="Masukkan seed yang sama",
        max_chars=4,
        key="decrypt_seed"
    )

    if st.button("Dekripsi", use_container_width=True):

        if not ciphertext_hex:
            st.warning("Masukkan ciphertext HEX terlebih dahulu.")

        elif not decrypt_seed:
            st.warning("Masukkan seed LFSR terlebih dahulu.")

        elif (
            len(decrypt_seed) != 4
            or any(bit not in "01" for bit in decrypt_seed)
        ):
            st.warning("Seed harus terdiri dari 4 bit, contoh: 1011.")

        else:

            try:

                result = process_decryption(
                    ciphertext_hex,
                    decrypt_seed
                )

                st.success("Dekripsi berhasil!")

                for step in result:
                    st.write(
                        f"**Tahap {step['Tahap']} — {step['Proses']}**"
                    )
                    st.code(step["Hasil"])

            except Exception as e:
                st.error(f"Dekripsi gagal: {e}")

    st.divider()

    with st.expander("📖 Lihat Proses Algoritma"):
        st.markdown(streamCipherNotes)


# =========================
# SUPER ENCRYPTION
# =========================

elif menu == "Super Encryption":

    st.header("Super Encryption")

    st.write(
        "Super Encryption menggabungkan beberapa algoritma kriptografi "
        "dengan urutan yang dapat ditentukan oleh pengguna."
    )

    st.divider()

    # =========================
    # SESSION STATE
    # =========================

    if "super_algorithms" not in st.session_state:
        st.session_state.super_algorithms = [
            "Caesar",
            "Rail Fence",
            "Stream",
            "AES"
        ]

    if "super_ciphertext" not in st.session_state:
        st.session_state.super_ciphertext = ""

    if "super_process" not in st.session_state:
        st.session_state.super_process = []

    if "super_aes_key" not in st.session_state:
        st.session_state.super_aes_key = None

    if "super_aes_nonce" not in st.session_state:
        st.session_state.super_aes_nonce = None

    if "super_aes_tag" not in st.session_state:
        st.session_state.super_aes_tag = None

    # =========================
    # PILIH ALGORITMA
    # =========================

    st.subheader("1. Pilih Algoritma")

    selected_algorithms = st.multiselect(
        "Pilih algoritma:",
        ["Caesar", "Rail Fence", "Stream", "AES"],
        default=st.session_state.super_algorithms
    )

    if len(selected_algorithms) < 2:

        st.warning(
            "Pilih minimal 2 algoritma."
        )

    elif len(selected_algorithms) > 4:

        st.warning(
            "Maksimal 4 algoritma."
        )

    # Sinkronisasi algoritma yang dipilih
    current_order = [
        alg
        for alg in st.session_state.super_algorithms
        if alg in selected_algorithms
    ]

    for alg in selected_algorithms:

        if alg not in current_order:
            current_order.append(alg)

    st.session_state.super_algorithms = current_order

    # =========================
    # URUTAN ALGORITMA
    # =========================

    st.subheader("2. Urutan Algoritma")

    if selected_algorithms:

        st.write("Urutan proses enkripsi:")

        for i, algorithm in enumerate(
            st.session_state.super_algorithms
        ):

            col1, col2, col3 = st.columns(
                [5, 1, 1]
            )

            with col1:

                st.write(
                    f"**{i + 1}. {algorithm}**"
                )

            with col2:

                if st.button(
                    "⬆️",
                    key=f"super_up_{algorithm}"
                ):

                    if i > 0:

                        algorithms = (
                            st.session_state.super_algorithms
                        )

                        algorithms[i], algorithms[i - 1] = (
                            algorithms[i - 1],
                            algorithms[i]
                        )

                        st.session_state.super_algorithms = (
                            algorithms
                        )

                        st.rerun()

            with col3:

                if st.button(
                    "⬇️",
                    key=f"super_down_{algorithm}"
                ):

                    algorithms = (
                        st.session_state.super_algorithms
                    )

                    if i < len(algorithms) - 1:

                        algorithms[i], algorithms[i + 1] = (
                            algorithms[i + 1],
                            algorithms[i]
                        )

                        st.session_state.super_algorithms = (
                            algorithms
                        )

                        st.rerun()

    st.divider()

    # =========================
    # PARAMETER
    # =========================

    st.subheader("3. Parameter Algoritma")

    caesar_key = 3
    rail_count = 3
    stream_seed = "1011"

    # Caesar
    if "Caesar" in st.session_state.super_algorithms:

        caesar_key = st.number_input(
            "Caesar Key",
            min_value=1,
            max_value=25,
            value=3,
            key="super_caesar_key"
        )

    # Rail Fence
    if "Rail Fence" in st.session_state.super_algorithms:

        rail_count = st.number_input(
            "Jumlah Rail",
            min_value=2,
            max_value=20,
            value=3,
            key="super_rail_count"
        )

    # Stream
    if "Stream" in st.session_state.super_algorithms:

        stream_seed = st.text_input(
            "Seed LFSR",
            value="1011",
            max_chars=4,
            key="super_stream_seed"
        )

        if (
            len(stream_seed) != 4
            or any(bit not in "01" for bit in stream_seed)
        ):

            st.warning(
                "Seed harus terdiri dari 4 bit, contoh: 1011."
            )

    # AES
    if "AES" in st.session_state.super_algorithms:

        st.write(
            "AES menggunakan AES-256-GCM."
        )

        if st.session_state.super_aes_key is not None:

            st.write("AES Key:")

            st.code(
                base64.b64encode(
                    st.session_state.super_aes_key
                ).decode("utf-8")
            )

    st.divider()

    # =========================
    # ENKRIPSI
    # =========================

    st.subheader("🔐 Enkripsi")

    super_plaintext = st.text_area(
        "Masukkan plaintext",
        placeholder="Contoh: INFORMATIKA UPN",
        key="super_plaintext"
    )

    if st.button(
        "🔒 Enkripsi Super",
        use_container_width=True
    ):

        algorithms = (
            st.session_state.super_algorithms
        )

        if len(algorithms) < 2:

            st.warning(
                "Pilih minimal 2 algoritma."
            )

        elif not super_plaintext:

            st.warning(
                "Masukkan plaintext terlebih dahulu."
            )

        elif (
            "Stream" in algorithms
            and (
                len(stream_seed) != 4
                or any(bit not in "01" for bit in stream_seed)
            )
        ):

            st.warning(
                "Seed LFSR harus terdiri dari 4 bit."
            )

        else:

            try:

                (
                    ciphertext,
                    process,
                    aes_key,
                    aes_nonce,
                    aes_tag
                ) = super_encrypt(
                    super_plaintext,
                    algorithms,
                    caesar_key=caesar_key,
                    rail_count=rail_count,
                    stream_seed=stream_seed
                )

                st.session_state.super_ciphertext = (
                    ciphertext
                )

                st.session_state.super_process = (
                    process
                )

                st.session_state.super_aes_key = (
                    aes_key
                )

                st.session_state.super_aes_nonce = (
                    aes_nonce
                )

                st.session_state.super_aes_tag = (
                    aes_tag
                )

                st.success(
                    "Super Encryption berhasil!"
                )

            except Exception as e:

                st.error(
                    f"Enkripsi gagal: {e}"
                )

    # =========================
    # HASIL ENKRIPSI
    # =========================

    if st.session_state.super_ciphertext:

        st.subheader(
            "Hasil Super Encryption"
        )

        st.code(
            st.session_state.super_ciphertext
        )

        st.write(
            "Urutan algoritma:"
        )

        st.write(
            " → ".join(
                st.session_state.super_algorithms
            )
        )

        # Informasi AES
        if "AES" in st.session_state.super_algorithms:

            st.write("AES Nonce:")

            st.code(
                st.session_state.super_aes_nonce
            )

            st.write(
                "AES Authentication Tag:"
            )

            st.code(
                st.session_state.super_aes_tag
            )

        # Proses algoritma
        with st.expander(
            "📖 Lihat Proses Super Encryption"
        ):

            for i, step in enumerate(
                st.session_state.super_process
            ):

                st.write(
                    f"**Tahap {i}: "
                    f"{step['algorithm']}**"
                )

                st.code(
                    str(step["result"])
                )

    st.divider()

    # =========================
    # DEKRIPSI
    # =========================

    st.subheader("🔓 Dekripsi")

    super_ciphertext_input = st.text_area(
        "Masukkan ciphertext",
        placeholder=(
            "Masukkan ciphertext hasil "
            "Super Encryption"
        ),
        key="super_ciphertext_input"
    )

    if "AES" in st.session_state.super_algorithms:

        st.info(
            "Untuk dekripsi AES, gunakan AES Key, "
            "Nonce, dan Authentication Tag "
            "yang diperoleh saat enkripsi."
        )

    if st.button(
        "🔓 Dekripsi Super",
        use_container_width=True
    ):

        algorithms = (
            st.session_state.super_algorithms
        )

        if len(algorithms) < 2:

            st.warning(
                "Pilih minimal 2 algoritma."
            )

        elif not super_ciphertext_input:

            st.warning(
                "Masukkan ciphertext terlebih dahulu."
            )

        elif (
            "Stream" in algorithms
            and (
                len(stream_seed) != 4
                or any(bit not in "01" for bit in stream_seed)
            )
        ):

            st.warning(
                "Seed LFSR harus terdiri dari 4 bit."
            )

        elif (
            "AES" in algorithms
            and (
                st.session_state.super_aes_key is None
                or st.session_state.super_aes_nonce is None
                or st.session_state.super_aes_tag is None
            )
        ):

            st.warning(
                "Data AES untuk dekripsi belum tersedia. "
                "Lakukan enkripsi terlebih dahulu."
            )

        else:

            try:

                plaintext, decrypt_process = (
                    super_decrypt(
                        super_ciphertext_input,
                        algorithms,
                        caesar_key=caesar_key,
                        rail_count=rail_count,
                        stream_seed=stream_seed,
                        aes_key=(
                            st.session_state.super_aes_key
                        ),
                        aes_nonce=(
                            st.session_state.super_aes_nonce
                        ),
                        aes_tag=(
                            st.session_state.super_aes_tag
                        )
                    )
                )

                st.success(
                    "Super Decryption berhasil!"
                )

                st.write("Plaintext:")

                st.code(
                    plaintext
                )

                with st.expander(
                    "📖 Lihat Proses Super Decryption"
                ):

                    for i, step in enumerate(
                        decrypt_process
                    ):

                        st.write(
                            f"**Tahap {i}: "
                            f"{step['algorithm']}**"
                        )

                        st.code(
                            str(step["result"])
                        )

            except Exception as e:

                st.error(
                    f"Dekripsi gagal: {e}"
                )