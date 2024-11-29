from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
def blowfish_encrypt_decrypt(data, key, mode='encrypt'):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    if mode == 'encrypt':
        encrypted = cipher.encrypt(pad(data.encode(), Blowfish.block_size))
        return encrypted
    else:
        decrypted = unpad(cipher.decrypt(data), Blowfish.block_size)
        return decrypted.decode()
key = b"secretkey"
data = "HelloWorld"
encrypted = blowfish_encrypt_decrypt(data, key, 'encrypt')
decrypted = blowfish_encrypt_decrypt(encrypted, key, 'decrypt')
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)