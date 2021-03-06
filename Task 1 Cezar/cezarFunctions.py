import re
import math


def prepareString(text):
    # Takes a string
    # Makes it lowercase and leaves only english lowercase letters
    # Returns a string
    text = text.lower()
    return re.sub(r"[^a-z]", "", text)


def makeMove(inputText, number):
    # Takes a string and an int (positive or negative).
    # Moves the ascii code of all the letters from a given text by the provided number.
    # Returns a string
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
    # Takes a string and an int (should be positive).
    # Prepares the text and calls the makeMove function with given parameters
    # Returns a string
    inputText = prepareString(inputText)
    return makeMove(inputText, number)


def decryption(inputText, number):
    # Takes a string and an int (should be positive).
    # Prepares the text and calls the makeMove function with given parameters, but with opposite number
    # Returns a string
    inputText = prepareString(inputText)
    return makeMove(inputText, -number)


def fullDecryption(inputText):
    # Takes a string
    # Makes sure the text is made of lowercase english letters and does a bruteforce decryption
    # Returns a string array containing 26 decrypted versions
    inputText = prepareString(inputText)
    decryptedTextArray = []
    for i in range(1, 27):
        decryptedTextArray.append(makeMove(inputText, i))
    return decryptedTextArray


def manualDecryption(encryptedText):
    # Takes a string
    # Calls fullDecryption, prints the results to the user and allows him to choose which one is right
    # Returns a string chose by the user or None if he didn't choose any value
    decryptedTextArray = fullDecryption(encryptedText)
    for i in range(26):
        print(f'Nr {i + 1} - {decryptedTextArray[i]}')
    print('Which one is it? (type 1-26 or 0 if all are wrong)')
    answer = int(input())  # TODO Taking more than 1 answer
    if 0 < answer < 27:
        return decryptedTextArray[answer - 1]
    return None


def calculateLettersProbability(text):
    # Takes a string
    # Calculates a score telling if it is a english text considering english letters probabilities
    # Returns a double (the less the better)
    englishLettersProbabilities = [0.073, 0.009, 0.030, 0.044, 0.130, 0.028, 0.016, 0.035, 0.074,
                                   0.002, 0.003, 0.035, 0.025, 0.078, 0.074, 0.027, 0.003,
                                   0.077, 0.063, 0.093, 0.027, 0.013, 0.016, 0.005, 0.019, 0.001]
    score = 0
    for letter in text:
        asciiCode = ord(letter)
        score += math.log(englishLettersProbabilities[asciiCode - 97])
    return -score / math.log(2) / len(text)


def automaticDecryption(encryptedText):
    # Takes a string
    # Calls the fullDecryption and calculates a score for every result
    # Returns a string of the lowest score
    decryptedTextArray = fullDecryption(encryptedText)
    scores = []
    for text in decryptedTextArray:
        scores.append(calculateLettersProbability(text))
    return decryptedTextArray[scores.index(min(scores))]


