from src.CustomCipher import CustomCipher
from src.CustomDecipher import CustomDecipher
import re
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    with open("input.txt", "r") as f:
        x = f.read()
        sourceText = re.sub("[^a-z\s]", "", x, 0, re.IGNORECASE | re.MULTILINE)

    cc = CustomCipher()
    cd = CustomDecipher()
    ciphered = cc.cipherPreview(sourceText)
    deciphered = cd.decipher(ciphered)

    if deciphered != cc.prepareStr(sourceText):
        logging.warning('Something went wrong')
    else:
        logging.info('Everything is ok')

    with open("output.txt", "w", encoding="utf-8") as n:
        n.write(ciphered)
