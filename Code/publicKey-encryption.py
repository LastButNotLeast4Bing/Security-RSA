import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

# msg = "Guess who I am"
msg = open('msg.txt','r').read()

# 读取文件中的公钥
key = open('public.pem').read()
publickey = RSA.importKey(key)

# 进行加密
pk = PKCS1_v1_5.new(publickey)
encrypt_text = pk.encrypt(msg.encode())

# 加密通过base64进行编码
result = base64.b64encode(encrypt_text)
with open('publicKey-encryption.txt','wb') as f:
    f.write(result)
print(result)