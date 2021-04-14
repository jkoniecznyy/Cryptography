from src.secret import move1, move2, words, emojiLetters
import re
import math
import random
import string
import logging


class CustomCipher:

    def __init__(self):
        """
            Import the config from secret.py
        """
        self.move1 = move1
        self.move2 = move2
        self.words = words
        self.emojiLetters = emojiLetters
        pass

    def cipher(self, sourceText: str) -> str:
        """
            Use all of the prepared ciphers and return ciphered text
            :rtype: str
        """
        inputText = self.prepareStr(sourceText)
        step1 = self.transpositionCipher(inputText, self.move1)
        step2 = self.cezarCipher(step1)
        step3 = self.homophonicCipher(step2)
        ciphered = self.transpositionCipher(step3, self.move2)
        return ciphered

    def cipherPreview(self, sourceText: str) -> str:
        """
            Use all of the prepared ciphers, return ciphered text and
            Log every step of a ciphering
            :rtype: str
        """
        inputText = self.prepareStr(sourceText)
        step1 = self.transpositionCipher(inputText, self.move1)
        step2 = self.cezarCipher(step1)
        step3 = self.homophonicCipher(step2)
        ciphered = self.transpositionCipher(step3, self.move2)
        logging.info(inputText)
        logging.info(step1)
        logging.info(step2)
        logging.info(step3)
        logging.info(ciphered)
        return ciphered

    def decipher(self, cipheredText: str) -> str:
        """
            Use all of the prepared deciphers and return deciphered text
            :rtype: str
        """
        step1 = self.transpositionDecipher(cipheredText, self.move2)
        step2 = self.homophonicDecipher(step1)
        step3 = self.cezarDecipher(step2)
        deciphered = self.transpositionDecipher(step3, self.move1)
        return deciphered

    def cezarCipher(self, inputText: str) -> str:
        """
            Do a little bit more complicated cezar cipher to a given text
            :rtype: str
        """
        n = random.randint(1, 25)
        return self.words[n % 5] + string.ascii_lowercase[n] + CustomCipher.cezarMove(inputText, n)

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

    def homophonicCipher(self, inputText: str) -> str:
        """
            Do a homophonic cipher of a given text
            :rtype: str
        """
        count = [0, 0, 0]
        outputText = ''
        for inputLetter in inputText:
            for dictionaryLetter in self.emojiLetters:
                if inputLetter == dictionaryLetter:
                    emojis = self.emojiLetters[dictionaryLetter]
                    rand = random.randint(0, len(emojis) - 1)
                    count[rand] += 1
                    outputText += emojis[rand]
        return outputText

    def homophonicDecipher(self, inputText: str) -> str:
        """
            Decipher a homophonic cipher of a given text
            :rtype: str
        """
        outputText = ''
        for inputLetter in inputText:
            for dictionaryLetter in self.emojiLetters:
                for emoji in self.emojiLetters[dictionaryLetter]:
                    if inputLetter == emoji:
                        outputText += dictionaryLetter
        return outputText

    @staticmethod
    def prepareStr(inputText: str) -> str:
        """
            Convert a string to lowercase and return only basic english characters
            :rtype: str
        """
        return re.sub(r"[^a-z]", "", inputText.lower())

    @staticmethod
    def cezarMove(inputText: str, number: int) -> str:
        """
            Moves the ascii code of all the letters from a given text by the provided number.
            :rtype: str
        """
        outputText = ''
        number = number % 26

        for letter in inputText:
            newAsciiCode = ord(letter) + number
            if newAsciiCode > 122:
                newAsciiCode -= 26
            if newAsciiCode < 97:
                newAsciiCode += 26
            outputText += chr(newAsciiCode)
        return outputText

    @staticmethod
    def transpositionCipher(text: str, key: int) -> str:
        """
            Do a transposition in a given text using the key value
            :rtype: str
        """
        cipherText = [""] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                cipherText[col] += text[pointer]
                pointer += key
        return "".join(cipherText)

    @staticmethod
    def transpositionDecipher(text: str, key: int) -> str:
        """
            Decipher a transposition in a given text using the key value
            :rtype: str
        """
        numCols = math.ceil(len(text) / key)
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
