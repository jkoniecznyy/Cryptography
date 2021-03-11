import unittest
from src.HashFunctions import HashFunctions


class HashTest(unittest.TestCase):

    def testGetAlgorithmNames(self):
        algorithms = ['blake2b', 'blake2s', 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha3_224', 'sha3_256',
                      'sha3_384', 'sha3_512', 'sha512', 'shake_128', 'shake_256']
        self.assertEqual(HashFunctions.getAlgorithmNames(), algorithms)

    def testBlake2bHashing(self):
        result = '488f88b4872bbe1aeba631d63184b68e74e207d510eb34b72ff363ad9433175e9b67d4c8ff582cd043848aef6a398' \
                 'fd08b4898112c455e069596015983844e7d'
        self.assertEqual(HashFunctions.blake2bHashing(b'very important message'), result)

    def testBlake2sHashing(self):
        result = '6bb2709b5f3e7648d464b5f2fd0abf055e153bb8185a95015907b445bbec21af'
        self.assertEqual(HashFunctions.blake2sHashing(b'very important message'), result)

    def testMd5Hashing(self):
        result = '499059389a3fcbc879478796a87d00c1'
        self.assertEqual(HashFunctions.md5Hashing(b'very important message'), result)

    def testSha1Hashing(self):
        result = '4072827108bdf3d2f807c83981348e275840cadb'
        self.assertEqual(HashFunctions.sha1Hashing(b'very important message'), result)

    def testFileSha256Hashing(self):
        path = r'D:\Siema\Pobrane\ubuntu-20.04.2.0-desktop-amd64.iso'
        self.assertEqual(HashFunctions.fileSha256Hashing(path),
                         '93bdab204067321ff131f560879db46bee3b994bf24836bb78538640f689e58f')
