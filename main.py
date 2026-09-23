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
    if st.button("RSA", use_container_width=True):
        st.session_state.menu = "RSA"

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