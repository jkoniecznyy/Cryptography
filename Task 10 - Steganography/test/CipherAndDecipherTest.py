import unittest
from src.CustomDecipher import CustomDecipher
from src.CustomCipher import CustomCipher


class CustomDecipherTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cd = CustomDecipher()
        cls.cc = CustomCipher()
        cls.text = 'aabcdefghijkklmnopqrstuvwxyzz'

    def testCipherAndDecipher(self):
        ciphered = self.cc.cipher(self.text)
        deciphered = self.cd.decipher(ciphered)
        self.assertEqual(self.text, deciphered)

    def testCipherPreviewAndDecipher(self):
        ciphered = self.cc.cipherPreview(self.text)
        deciphered = self.cd.decipher(ciphered)
        self.assertEqual(self.text, deciphered)

    def testCezarCipherAndDecipher(self):
        ciphered = self.cc.cezarCipher(self.text)
        deciphered = self.cd.cezarDecipher(ciphered)
        self.assertEqual(self.text, deciphered)

    def testTranspositionCipherAndDecipher(self):
        ciphered = self.cc.transpositionCipher(self.text, 6)
        deciphered = self.cd.transpositionDecipher(ciphered, 6)
        self.assertEqual(self.text, deciphered)

    def testHomophonicCipherAndDecipher(self):
        ciphered = self.cc.homophonicCipher(self.text)
        deciphered = self.cd.homophonicDecipher(ciphered)
        self.assertEqual(self.text, deciphered)
