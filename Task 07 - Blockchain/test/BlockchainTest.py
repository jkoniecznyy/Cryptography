import unittest
from src.Blockchain import Blockchain


class BlockchainTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cc = Blockchain()
        cls.text = 'minecraftisnotoriousinthegamingworldforhavingabsolutelynoplotlinenovariationinga' \
                   'meplayandnoaimatallallinallitmakesthegameasaboutasinterestingasthemathhomeworkmo' \
                   'stofitsplayersshouldbedoinginsteadofplayingit'

    def testPrepareStr(self):
        textMinecraft = 'Minecraft is notorious in the gaming world for having absolutely no plot line,' \
                        ' no variation in gameplay and no aim at all. All in all, it makes the game as about' \
                        ' as interesting as the math homework most of its players should be doing instead of ' \
                        'playing it.'
        result = ''
        self.assertEqual(self.text, result)

