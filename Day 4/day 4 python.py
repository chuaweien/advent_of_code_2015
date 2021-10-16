import hashlib

input = "ckczppom"
i = 0 
while True:
    base_hash = input + str(i)
    m = hashlib.md5(base_hash).hexdigest()
    if m[0:6] == "000000":
        break
    i+=1


print "Found it! i = " + str(i)