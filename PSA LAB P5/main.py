# 5. Birthday Attack:
import hashlib
import os


hash = {}
while True:
    r1 = os.urandom(40)
    defdic = r1
    x = hashlib.md5(r1).hexdigest()[:10]
    if x in hash:
        print("Collision:", x)
        print(r1, ' ', x)
        print(hash[x], ' ', x)
        break
    else:
        hash[x] = r1
