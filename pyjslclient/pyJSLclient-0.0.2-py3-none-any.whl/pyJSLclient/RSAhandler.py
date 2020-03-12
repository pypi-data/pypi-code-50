# Released by 2runo

try:
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_v1_5
    from Crypto import Random
    from Crypto.Cipher import AES
except ImportError:
    from crypto.PublicKey import RSA
    from crypto.Cipher import PKCS1_v1_5
    from crypto import Random
    from crypto.Cipher import AES
import base64
import random
import os
import zlib


class AEScipher():  # 192bits AES(cbc)
    def __init__(self, key=b'R\\JG\x0c\x10R\x0eTO\x11VKW\\POA]\x11]\x0f\x06\x1cCW\x17\x00]\x03\x1bD', iv=b'_P\x18\x14\\G\x05RPOOZ\x11\x06]\x07'):
        self.key = key  # key (32bit)
        self.iv = iv  # iv (16bit)

        self.pad = lambda s: s + (AES.block_size - len(s.encode()) % AES.block_size) * chr(AES.block_size - len(s.encode()) % AES.block_size)  # padding
        self.unpad = lambda s: s[0:-ord(s[-1])]  # unpadding

        self.key,self.iv=eval(zlib.decompress(bytes(c ^ b'keyword'[i % 7] for i, c in enumerate(b'\x13\xf9\xf29\xc5^-F\xb31!\xe7!,9\xaa7\xdaC\xbdK!4\xf6\xb9;"1[\xea,?\xa4]6\xa3\xb1(?9\xba\xa88-\xb4\\\xa2?I!I0\xa2G<\xa9"\xb6z]\xba\xa6\xb0 ,4\xb9 ;\xb1\xbb\xb1X\xa4\xfb\xbeVO&\x1bv\xdfeI\x98'))).decode())

    def encrypt(self, msg):
        cipher = AES.new(self.key, AES.MODE_CBC, IV=self.iv)
        cryptogram = base64.b64encode(cipher.encrypt(self.pad(msg))).decode()
        return cryptogram

    def decrypt(self, cryptogram):
        if isinstance(cryptogram, str):
            cryptogram = cryptogram.encode()
        try:
            cipher = AES.new(self.key, AES.MODE_CBC, IV=self.iv)
            msg = cipher.decrypt(base64.b64decode(cryptogram)).decode()
            return self.unpad(msg)
        except:
            return ''


class RSAcipher:  # 2048bits RSA
    def __init__(self, generate=True, byte=4096):
        self.get_key()

        self.rsa = RSA.importKey(self.private_key)
        self.cipher = PKCS1_v1_5.new(self.rsa)

    def generate_key(self, byte=2048):
        # private key와 public key를 openssl로 생성한다.
        # 그러나 생성하는 데 시간이 오래 걸리므로 사용하지 않고,
        # 기존에 미리 생성해 뒀던 key를 불러와서 사용한다. (-> get_key)
        import OpenSSL
        k = OpenSSL.crypto.PKey()
        k.generate_key(OpenSSL.crypto.TYPE_RSA, byte)
        self.private_key = OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, k).decode()
        self.public_key = OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_PEM, k).decode()
        return self.private_key, self.public_key

    def get_key(self):
        # 기존에 미리 생성해 둔 key를 랜덤으로 골라서 사용한다.
        # 미리 생성해 둔 key가 없으면 새로 생성한다.
        try:
            certs = os.listdir("certs")
        except:
            os.mkdir("certs")
            certs = []
        if not certs:
            print("Generate RSA keys..")
            priv, pub = self.generate_key()
            with open("certs/key.private", 'w') as f:
                f.write(priv)
            with open("certs/key.public", 'w') as f:
                f.write(pub)
            certs = os.listdir("certs")
        keys = {}
        for cert in certs:
            try:
                with open('certs/' + cert, 'r') as f:
                    keys[cert.split('.')[0]].append(f.read())
            except:
                with open('certs/' + cert, 'r') as f:
                    keys[cert.split('.')[0]] = [f.read()]
        self.private_key, self.public_key = random.choice(list(keys.values()))

    def encrypt(self, msg):
        ciphertext = self.cipher.encrypt(msg.encode('utf8'))
        return base64.b64encode(ciphertext).decode('ascii')

    def decrypt(self, msg):
        ciphertext = base64.b64decode(msg.encode('ascii'))
        plaintext = self.cipher.decrypt(ciphertext, 13)
        try:
            return plaintext.decode('utf8')
        except AttributeError as err:
            return ''