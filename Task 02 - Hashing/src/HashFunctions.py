import hashlib


class HashFunctions:

    def __init__(self):
        pass

    # Not all algorithms from algorithms_available are ready to use
    # so I used the guaranteed algorithms
    @staticmethod
    def getAlgorithmNames():
        return sorted(hashlib.algorithms_guaranteed)

    @staticmethod
    def blake2bHashing(cleartext: bytes) -> str:
        blake2b = hashlib.blake2b()
        blake2b.update(cleartext)
        return blake2b.hexdigest()

    @staticmethod
    def blake2sHashing(cleartext: bytes) -> str:
        blake2s = hashlib.blake2s()
        blake2s.update(cleartext)
        return blake2s.hexdigest()

    @staticmethod
    def md5Hashing(cleartext: bytes) -> str:
        md5 = hashlib.md5()
        md5.update(cleartext)
        return md5.hexdigest()

    @staticmethod
    def sha1Hashing(cleartext: bytes) -> str:
        sha1 = hashlib.sha1()
        sha1.update(cleartext)
        return sha1.hexdigest()

    @staticmethod
    def sha224Hashing(cleartext: bytes) -> str:
        sha224 = hashlib.sha224()
        sha224.update(cleartext)
        return sha224.hexdigest()

    @staticmethod
    def sha256Hashing(cleartext: bytes) -> str:
        sha256 = hashlib.sha256()
        sha256.update(cleartext)
        return sha256.hexdigest()

    @staticmethod
    def sha384Hashing(cleartext: bytes) -> str:
        sha384 = hashlib.sha384()
        sha384.update(cleartext)
        return sha384.hexdigest()

    @staticmethod
    def sha3224Hashing(cleartext: bytes) -> str:
        sha3224 = hashlib.sha3_224()
        sha3224.update(cleartext)
        return sha3224.hexdigest()

    @staticmethod
    def sha3256Hashing(cleartext: bytes) -> str:
        sha3256 = hashlib.sha3_256()
        sha3256.update(cleartext)
        return sha3256.hexdigest()

    @staticmethod
    def sha3384Hashing(cleartext: bytes) -> str:
        sha3384 = hashlib.sha3_384()
        sha3384.update(cleartext)
        return sha3384.hexdigest()

    @staticmethod
    def sha3512Hashing(cleartext: bytes) -> str:
        sha3512 = hashlib.sha3_512()
        sha3512.update(cleartext)
        return sha3512.hexdigest()

    @staticmethod
    def sha512Hashing(cleartext: bytes) -> str:
        sha512 = hashlib.sha512()
        sha512.update(cleartext)
        return sha512.hexdigest()

    @staticmethod
    def shake128Hashing(cleartext: bytes, length: int) -> str:
        shake128 = hashlib.shake_128()
        shake128.update(cleartext)
        return shake128.hexdigest(length)

    @staticmethod
    def shake256Hashing(cleartext: bytes, length: int) -> str:
        shake256 = hashlib.shake_256()
        shake256.update(cleartext)
        return shake256.hexdigest(length)

    @staticmethod
    def fileSha256Hashing(path: str) -> str:
        sha256 = hashlib.sha256()

        with open(path, 'rb') as file:
            while True:
                chunk = file.read(sha256.block_size)
                if not chunk:
                    break
                sha256.update(chunk)

        return sha256.hexdigest()
