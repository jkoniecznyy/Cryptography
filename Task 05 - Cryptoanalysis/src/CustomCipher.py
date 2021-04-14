import re
import random
import string
from src.secret import words, emojiLetters


class CustomCipher:

    def __init__(self):
        self.words = words
        self.emojiLetters = emojiLetters
        pass

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

    def customCezarCipher(self, inputText: str) -> str:
        n = random.randint(1, 25)
        return self.words[n % 5] + string.ascii_lowercase[n] + CustomCipher.cezarMove(inputText, n)

    def customCezarDecipher(self, inputText: str):
        check = inputText[0:6]
        for word in self.words:
            if word in check:
                keyWordLen = len(word)
                keyChar = check[keyWordLen]
                keyCharNumber = ord(keyChar) - 97
                realText = inputText[keyWordLen + 1:]
                return CustomCipher.cezarMove(realText, -keyCharNumber)

    def customHomophonicCipher(self, inputText: str):
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

    def customHomophonicDeipher(self, inputText: str):
        outputText = ''
        # print('-----------Decipher------------')
        for inputLetter in inputText:
            for dictionaryLetter in self.emojiLetters:
                for emoji in self.emojiLetters[dictionaryLetter]:
                    if inputLetter == emoji:
                        outputText += dictionaryLetter
                        # print(emoji, dictionaryLetter)
        return outputText
