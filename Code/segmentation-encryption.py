import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

def cipher(msg):
    """
    公钥加密
    :param msg: 要加密内容
    :return:  加密之后的密文
    """
    # 获取公钥
    key = open('public.pem').read()
    publickey = RSA.importKey(key)
    # 分段加密
    pk = PKCS1_v1_5.new(publickey)
    encrypt_text = []
    for i in range(0,len(msg),100):
        cont = msg[i:i+100]
        encrypt_text.append(pk.encrypt(cont.encode()))
    # 加密完进行拼接
    cipher_text = b''.join(encrypt_text)
    # base64进行编码
    result = base64.b64encode(cipher_text)
    # print(result.decode())
    return result.decode()

def decrypt(msg):
    """
    私钥进行解密
    :param msg: 密文：字符串类型
    :return:  解密之后的内容
    """
    # base64解码
    msg = base64.b64decode(msg)
    # 获取私钥
    privatekey = open('private.pem').read()
    rsakey = RSA.importKey(privatekey)
    cipher =  PKCS1_v1_5.new(rsakey)
    # 进行解密
    text = []
    for i in range(0,len(msg),128):
        cont = msg[i:i+128]
        text.append(cipher.decrypt(cont,1))
    text = b''.join(text)
    # print(text.decode())
    return text.decode()