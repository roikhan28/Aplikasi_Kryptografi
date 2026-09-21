import streamlit as st

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

# menu = st.sidebar.radio(
#     "Pilih Algoritma",
#     [
#         "1. Caesar Cipher",
#         "2. Rail Fence Cipher",
#         "3. AES",
#         "4. RSA",
#         "5. Super Encryption"
#     ]
# )

if menu == "Rail Fence Cipher":

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

elif menu == "Caesar Cipher":
    
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