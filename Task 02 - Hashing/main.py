import hashlib
import timeit

content = b'Awwwhh jyeaaah! - Bob Marley on hash.'

print(timeit.timeit("-".join(str(n) for n in range(100)), number=100))
print(timeit.timeit("-".join(str(n) for n in range(100)), number=10000))

print(sorted(hashlib.algorithms_available))

md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha224 = hashlib.sha224()
sha256 = hashlib.sha256()
sha384 = hashlib.sha384()
sha512 = hashlib.sha512()
list_hash_objects = [md5, sha1, sha224, sha256, sha384, sha512]

for hash_object in list_hash_objects:
    hash_object.update(content)
    print('{}: {}'.format(hash_object.name, hash_object.hexdigest()))
