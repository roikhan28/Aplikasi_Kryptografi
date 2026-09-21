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