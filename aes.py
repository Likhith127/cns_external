from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
def aes_encrypt_decrypt(data, key, mode='encrypt'):
    cipher = AES.new(key, AES.MODE_ECB)
    if mode == 'encrypt':
        encrypted = cipher.encrypt(pad(data.encode(), AES.block_size))
        return encrypted
    else:
        decrypted = unpad(cipher.decrypt(data), AES.block_size)
        return decrypted.decode()
key = b"thisisaverysecretkey!!"[:16]
data = "SecretMessage"
encrypted = aes_encrypt_decrypt(data, key, 'encrypt')
decrypted = aes_encrypt_decrypt(encrypted, key, 'decrypt')
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)