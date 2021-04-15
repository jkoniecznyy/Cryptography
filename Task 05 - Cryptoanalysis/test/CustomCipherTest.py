import unittest
from src.CustomCipher import CustomCipher


class CustomCipherTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cc = CustomCipher()
        cls.text = 'minecraftisnotoriousinthegamingworldforhavingabsolutelynoplotlinenovariationinga' \
                   'meplayandnoaimatallallinallitmakesthegameasaboutasinterestingasthemathhomeworkmo' \
                   'stofitsplayersshouldbedoinginsteadofplayingit'

    def testPrepareStr(self):
        textMinecraft = 'Minecraft is notorious in the gaming world for having absolutely no plot line,' \
                        ' no variation in gameplay and no aim at all. All in all, it makes the game as about' \
                        ' as interesting as the math homework most of its players should be doing instead of ' \
                        'playing it.'
        result = CustomCipher.prepareStr(textMinecraft)
        self.assertEqual(self.text, result)

    def testCezarMove(self):
        expected = 'qmrigvejxmwrsxsvmsywmrxlikeqmrkasvphjsvlezmrkefwspyxipcrstpsxpmrirszevmexmsrmrkeqitpecerh' \
                   'rsemqexeppeppmreppmxqeoiwxlikeqiewefsyxewmrxiviwxmrkewxliqexllsqiasvoqswxsjmxwtpecivwwlsy' \
                   'phfihsmrkmrwxiehsjtpecmrkmx'
        result = CustomCipher.cezarMove(self.text, 4)
        self.assertEqual(expected, result)

    def testHomophonicCipher(self):
        result = self.cc.homophonicCipher(self.text)
        self.assertEqual(205, len(result))

    def testTranspositionCipher(self):
        expected = 'mncatsooiuiteaigolfraigboueyoltieoaitoigmpaa' \
                   'doiaallialtaeteaesbuaitrsigshmthmwrmsoislyrs' \
                   'olbdigntaopaigtierfintrosnhgmnwrdohvnasltlnp' \
                   'olnnvrainnaelynnamtlalnlimkshgmaaotsneetnate' \
                   'ahoeokotftpaeshudeonisedflyni'
        result = CustomCipher.transpositionCipher(self.text, 2)
        self.assertEqual(expected, result)
