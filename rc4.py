def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S
def PRGA(S, n):
    i = j = 0
    key_stream = []
    for _ in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        key_stream.append(K)
    return key_stream
def rc4(key, plaintext):
    key = [ord(c) for c in key]
    S = KSA(key)
    key_stream = PRGA(S, len(plaintext))
    ciphertext = ''.join([chr(ord(p) ^ k) for p, k in zip(plaintext, key_stream)])
    return ciphertext
key = "secretkey"
plaintext = "hello world"
ciphertext = rc4(key, plaintext)
print("Ciphertext:", ciphertext)
decrypted_text = rc4(key, ciphertext)
print("Decrypted:", decrypted_text)