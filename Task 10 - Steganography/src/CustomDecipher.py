from src.secret import move1, move2, words
from src.CustomCipher import CustomCipher
import math


class CustomDecipher:

    def __init__(self):
        """
            Import the config from secret.py
        """
        self.move1 = move1
        self.move2 = move2
        self.words = words
        pass

    def decipher(self, cipheredText: str) -> str:
        """
            Use all of the prepared deciphers and return deciphered text
            :rtype: str
        """
        step1 = self.transpositionDecipher(cipheredText, self.move2)
        step2 = self.cezarDecipher(step1)
        deciphered = self.transpositionDecipher(step2, self.move1)
        return deciphered

    def cezarDecipher(self, inputText: str):
        """
            Decipher the cezar cipher of a given text
            :rtype: str
        """
        check = inputText[0:6]
        for word in self.words:
            if word in check:
                keyWordLen = len(word)
                keyChar = check[keyWordLen]
                keyCharNumber = ord(keyChar) - 97
                realText = inputText[keyWordLen + 1:]
                return CustomCipher.cezarMove(realText, -keyCharNumber)

    @staticmethod
    def transpositionDecipher(text: str, key: int) -> str:
        """
            Decipher a transposition in a given text using the key value
            :rtype: str
        """
        try:
            numCols = math.ceil(len(text) / key)
        except TypeError:
            return "ERROR: Wrong data passed to deciphering!"
        numRows = key
        numShadedBoxes = (numCols * numRows) - len(text)
        plainText = [""] * numCols
        col = 0
        row = 0

        for symbol in text:
            plainText[col] += symbol
            col += 1

            if (
                    (col == numCols)
                    or (col == numCols - 1)
                    and (row >= numRows - numShadedBoxes)
            ):
                col = 0
                row += 1

        return "".join(plainText)
