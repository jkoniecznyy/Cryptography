from src.secret import move1, move2, words, emojiLetters
import re
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

    def cezarCipher(self, inputText: str) -> str:
        """
            Do a little bit more complicated cezar cipher to a given text
            :rtype: str
        """
        n = random.randint(1, 25)
        return self.words[n % 5] + string.ascii_lowercase[n] + CustomCipher.cezarMove(inputText, n)

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
        # print('count', count)
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
