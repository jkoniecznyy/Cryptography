# Na dst:
# 1. W dowolnym języku programowania wykonaj szyfrator i deszyfrator Cezara i Vigenere'a.
# Wersja konsolowa wystarczy. Miło byłoby, gdyby było jakieś fajne API, walidacja danych wejściowych,
# testy automatyczne.
#
# Na db:
# 1. Wykonaj manualny łamacz szyfru Cezara.
#
# Na bdb:
# 1. Wykonaj automatyczny łamacz szyfru Cezara.
#
# Dla zadań na db i bdb założenia: 1. Alfabet to ASCI. 2. Tekst jawny jest po angielsku. 3. Nie przesadzajcie z
# długością tekstu jawnego. 4. Jakość kodu też się liczy. Czyli komentarze, zasady clean code i SOLID,
# testy jednostkowe, walidacja danych i takie tam.

import re
import math


def prepareString(text):
    text = text.lower()
    return re.sub(r"[^a-z]", "", text)


def makeMove(inputText, number):
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


def encryption(inputText, number):
    inputText = prepareString(inputText)
    return makeMove(inputText, number)


def decryption(inputText, number):
    inputText = prepareString(inputText)
    return makeMove(inputText, -number)


def fullDecryption(inputText):
    inputText = prepareString(inputText)
    decryptedTextArray = []
    for i in range(1, 27):
        decryptedTextArray.append(makeMove(inputText, i))
    return decryptedTextArray


def manualDecryption(encryptedText):
    encryptedText = prepareString(encryptedText)
    decryptedTextArray = fullDecryption(encryptedText)
    for i in range(26):
        print(f'Nr {i + 1} - {decryptedTextArray[i]}')
    print('Which one is it? (type 1-26 or 0 if all are wrong)')
    answer = int(input())  # TODO Taking more than 1 answer
    if 0 < answer < 27:
        return decryptedTextArray[answer - 1]
    return False


def calculateLettersProbability(text):
    englishLettersProbabilities = [0.073, 0.009, 0.030, 0.044, 0.130, 0.028, 0.016, 0.035, 0.074,
                                   0.002, 0.003, 0.035, 0.025, 0.078, 0.074, 0.027, 0.003,
                                   0.077, 0.063, 0.093, 0.027, 0.013, 0.016, 0.005, 0.019, 0.001]
    score = 0
    for letter in text:
        asciiCode = ord(letter)
        score += math.log(englishLettersProbabilities[asciiCode - 97])
    return -score / math.log(2) / len(text)


def automaticDecryption(encryptedText):
    encryptedText = prepareString(encryptedText)
    decryptedTextArray = fullDecryption(encryptedText)
    scores = []
    for text in decryptedTextArray:
        scores.append(calculateLettersProbability(text))
    return decryptedTextArray[scores.index(min(scores))]


