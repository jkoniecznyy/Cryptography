import unittest
from src.Symmetric import Symmetric


class SymmetricTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.symmetric = Symmetric()

    def testGenerateKey(self):
        result = self.symmetric.generateKey()
        self.assertIsNotNone(result)

    def testSetKey(self):
        result = self.symmetric.setKey('566857386e487644384664714c3057424d4c6e'
                                       '754c6334746d4a5472594567784a344d695a4456544f4d593d')
        self.assertTrue(result)

    def testEncryptAndDecrypt(self):
        self.symmetric.setKey('566857386e487644384664714c3057424d4c6e754c63347'
                              '46d4a5472594567784a344d695a4456544f4d593d')
        encrypted = self.symmetric.encrypt('Eragon Bromsson')
        decrypted = self.symmetric.decrypt(encrypted)
        self.assertEqual(decrypted, 'Eragon Bromsson')


if __name__ == '__main__':
    unittest.main()
