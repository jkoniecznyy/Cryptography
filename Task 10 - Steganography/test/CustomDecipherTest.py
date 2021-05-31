import unittest
from src.CustomDecipher import CustomDecipher
from src.CustomCipher import CustomCipher


class CustomDecipherTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cd = CustomDecipher()
        cls.cc = CustomCipher()

    def testCezarDecipher(self):
        text = 'meyyacegikmoqsuwzbdfhjlnprtvx'
        result = self.cd.cezarDecipher(text)
        self.assertEqual('acegikmoqsuwybdfhjlnprtvxz', result)

    def testTranspositionDecipher(self):
        text = 'acegikmoqsuwybdfhjlnprtvxz'
        result = CustomDecipher.transpositionDecipher(text, 2)
        self.assertEqual('abcdefghijklmnopqrstuvwxyz', result)
