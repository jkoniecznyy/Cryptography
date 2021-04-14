import unittest
from src.CustomCipher import CustomCipher


class CustomCipherTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cc = CustomCipher()
        cls.testText = 'minecraftisnotoriousinthegamingworldforhavingabsolutelynoplotlinenovariationinga' \
                       'meplayandnoaimatallallinallitmakesthegameasaboutasinterestingasthemathhomeworkmo' \
                       'stofitsplayersshouldbedoinginsteadofplayingit'

    def testPrepareStr(self):
        text = 'Minecraft is notorious in the gaming world for having absolutely no plot line,' \
               ' no variation in gameplay and no aim at all. All in all, it makes the game as about' \
               ' as interesting as the math homework most of its players should be doing instead of playing it.'
        result = CustomCipher.prepareStr(text)
        self.assertEqual(self.testText, result)

    def testCezarMove(self):
        text = 'abcdefghijklmnopqrstuvwxyz'
        result = CustomCipher.cezarMove(text, 4)
        self.assertEqual('efghijklmnopqrstuvwxyzabcd', result)

    def testTranspositionCipher(self):
        text = 'abcdefghijklmnopqrstuvwxyz'
        result = CustomCipher.transpositionCipher(text, 2)
        self.assertEqual('acegikmoqsuwybdfhjlnprtvxz', result)

    def testTranspositionDecipher(self):
        text = 'acegikmoqsuwybdfhjlnprtvxz'
        result = CustomCipher.transpositionDecipher(text, 2)
        self.assertEqual('abcdefghijklmnopqrstuvwxyz', result)
