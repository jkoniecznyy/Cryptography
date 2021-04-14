import math
import re
import random
import string
from src.secret import move1, move2, words, emojiLetters


class CustomCipher:

    def __init__(self):
        self.move1 = move1
        self.move2 = move2
        self.words = words
        self.emojiLetters = emojiLetters
        pass

    def cipher(self, sourceText: str) -> str:
        inputText = self.prepareStr(sourceText)
        step1 = self.transposition(inputText, self.move1)
        step2 = self.cezarCipher(step1)
        step3 = self.homophonicCipher(step2)
        step4 = self.transposition(step3, self.move2)
        return step4

    def deCipher(self, cipheredText: str) -> str:
        step1 = self.deTransposition(cipheredText, self.move2)
        step2 = self.homophonicDeipher(step1)
        step3 = self.cezarDecipher(step2)
        step4 = self.deTransposition(step3, self.move1)
        return step4


    @staticmethod
    def prepareStr(inputText: str) -> str:
        return re.sub(r"[^a-z]", "", inputText.lower())

    @staticmethod
    def cezarMove(inputText: str, number: int) -> str:
        # Takes a string and an int (positive or negative).
        # Moves the ascii code of all the letters from a given text by the provided number.
        # Returns a string
        outputText = ''
        inputText = CustomCipher.prepareStr(inputText)
        number = number % 26

        for letter in inputText:
            newAsciiCode = ord(letter) + number
            if newAsciiCode > 122:
                newAsciiCode -= 26
            if newAsciiCode < 97:
                newAsciiCode += 26
            outputText += chr(newAsciiCode)
        return outputText

    def cezarCipher(self, inputText: str) -> str:
        n = random.randint(1, 25)
        return self.words[n % 5] + string.ascii_lowercase[n] + CustomCipher.cezarMove(inputText, n)

    def cezarDecipher(self, inputText: str):
        check = inputText[0:6]
        for word in self.words:
            if word in check:
                keyWordLen = len(word)
                keyChar = check[keyWordLen]
                keyCharNumber = ord(keyChar) - 97
                realText = inputText[keyWordLen + 1:]
                return CustomCipher.cezarMove(realText, -keyCharNumber)

    def homophonicCipher(self, inputText: str):
        inputText = CustomCipher.prepareStr(inputText)
        count = [0, 0, 0]
        outputText = ''
        # print('-----------Cipher------------')
        for inputLetter in inputText:
            for dictionaryLetter in self.emojiLetters:
                if inputLetter == dictionaryLetter:
                    emojis = self.emojiLetters[dictionaryLetter]
                    rand = random.randint(0, len(emojis) - 1)
                    count[rand] += 1
                    outputText += emojis[rand]
                    # print(inputLetter, emojis, rand, emojis[rand])
        # print(count)
        return outputText

    def homophonicDeipher(self, inputText: str):
        outputText = ''
        # print('-----------Decipher------------')
        for inputLetter in inputText:
            for dictionaryLetter in self.emojiLetters:
                for emoji in self.emojiLetters[dictionaryLetter]:
                    if inputLetter == emoji:
                        outputText += dictionaryLetter
                        # print(emoji, dictionaryLetter)
        return outputText

    def transposition(self, message, key):
        """
        """
        cipherText = [""] * key
        for col in range(key):
            pointer = col
            while pointer < len(message):
                cipherText[col] += message[pointer]
                pointer += key
        return "".join(cipherText)

    def deTransposition(self, message, key):
        """

        """
        numCols = math.ceil(len(message) / key)
        numRows = key
        numShadedBoxes = (numCols * numRows) - len(message)
        plainText = [""] * numCols
        col = 0
        row = 0

        for symbol in message:
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
