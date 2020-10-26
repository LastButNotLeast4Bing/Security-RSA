import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

# 密文
# msg = 'UtPyjyuiSa9gomZBDif8d6qENBJqnwdyA8R10k9+JuQr+M9co6FKOh7NRck27' \
#       'jnUJst4KXqno8wUnbgJSTG3s/+1xk6roy7otgWkXfwCQZWF3CI8t3nhrKXisPIGwc' \
#       '8aKWmP6t8VbL0ujrdUm2I8jPb6JVg+rlOmSca81mCvcM0='

msg = open('publicKey-encryption.txt','r').read()

# base64解码
msg = base64.b64decode(msg)

# 获取私钥
privatekey = open('private.pem').read()
rsakey = RSA.importKey(privatekey)

# 进行解密
cipher = PKCS1_v1_5.new(rsakey)
text = cipher.decrypt(msg,'DecryptError')

# 解密出来的是字节码格式，decode转换为字符串
with open('privateKey-encryption.txt','w') as f:
    f.write(text.decode())
print(text.decode())