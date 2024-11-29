from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Generate a random 24-byte key for 3DES
key = get_random_bytes(24)  # 24 bytes for 3DES key

# Create a new DES3 cipher in ECB mode
cipher = DES3.new(key, DES3.MODE_ECB)

# Define the plaintext message to be encrypted
plaintext = b"This is a secret message."

# Encrypt the message
# Padding to make it a multiple of 8 bytes
padded_text = pad(plaintext, DES3.block_size)
ciphertext = cipher.encrypt(padded_text)
print("Encrypted:", ciphertext)

# Decrypt the message
decrypted_padded_text = cipher.decrypt(ciphertext)
decrypted_text = unpad(decrypted_padded_text, DES3.block_size)
print("Decrypted:", decrypted_text.decode('utf-8'))