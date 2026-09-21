import streamlit as st

from rail_fence import(
    railFenceEncrypt,
    railFenceDecrypt,
    railFenceProcess,
)

st.title("Aplikasi Enkripsi dan Dekripsi Kriptografi")


menu = st.radio(
    "Pilih Algoritma",
    [
        "1. Caesar Cipher",
        "2. Rail Fence Cipher",
        "3. AES",
        "4. RSA",
        "5. Super Encryption"
    ]
)

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

if menu == "2. Rail Fence Cipher":

    st.header("2. Rail Fence Cipher")

    st.write(
        "Rail Fence Cipher merupakan algoritma transposisi klasik "
        "yang menyusun plaintext secara zig-zag pada beberapa rail."
    )

    text = st.text_area(
        "Masukkan teks",
        placeholder="Contoh: WE ARE DISCOVERED"
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

        st.markdown("""
        **Proses Enkripsi:**

        1. Plaintext ditulis secara zig-zag.
        2. Penulisan dilakukan pada sejumlah rail.
        3. Setelah mencapai rail terakhir, arah berubah.
        4. Ciphertext dibentuk dengan membaca setiap rail dari atas ke bawah.

        **Contoh dengan 3 rail:**

        ```text
        WEAREDISCOVERED
        ```

        Disusun menjadi pola zig-zag:

        ```text
        W   E   D   C   V   R   D
         E R D S O E E
          A   I   C   O
        ```

        Kemudian karakter dibaca per rail untuk menghasilkan ciphertext.

        **Dekripsi:**

        Ciphertext disusun kembali berdasarkan pola zig-zag,
        kemudian dibaca mengikuti pola tersebut untuk mendapatkan plaintext.
        """)
