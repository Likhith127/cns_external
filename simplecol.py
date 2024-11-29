def columnar_encrypt(text, key):
    n = len(key)
    columns = sorted(range(n), key=lambda x: key[x])
    matrix = [text[i:i + n] for i in range(0, len(text), n)]
    while len(matrix[-1]) < n: # Padding
        matrix[-1] += 'X'
    encrypted = ''.join([''.join(row[col] for row in matrix) for col in columns])
    return encrypted
def columnar_decrypt(text, key):
    n = len(key)
    num_rows = len(text) // n
    columns = sorted(range(n), key=lambda x: key[x])
    reverse_columns = sorted(range(n), key=lambda x: columns[x])
    cols = [text[i * num_rows:(i + 1) * num_rows] for i in range(n)]
    matrix = [''.join(cols[col][row] for col in reverse_columns) for row in range(num_rows)]
    return ''.join(matrix).rstrip('X')
key = [3, 1, 4, 2]
text = "HELLO WORLD"
encrypted = columnar_encrypt(text, key)
decrypted = columnar_decrypt(encrypted, key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)