

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt_decrypt(data, key, mode='encrypt'):
    des = DES.new(key, DES.MODE_ECB)
    if mode == 'encrypt':
        padded_data = pad(data.encode(), DES.block_size)  # Proper padding
        encrypted = des.encrypt(padded_data)
        return encrypted
    else:
        decrypted = des.decrypt(data)
        unpadded_data = unpad(decrypted, DES.block_size)
        return unpadded_data.decode()

key = b"abcdefgh"
data = "plaintext"
encrypted = des_encrypt_decrypt(data, key, 'encrypt')
decrypted = des_encrypt_decrypt(encrypted, key, 'decrypt')

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

