import hashlib
print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)
hashObj = hashlib.md5(b'Hello World')
print(hashObj.digest())
print('hello World'.encode())
print(hash("hello"))