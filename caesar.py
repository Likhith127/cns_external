def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            result += char
    return result
def decrypt(text, shift):
    return encrypt(text, -shift)
text = "Hello, World!"
shift = 3
encrypted_text = encrypt(text, shift)
decrypted_text = decrypt(encrypted_text, shift)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)