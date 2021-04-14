from src.CustomCipher import CustomCipher
import re

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        x = f.read()
        sourceText = re.sub("[^a-z\s]", "", x, 0, re.IGNORECASE | re.MULTILINE)

    cc = CustomCipher()
    cipher1 = cc.customCezarCipher(sourceText)
    cipher2 = cc.customHomophonicCipher(cipher1)
    decipher2 = cc.customHomophonicDeipher(cipher2)
    decipher1 = cc.customCezarDecipher(decipher2)
    print(sourceText)
    print(cipher2)
    print(decipher1)
    if decipher1 != CustomCipher.prepareStr(sourceText):
        print('We have a problem')

    with open("output.txt", "w", encoding="utf-8") as n:
        n.write(cipher2)
