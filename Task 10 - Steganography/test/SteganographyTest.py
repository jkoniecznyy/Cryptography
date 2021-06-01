import unittest
from src.Steganography import Steganography


class CustomCipherTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.st = Steganography('testimg/')

    def testEncodeFileDoesntExist(self):
        result = self.st.Encode('Madagascar.png', 'Very important testing message', 'hiddentest.png')
        self.assertEqual("ERROR: Source file doesn't exist!", result)

    def testEncodeSuccess(self):
        result = self.st.Encode('testimg1.png', 'Very important testing message', 'hiddentest.png')
        self.assertEqual("Image Encoded Successfully", result)

    def testDecodeSuccess(self):
        result = self.st.Decode('hiddentest.png')
        self.assertEqual("Very important testing message", result)

    def testDecodeFileDosentExist(self):
        result = self.st.Decode('Madagascar.png')
        self.assertEqual("ERROR: Source file doesn't exist!", result)

