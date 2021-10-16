import hashlib
#hash_object = hashlib.md5(b'Hello world') #b changes string to bytes
#print (hash_object.hexdigest())

mystring = raw_input('Enter String to hash: ')

i = 0
hash_object = hashlib.md5(mystring.encode()+ str(i).encode()) #encode change string to bytes
while hash_object.hexdigest()[0:6] != "000000":
    hash_object = hashlib.md5(mystring.encode()+ str(i+1).encode())
    i += 1
    
print i