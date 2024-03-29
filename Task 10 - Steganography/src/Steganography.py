import sys
import numpy as np
from PIL import Image

np.set_printoptions(threshold=sys.maxsize)


class Steganography:

    def __init__(self, imageDirectory):
        """
            Set the image directory
        """
        self.imgDir = imageDirectory

    def Encode(self, src: str, message: str, destination: str) -> str:
        """
            Encode the message in the src png image and save the result to the destination path
            :rtype: str
        """
        src = self.imgDir + src
        destination = self.imgDir + destination

        try:
            img = Image.open(src, 'r')
        except FileNotFoundError:
            return "ERROR: Source file doesn't exist!"

        width, height = img.size
        array = np.array(list(img.getdata()))
        if img.mode == 'RGB':
            n = 3
        elif img.mode == 'RGBA':
            n = 4

        total_pixels = array.size // n

        message += "$t3g0"
        b_message = ''.join([format(ord(i), "08b") for i in message])
        req_pixels = len(b_message)

        if req_pixels > total_pixels:
            return "ERROR: Need larger file size"

        else:
            index = 0
            for p in range(total_pixels):
                for q in range(0, 3):
                    if index < req_pixels:
                        array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                        index += 1

            array = array.reshape(height, width, n)
            enc_img = Image.fromarray(array.astype('uint8'), img.mode)
            enc_img.save(destination)
            return "Image Encoded Successfully"

    def Decode(self, src: str) -> str:
        """
            Decode the message from the source png image and return the message
            :rtype: str
        """
        src = self.imgDir + src

        try:
            img = Image.open(src, 'r')
        except FileNotFoundError:
            return "ERROR: Source file doesn't exist!"

        array = np.array(list(img.getdata()))

        if img.mode == 'RGB':
            n = 3
        elif img.mode == 'RGBA':
            n = 4

        total_pixels = array.size // n

        hidden_bits = ""
        for p in range(total_pixels):
            for q in range(0, 3):
                hidden_bits += (bin(array[p][q])[2:][-1])

        hidden_bits = [hidden_bits[i:i + 8] for i in range(0, len(hidden_bits), 8)]

        message = ""
        for i in range(len(hidden_bits)):
            if message[-5:] == "$t3g0":
                break
            else:
                message += chr(int(hidden_bits[i], 2))
        if "$t3g0" in message:
            return message[:-5]
        else:
            return "No Hidden Message Found"
