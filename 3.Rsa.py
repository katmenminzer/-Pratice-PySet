import base64
import os
import rsa

def main():
    def encrypt(_publicKey, plainTxt):
        return rsa.encrypt(plainTxt.encode(), _publicKey)

    def decrypt(_privateKey, cipherTxt):
        return rsa.decrypt(cipherTxt, _privateKey)

    def test():
        publicK,privateK = rsa.newkeys(256)
        #publicKPEM = publicK.save_pkcs1().decode('utf8')
        #privateKPEM = privateK.save_pkcs1().decode('utf8')
        print(help(publicK))
        print(f'[public key]{publicK}')
        print(f'[private key]{privateK}')
        msg = '請支援收銀'

        ciphertext = encrypt(publicK, msg)
        ciphertext_b64 = base64.b64encode(ciphertext)

        print(f'[original string]{msg}')
        print(f'[encrypted byte]{ciphertext}')        
        print(f'[base64 encoded byte]{ciphertext_b64}')


        plaintext = decrypt(privateK, ciphertext)
        print(f'[after decrypted]{plaintext}') #解密後為byte
        
    test()

def customTest():    
    def encrypt(_publicKey, plainTxt):
        return rsa.encrypt(plainTxt.encode(), _publicKey)

    def decrypt(_privateKey, cipherTxt):
        return rsa.decrypt(cipherTxt, _privateKey)

    publicKey = rsa.PublicKey(58321134580384502674922031692525958638235264089135520070768376939805535085321, 65537)
    msg = 'Angus Die'
    ciphertext = encrypt(publicKey, msg)
    print(base64.b64encode(ciphertext))
    
    privateKey = rsa.PrivateKey(75127776959833086332968872051826991436444735849611726667714609504150294991943, 65537, 73140020955616375593976119497729794318289691351403958145998229247835068838465, 68674861388592143993180006873668416307489, 1093963284974505415815892940275523687)
    msg = 'dWUQSP2fIs9QrXu/7/ESYesgfYM2KbfBpHGsZYYXn/Q='
    msg = base64.b64decode(msg)
    print(msg)
    plaintext = decrypt(privateKey,msg)
    print(plaintext.decode())

"""
def keyGen():
    publicK,privateK = rsa.newkeys(256)
    print(f'[public key]{publicK.n}|{publicK.e}')
    print(f'[private key]{privateK.n}|{privateK.d}')
"""
   
#main()
#customDecrypt()
customTest()
