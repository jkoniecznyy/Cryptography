from src.CustomCipher import CustomCipher
import re

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        x = f.read()
        sourceText = re.sub("[^a-z\s]", "", x, 0, re.IGNORECASE | re.MULTILINE)

    cc = CustomCipher()
    ciphered = cc.cipher(sourceText)
    deciphered = cc.deCipher(ciphered)
    
    print(cc.prepareStr(sourceText))
    print(ciphered)
    print(deciphered)
    print(len(deciphered))
    print()
    if deciphered != cc.prepareStr(sourceText):
        print('We have a problem')
    else:
        print('Everything is ok')

    with open("output.txt", "w", encoding="utf-8") as n:
        n.write(ciphered)
