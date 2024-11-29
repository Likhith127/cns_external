import string
def create_substitution_dict(key):
    alphabet = string.ascii_uppercase
    key = key.upper()
    return {alphabet[i]: key[i] for i in range(len(alphabet))}
def encrypt(plaintext, key):
    substitution_dict = create_substitution_dict(key)
    ciphertext = ""
    for char in plaintext.upper():
        ciphertext += substitution_dict.get(char, char)
    return ciphertext
def decrypt(ciphertext, key):
    substitution_dict = create_substitution_dict(key)
    reverse_dict = {v: k for k, v in substitution_dict.items()}
    plaintext = ""
    for char in ciphertext.upper():
        plaintext += reverse_dict.get(char, char)
    return plaintext

key = "QWERTYUIOPASDFGHJKLZXCVBNM"
plaintext = "HELLO WORLD"
encrypted_text = encrypt(plaintext, key)
decrypted_text = decrypt(encrypted_text, key)
print("Plaintext:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)