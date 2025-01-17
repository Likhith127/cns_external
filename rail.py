def encryptRailFence(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    dir_down, row, col = False, 0, 0

    for char in text:
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = char
        col += 1
        row += 1 if dir_down else -1

    result = [rail[i][j] for i in range(key) for j in range(len(text)) if rail[i][j] != '\n']
    return "".join(result)
def decryptRailFence(cipher, key):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    dir_down, row, col = None, 0, 0

    for _ in cipher:
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result, row, col = [], 0, 0
    for _ in cipher:
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        if rail[row][col] != '*' and rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1
        row += 1 if dir_down else -1
    return "".join(result)
encrypted_message = encryptRailFence("attack at once", 2)
print(encrypted_message)
print(decryptRailFence(encrypted_message, 2))