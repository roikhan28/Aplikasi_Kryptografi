from caesar import (
    caesar_encrypt,
    caesar_decrypt
)

from rail_fence import (
    railFenceEncrypt,
    railFenceDecrypt
)

from stream import (
    encrypt as stream_encrypt,
    decrypt as stream_decrypt
)

from block import (
    generate_key,
    aesencrypt,
    aesdecrypt
)


def super_encrypt(
    text,
    algorithms,
    caesar_key=3,
    rail_count=3,
    stream_seed="1011",
    aes_key=None
):
    result = text
    process = []

    aes_nonce = None
    aes_tag = None

    process.append({
        "algorithm": "Plaintext",
        "result": result
    })

    for algorithm in algorithms:

        if algorithm == "Caesar":

            result = caesar_encrypt(
                result,
                caesar_key
            )

        elif algorithm == "Rail Fence":

            result = railFenceEncrypt(
                result,
                rail_count
            )

        elif algorithm == "Stream":

            stream_result = stream_encrypt(
                result,
                stream_seed
            )

            result = stream_result["ciphertext_hex"]

        elif algorithm == "AES":

            if aes_key is None:
                aes_key = generate_key()

            aes_nonce, ciphertext, aes_tag = aesencrypt(
                result,
                aes_key
            )

            result = ciphertext

        else:
            raise ValueError(
                f"Algoritma tidak dikenal: {algorithm}"
            )

        process.append({
            "algorithm": algorithm,
            "result": result
        })

    return (
        result,
        process,
        aes_key,
        aes_nonce,
        aes_tag
    )


def super_decrypt(
    text,
    algorithms,
    caesar_key=3,
    rail_count=3,
    stream_seed="1011",
    aes_key=None,
    aes_nonce=None,
    aes_tag=None
):
    result = text
    process = []

    process.append({
        "algorithm": "Ciphertext",
        "result": result
    })

    for algorithm in reversed(algorithms):

        if algorithm == "AES":

            if aes_key is None:
                raise ValueError(
                    "AES key belum tersedia."
                )

            if aes_nonce is None or aes_tag is None:
                raise ValueError(
                    "Nonce dan authentication tag AES "
                    "belum tersedia."
                )

            result = aesdecrypt(
                result,
                aes_key,
                aes_nonce,
                aes_tag
            )

        elif algorithm == "Stream":

            stream_result = stream_decrypt(
                result,
                stream_seed
            )

            result = stream_result["plaintext"]

        elif algorithm == "Rail Fence":

            result = railFenceDecrypt(
                result,
                rail_count
            )

        elif algorithm == "Caesar":

            result = caesar_decrypt(
                result,
                caesar_key
            )

        else:
            raise ValueError(
                f"Algoritma tidak dikenal: {algorithm}"
            )

        process.append({
            "algorithm": algorithm,
            "result": result
        })

    return result, process