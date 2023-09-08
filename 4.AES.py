import base64
import os
import hashlib
import random

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from cryptography.fernet import Fernet


#8 digit

def autoGen():
    key = hashlib.sha256(b'TheColor').digest()
    iv = os.urandom(16)
    data = 'gogogo'.encode('utf8')
    ciphertext = encrypt(data,key,iv)
    print('Dynamic:|{0},{1}'.format(ciphertext, encrypted_b64 := base64.b64encode(ciphertext)))
    xd = base64.b64encode(ciphertext).decode()
    xd = base64.b64decode(xd)
    print(xd)
    plaintext = decrypt(xd,key,iv)
    print(plaintext)
    
def manualGen():
    key = hashlib.sha256(b'TheColor').digest()
    iv = b'0000000000000000'
    data = 'gogogo'.encode('utf8')
    ciphertext = encrypt(data,key,iv)
    print('Fixed:  |{0},{1}'.format(ciphertext, encrypted_b64 := base64.b64encode(ciphertext)))
    iv2 = b'0000000000000001'
    ciphertext = encrypt(data,key,iv2)
    print('Fixed2: |{0},{1}'.format(ciphertext, encrypted_b64 := base64.b64encode(ciphertext)))

def guessing():
    iv = b'0000000000000000'
    target = '5u1sGa9k6ZO/zUIDp+4Fz7N7dKQMUF/DT0AHtrRWJe8='
    target = base64.b64decode(target)
    for index in range(12000000, 20000000):
        try: 
            pw = f'{index:>08}'
            key = hashlib.sha256(pw.encode()).digest() # pwd -> shr256
            result = decrypt(target, key, iv).decode()
            print("cracker:{0}|{1}".format(pw, result))
            break
        except Exception as e:
            # print(index, e)
            pass

def encrypt(data, _key, _iv):
    c = AES.new(_key, AES.MODE_CBC, _iv)
    return c.encrypt(pad(data, AES.block_size))

def decrypt(data, _key, _iv):
    c = AES.new(_key, AES.MODE_CBC, _iv)
    return unpad(c.decrypt(data),AES.block_size)

def testA():
    guessing()

testA()
