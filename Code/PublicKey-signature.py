from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Sig_pk
from Crypto.PublicKey import RSA
import base64

# 签名之前的内容
# name = "fuck"
name = open('tobesign.txt', 'r').read()

# 签名数据
# data="e6XD9UVveEKVDF6YWPy1yeqR8oYTCqpGG2bBHEAELpDrIofbimvkUoA" \
#      "hpJyOF1p4jCDaZMl0hpbD94afGI+LdsHwnYEnxbUAis2ucooFRPkedsk+4" \
#      "UR7naaMSuPq3kvLgdhB8ZEH9i1Avzw7fHT4rPdMroXfNljjHJud2GY67ss="

data = open('privateKey-signature.txt','r').read()

# base64解码
data = base64.b64decode(data)
# 获取公钥
key = open('public.pem').read()
rsakey = RSA.importKey(key)
# 将签名之前的内容进行hash处理
sha_name = SHA.new(name.encode())
# 验证签名
signer = Sig_pk.new(rsakey)
result = signer.verify(sha_name, data)
# 验证通过返回True   不通过返回False
print(result)