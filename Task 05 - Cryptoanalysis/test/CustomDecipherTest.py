import unittest
from src.CustomDecipher import CustomDecipher


class CustomDecipherTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cd = CustomDecipher()

    def testHomophonicDecipher(self):
        text = '💍🥩🛌👉👑🧳'
        result = self.cd.homophonicDecipher(text)
        self.assertEqual(6, len(result))

    def testHomophonicDecipherZero(self):
        text = 'abcdefghijklmnopqrstuvwxyz'
        result = self.cd.homophonicDecipher(text)
        self.assertEqual(0, len(result))

    def testTranspositionDecipher(self):
        text = 'acegikmoqsuwybdfhjlnprtvxz'
        result = CustomDecipher.transpositionDecipher(text, 2)
        self.assertEqual('abcdefghijklmnopqrstuvwxyz', result)
