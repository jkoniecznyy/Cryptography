<b>Exercise 10: Steganography</b>

Design and write a steganography program:

with a graphical interface (web or desktop)

that allows you to "hide" text using an image in any graphic format (hint: some are simpler than others)

that allows you to "read" the text hidden in the picture (we assume the same scheme and algorithm)

that allows you to encrypt the text with any algorithm (does not have to be your own, but it can)

<b>Worth to mention:</b>

[Source of the Steganography methods](https://medium.com/swlh/lsb-image-steganography-using-python-2bbbee2c69a2)

Cipher and Decipher methods are copied from Task 05, but the emoji part is missing because
it was harder to encode emojis than the plaintext

To simplify showing the image on frontend I hardcoded the encrypted image name to hidden.png

To use the program you need to manually put your png images into the /frontend/public/img/ directory.


<b>Installation</b>

1. Make sure [Python 3.6+](https://www.python.org/downloads/) is installed. 
2. Install backend.
```
$ pip install pipenv 
$ pipenv install 
``` 
3. Install frontend
```
cd frontend/
npm install
```
4. Run backend and frontend in two separate consoles:
    * `/Task 10 - Steganography/> pipenv run python main.py` 
    * `/Task 10 - Steganography/frontend> npm run serve`
   
5. Use postman  or go to http://localhost:8080/ 
   
   [My postman collection](https://www.getpostman.com/collections/8cfddab1a272fc2a4ea0)
