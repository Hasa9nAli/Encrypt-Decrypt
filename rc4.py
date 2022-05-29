from Crypto.Cipher import ARC4 as rc4cipher
import base64


def encryptRc4(data, key1):
    key = bytes(key1, encoding='utf-8')
    enc = rc4cipher.new(key)
    res = enc.encrypt(data.encode('utf-8'))
    res = base64.b64encode(res)
    res = str(res, 'utf8')
    return res


def decryptRc4(data, key1):
    data = base64.b64decode(data)
    key = bytes(key1, encoding='utf-8')
    enc = rc4cipher.new(key)
    res = enc.decrypt(data)
    res = str(res, 'utf8')
    return res

# data = input("enter the text : ")
# key = input("enter the key at lest 8 characters:  ")
#
# print(encrypt( data, key))
# res = encrypt(data,
# )
# print( decrypt(res , key))
