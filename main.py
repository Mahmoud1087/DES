from Crypto.Cipher import DES
import base64

def encrypt_ecb(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(plaintext)

def encrypt_cbc(plaintext, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    return cipher.encrypt(plaintext)

def read_plaintext_file(filename):
    with open(filename, 'rb') as file:
        return file.read()

def write_ciphertext_file(filename, ciphertext):
    with open(filename, 'wb') as file:
        file.write(ciphertext)

plaintext_file = 'plaintext.txt'
key = b'\x00\x11\x22\x33\x44\x55\x66\x77'
iv = b'\x88\x99\xaa\xbb\xcc\xdd\xee\xff'

plaintext = read_plaintext_file(plaintext_file)

cipher_ecb = DES.new(key, DES.MODE_ECB)
plaintext_padded = plaintext + bytes((8 - len(plaintext) % 8) * chr(8 - len(plaintext) % 8), 'utf-8')
ciphertext_ecb = cipher_ecb.encrypt(plaintext_padded)
ciphertext_ecb = base64.b64encode(ciphertext_ecb)

write_ciphertext_file('ciphertext_ecb.txt', ciphertext_ecb)

cipher_cbc = DES.new(key, DES.MODE_CBC, iv)
plaintext_padded = plaintext + bytes((8 - len(plaintext) % 8) * chr(8 - len(plaintext) % 8), 'utf-8')
ciphertext_cbc = cipher_cbc.encrypt(plaintext_padded)
ciphertext_cbc = base64.b64encode(ciphertext_cbc)

write_ciphertext_file('ciphertext_cbc.txt', ciphertext_cbc)
