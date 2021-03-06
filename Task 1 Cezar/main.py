from cezarFunctions import *


def startEncryption():
    # Allows user to do an encryption using commandline
    sampleText = "After having used Python for some time, any programmer feels a strong discomfort when using any" \
                 " other omputer language. This side-effect was van Rossum's personal idea. "

    print('Type the text to be encrypted, if you want to use sample Text leave this empty')
    userText = input()
    if not userText:
        userText = sampleText
    print('Now type the number of how many digits we should move it')
    numberOfMoves = int(input())
    encryptedText = encryption(userText, numberOfMoves)
    print('Your encrypted text: ', encryptedText)


def startDecryption():
    # Allows user to do a decryption using commandline
    sampleText = 'wbpandwrejcqoazlupdkjbknokiapeiawjulnkcnwiianbaahowopnkjczeoykibknpsdajqoejcwjukp' \
                 'danykilqpanhwjcqwcapdeooezaabbaypsworwjnkooqiolanokjwhezaw '
    print('Type your encrypted text or leave it empty to try out our sample')
    userText = input()
    if not userText:
        userText = sampleText
    decryptedText = manualDecryption(userText)
    print('Your manually decrypted text: ', decryptedText)
    print('Calculation shows that the right answer is probably: ', automaticDecryption(userText))


answer = ''
while answer != 'q':
    print('Type e for encryption, d for decryption or q to quit')
    answer = input()
    if answer == 'e':
        startEncryption()
    if answer == 'd':
        startDecryption()
