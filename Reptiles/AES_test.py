from Crypto.Cipher import AES

# 加密
obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
# 相当于service和client约定的口令，有了这个口令才能进行加密和解密操作

'''
  "This is a key123"    为key,长度有着严格的要求,必须为16,24或32位
  "This is an VI456"    为VI,长度要求更加严格,只能为16位
'''

print(obj)
message = "The answer is no"
ciphertext = obj.encrypt(message)      # 通过encrypt加密字符串
print(ciphertext)


# =================================================== #
# 解密
obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
print(obj2)
# 如果key错误,那无法得到正确的加密字符串
# 如果VI错误,那无法得到正确的加密之前的字符串
s = obj2.decrypt(ciphertext)       # 通过decrypt解密字符串
print(s)

