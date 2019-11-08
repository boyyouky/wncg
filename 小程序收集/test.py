import rsa
import base64
publickeypath = r"C:\Users\ASUS\Desktop\数据\data-public.pem"
privatekeypath =r"C:\Users\ASUS\Desktop\数据\data-private.pem"
with open(publickeypath, 'r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
with open(privatekeypath, 'r') as f:
    prikey = rsa.PrivateKey.load_pkcs1(f.read().encode())

def encrypt(message):
    crypto = rsa.encrypt(message.encode(), pubkey)
    return base64.b64encode(crypto).decode()
def decrypt(crypto):
    message = rsa.decrypt(base64.b64decode(crypto), prikey).decode()
    return message
